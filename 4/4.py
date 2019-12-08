class Human:

    def __init__(self, name, pass_no, uuid):
        self.name = name
        self.pass_no = pass_no
        self.uuid = uuid

    def greet(self, title='Mr'):
        self.title = title 
        print('hello my name is {} {}'.format(title, self.name))


class Worker(Human):

    def __init__(self, name, pass_no, uuid, position):
        self.position = position
        self.__secret = 1223
        super().__init__(name, pass_no, uuid)
        
    def __my_privat_method(self):
        print('__my_privat_method')

    def __getattribute__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        try:
            return super().__getattribute__(*args, **kwargs)
        except:
            return 'all is ok'

    def __lt__(self, value):
        print(value)
        return self.uuid < value.uuid

    @property
    def is_worker(self):
        print('work done by {} {}'.format(self.position, self.name))
        return True

    def __str__(self):
        self.__my_privat_method()
        return 'Worker name:{} uuid:{}'.format(self.name, self.uuid)


#object
h1 = Human(
    name = 'Jo',
    pass_no = 'ME123',
    uuid = 1
)

#h1.name = 'Jo'

h1.greet()
print(h1)

w1 = Worker(
    name = 'Bill',
    pass_no = 'ME778899',
    uuid = -988998,
    position = 'boss'
)
print(dir(w1))
print(w1 < h1)

#w1.greet()
#if w1.is_worker:
#    print('ok')
#print(w1)
#print(dir(w1))
#w1._Worker__secret
#w1._Worker__my_privat_method()

#print(dir())

