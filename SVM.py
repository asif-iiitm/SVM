##support vector machine python code by:

import numpy as np
import Read

from sklearn import svm
from sklearn.metrics import accuracy_score

###reading the input csv data

f=open("in1.csv")
arr=[]
arr2=[]
"""
for rows in f:
    fields=rows.split(",")
    
    count=1
    
    
    for field in fields:
        if field=='1':
            arr.append(count)
            count=1
            break
        else:
            count+=1
print arr
"""
Matrix = [[0 for x in range(14)] for x in range(300)] 
###Loading the Input
count=1
for rows in f:
    ctr=1
    ctr1=0
    fields=rows.split(",")
    
    i=0
    print fields[0]
    for field in fields:
        
        Matrix[count-1][ctr-1]=field
        arr.append(field)
        ctr+=1
        if ctr==15:
            break
        
    #arr2.append(arr)
    count+=1;
    if count==301:
        break

print Matrix
#np.X=arr2
print "done"    
#print arr2
#print arr2.count
arr3=[]
X=(arr2)
#X = np.loadtxt("in1.csv",delimiter=',')
y=[1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 19, 19, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 25, 25, 25, 25, 25, 25, 26, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 28, 29, 29, 29, 29, 29, 29, 30, 30, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31, 32, 32, 32, 32, 32, 32, 33, 33, 33, 33, 33, 33, 34, 34, 34, 34, 34, 34, 35, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 36, 37, 37, 37, 37, 37, 37, 38, 38, 38, 38, 38, 38, 39, 39, 39, 39, 39, 39, 40, 40, 40, 40, 40, 40, 41, 41, 41, 41, 41, 41, 42, 42, 42, 42, 42, 42, 43, 43, 43, 43, 43, 43, 44, 44, 44, 44, 44, 44, 45, 45, 45, 45, 45, 45, 46, 46, 46, 46, 46, 46, 47, 47, 47, 47, 47, 47, 48, 48, 48, 48, 48, 48, 49, 49, 49, 49, 49, 49,50,50,50,50,50,50]
#y = np.loadtxt("out2.csv",delimiter=',')

#chz.bb()
clf = svm.SVC()
clf.fit(Matrix,y)
print Matrix[0]
for x in range(1,300):
    str1=""
    predicted=clf.predict(Matrix[x])
    #print predicted
    #str1=predicted
    #aa=np.fromstring(predicted, dtype=int)
    #str1.replace("[","")
    #print str1
    #str1.replace("array[","")
    str1=int(predicted)
    arr3.append(str1)
    #print arr3[x-1]
#arr3.tolist()
#print arr3
arr3.append(4)


#print y

#print accuracy_score(y, arr3)
#print arr3
print "SVM Done"

print " Accuracy = "
print accuracy_score(y, arr3)
