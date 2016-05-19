import json

f = open('50linhasfd.txt')

total = {}
for l in f:
	# print(l)
	if l[0] == '{':
		obj = json.loads(l)

		id_original = obj['id']

		if "retweeted_status" in obj:
			id_retweetado = obj["retweeted_status"]['id']
		
			print(id_original,'retweetou',id_retweetado)

			if id_retweetado in total:
				total[id_retweetado] = total[id_retweetado] + 1
			else:
				total[id_retweetado] = 1

		else:
			print(id_original,'nao eh um retweet')

for k in total:
	print(k,total[k],'retweets')