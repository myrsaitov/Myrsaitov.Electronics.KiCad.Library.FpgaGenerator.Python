
# Глобальные переменные модуля
lyb_content = []


def create_symbol(
        file_name,
        reference,  # Обозначение на схеме
        component_name,  # Наименование компонента
        footprint,  # Футпринт компонента
        datasheet,  # Datasheet URL
        part_count,  # Количество частей
):

    # Добавляет начало библиотеки
    add_begin(
        reference,
        component_name,
        footprint,
        datasheet
    )

    # Имена частей одного компонента
    #for i in range(1, part_count):
        #add_part(i)

    # Добавляет конец библиотеки
    add_end()

    # w: Создает новый файл или перезаписывает уже имеющийся
    f = open(file_name, 'w')
    f.write("\n".join(lyb_content))
    f.close()


# Добавляет начало библиотеки
def add_begin(
        reference,
        component_name,
        footprint,
        datasheet
):

    # Версия библиотеки
    lyb_content.append('(kicad_symbol_lib (version 20211014) (generator kicad_symbol_editor)')

    # Название символа компонента
    lyb_content.append('  (symbol ' + '"' + component_name + '" (in_bom yes) (on_board yes)')

    # Свойство "Reference"
    property_id = 0
    lyb_content.append('    (property "Reference" "' + reference + '" (id ' + str(property_id) + ') (at 2.54 12.7 0)')
    lyb_content.append('      (effects (font (size 1.27 1.27)))')
    lyb_content.append('    )')

    # Свойство "Value"
    property_id += 1
    lyb_content.append('    (property "Value" "' + component_name + '" (id ' + str(property_id) + ') (at -10.16 11.43 0)')
    lyb_content.append('      (effects (font (size 1.27 1.27)))')
    lyb_content.append('    )')

    # Свойство "Footprint"
    property_id += 1
    lyb_content.append('    (property "Footprint" "' + footprint + '" (id ' + str(property_id) + ') (at 0 0 0)')
    lyb_content.append('      (effects (font (size 1.27 1.27)) hide)')
    lyb_content.append('    )')

    # Свойство "Datasheet"
    property_id += 1
    lyb_content.append('    (property "Datasheet" "' + footprint + '" (id ' + str(property_id) + ') (at 0 0 0)')
    lyb_content.append('      (effects (font (size 1.27 1.27)) hide)')
    lyb_content.append('    )')


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
    lyb_content.append('  )')
    lyb_content.append(')')