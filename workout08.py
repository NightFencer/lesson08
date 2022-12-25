# -*- coding: utf-8 -*-
from def_oprint import oprint
from termcolor import cprint, colored
from random import randint


# oprint('ghjk','red')

class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.mud = 0

    def __str__(self):
        self.mud += 5
        return 'В доме денег: {}  еды в холодильнике: {} грязи:{}'.format(self.money, self.food, self.mud)
        pass


class Men:

    def __init__(self, name):
        self.role = None
        self.name = name
        self.house = home
        self.fullness = 30
        self.happyness = 100
        self.life = True
        self.days = 0

    def eat(self):
        if self.house.food >= 30:
            self.fullness += 40
            self.house.food -= 30
            print('{} сегодня уничтожал еду'.format(self.name))
        elif self.house.food > 0:
            self.fullness += self.house.food + 10
            self.house.food = 0

            print('{} сегодня уничтожал еду'.format(self.name))
        else:
            print('{} хочет есть, но еды нет'.format(self.name))

    def act(self):
        if self.life:
            if self.fullness <= 0:
                self.life = False
                print('{} умер от голода'.format(self.name))
                return
            elif self.happyness < 10:
                self.life = False
                print('{} покинул этот мир из-за тоски'.format(self.name))
                return
        self.fullness -= 10


    def __str__(self):
        if self.life:
            self.days += 1
            if self.house.mud > 50:
                self.happyness -= 10
                print('грязновато становится. уже {}'.format(self.house.mud))
                print(f'грязновато становится. уже {self.house.mud}')
                oprint('----------------------', 'red')
            return 'Я {} {} - сытость {}, счастья {}'.format(self.role, self.name, self.fullness, self.happyness)
        else:

            return '{} умер {} дней назад'.format(self.name, day - self.days)


class Husband(Men):

    def __init__(self, name):
        super().__init__(name=name)
        self.role = 'муж, объелся груш,'

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()

        if self.life:
            # cf   global dice
            dice = randint(1, 6)

            if self.fullness < 20 and self.house.food > 0:
                self.eat()
            elif self.happyness < 20:
                self.gaming()
            elif home.money < 100:
                self.work()
            elif dice < 4:
                self.work()
            elif dice > 3:
                self.gaming()
            else:
                self.eat()

            pass

    def eat(self):
        super().eat()

        pass

    def work(self):
        global working_days, total_money
        self.house.money += 150
        print('{} сегодня работал на стройке'.format(self.name))
        working_days += 1
        total_money += 150
        pass

    def gaming(self):
        self.happyness += 20
        print('{} весь день играл в танчики'.format(self.name))

        pass


class Wife(Men):

    def __init__(self, name):
        super().__init__(name=name)
        self.role = 'жена, нахрен не нужна,'

        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        if self.life:
            dice = randint(1, 6)

            if self.fullness < 20 and self.house.food > 0:
                self.eat()
            elif home.food < 100:
                self.shopping()
            elif self.house.mud > 70:
                self.clean_house()
            elif self.house.money > 340:
                self.buy_fur_coat()

            elif dice < 4:
                self.shopping()
            elif dice > 3:
                self.clean_house()
            else:
                self.eat()

            pass

    def eat(self):
        super().eat()
        pass

    def shopping(self):
        global total_food
        if self.house.money > 70:
            self.house.food += 70
            self.house.money -= 70
            total_food +=70
        else:
            self.house.food += self.house.money
            total_food +=self.house.money
            self.house.money = 0

        print('{} сегодня ходила в пятёрочку и затарилась едой'.format(self.name))
        pass

    def buy_fur_coat(self):
        global fur_coat
        if self.house.money > 340:
            self.house.money -= 350
            self.happyness += 60
            fur_coat += 1
            print('{} безмерно счастлива. Ей привалила новая шуба'.format(self.name))
        else:
            print('{} хотела купить шубу, но денег всего {}'.format(self.name, self.house.money))
        pass

    def clean_house(self):
        global cleaning_days, total_mud
        if self.house.mud >= 100:
            self.house.mud -= 100
            total_mud += 100
        else:
            total_mud += self.house.mud
            self.house.mud = 0
        print('{} весь день убиралась в доме'.format(self.name))
        cleaning_days += 1
        pass


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
fur_coat = 0
total_food = 0
total_mud = 0
working_days = 0
cleaning_days = 0
total_money = 0
for day in range(1, 366):
    print('================== День {} =================='.format(day))

    serge.act()
    masha.act()
    print(serge)
    print(masha)
    print(home)
print(masha.name, 'купила {} шуб'.format(fur_coat))
print('Всего съедено пельменей - {}кг'.format(total_food-home.food))
print('Всего дней {}  {} гнил на работе и заработал {} деревянных'.format(working_days, serge.name, total_money))
print("Всего {} дней {} провела с шваброй и вывезла {}кг грязи".format(cleaning_days, masha.name, total_mud))

