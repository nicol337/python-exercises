
#unweighted, directed adjacency list
list1 = [[1,2],[2,3],[4],[],[0]]

for v_start in range(len(list1)):
	for v_end in list1[v_start]:
		print("{0} -> {1}".format(v_start, v_end))

#weighted, directed adjacency list
list2 = [{1:1,2:8},{2:1,3:4},{4:5},{},{0:10}]

for v_start in range(len(list2)):
	for v_end in list2[v_start]:
		print("{0} --{1}--> {2}".format(v_start,list2[v_start][v_end],v_end))


