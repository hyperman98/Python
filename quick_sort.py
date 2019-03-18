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

ch = [int(i) for i in x if i % 2 == 0]
un = [int(i) for i in x if i % 2 != 0]
L = sort_mas(ch)
R = sort_mas(un)
res = L + list(reversed(R))
print(res)


