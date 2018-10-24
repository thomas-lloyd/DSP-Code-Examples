#Import numerical python library
import numpy as np
#Define input data
x=np.array([2,1,-1,-2,3])
h=np.array([4,2,1,0.5])
# Two ways of computing convolution...
#--------------------------------------
# Method 1, the easy way
#--------------------------------------
#Use Numpy's version
y=np.convolve(x,h);
#print values
print("Easy method: ")
print(y);
#--------------------------------------
# Method 2, the manual way
#--------------------------------------
# convolution length N+M-1
conLen=len(x)+len(h)-1
# zero pad x for time reversal
x=np.pad(x,len(h)-1,mode='constant',constant_values=0);
#initialise output array
y=np.zeros(conLen);
#Perform convolution
#the first loop starts at the end of the zero pad region in x
for n in range(len(h)-1,conLen+len(h)-1):
	y[n-(len(h)-1)]=0;
	for k in range(len(h)):
		y[n-(len(h)-1)]+=h[k]*x[n-k];
#print values
print("Manual method: ")
print(y)