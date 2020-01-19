def prime_number(finish_num):
    numbers = list(range(finish_num + 1))
    numbers[1] = 0
    lst = []
    i = 2
    while i <= finish_num:
        if numbers[i] != 0:
            lst.append(numbers[i])
            for j in range(i, finish_num + 1, i):
                numbers[j] = 0
        i += 1
    return lst
