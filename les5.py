class Environment:

    def __init__(self, city, country, street):
        self.city = city
        self.country = country
        self.street = street

    @property
    def enr(self):
        if self.street and self.country:
            return f'I live in {self.city}, this is a {self.country}'
        else:
            return 'Bad for me('

    def __str__(self):
        return 'World around us!'


class Bank(Environment):

    def __init__(self, acc, cred, city, country, street):
        super(Bank, self).__init__(city=city, country=country, street=street)
        self.acc = acc
        self.cred = cred

    @property
    def motto(self):
        if self.cred >= 1500:
            return f'Your {self.acc} have {self.cred}\nWe make you feel own! >:)'
        else:
            return 'Its never late to take a credit)'

    def __str__(self):
        return 'Please take a credit!'


class Person(Bank):

    def __init__(self, name, p_num, gen, acc, cred, city, country, street):
        super(Person, self).__init__(acc=acc, cred=cred, city=city, country=country, street=street)
        self.name = name
        self.p_num = p_num
        self.gen = gen

    @property
    def i_am(self):
        return "I'm a person!"

    def __str__(self):
        return 'I just do what i want!!'


class Occupation(Person):

    def __init__(self, vac, wh, sal, gen, p_num, name, cred, acc, country, city, street):
        super(Occupation, self).__init__(
            gen=gen, p_num=p_num, name=name, acc=0, cred=0, city=0, country=0, street=0
        )
        self.wh = wh
        self.sal = sal
        self.vac = vac

    @property
    def occ(self):
        return f'Im working {self.wh} each day and i reach my {self.sal}!'

    def __str__(self):
        return f'Person {self.name}, {self.gen}\n' \
               f'Have a workday {self.wh} hours also have a goal {self.sal}'


class Student(Occupation):

    def __init__(self, mark, uni, fac, gen, p_num, name, wh, vac, acc, cred, city, country, street):
        super(Student, self).__init__(
            wh=wh, gen=gen, p_num=p_num, name=name, vac=vac,
            sal=0, acc=acc, cred=cred, country=country, city=city, street=street
        )
        self.mark = mark
        self.uni = uni
        self.fac = fac

    @property
    def good_learn(self):
        if self.mark >= 3.5:
            return 'He has a great marks!'
        else:
            return 'Trying to get education!\nDo not touch me'

    def __str__(self):
        return "I have a bright future because I'm a student!"


class Worker(Occupation):

    def __init__(self, bs, comp, vac, name, wh, acc, p_num, gen, cred, sal, street, country, city):
        super(Worker, self).__init__(
            vac=vac, name=name, acc=acc, gen=gen, wh=wh, p_num=p_num,
            cred=cred, sal=sal, street=street, country=country, city=city
        )
        self.bs = bs
        self.comp = comp

    @property
    def b_work(self):
        if self.wh >= 9:
            return f'I get {self.bs}$ for work, but i feel empty'
        else:
            return 'Get good salary, and have a time for family'

    def __str__(self):
        return "Hei I'm Worker who's doing a lot of job"


class Military(Occupation):

    def __init__(self, vac, gen, name, p_num, wh, sal, wea, gov, s_tax, acc, cred, country, city, street):
        super(Military, self).__init__(
            vac=vac, wh=wh, sal=sal, gen=gen, p_num=p_num, name=name,
            acc=acc, cred=cred, street=street, country=country, city=city
        )
        self.wea = wea
        self.gov = gov
        self.s_tax = s_tax

    @property
    def mil(self):
        if self.s_tax:
            return 'I got less taxes! TY my lovely work!'
        else:
            return 'Damn'

    def __str__(self):
        return f'I work with {self.wea}, proud of that!'


class Scientist(Occupation):

    def __init__(self, vac, gen, name, p_num, wh, sal, res, kos, acc, cred, country, city, street):
        super(Scientist, self).__init__(
            acc=acc, sal=sal, gen=gen, p_num=p_num, wh=wh, name=name,
            cred=cred, vac=vac, street=street, country=country, city=city
        )
        self.res = res
        self.kos = kos

    @property
    def sci(self):
        if self.res:
            return f'Finally ive mastered {self.kos}, can move ahead'
        else:
            return 'I should discover a lot of things!'

    def __str__(self):
        return 'E = MC**\nMaybe?)'


class Discoverer(Scientist):

    def __init__(
            self, vac, gen, name, p_num, wh, sal, res, kos, acc,
            cred, env, deep_learn, project, country, city, street
    ):
        super(Discoverer, self).__init__(
            acc=acc, sal=sal, gen=gen, p_num=p_num, wh=wh, name=name,
            cred=cred, vac=vac, res=res, kos=kos, street=street, country=country, city=city
        )
        self.env = env
        self.project = project
        self.deep_learn = deep_learn

    @property
    def disc(self):
        if self.deep_learn == 'Math'.lower() or self.deep_learn == 'Physics':
            return f'Get my own {self.deep_learn} project'
        else:
            return 'Study study study!'

    def __str__(self):
        return 'Absolute zero is not so "absolute"!\nI can prove!'


