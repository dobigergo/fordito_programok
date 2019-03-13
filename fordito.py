#Dömösi Pál
#domosi@unideb.hu
#30/944-9622
#lexikális elemző -> lexéma/token <---> táblázatelemző (azonosítók, konstansok, címkék)
#kulcsok -- begin,end,do,if,else
#-----------------------------------------------------------------------------------------
#www.martinbroadhust.com/cyk-algorithm-in-c
#vilmos12>=231<>péter(*{izé}**){nem} --- <azonosító><nagyobbegyenlő><szám><nemegyenlő><azonosító><kommentár(**)><kommentár{}>
#kell egy bemeneti szabályrendszer



def cyk(b,r):

	triangle=[[[],[],[],[],[],[],[]],[[],[],[],[],[],[],[]],[[],[],[],[],[],[],[]],[[],[],[],[],[],[],[]],[[],[],[],[],[],[],[]],[[],[],[],[],[],[],[]],[[],[],[],[],[],[],[]]]
	
	
	for i in range(len(b)):
		counter=0	
		for j in r:
			value = b[i]
			if value in r[j]:
				triangle[0][i].append(list(r.keys())[counter])
			counter += 1
				
	
	s=1
	for s in range(len(b)):
		for o in range(len(b)-s):
			for f in range(s):
				for d in triangle[s-1-f][o]:
					for d2 in triangle[f][s+o-f]:
						result=d + d2
						counter = 0
						for j in r:
							if result in r[j]:
								triangle[s][o].append(list(r.keys())[counter])
							counter += 1
	
	for i in triangle:
		print(i)
		
	if( "S" in triangle[6][0]):
		print("a szó levezethető")
	else:
		print("a szó nem vezethető le")
			
ruledict={
	"S": ["AB", "CD", "CB", "SS"],
	"A": ["BC", "1"],
	"C": ["DD", "0"],
	"B": ["SC", "0"],
	"D": ["BA"]
}

bemenet=["1","1","0","0","1","0","1"]


cyk(bemenet,ruledict)