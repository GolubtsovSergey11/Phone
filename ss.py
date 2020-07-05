def islover(lover_contact):
    if lover_contact == False:
        return 'Нет'
    else:
        return lover_contact


class Phone_Book:

    def __init__(self, name):
        self.name_tel_book = name
        self.contact_book = []

    def __add__(self, other):
        self.contact_book.append(other)

    def all_contact(self):
        for contact in self.contact_book:
            print(contact)

    def del_contact(self, tel_number):
        i = 0
        for contact in self.contact_book:
            if contact.get_tel_number() == tel_number:
                del(self.contact_book[i])
            i += 1

    def search_for_a_contact(self, name):
        for names in self.contact_book:
            if names.get_name() == name:
                return names

    def search_lover(self, lover_number):
        contacts_with_lover_numbers = []
        for contact in self.contact_book:
            if contact.get_lover() == lover_number:
                contacts_with_lover_numbers.append(contact)
        for contacts in contacts_with_lover_numbers:
            print(contacts)

class Contact:

    def __init__(self, name, surname, tel_number, lover_contact=False, **kwargs):
        self.dict_contact = {}
        self.dict_contact['Имя'] = name
        self.dict_contact['Фамилия'] = surname
        self.dict_contact['Номер телефона'] = tel_number
        self.dict_contact['Избранный контакт'] = islover(lover_contact)
        self.dict_contact['Дополнительная информация'] = kwargs

    def get_lover(self):
        return  self.dict_contact['Избранный контакт']

    def get_name(self):
        return self.dict_contact['Имя']

    def get_surname(self):
        return self.dict_contact['Фамилия']

    def get_tel_number(self):
        return self.dict_contact['Номер телефона']

    def __str__(self):
        for key, value in self.dict_contact.items():
            print(f'{key}: {value}')
        return ''


#number = int(input('Введите номер телефона: '))
Sergey = Contact('Сергей', 'Голубцов', 89118887766, 44455545454, email='sergey.ru', sait='sergey.ru')
Mila = Contact('Мила', 'Виноградова', 899997778866, email='mila.ru', sait='mila.ru', job='IT')
Vova = Contact('Владимир', 'Кузнецов', 89997776655, email='vova.com', sait='vova.com')
Ivan = Contact('Иван', 'Иванов', 81116655111, email='ivan.ru', sait='ivan.ru')
Anton = Contact('Антон', 'Антонов', 89993338866, email='anton.ru', sait='anton.ru', job='IT')
Petr = Contact('Петр', 'Петров', 8999711111, email='petr.com', sait='petr.ru')



first_book = Phone_Book('contact book')
first_book.__add__(Mila)
first_book.__add__(Sergey)
first_book.__add__(Vova)
first_book.__add__(Ivan)
first_book.__add__(Anton)
first_book.__add__(Petr)


first_book.del_contact(89997776655)
first_book.all_contact()
print(first_book.search_for_a_contact('Мила'))
first_book.search_lover(44455545454)

