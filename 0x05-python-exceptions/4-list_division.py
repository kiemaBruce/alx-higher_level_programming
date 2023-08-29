#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    b = 0
    for i in range(list_length):
        try:
            res.append(my_list_1[b] / my_list_2[b])
        except ZeroDivisionError:
            res.append(0)
            print("division by 0")
        except TypeError:
            res.append(0)
            print("wrong type")
        except IndexError:
            res.append(0)
            print("out of range")
        finally:
            b += 1
    return res
