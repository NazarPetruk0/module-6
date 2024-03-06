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
        if not (value.isdigit() or len(value) == 10):
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
        return None

    def remove_phone(self,phone:str):
        self.phones.remove(self.find_phone(phone))

def edit_phone(self, old_phone:str, new_phone:str):
    if self.find_phone(old_phone):
        self.remove_phone(old_phone)
        self.add_phone(new_phone)
    else:
        raise ValueError
    
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
