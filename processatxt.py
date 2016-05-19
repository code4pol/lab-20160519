import json

f = open('50linhasfd.txt')

for l in f:
	# print('[',l,']',end='')
	if l[0] == '{':
		obj = json.loads(l)
		identificador = obj['id']
		usuario = obj['user']['screen_name']
		texto = obj['text']

		try:
			r = texto.index('rua')
		except:
			r = ''

		if r:	
			print('%s,%s,"%s"' % (identificador,usuario,texto))


