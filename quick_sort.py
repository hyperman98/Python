N = int(input("Введите размерность массива"))
x = list(map(int, input("Введите количество элементов в списке").split()))
if (len(x) > N or N > len(x)):
    print("Количество элементов в последовательности должно быть равно N")
else:
    import random
    def sort_mas(x):
        if len(x) <= 1:
            return x
        else:
            v = random.choice(x)
            big_nums = []
            sm_nums = []
            q_nums = []
            for j in x:
                if j < v:
                    sm_nums.append(j)
                elif j > v:
                    big_nums.append(j)
                else:
                    q_nums.append(j)
            return sort_mas(sm_nums) + q_nums + sort_mas(big_nums)
    y = sort_mas(x)

    def quicksort(y):
        if len(y) <= 1:
            return y
        else:
            q = random.randint(1, 100)
            ch_nums = [] 
            un_nums = []
            e_nums = []
            for i in y:
                if (i <= q and i % 2 == 0):
                    ch_nums.append(i)
                elif (i <= q and i % 2 != 0):
                    un_nums.append(i)
                else:
                    e_nums.append(i)

            return quicksort(ch_nums) + e_nums + quicksort(list(reversed(un_nums)))

res = quicksort(y)
print(res)


