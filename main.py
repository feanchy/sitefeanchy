def foo():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in numbers:
        if i % 2 == 0:
            print(i, "Чётное")
        else:
            print(i, "Нечётное")
foo()