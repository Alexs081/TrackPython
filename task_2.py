# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
def find_common_participants(first_group, second_group, separator=','):
    first_list = first_group.split(separator)
    second_list = second_group.split(separator)

    common_participants = list(set(first_list) & set(second_list))
    common_participants.sort()

    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator='|'
)
print(result)
# TODO Провеьте работу функции с разделителем отличным от запятой
