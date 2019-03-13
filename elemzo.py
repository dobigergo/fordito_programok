#vilmos12>=231<>péter(*{izé}**){nem} --- <azonosító><nagyobbegyenlő><szám><nemegyenlő><azonosító><kommentár(**)><kommentár{}>

false=False
true=True
str=input()
atmenet_vektor=["","","{","}","(","*",")",":","=","<",">"," "]
atmenet={
"start" : [2,4,6,19,8,19,19,12,19,14,17,1,19,21,false,true],
"azonosító": [2,2,3,3,3,3,3,3,3,3,3,3,3,3,false,true],
"<azonosító>":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,true,false],
"szám":[5,4,5,5,5,5,5,5,5,5,5,5,5,5,false,true],
"<szám>":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,true,false],
"{}":[6,6,6,7,6,6,6,6,6,6,6,6,6,19,false,true],
"<{} kommentár>":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,false,false],
"<(>":[20,20,20,20,20,9,20,20,20,20,20,20,20,19,false,true],
"(*-t talált":[9,9,9,9,9,10,9,9,9,9,9,9,9,19,false,true],
"*-t talált":[9,9,9,9,9,10,11,9,9,9,9,9,9,19,false,true],
"<(**) komment>":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,false,false],
"<kettőspont>":[20,20,20,20,20,20,20,20,13,20,20,20,20,19,false,true],
"<egyenlő>":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,false,false],
"<kisebb>":[20,20,20,20,20,20,20,20,15,20,16,20,20,19,false,true],
"<kisebbegyenlő>":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,false,false],
"<nemegyenlő>":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,false,false],
"<nagyobb>":[20,20,20,20,20,20,20,20,18,20,20,20,20,19,false,true],
"<nagyobbegyenlő>":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,false,false],
"hibakezelő":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,false,false],
"továbblépés":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,true,false],
"stop":[1,1,1,1,1,1,1,1,1,1,1,1,1,1,false,true]
}
allapot=list(atmenet.keys())
outputt=0
index_oszlop=0
index_sor=0
i=0
result=""
hibakod=0
tovabblep=False
visszalep=False
while i in range(len(str)+1):
	if i in range(len(str)) and str[i].isalpha():
		index_oszlop=0
	elif i in range(len(str)) and str[i].isdecimal():
		index_oszlop=1
	elif i in range(len(str)):
		index_oszlop=11
		for j in range(len(atmenet_vektor)):
			if atmenet_vektor[j]==str[i]:
				index_oszlop=j
	else:
		index_oszlop=13
	
	
	tovabblep=atmenet[allapot[index_sor]][15]
	visszalep=atmenet[allapot[index_sor]][14]
	index_sor=atmenet[allapot[index_sor]][index_oszlop]-1

	if index_sor in [2,4,6,7,10,11,12,13,14,15,16,17]:
		outputt=index_sor
	elif index_sor in [5,7,8,9,10,11,12,13,14,15,16,17]:
		hibakod=index_sor
	if tovabblep:
		i+=1
	if visszalep:
		i-=1
	if index_sor==0 and outputt!=0:
		result+=list(atmenet.keys())[outputt]
	elif index_sor==18:
		result+="<szintaktikai hiba a {}-részen>".format(list(atmenet.keys())[hibakod])
		
print(result)
		
	