def cyk(b,r):
	triangle=[]
	
	for i in range(len(b)):
		triangle.append([])
		for j in range(len(b)):
			triangle[i].append([])
			
	
	
	for i in range(len(b)):
		counter = 0
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
	
	
	for i in range(len(b),0,-1):
		print(" "*i, end=" ")
		for j in range(len(b)-i):
			print("[", end=" ")
			if len(triangle[i][j])==0:
					print("-- ",end=" ")
			for k in triangle[i][j]:
					print(k + " ",end=" ")
			print("]",end=" ")
		print()
		
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