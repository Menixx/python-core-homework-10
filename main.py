from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Phone(Field):
    def __init__(self, value):
        str_phone = str(value)
        if len(str_phone) == 10 and str_phone.isdigit():
            self.value = str_phone
        else:
            msg = 'Номер не валідний'
            raise ValueError(msg)

    def __str__(self):
        return self.value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, *args):
        for value in args:
            self.phones.append(Phone(value))
    
    def remove_phone(self, *args):
        for value in args:
            phone = Phone(value)
            phone_values = [p.value for p in self.phones]

            if phone.value in phone_values:
                index = phone_values.index(phone.value)
                self.phones.remove(self.phones[index])

    def edit_phone(self, old_phone_value, new_phone_value):
        old_phone = Phone(old_phone_value)
        new_phone = Phone(new_phone_value)
        phone_values = [p.value for p in self.phones]

        if old_phone.value in phone_values:
            index = phone_values.index(old_phone.value)
            self.phones[index] = new_phone
        else:
            msg = 'Такого номеру не існує в книзі контактів'
            raise ValueError(msg)

    def find_phone(self, *args):
        for value in args:
            phone = Phone(value)
            phone_values = [p.value for p in self.phones]

            if phone.value in phone_values:
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)


# a = Record('ivan')
# # a.add_phone('1234567890')
# a.add_phone('0987654321')
# print(a)
# a.edit_phone('0987654321', 1234567890)
# print(a)

# Створення нової адресної книги
# book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567891", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# # Видалення запису Jane
# book.delete("Jane")
# for name, record in book.data.items():
#     print(record)
