from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a non-empty string.")
        super().__init__(value.strip())

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        value_str = str(value).strip()
        if not (value_str.isdigit() and len(value_str) == 10):
            raise ValueError("Phone number must contain exactly 10 digits.")
        super().__init__(value_str)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_str = str(phone).strip()
        for i, p in enumerate(self.phones):
            if p.value == phone_str:
                del self.phones[i]
                return
        raise ValueError(f"Phone {phone_str} not found.")

    def edit_phone(self, old_phone, new_phone):
        old_str = str(old_phone).strip()
        new_obj = Phone(new_phone)
        for i, p in enumerate(self.phones):
            if p.value == old_str:
                self.phones[i] = new_obj
                return
        raise ValueError(f"Phone {old_str} not found.")

    def find_phone(self, phone):
        phone_str = str(phone).strip()
        for p in self.phones:
            if p.value == phone_str:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(str(name).strip())

    def delete(self, name):
        key = str(name).strip()
        if key not in self.data:
            raise KeyError(f"Contact {key} not found.")
        del self.data[key]

book = AddressBook()

john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

book.add_record(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

for name, record in book.data.items():
    print(record)

john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)

found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")

book.delete("Jane")