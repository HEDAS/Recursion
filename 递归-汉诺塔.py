#递归定义hanoi塔
#A表示开始桩，B表示中转桩，C表示终点桩
def hanoi(n,A,B,C):
	if n==1:
		print("Move %d from %s to %s"%(1,A,C))
	else:
		hanoi(n-1,A,C,B)
		print("Move %d from %s to %s"%(n,A,C))
		hanoi(n-1,B,A,C)
		
hanoi(4,'A','B','C')
