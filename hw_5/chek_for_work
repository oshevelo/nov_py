import string
import re


def ask(msg=None):  # используется для запроса повторного ввода данных
    while True:
        question = input(msg + '(Y/N)')
        if question.upper() == 'Y':
            return True
        elif question.upper() == 'N':
            return False
        else:
            print('Щось не те ввели введіть або Y або N')


def check_full_name(msg):  # проверка ФИО
    while True:
        full_name = input('Введіть ПІБ {} через пробіл'.format(msg))
        for i in string.punctuation:
            full_name = full_name.replace(i, '')  # удаляем случайные знаки препинания
        if len(list(full_name.strip().split(' '))) != 3:
            print('Щось піло не так - ПІБ має складатись з трьох слів')  # проверяем что бы не было лишних пробелов и что бы были введены все 3 позиции
        else:
            if (i.isalpha() for i in full_name):  # проверяем что бы это были только буквы
                full_name = full_name.title()
                return full_name
            else:
                print('Щось пішло не так = ПІБ не може містити ніяких символів, окрім букв')

#
# def check_passport():  # проверка пасспортных данных согласно стандартов Украины
#     while True:
#         passport = input(f'Введіть серію та номер паспорту клієнта через пробіл (приклад: "ЕЕ 12345")')
#         patt = r'[А-Я]{2}\s\d{5}'
#         res = re.fullmatch(patt,passport.strip()) # убираем символы в началае и в конце строки и проверяем
#         date_pass = input(f'Введіть дату видачі паспорту у форматі: "28 жовтня 2019" - допускається тільки українська мова')
#         patt_date = r'\d{2}\s\b\w{5,9}\b\s\d{4}'
#         res2 = re.fullmatch(patt_date, date_pass.strip())  # убираем символы в началае и в конце строки и проверяем
#         if not res:
#             print('Щось пішло не так, ви не вірно ввели серію та номер пасспорта, спробуйте ще раз')
#         elif not res2:
#             print('Щось пішло не так, ви не вірно ввели дату, спробуйте ще раз')
#         else:
#             passport_org = input(f'Введіть ким виданий паспорт (приклад: Дарницьким РУГУ МВС України в м. Києві)')
#             return 'Паспорт: серія номер {}, виданий {}р. {}'.format(res[0],res2[0],passport_org.strip())


def check_login():  # проверка ввода логина
    while True:
        login = input('Введіть і\'мя користувача(login) не менше 5 символів')
        for i in string.punctuation:
            login = login.replace(i, '')  # удаляем случайные знаки препинания
        if len(login.strip()) < 5:
            print('І\'мя користувача(login) не може бути менше 5 символів')
        else:
            return login


def check_address():  # проверка почтового адреса
    while True:
        index = input('Введіть поштовий індекс (5 цифр)')
        if len(index) != 5:
            print('Не вірно введено, індекс має бути 5 цифр')
        else:
            try:
                index = int(index)
            except TypeError:
                print('Не вірно введено, індекс має складатись лише з цифр')
            obl = input('Введіть область')
            district = input('Введіть район')
            city = input('Введіть місто')
            street = input('Введіть вулицю')
            house = input('Введіть номер будинку')
            fl = input('Введіть номер квартири або офісу')
            return 'Поштова адреса клієнта: \nІндекс: {} \nОбласть: {}' \
                   ' \nМісто: {} \nРайон: {} \nВулиця: {} \nБудинок: №{} \nОфіс/Квартира: №{}'.format(index,obl.title(),city.title(),district.title(),street.title(),house,fl)


def check_cell_numb(msg):  # приведение номера телефона в определенный формат и добавление в список телефонов
    cellnumb = []
    while True:
        cell = input('Введіть контактний номер телефону {} в форматі 0503305464'.format(msg))
        for i in cell:
            if i in string.punctuation:
                cell = cell.replace(i, '')
        if cell[0] != '0' and len(cell) != 10:
            print('Не вірно введно номер, введіть номер без пробілів і інших знаків')
        else:
            cellnumb.append('{} {} {} {}'.format(cell[0:3],cell[3:6],cell[6:8],cell[8:10]))
        if not ask('Бажаєте ввести додатковий номер телефону?'):
            return cellnumb


def check_email(msg):  # проверка e-mail адреса
    email_list = []
    while True:
        mail = input('Введіть контактний e-mail {} (приклад:ckt@ckt.in.ua)'.format(msg))
        mail = mail.strip()
        if ('@' in mail) and ('.' in mail):
            raw_list = mail.split('@')
            if len(raw_list) == 2:
                if raw_list[0].isalpha() and len(raw_list[0]) > 2:
                    part_raw = raw_list[1].split('.')
                    if (part_raw[0].isalpha() and len(part_raw[0]) >= 2) and (part_raw[1].isalpha() and len(part_raw[1]) >= 2):
                        email_list.append(mail)
        else:
            print('Щось пішло не так,спробуйте ще раз')

        if not ask('Бажаєте ввести додатковий e-mail?'):
            return email_list


