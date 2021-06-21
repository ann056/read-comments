data = []
count = 0
with open('reviews.txt', 'r') as reviews:
	for line in reviews:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
# 計算平均留言字數
sum_len = 0
for c in data:
	sum_len += len(c)
print('平均留言字數為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('留言字數小於100字，總共有', len(new), '筆')