number = 361527

target = 25
number_series = [1,1,2,4,5,10,11,23,25]

for i in range(7, target, 2):
	
	prevgroups = (i - 2, i - 4)
	numberfound = False

	for j in range(0, i, 1):
		steps = []
		# TWO
		if(j == 0 or j == (i/2)):
			if(j == 0):
				steps = (1, sum(prevgroups))
			else:
				steps = (1, sum(prevgroups) + 2)
		# THREE
		elif(j == i - 1 or j == (i/2) - 1):
			if(j > i/2):
				steps = (1, sum(prevgroups) + 3, sum(prevgroups) + 4)
			else:
				steps = (1, sum(prevgroups) + 1, sum(prevgroups) + 2)
		# FOUR
		else:
			if(j == 1 or j == i/2 + 1):
				if(j < i/2):
					steps = (1, 2, sum(prevgroups), sum(prevgroups) + 1)
				else:
					steps = (1, 2, sum(prevgroups) + 2, sum(prevgroups) + 3)
			else:
				if(j < i/2):
					steps = (1, sum(prevgroups), sum(prevgroups) + 1, sum(prevgroups) + 2)
				else:
					steps = (1, sum(prevgroups) + 2, sum(prevgroups) + 3, sum(prevgroups) + 4)

		sum_to_add = 0
		for val in steps:
			sum_to_add += number_series[len(number_series)-val]
		number_series.append(sum_to_add)

		if(sum_to_add > number):
			print sum_to_add
			numberfound = True
			break

	if(numberfound):
		break

'''
1

1 [1] 1
2 [1, 2] 2
4 [1, 2, 3] 3

5 [1, 4] 2
10 [1, 2, 5] 3
11 [1, 6] 2
23 [1, 2, 6, 7] 4
25 [1, 7, 8] 3

26 [1, 8] 2
54 [1, 2, 8, 9] 4
57 [1, 9, 10] 3
59 [1, 10] 2
122 [1, 2, 10, 11] 4
133 [1, 10, 11, 12] 4
142 [1, 11, 12] 3

147 [1, 12] 2
304 [1, 2, 12, 13] 4
330 [1, 12, 13, 14] 4
351 [1, 13, 14] 3
362 [1, 14] 2
747 [1, 2, 14, 15] 4
806 [1, 14, 15, 16] 4
... [1, 14, 15, 16] 4
... [1, 15, 16] 3
'''