from faker import Faker
from random import randint

fake = Faker('uk_UA')


class Human:
    human = {}

    def __init__(self):
        self.human["address"] = fake.address()
        self.human["phone number"] = fake.phone_number()
        self.human["job"] = fake.job()
        self.human.update({"salary": f'{randint(1000, 10000)}$'})

    def show_info(self):
        print('[*]')
        for key in self.human:
            print(f'<{key}> \n{self.human[key]}\n')


class Woman(Human):
    def __init__(self):
        self.human["woman name"] = fake.first_name_female()
        self.human["woman surname"] = fake.last_name_female()
        super().__init__()


class Man(Human):
    def __init__(self):
        self.human["man name"] = fake.first_name_male()
        self.human["man surname"] = fake.last_name_male()
        super().__init__()


woman = Human()
woman.show_info()
woman = Woman()
woman.show_info()
woman = Man()
woman.show_info()
