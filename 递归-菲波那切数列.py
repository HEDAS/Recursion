#问题：
#输出斐波那契数列：F(0)=0，F(1)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*）
#1 1 2 3 5 8 13...(从第三个数开始，它的值等于前两个数相加)
def fibonacci(n):
	if n==1 or n==2:
		return 1
	else:
		return fibonacci(n-1)+fibonacci(n-2)
for i in range(1,11):
	print(fibonacci(i),end=' ')