def check_curator():  # данные куратора(представителя) клиента
    curator = check_full_name('куратора (представника) з боку клієнта')
    curator_cell = check_cell_numb('куратора (представника) з боку клієнта')
    curator_mail = check_email('куратора (представника) з боку клієнта')
    return 'Куратор з боку клієнта: \nПІБ:{} \nКонтактні номери телефонів: {}\nКонтактні e-mail(и) куратора: {}'.format(curator, "; ".join(curator_cell), "; ".join(curator_mail))


def check_pay_form():  # проверка формы оплаты
    while True:
        try:
            pay_form = int(input('введіть форму оплати 1 або 2'))
        except ValueError:
            print('це не цифра пробуйте ще')
        else:
            if pay_form != 1 and pay_form != 2:
                print('варіантів всього два, вибачте')
            else:
                return pay_form


def check_name_company():
    while True:
        form_comp = input('Введіть тип компанії, наприклад: ТОВ, ПРАТ, ФОП, ЗАТ і т.д.')
        if len(form_comp) < 2 or len(form_comp) > 4:
            print('Занадто довга або коротка назва типу, від 2 до 4 символів')
        else:
            name_comp = input('Введіть назву компанії')
            return '{} "{}"'.format(form_comp,name_comp)


def check_name_gps():
    while True:
        name_gps = input('Оберіть виробника Bitrek або Глобус, натисніть В або Г')
        if name_gps.upper() == 'В' or name_gps.upper() == 'B':
            return 'Bitrek'
        elif name_gps.upper() == 'Г':
            return 'Глобус'
        else:
            print('Щось не те ввели введіть або В або Г')


def check_gps_rec_numb(name):
    if name == 'Bitrek':
        msg = 'Введіть номер реєстратору (15 цифр)'
        while True:
            gps_rec_numb = input(msg)
            if not gps_rec_numb.isnumeric() or len(gps_rec_numb) != 15:
                print('Допустимі тільки цифри та кількість 15')
            else:
                return gps_rec_numb
    else:
        while True:
            msg = 'Введіть номер реєстратору (від 4 до 5 цифр)'
            gps_rec_numb = input(msg)
            if gps_rec_numb.isnumeric() and (len(gps_rec_numb) == 4 or len(gps_rec_numb) == 5):
                return gps_rec_numb
            else:
                print('Допустимі тільки цифри та кількість 4 або 5')


def check_name_sim():
    while True:
        name_sim = input('Оберіть оператора Kiyvstar, TravelSim, або Lifecell, натисніть K,T або L')
        if name_sim.upper() == 'K' or name_sim.upper() =='К':
            return 'Kiyvstar'
        elif name_sim.upper() == 'Т' or name_sim.upper() == 'T':
            return 'TravelSim'
        elif name_sim.upper() == name_sim.upper() == 'L':
            return 'Lifecell'
        else:
            print('Щось не те ввели введіть або K або T або L')


def check_sim_numb(name):
    while True:
        if name == 'TravelSim':
            msg = 'Введіть номер sim (11 цифр)'
            sim_numb = input(msg)
            if not sim_numb.isnumeric() or len(sim_numb) != 11:
                print('Допустимі тільки цифри та кількість 11')
            else:
                return '+3{}'.format(sim_numb)
        else:
            msg = 'Введіть номер sim (9 цифр)'
            sim_numb = input(msg)
            if not sim_numb.isnumeric() or len(sim_numb) != 9:
                print('Допустимі тільки цифри та кількість 9')
            else:
                return '+{}'.format(sim_numb)


def check_fls_mark():
    fls_mark_list = ['H4','Н4','H7','Н7','H10','Н10','H20','Н20', 'D4', 'D7','D10','D20']
    while True:
        fls_mark = input('Введіть маркування ДВРП, наприклад "Н7" або "D7"')
        if fls_mark.upper() not in fls_mark_list:
            print('не існує такого маркування ДВРП, спробуйте ще')
        else:
            return fls_mark


def check_fls_numb():
    while True:
        fls_numb = input('введіть серійний номер ДВРП')
        if not fls_numb.isnumeric() or len(fls_numb) !=5:
            print('Допустимі тільки цифри та кількість 5')
        else:
            return fls_numb


def check_rate_price():
    while True:
        try:
            rate_price = int(input('Введіть вартість тарифу за місяць'))
            if rate_price > 0:
                return rate_price
            else:
                print('Вартість не може бути менше 0')
        except:
            print('Потрібно вводити тільки цифри')
