def print_values_less_than(base_value, value_list):
    for value in value_list:
        if value < base_value:
            print(value)

numbers = []
alphabets = []

for i in range(10):
    value = input('입력 ' + str(i+1) + ':')
    if value.isalpha():
        alphabets.append(value)
    else:
        numbers.append(value)

sort_number = input('정렬 기준 숫자 입력:')
sort_alphabet = input('정렬 기준 알파벳 입력:')

print_values_less_than(sort_number, numbers)
print_values_less_than(sort_alphabet, alphabets)

