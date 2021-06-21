data = []
count = 0
with open('reviews.txt', 'r') as reviews:
	for line in reviews:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(data)
print(len(data))
print(data[3])