# Задача 1
# ШаховКирилл
 # 2 курс
# Задача - Найдите все двузначные и трехзначные числа, сумма квадратов цифр которых делится на 17

def sum_number_in_2(number):
	number = str(number)
	sum = 0
	for ch in number:
		sum = sum + int(ch) ** 2
	return sum

def fun():
	n = int(input("n = "))
	print("{}значные числа, сумма квадратов цифр которых делится на 17:". format(n))
	for i in range(10 ** (n - 1), 10 ** n):
		if sum_number_in_2(i) % 17 == 0:
			print(i, end = ', ')
	print()

	fun()
