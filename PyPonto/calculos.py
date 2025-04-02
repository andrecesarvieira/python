from datetime import datetime, timedelta


class Calculos:

    @staticmethod
    def calcular_duracao(inicio, fim):
        fmt = "%H:%M"
        tdelta = datetime.strptime(fim, fmt) - datetime.strptime(inicio, fmt)
        if tdelta < timedelta(0):
            tdelta += timedelta(days=1)
        return str(tdelta)[:-3]

    @staticmethod
    def somar_tempos(t1, t2):
        h1, m1 = map(int, t1.split(":"))
        h2, m2 = map(int, t2.split(":"))
        total = timedelta(hours=h1 + h2, minutes=m1 + m2)
        return str(total)[:-3]
