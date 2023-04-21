n=6


str="hello, how are you, where you live, I live in Wellington"
list = []

word = str.split(" ")

for a in word:
	if len(a) > n:
		list.append(a)
		
print(list)