def sum_individual(num):
    result = 0
    while num != 0:
        result += (num % 10)
        num = num // 10

    return result
        

def test():
    # 5 -> 5
    print('Test : 5 -> 5')
    result = sum_individual(5)
    if result == 5:
        print('True')
    else:
        print('False ' + result)
    
    # 48 -> 12
    print('Test : 48 -> 12')
    result = sum_individual(48)
    if sum_individual(48) == 12:
        print('True')
    else:
        print('False ' + result)
        
    # 1234 -> 10
    print('Test : 1234 -> 10')
    result = sum_individual(1234)
    if sum_individual(1234) == 10:
        print('True')
    else:
        print('False ' + result)
    

if __name__ == '__main__':
    num_str = input('양의 정수 하나를 입력: ')
    try:
        num = int(num_str)
    except ValueError:
        print('양의 정수를 입력하세요\n')
        exit()

    result = sum_individual(num)
    print(result)

    # test()
