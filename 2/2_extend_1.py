def my_test():
    import lib
    from lib import calc_price, CONST


    print(dir(lib))
    print(calc_price(100, 0.2))
    print(calc_price(500, 0.2))
    print(lib.calc_price(100))
    print(lib.calc_price(500))


print(dir())
my_test()
my_test()
my_test()
my_test()
print(dir())

