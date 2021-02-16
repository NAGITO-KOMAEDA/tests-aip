def task_1(two_dim_words):
    """
        Здесь должен быть ваш код.
        Переменная two_dim_words - ваш двумерный список.
        Заполнять список значениями не нужно.
        Финальное значение должно быть помещено в переменную sorted_words.
        """


    def f(vxod):
        spiso = []
        for i in vxod:
            if type(i) != list:
                spiso.append(i)
            else:
                spiso += f(i)
        return spiso


    sorted_words = f(two_dim_words)
    sorted_words.sort()
    sorted_words.sort(key=len, reverse=True)
    print(sorted_words)


    return sorted_words


def task_3(numbers):
    """
        Здесь должен быть ваш код.
        Переменная numbers - ваша строка чисел.
        Финальное значение должно быть помещено в переменную dict_min.
        """
    slovar = []
    dict_min = {}
    for i in numbers:
        slovar.append(i)
        for kolichestvo in slovar:
                dict_min[i] = slovar.count(kolichestvo)

    print(dict_min)


    return dict_min


def task_4_1(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_4_2(words):  # можно сделать тесты
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_4_3(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_5(lst1, lst2):
    """
        Здесь должен быть ваш код.
        Переменные lst1 и lst2 - два данных списка.
        Финальное значение должно быть помещено в переменную diff.
        """
    lst1 = set(lst1)
    lst2 = set(lst2)
    diff = lst1.difference(lst2)
    diff = list(diff)
    diff.sort(reverse=False)
    print(diff)

    return diff


def task_6(lst):
    """
        Здесь должен быть ваш код.
        Переменная lst - ваш список.
        Финальное значение должно быть помещено в переменную res.
        """
    lst.sort(reverse=True)
    res = tuple(lst)
    print(res)
    return res

