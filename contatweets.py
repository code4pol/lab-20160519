import json

f = open('50linhasfd.txt')

total = {}
for l in f:
	# print(l)
	if l[0] == '{':
		obj = json.loads(l)
		u = obj['user']['screen_name']
		# print(u, end=' - ')
		if u in total:
			# print(total[u])
			total[u] = total[u] + 1
		else:
			# print(0)
			total[u] = 1

for k in total:
	print(k,total[k],'tweets')