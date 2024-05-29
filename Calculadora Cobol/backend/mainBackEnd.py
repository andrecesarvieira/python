import re


def calcularAreaTotal(area_cobol):
    total_area = 0
    campos = []
    linhas = area_cobol.split('\n')
    redefined_fields = set()
    in_redefines_block = False
    redefines_indentation = 0

    for linha in linhas:
        match_redefines = re.match(
            r'\s*(\d+)\s+(\S+)\s+REDEFINES\s+(\S+)\.', linha)
        if match_redefines:
            redefined_name = match_redefines.group(3)
            redefined_fields.add(redefined_name)
            in_redefines_block = True
            redefines_indentation = len(re.match(r'(\s*)', linha).group(1))
            continue

        if in_redefines_block:
            line_indentation = len(re.match(r'(\s*)', linha).group(1))
            if line_indentation <= redefines_indentation:
                in_redefines_block = False
            else:
                continue

        match_field = re.match(
            r'\s*(\d+)\s+(\S+)\s+PIC\s+([9X])(?:\((\d+)\))?(?:\s+(?:OCCURS|OC)\s+(\d+))?(?:\s+DEPENDING\s+ON\s+(\S+))?(?:\s+(BINARY|COMP(?:-2|-3|-4|-5)?))?', linha)
        if match_field:
            name = match_field.group(2)
            field_type = match_field.group(3)
            size = int(match_field.group(4)) if match_field.group(4) else 1
            occurs = int(match_field.group(5)) if match_field.group(5) else 1

            if match_field.group(7):
                comp_type = match_field.group(7)
                if comp_type == 'COMP':
                    size = (size + 1) // 2
                elif comp_type == 'COMP-2':
                    size = size // 2
                elif comp_type in ['COMP-3', 'COMP-4', 'COMP-5']:
                    size = (size // 2) + 1

            if name in redefined_fields:
                continue

            total_area += size * occurs
            campos.append((name, field_type, size, occurs))

    return total_area, campos
