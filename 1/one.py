# Задача 1
# Шахов Кирилл
 # 2 курс
# Задача - Вычислите сумму цифр данного натурального числа

def enter():  #ф. для ввода числа
    number = int(input("Enter the number = "))
    return number

def sum_number(number):  #ф. для подсчета суммы чифр числа, на вход подается число, на выходе выдается сумма
	number = str(number)
	sum = 0
	for ch in number:
		sum = sum + int(ch)
	return sum

def out(number):
	print("Sum of numbers {} = {}".format(number, sum_number(number)))

out(sum_number(enter()))
