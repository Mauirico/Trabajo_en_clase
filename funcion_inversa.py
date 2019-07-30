import numpy as np 
def gauss(a,b):
	n=len(b)
	c=np.concatenate([a,b],axis=1)
	for e in range (n):
		T=c [e,e]
		for j in range (e,n+1):
			[e,j]=c[e,j]/T
			for i in range (e+1,n):
				t=c[i,e]
				for j in range (e,n+1):
					c[i,j]=c[i,j]-T*c[e,j]
	x=np.zeros([n,1])
	x[n-1]=c[n-1,n]
	for i in range(n-2,-1-1):
		s=0
		for j in range (i+1,n):
			s=s+c[i,j]*x[j]
	x[i]=c[i,n]-s
	return x
