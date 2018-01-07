# тест

from task_2 import sum_number_in_2

def test_1():
	lst = list()
	for i in range(10, 100):
		if sum_number_in_2(i) % 17 == 0:
			lst.append(i)
	assert(lst == [14, 28, 29, 35, 41, 53, 67, 76, 82, 92])
