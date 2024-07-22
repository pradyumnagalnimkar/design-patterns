from abc import ABC, abstractmethod


class User:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.age = 24
        self.phone_number = ''
        self.address = ''
        self.email_address = ''

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def get_phone_number(self):
        return self.phone_number

    def get_address(self):
        return self.address

    def get_email_address(self):
        return self.email_address


class UserBuilder(ABC):
    @abstractmethod
    def set_first_name(self):
        pass

    @abstractmethod
    def set_last_name(self):
        pass

    @abstractmethod
    def set_age(self):
        pass

    @abstractmethod
    def set_phone_number(self):
        pass

    @abstractmethod
    def set_address(self):
        pass

    @abstractmethod
    def set_email_address(self):
        pass


class CustomUserBuilder(UserBuilder):
    def __init__(self):
        self.user = User()

    def set_first_name(self, first_name):
        self.user.first_name = first_name

    def set_last_name(self, last_name):
        self.user.last_name = last_name

    def set_age(self, age):
        self.user.age = age

    def set_phone_number(self, phone_number):
        self.user.phone_number = phone_number

    def set_address(self, address):
        self.user.address = address

    def set_email_address(self, email_address):
        self.user.email_address = email_address


class UserDirector:
    def __init__(self, builder):
        self.builder = builder

    def create_user(self, props):
        self.builder.set_first_name(props["first_name"])
        self.builder.set_last_name(props["last_name"])
        self.builder.set_age(props["age"])
        self.builder.set_phone_number(props["phone_number"])
        self.builder.set_address(props["address"])
        self.builder.set_email_address(props["email_address"])


props = {
    "first_name": "Ram",
    "last_name": "Joshi",
    "age": 27,
    "phone_number": "9876543210",
    "address": "Delhi, India",
    "email_address": "ram.joshi@domain.com"
}

expected_props = {
    "first_name": "Ram",
    "last_name": "Joshi",
    "age": 27,
    "phone_number": "9876543210",
    "address": "Delhi, India",
    "email_address": "ram.joshi@domain.com"
}

builder = CustomUserBuilder()
director = UserDirector(builder)
director.create_user(props)
user = builder.user
print(user.get_first_name())
print(user.get_last_name())
print(user.get_age())
print(user.get_phone_number())
print(user.get_address())
print(user.get_email_address())
assert user.__dict__ == expected_props

