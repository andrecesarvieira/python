import re
import sys

try:
    import gi
except ModuleNotFoundError:
    print("Erro: O módulo 'gi' não está instalado. Instalar usando o comando 'pip install PyGObject'.")
    sys.exit(1)


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class appCalcGUI:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_string(self.get_glade_content())
        self.builder.connect_signals(self)

        # Widgets principais
        self.window = self.builder.get_object("main_window")
        self.area_texto = self.builder.get_object("area_texto")
        self.label_resultado = self.builder.get_object("label_resultado")
        self.treeview = self.builder.get_object("treeview")
        self.liststore = self.builder.get_object("liststore")

        # Configurando a TreeView
        self.configurar_treeview()

        self.window.show_all()

    def get_glade_content(self):
        return '''
        <interface>
          <requires lib="gtk+" version="3.0"/>
          <object class="GtkWindow" id="main_window">
            <property name="title">Calculadora de Área COBOL</property>
            <property name="default_width">600</property>
            <property name="default_height">600</property>
            <child>
              <object class="GtkGrid" id="main_grid">
                <property name="column_spacing">10</property>
                <property name="row_spacing">10</property>
                <property name="margin">10</property>
                <child>
                  <object class="GtkScrolledWindow" id="scrolled_window">
                    <property name="vexpand">true</property>
                    <property name="hexpand">true</property>
                    <child>
                      <object class="GtkTextView" id="area_texto">
                        <property name="wrap_mode">GTK_WRAP_NONE</property>
                      </object>
                    </child>
                  </object>
                  <packing>
                    <property name="top_attach">0</property>
                    <property name="left_attach">0</property>
                    <property name="width">2</property>
                    <property name="height">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkButtonBox" id="button_box">
                    <property name="layout_style">spread</property>
                    <property name="hexpand">true</property>
                    <child>
                      <object class="GtkButton" id="botao_calcular">
                        <property name="label">Calcular Área</property>
                        <signal name="clicked" handler="on_calcular_area" swapped="no"/>
                      </object>
                    </child>
                    <child>
                      <object class="GtkButton" id="botao_limpar">
                        <property name="label">Limpar</property>
                        <signal name="clicked" handler="on_limpar_area" swapped="no"/>
                      </object>
                    </child>
                  </object>
                  <packing>
                    <property name="top_attach">1</property>
                    <property name="left_attach">0</property>
                    <property name="width">2</property>
                    <property name="height">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkLabel" id="label_resultado">
                    <property name="label"></property>
                    <property name="hexpand">true</property>
                  </object>
                  <packing>
                    <property name="top_attach">2</property>
                    <property name="left_attach">0</property>
                    <property name="width">2</property>
                    <property name="height">1</property>
                  </packing>
                </child>
                <child>
                  <object class="GtkTreeView" id="treeview">
                    <property name="model">liststore</property>
                    <property name="vexpand">true</property>
                    <property name="hexpand">true</property>
                  </object>
                  <packing>
                    <property name="top_attach">3</property>
                    <property name="left_attach">0</property>
                    <property name="width">2</property>
                    <property name="height">1</property>
                  </packing>
                </child>
              </object>
            </child>
          </object>
          <object class="GtkListStore" id="liststore">
            <columns>
              <column type="gchararray"/>
              <column type="gchararray"/>
              <column type="gint"/>
              <column type="gint"/>
            </columns>
          </object>
        </interface>
        '''

    def configurar_treeview(self):
        for i, column_title in enumerate(["Nome do Campo", "Tipo", "Tamanho", "Ocorrências"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)

    def on_calcular_area(self, button):
        area_cobol = self.area_texto.get_buffer()
        start_iter, end_iter = area_cobol.get_bounds()
        area_text = area_cobol.get_text(start_iter, end_iter, True)
        area_total, campos = Calculo.calcularAreaTotal(area_text)
        self.label_resultado.set_text(f"Área total do layout: {area_total} bytes")
        self.exibir_campos(campos)

    def on_limpar_area(self, button):
        area_cobol = self.area_texto.get_buffer()
        area_cobol.set_text("")
        self.liststore.clear()

    def exibir_campos(self, campos):
        self.liststore.clear()
        for campo in campos:
            self.liststore.append(campo)


class Calculo:
    @staticmethod
    def calcularAreaTotal(area_cobol):
        total_area = 0
        campos = []
        linhas = area_cobol.split('\n')
        redefinidos = set()
        redefinindo = False
        nivel_redefine = 0
        fatores_ocorrencia = [1] * 50

        for linha in linhas:
            match_redefine = re.match(r'\s*(\d+)\s+(\S+)\s+REDEFINES\s+(\S+)\.', linha)
            if match_redefine:
                redefinidos.add(match_redefine.group(3))
                redefinindo = True
                nivel_redefine = int(match_redefine.group(1))
                continue

            if redefinindo:
                match_nivel = re.match(r'\s*(\d+)', linha)
                if match_nivel:
                    nivel_linha = int(match_nivel.group(1))
                    if nivel_linha <= nivel_redefine:
                        redefinindo = False
                    else:
                        continue

            expressao = (
                r'\s*(\d+)\s+(\S+)\s+PIC\s+([9XZS])'
                r'(?:\((\d+)\))?'
                r'(?:V9\((\d+)\))?'
                r'(?:\s+OCCURS\s+(\d+))?'
                r'(?:\s+(BINARY|COMP(?:-1|-2|-3|-4|-5)?))?'
            )

            match_campo = re.match(expressao, linha)
            if match_campo:
                nivel = int(match_campo.group(1))
                nome = match_campo.group(2)
                tipo = match_campo.group(3)
                tamanho = int(match_campo.group(4)) if match_campo.group(4) else 1
                decimal_size = int(match_campo.group(5)) if match_campo.group(5) else 0
                ocorrencias = int(match_campo.group(6)) if match_campo.group(6) else 1
                comp_tipo = match_campo.group(7)

                if tipo in ['9', 'S']:
                    tamanho += decimal_size

                if comp_tipo:
                    if comp_tipo in ['BINARY', 'COMP', 'COMP-4']:
                        if tamanho <= 4:
                            tamanho = 2
                        elif tamanho <= 9:
                            tamanho = 4
                        elif tamanho <= 18:
                            tamanho = 8
                    elif comp_tipo == 'COMP-1':
                        tamanho = 4
                    elif comp_tipo == 'COMP-2':
                        tamanho = 8
                    elif comp_tipo == 'COMP-3':
                        tamanho = (tamanho + 1) // 2
                    elif comp_tipo == 'COMP-5':
                        if tamanho <= 4:
                            tamanho = 2
                        elif tamanho <= 9:
                            tamanho = 4
                        elif tamanho <= 18:
                            tamanho = 8

                fatores_ocorrencia[nivel] = ocorrencias

                if nome in redefinidos:
                    continue

                multiplicador = 1
                for i in range(1, nivel + 1):
                    multiplicador *= fatores_ocorrencia[i]

                total_area += tamanho * multiplicador
                campos.append((nome, tipo, tamanho, multiplicador))

        return total_area, campos


def main():
    app = appCalcGUI()
    Gtk.main()


if __name__ == "__main__":
    main()