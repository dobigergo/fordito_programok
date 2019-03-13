import sys
import json

filename=open(sys.argv[1],"r")
text=filename.readline()

x=json.loads(text)

not_terminals=list(x.keys())
allapot_vekt=[]
symbols=[]
symbols.extend(list(x.keys()))
for i in not_terminals:
	for j in range(len(x[i])):
		for k in range(len(x[i][j])):
			if x[i][j][k] not in allapot_vekt and x[i][j][k] not in not_terminals:
				allapot_vekt.append(x[i][j][k])
				symbols.append(x[i][j][k])
symbols.append("#")
allapot_vekt.append("#")
print(symbols,allapot_vekt)			
rules={}
result=[]
counter=1
talalt=False
for i in not_terminals:
	for j in allapot_vekt:
		for k in x[i]:
			if k[0]==j:
				result.append("{},{}".format(k,counter))
				counter+=1
				talalt=True
		if talalt==False:
			result.append("error")
		talalt=False
	rules.update({i:result})
	result=[]
	
for i in allapot_vekt:
	for j in allapot_vekt:
		if j==i and j=="#":
			result.append("ok")
		elif j==i:
			result.append("pop")
		else:
			result.append("error")
	rules.update({i:result})
	result=[]
	
for i,j in rules.items():
	print(i,j)

bemenet=["a","a","b","b","d","c","c","#"]
gram=["S","#"]
steps=[]
message="ok"
sor_index=0
oszlop_index=0
index=0


while gram[0]!="#" and message!="error":
	sor_index=symbols.index(gram[0])
	oszlop_index=allapot_vekt.index(bemenet[0])
	if rules[symbols[sor_index]][oszlop_index] == "error":
		message="error"
	elif rules[symbols[sor_index]][oszlop_index] == "pop":
		gram.pop(0)
		bemenet.pop(0)
	else:
		index=gram.index(symbols[sor_index])
		gram.pop(index)
		for i in range(len(list(rules[symbols[sor_index]][oszlop_index].split(",")[0]))):
			gram.insert(index+i,list(rules[symbols[sor_index]][oszlop_index].split(",")[0])[i])
		steps.append(rules[symbols[sor_index]][oszlop_index].split(",")[1])
	print(bemenet,gram,steps)

print(message)	



