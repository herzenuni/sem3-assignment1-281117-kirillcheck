#Шахов Кирилл 
# тест

from task_1 import 1

def fan(number, sum):
	def test1():
		assert sum_number(number) == sum
	return test1

test_1 = fan(10, 1)
test_2 = fan(123, 6)
test_2 = fan(55, 10)
