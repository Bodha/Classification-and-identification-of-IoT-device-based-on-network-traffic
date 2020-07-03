import csv
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
arra = []
with open('16-09-27.csv') as file:
    reader = csv.reader(file, delimiter='\t')
    a = 0
    for row in reader:
        if(a==0):
            a+=1
            continue
#         if(a==10):
#             break
        arr = np.array(row)
        if(arr[7]==""):
            arr[7]=arr[9]
        if(arr[8]==""):
            arr[8]=arr[10]
        arr = np.delete(arr,(9,10))
        
        arra.append(arr)
#         a += 1
#     print(arr)
#     print(ar)
file.close()
 
# arra = np.array(ar)
columns = ['frameNumber','timeRelative','frame.len','protocolNumber','protocolName','ipSrc','ipDst','srcPort','dstPort','ipDSCP','ethsrc','ethdst']

df = pd.DataFrame(data=arra,columns=columns)
# print(df)
# df.head(5)
features = ['frameNumber','timeRelative','frame.len','protocolNumber','protocolName','ipSrc','ipDst','srcPort','dstPort','ipDSCP']

# print(arra)
X = df[features]
# print(X)
# X.head()
y1 = df['ethsrc']
# print(y1)
# y1.head()
y2 = df['ethdst']
# print(y2)

# X, y1 = shuffle(X, y1, random_state=0)
# print(X, y1)
# print("here")
df.head(15)