data = []
count = 0
# 計算留言長度，每100000次顯示一次
with open('reviews.txt', 'r') as reviews:
	for line in reviews:
		data.append(line)
		count += 1
		if count % 100000 == 0:
			print(len(data))
wc = {}
for line in data:
	words = line.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('請輸入想查詢的字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '顯示了', wc[word], '次')
	else:
		print('裡面沒有這個字！')
print('感謝使用本查詢功能')







# # 計算平均留言字數
# sum_len = 0
# for line in data:
# 	sum_len += len(line)
# print('平均留言字數為', sum_len / len(data))

# # 留言字數小於100
# new = []
# for line in data:
# 	if len(line) < 100:
# 		new.append(d)
# print('留言字數小於100字，總共有', len(new), '筆')

# # 提到good幾次
# good = []
# for line in data:
# 	if 'good' in line:
# 		good.append(line)
# print('一共有', len(good), '筆留言提到good')

# # 提到good留言的清單簡寫
# good = [ line for line in data if 'good' in line]
# print(len(good))

# # 提到bad留言的清單簡寫
# bad = ['bad' in line for line in data]

# # bad = []
# # for line in data:
# # 	bad.append('bad' in line)