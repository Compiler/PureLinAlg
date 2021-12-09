[(i, j, k) for i in {-4, -2, 1, 2, 5, 0} for j in {-4, -2, 1, 2, 5, 0} for k in {-4, -2, 1, 2, 5, 0} if i + j + k == 0 and not (i ==0 and j == 0 and k ==0)][0]

[x for x in range(100) if x % 2 == 1]

L = ['A','B','C','D','E']
list(zip(range(5), L))

dlist = [{'Bilbo':'Ian','Frodo':'Elijah'}, {'Bilbo':'Martin','Thorin':'Richard'}]
k = "Frodo"

[dlist[i][k] if k in dlist[i] else "NOT PRESENT" for i in range(len(dlist))]


{x:x**2 for x in range(99)}


D ={'red','white','blue'}
