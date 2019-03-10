N = int(input("Введите размерность массива"))
x = list(map(int, input("Введите количество элементов в списке").split()))
if (len(x) > N or N > len(x)):
    print("Количество элементов в последовательности должно быть равно N")
else:
    def quicksort(x):
        if len(x) <= 1:
            return x
        else:
            q = len(x)
            ch_nums = []
            un_nums = []
            e_nums = []
            for i in x:
                if (i <= q and i % 2 == 0):
                    ch_nums.append(i)
                elif (i <= q and i % 2 != 0):
                    un_nums.append(i)
                else:
                    e_nums.append(i)

            return quicksort(ch_nums) + e_nums + quicksort(list(reversed(un_nums)))

res = quicksort(x)
print(res)


