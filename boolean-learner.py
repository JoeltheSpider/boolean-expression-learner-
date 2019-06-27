import numpy as np
import matplotlib.pyplot as plt

X=list()    
Y=list()

# this is to generate binary codes for dimension(n)
def tobin(n):      
    out=[]
    for i in range(pow(2,n)):
        b = bin(i)[2:]
        b = str(0) * (n - len(b)) + b
        out.append(b)
    return out

#give binary output code and dimension(K) to return boolean expression
def boolean(code,K):    
    a=[]
    x=tobin(K)
    for i in range(K):
        a.append(chr(65+i))
    n = pow(2,K)
    temp=""
    for i in range(n):
        if(code[i]=='1'):
            if(temp!=""):
                temp+="+"
            for j in range(K):
                temp+=a[j]
                if(x[i][j]=='0'):
                    temp+='`'
    if(temp==""):
        temp='0'
    return temp
    
#Get inputs
K = int(input("Enter dimension:\t"))
n = int(input("Enter number of input:\t"))
print("Enter input and output:\n")

for i in range(n):
    data=input("Data point %d:"%(i+1))
    data=data.split()
    temp=list()
    for j in range(K):
        temp.append(data[j])
    Y.append(data[K])
    X.append("".join(temp))
Y="".join(Y)

#Genrate Hypothesis Space
H = tobin(pow(2,K))

#plotx - Data point axix | ploty - VS reduction axis |  
ploty=[len(H)]
ploty2=[0]
plotx=list(np.arange(len(X)+1))

#Initially Version Space = Hypothesis Space 
VS=H
for i in X:
    print("Consistent Hypothesis at data point ",X.index(i)+1,":\n")
    temp_hyp=list()
    for j in VS:
        if(j[int(i,2)]==Y[X.index(i)]):
            print(boolean(j,K))
            temp_hyp.append(j)
    VS=temp_hyp
    ploty.append(len(VS))
    ploty2.append(len(H)-len(VS))
    
#Plot Respective Graphs
plt.plot(plotx,ploty,'-o')
plt.ylim(0,max(ploty)+1)
plt.xlim(0,max(plotx)+1)
plt.title("No. of data points VS No. of Consistent Hypothesis")
plt.xlabel("No. of datapoints")
plt.ylabel("No. of Consistant Hypothesis")
plt.show()

plt.plot(plotx,ploty2,'-o')
plt.ylim(0,max(ploty2)+1)
plt.xlim(0,max(plotx)+1)
plt.title(" No. of data points VS No. of Hypothesis ruled out")
plt.xlabel("No. of datapoints")
plt.ylabel("No. of Hypothesis ruled out")
plt.show()