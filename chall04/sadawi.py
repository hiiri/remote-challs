#! /usr/bin/python3

i = int(input())

arr = []
for j in range(i):
	arr.append(list(input()))

flag = 1
while flag:
	flag = 0
	for j in range(i -2, -1, -1):
		for k, c in enumerate(arr[j]):
			if c == '.':
				if arr[j+1][k] == ' ':
					arr[j][k] = ' '
					arr[j+1][k] = '.'
					flag = 1

for lst in arr:
	for c in lst:
		print(c, end="")
	print()
