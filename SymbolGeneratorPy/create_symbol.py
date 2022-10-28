
# Глобальные переменные модуля
lyb_content = []


def create_symbol(
        library_version,  # Версия библиотеки KiCAD
        file_name,  # Имя файла
        properties,  # Общие свойства компонента
        part_count,  # Количество частей
        in_bom=True,  # Находится ли в списке BOM
        on_board=True  # Находится ли на плате
):

    # Добавляет начало библиотеки
    add_begin(
        library_version,
        properties,
        in_bom,
        on_board
    )

    # Имена частей одного компонента
    #for i in range(1, part_count):
        #add_part(i)

    # Добавляет конец библиотеки
    add_end()

    # w: Создает новый файл или перезаписывает уже имеющийся
    f = open(file_name, 'w')
    f.write(''.join(lyb_content))
    f.close()


# Добавляет начало библиотеки
def add_begin(
        library_version,
        properties,
        in_bom,
        on_board
):

    # Версия библиотеки
    lyb_content.append(f'(kicad_symbol_lib (version {library_version}) (generator kicad_symbol_editor)\n')

    # Название символа компонента
    component_name = ''

    for data in properties:
        if data[0] == 'Value':
            component_name = data[1]

    if not component_name:

        print('Error! Component Name is not found!')
        return

    symbol_str = f'  (symbol "{component_name}"'

    if in_bom:
        symbol_str += ' (in_bom yes)'
    else:
        symbol_str += ' (in_bom no)'

    if on_board:
        symbol_str += ' (on_board yes)'
    else:
        symbol_str += ' (on_board no)'

    symbol_str += '\n'

    lyb_content.append(symbol_str)

    index = 0
    for data in properties:
        lyb_content.append(
            ''.join([
                f'    (property "{data[0]}" "{data[1]}"',
                f' (id {index})',
                f' ({data[2]})\n',
                f'      ({data[3]})\n',
                '    )\n'
            ])
        )
        index += 1


# Добавляет информацию об одной части компонента
def add_part(
        component_name,
        index
):

    lyb_content.append('    (symbol "' + component_name + '_' + index + '_1"')
    part_name = component_name + '_' + str(index)
    lyb_content.append(part_name)


# Добавляет pin
def add_pin(
        name,
        number
):
    lyb_content.append('      (pin power_out line (at -19.05 -2.54 0) (length 5.08)')
    lyb_content.append('        (name "GND" (effects (font (size 1.27 1.27))))')
    lyb_content.append('        (number "-UA" (effects (font (size 1.27 1.27))))')
    lyb_content.append('      )')


# Добавляет конец библиотеки
def add_end():

    lyb_content.append(
        ''.join([
            '  )\n',
            ')\n'
        ])
    )
