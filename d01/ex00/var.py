#! /usr/bin/python3

def my_var():
    int_42 = 42
    str_42 = '42'
    str_42_long = 'quarante-deux'
    float_42 = 42.0
    bool_42 = True
    list_42 =[42]
    dict_42 = {42: 42}
    tuple_42 = (42,)
    set_42 = set()
    print("{} est de type {}".format(int_42, type(int_42)))
    print("{} est de type {}".format(str_42, type(str_42)))
    print("{} est de type {}".format(str_42_long, type(str_42_long)))
    print("{} est de type {}".format(float_42, type(float_42)))
    print("{} est de type {}".format(bool_42, type(bool_42)))
    print("{} est de type {}".format(list_42, type(list_42)))
    print("{} est de type {}".format(dict_42, type(dict_42)))
    print("{} est de type {}".format(tuple_42, type(tuple_42)))
    print("{} est de type {}".format(set_42, type(set_42)))

if __name__ == '__main__':
    my_var()