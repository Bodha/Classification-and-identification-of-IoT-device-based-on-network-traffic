import csv
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
arra = []
with open('simulated_csv.csv') as file:
    reader = csv.reader(file, delimiter=',')
    a = 0
    for row in reader:
        if(a==0):
            a+=1
            continue

        arr = np.array(row)
        if(arr[7]==""):
            arr[7]=arr[9]
        if(arr[8]==""):
            arr[8]=arr[10]
        arr = np.delete(arr,(9,10))
        
        arra.append(arr)

file.close()
 

    
# preprocessing this data #############################################

columns = ['frameNumber','timeRelative','frame.len','protocolNumber','protocolName','ipSrc','ipDst','srcPort','dstPort','ipDSCP','ethsrc','ethdst']

dfs = pd.DataFrame(data=arra,columns=columns)

features = ['frameNumber','timeRelative','frame.len','protocolNumber','protocolName','ipSrc','ipDst','srcPort','dstPort','ipDSCP']


X = dfs[features]

y1 = dfs['ethsrc']

y2 = dfs['ethdst']




import pickle
cat_list = pickle.load(open('cat_lists.txt','rb'))
cat_list

#Adding new values introduced in this file to previous categories respectively
cat_list[2] = np.append(cat_list[2],[341,774])               # frame len
cat_list[6] = np.append(cat_list[6],['62.210.177.42','158.69.38.240','62.210.205.141'])      # ip.dst
cat_list[7] = np.append(cat_list[7],[44675,44756,45546,45547,45548,23323,23325,23326,23456])     # src.port
cat_list


enc = OrdinalEncoder(categories=cat_list,dtype=np.float64)
enc.fit(X)
X_enc = enc.transform(X)
X = pd.DataFrame(data=X_enc,columns=features)


from sklearn.preprocessing import LabelEncoder
le1 = LabelEncoder()
le1.fit(y1)
le1.classes_
le1.transform(y1)


import pickle
model = pickle.load(open('final_model.sav','rb'))   # saved model

# accuracy on new data
model.score(X,y1)