class Inventor(Discoverer):

    def __init__(
            self, vac, gen, name, p_num, wh, sal, res, kos, acc, cred,
            env, deep_learn, project, ep, risk, sec, country, city, street
    ):
        super(Inventor, self).__init__(
            acc=acc, sal=sal, gen=gen, p_num=p_num, wh=wh, name=name, street=street, cred=cred, vac=vac,
            res=res, kos=kos, env=env, project=project, deep_learn=deep_learn, country=country, city=city
        )
        self.risk = risk
        self.ep = ep
        self.sec = sec

    @property
    def ufo(self):
        if self.sec and self.risk:
            return 'So risky, but, but sooo excited...'
        else:
            return 'To close but so far...'

    def __str__(self):
        return 'What?\nWho are you?'


class Driver(Occupation):

    def __init__(self, gen, sal, vac, street, city, country, name, p_num, wh, acc, cred, hp, ven):
        super(Driver, self).__init__(
            gen=gen, sal=sal, vac=vac, street=street, city=city, country=country,
            name=name, p_num=p_num, wh=wh, acc=acc, cred=cred
        )
        self.hp = hp
        self.ven = ven

    @property
    def drive(self):
        return f'Good to have {self.hp} under my cabin :)'

    def __str__(self):
        return 'Happy to deliver anything anywhere!'


class PersonalDriver(Driver):

    def __init__(self, gen, sal, vac, street, city, country, name, p_num, wh, acc, cred, hp, ven, ds, comfort):
        super(PersonalDriver, self).__init__(
            gen=gen, sal=sal, vac=vac, street=street, city=city, country=country,
            name=name, p_num=p_num, wh=wh, acc=acc, cred=cred, hp=hp, ven=ven
        )
        self.ds = ds
        self.comfort = comfort

    @property
    def p_drive(self):
        if self.comfort:
            return 'Will drive with my Boss in a highest comfort!'
        else:
            return 'Do my best here'

    def __str__(self):
        return 'Fasten seat belt'


class DeliveryMan(Driver):

    def __init__(self, gen, sal, vac, street, city, country, name, p_num, wh, acc, cred, hp, ven, delivery_speed, sa):
        super(DeliveryMan, self).__init__(
            gen=gen, sal=sal, vac=vac, street=street, city=city, country=country, ven=ven,
            name=name, p_num=p_num, wh=wh, acc=acc, cred=cred, hp=hp
        )
        self.delivery_speed = delivery_speed
        self.sa = sa

    @property
    def deliver(self):
        if self.delivery_speed == 'High'.lower:
            return 'Ha-Ha, I will do the fastest delivery ever!'
        elif self.delivery_speed == 'Average'.lower:
            return 'Best decision, time is money!'
        else:
            return 'Good choice!\nThanks for using Glovo'

    def __str__(self):
        return 'We can deliver everything anywhere'


class Trucker(Driver):

    def __init__(self, gen, sal, vac, street, city, country, name, p_num, wh, acc, cred, hp, ven, cc, dis):
        super(Trucker, self).__init__(
            gen=gen, sal=sal, vac=vac, street=street, city=city, country=country,
            name=name, p_num=p_num, wh=wh, acc=acc, cred=cred, hp=hp, ven=ven
        )
        self.cc = cc
        self.dis = dis

    @property
    def truck(self):
        if self.dis >= 500:
            return 'I am driving to far, so I am driving to fast'
        else:
            return 'Close distance fast comeback'

    def __str__(self):
        return 'Week for a road... Calm down...'


class House(Bank):

    def __init__(self, city, country, street, coi, sq, acc, cred):
        super(House, self).__init__(city=city, country=country, street=street, acc=0, cred=0)
        self.coi = coi
        self.sq = sq

    @property
    def home(self):
        return 'Small but so comfortable'

    def __str__(self):
        return 'This place is so cool'


class Parking(House):

    def __init__(self, city, country, street, coi, sq, acc, cred, php, sh):
        super(Parking, self).__init__(city=city, country=country, street=street, coi=coi, sq=sq, acc=acc, cred=cred)
        self.php = php
        self.sh = sh

    @property
    def park(self):
        if self.coi < 1:
            return 'Sorry no space for you('
        else:
            return 'Come ride in, we have a free space!'

    def __str__(self):
        return 'Your car will be safe with us'


class Cinema(Parking):

    def __init__(self, city, country, street, coi, sq, acc, cred, php, sh, cost, com):
        super(Cinema, self).__init__(
            city=city, acc=acc, cred=cred, php=php, sh=sh, sq=sq, street=street, country=country, coi=coi
        )
        self.cost = cost
        self.com = com

    @property
    def look(self):
        return 'New movie and a high comfort here!'

    def __str__(self):
        return 'Movie time!'


class Restaurant(Cinema):

    def __init__(self, city, country, street, coi, sq, acc, cred, php, sh, cost, com, tas, mus):
        super(Restaurant, self).__init__(
            sq=sq, acc=acc, cred=cred, cost=cost, com=com, sh=sh, php=php,
            city=city, country=country, coi=coi, street=street
        )
        self.tas = tas
        self.mus = mus

    @property
    def food(self):
        if self.tas:
            return 'So good!\nI will recommend this restaurant to all my friends!'
        else:
            return 'Just another one fast food'

    def __str__(self):
        return 'Chinese food!'
