from collections import UserDict
from datetime import datetime as dtdt

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not (value.isdigit() and len(value) == 10):
            raise ValueError
        self.value=value

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = dtdt.strftime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError
        
    def __str__(self):
        return self.value.strftime('%d.%m.%Y')

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        ph = Phone(phone)
        self.phones.append(ph)
        return ph

    def add_birthday(self, birthday:str):
        self.birthday = Birthday(birthday)

    def get_upcoming_birthdays(self):
        return []

    def find_phone(self, phone:str):
        for ph in self.phones:
            if ph.value == phone:
                return ph
        return ph

    def remove_phone(self, phone):
        ph = self.find_phone(phone)
        if ph:
            self.phones.remove(ph)
        else:
            raise ValueError("Phone not found")

    def edit_phone(self, old_phone, new_phone):
        old_ph = self.find_phone(old_phone)
        if old_ph:
            if not (new_phone.isdigit() and len(new_phone) == 10):
                raise ValueError("Invalid new phone number")
            old_ph.value = new_phone
        else:
            raise ValueError("Phone not found")
    
    def __str__(self):
        return f"Contact name: {str(self.name)}, phones: {'; '.join(str(p) for p in self.phones)}, birthday"

class AddressBook(UserDict):
    def add_record(self, record:Record):
        self.data[record.name.value] = record
        return record

    def delete(self, name:str):
        if self.find(name):
            del self.data[name]

    def find(self, name:str):
        return self.data.get(name)
