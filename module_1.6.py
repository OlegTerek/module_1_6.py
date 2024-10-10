from example_1 import my_set

my_dict={'Boris': 2001, 'Alex': 2005,'Katya':2003} # создаю переменную и присваиваю ей словарь
print('Год рождения моих друзей:',my_dict)  # вывожу в консоль
print('Год рождения Бориса-', my_dict.get('Boris'),';','Год рождения Олега-',my_dict.get('Oleg','такого друга у вас нет.'))
my_dict['Denis']=2004
my_dict['Roman']=2002
remove_d=my_dict.pop('Katya')
print('Год рожденья бывшей подруги:', (remove_d))
print('Нынешние друзья:', my_dict)
# Работа с множествами
my_set={25,5,6,7,7,5,0,5,0,25,'numbers',(1,2,3,4)}
print(my_set)
my_set.add(8) #добавляю элементы множества
my_set.add(9)
my_set.add('decimal')
my_set.remove(25) #удаляю элемент из множества
print(my_set)
