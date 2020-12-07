from day7_python.input_test import test_input


def extract_name(input: str) -> str:
    return ' '.join(input.split(" bag")[0].split()[1:])


colors = []
available_colors = set({})
changed = True
while changed:
    print(f'{available_colors}')
    changed = False
    for str in test_input:
        contenant = str.split(';')[0].split(" bags")[0]
        colors.append(contenant)
        contenus = str.split(';')[1].split(',')
        for contenu in contenus:
            if contenant not in available_colors and "shiny gold" in contenu:
                available_colors.add(contenant)
                changed = True
            if extract_name(contenu) in available_colors and contenant not in available_colors:
                print(f'{contenant=}')
                available_colors.add(contenant)
                changed = True

                print(f'{available_colors}')
