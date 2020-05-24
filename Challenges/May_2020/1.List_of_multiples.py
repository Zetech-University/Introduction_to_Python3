
def multiple(num, length):
    the_list = []
    for i in range(length):
        i += 1
        the_list.append(num*i)

    print(the_list)

multiple(3, 5)  # Returns [3, 6, 9, 12, 18]
