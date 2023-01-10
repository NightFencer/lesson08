# -*- coding: utf-8 -*-
# from def_oprint import oprint
from colorama import Fore
from random import randint


# oprint('ghjk','red')

class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.mud = 0
        self.cats_food = 30

    def __str__(self):
        self.mud += 5
        return 'В доме денег: {},  еды в холодильнике: {},  для кота: {}, грязи:{}'.format(self.money, self.food,
                                                                                           self.cats_food, self.mud)
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
        self.sex = None

    def eat(self):
        if self.house.food >= 30:
            self.fullness += 40
            self.house.food -= 30

            print(Fore.CYAN+'{} сегодня уничтожал'.format(self.name)+aa+' еду', Fore.RESET)
        elif self.house.food > 0:
            self.fullness += self.house.food + 10
            self.house.food = 0

            print('{} сегодня уничтожал'.format(self.name)+aa+' еду')
        else:
            print(Fore.YELLOW+'{} хочет есть, но еды нет'.format(self.name))

    def kissing_cat(self):
        self.happyness +=5
        print(Fore.LIGHTYELLOW_EX+f'{self.name} гладил'+aa+' кота', Fore.RESET)

    def act(self):
        global aa
        if self.sex == 'male':
            aa = ''
        else:
            aa = 'a'
        if self.life:
            if self.fullness <= 0:
                self.life = False
                print(Fore.RED+'{} умер от голода'.format(self.name))
                return
            elif self.happyness < 10:
                self.life = False
                print(Fore.RED+f'{self.name} покинул'+aa+' этот мир из-за тоски')
                return
        self.fullness -= 10

    def __str__(self):
        if self.life:
            self.days += 1
            #print(self.__class__.__name__)
            if self.house.mud > 50:
                self.happyness -= 10
                #print(Fore.RED+f'грязновато становится. уже {self.house.mud}', Fore.RESET)
                if self.__class__.__name__ == 'Child':
                    self.happyness = 100
                    #print('я ребенок, мне пох на грязь')



            return 'Я {} {} - сытость {}, счастья {}'.format(self.role, self.name, self.fullness, self.happyness)
        else:

            return '{} умер {} дней назад'.format(self.name, day - self.days)


class Husband(Men):

    def __init__(self, name):
        super().__init__(name=name)
        self.role = 'муж, объелся груш,'
        self.sex = 'male'

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
            elif dice < 3:
                self.work()
            elif dice > 4:
                self.gaming()
            else:
                self.kissing_cat()

            pass

    def eat(self):
        super().eat()

        pass

    def work(self):
        global working_days, total_money
        self.house.money += 150
        print('{} сегодня работал на стройке'.format(self.name),aa)
        working_days += 1
        total_money += 150
        pass

    def gaming(self):
        global gaming_days
        self.happyness += 20
        gaming_days +=1
        print('{} весь день играл в танчики'.format(self.name),aa)

        pass


class Wife(Men):

    def __init__(self, name):
        super().__init__(name=name)
        self.role = 'жена, нахрен не нужна,'
        self.sex = 'female'

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

            elif dice < 3:
                self.shopping()
            elif dice > 4:
                self.clean_house()
            else:
                self.kissing_cat()

            pass

    def eat(self):
        super().eat()
        pass

    def shopping(self):
        global total_food
        if self.house.money > 70:
            self.house.food += 60
            self.house.cats_food += 10
            self.house.money -= 70
            total_food += 70
        else:
            self.house.food += self.house.money
            total_food += self.house.money
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
        print(Fore.LIGHTGREEN_EX+f'{self.name} весь день убиралась в доме',Fore.RESET)
        cleaning_days += 1
        pass


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.life = True
        self.house = home
        self.sex = None
        pass

    def __str__(self):
        if self.life:
            return f'я {self.name} сытость:{self.fullness}'
        else:
            return f'{self.name} давно закопан за баней'

    def act(self):
        global aa
        if self.sex == 'male':
            aa = ''
        else:
            aa  = 'a'
        if self.fullness < 10:
            self.life = False
            return

        if self.life:
            dice = randint(1, 3)
            if self.fullness < 20:
                self.eat()
            else:
                if dice == 1:
                    self.sleep()
                elif dice == 2:
                    self.eat()
                else:
                    self.soil()
        self.fullness -= 10

        pass

    def eat(self):

        global a
        if self.house.cats_food > 0:
            self.fullness += 20
            self.house.cats_food -= 5
            print(f'{self.name} жрал'+aa+' свою кошачью еду')
        else:
            print(f'{self.name} хотел'+aa+' пожрать, но нет еды')

        pass

    def sleep(self):
        # self.fullness -=10
        global aa
        print(f'{self.name} сегодня спал'+aa,'весь день')
        pass

    def soil(self):
        # self.fullness -= 10
        global a
        self.house.mud += 5

        print(f'{self.name} сегодня драл'+aa+' обои')
        pass

class Child(Men):
    def __init__(self,name):
        super().__init__(name = name)
        self.name = name

        self.happyness = 100


    def __str__(self):
        return super().__str__()

    def sleep(self):
        print(f'{self.name} спал'+aa+' и никого не трогал'+aa)
        self.fullness -= 10

    def eat(self):
        print(Fore.CYAN+f'{self.name} ел'+aa+' весь день', Fore.RESET)
        self.fullness += 10
        self.house.food -= 10
        masha.happyness += 5
    def act(self):
        global aa
        if self.sex == 'male':
            aa = ''
        else:
            aa = 'a'

        #self.happyness =100
        if self.life:
            if self.fullness < 30:
                self.eat()
            elif self.fullness > 90:
                self.sleep()
            else:
                dice = randint(1,2)
                if dice == 1:
                    self.eat()
                else:
                    self.sleep()


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
cat1 = Cat(name='Ржавая тварь')
cat1.sex = 'female'
cat2 = Cat(name='Упырь')
cat2.sex = 'male'
kolya = Child (name = 'Колян')
kolya.sex = 'male'
kolya.role = 'сын'

olya = Child (name= 'Оля')
olya.sex = 'female'
olya.role = 'дочь'

sonya = Child (name='Соня')
sonya.sex = 'female'
sonya.role = 'дочь'


fur_coat = 0
total_food = 0
total_mud = 0
working_days = 0
gaming_days = 0
cleaning_days = 0
total_money = 0
for day in range(1, 366):
    print(Fore.BLUE+'================== День {} =================='.format(day),Fore.RESET)


    serge.act()
    masha.act()
    kolya.act()
    olya.act()
    sonya.act()
    cat1.act()
    cat2.act()
    print(serge)
    print(masha)
    print(kolya)
    print(olya)
    print(sonya)
    print(cat1)
    print(cat2)
    print(home)
print(masha.name, 'купила {} шуб'.format(fur_coat))
print('Всего съедено пельменей - {}кг'.format(total_food - home.food))
print('Всего дней {}  {} гнил на работе и заработал {} деревянных'.format(working_days, serge.name, total_money))
print(f'Всего {gaming_days} дней {serge.name} играл на компе')
print("Всего {} дней {} провела с шваброй и вывезла {}кг грязи".format(cleaning_days, masha.name, total_mud))
