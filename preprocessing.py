# ar = arra
# # print(ar)
# listProto = set(ar[:,4])
# listProto = list(listProto)
# print(listProto)
# X.loc[X['ipDSCP']=='48,0', ['ipDSCP']] = '480'


catCols = ['frameNumber','timeRelative','frame.len','protocolNumber','srcPort','dstPort','ipDSCP']
for col in catCols:
    X[col] = pd.to_numeric(X[col],errors='coerce')
# X['frameNumber'] = pd.to_numeric(X['frameNumber'])
# X.astype({'frameNumber':'int32','timeRelative':'float64','frame.len':'int32','protocolNumber':'int32'}).dtypes
# intCols intCols= X.columns[X.dtypes=='int32']
X.dtypes
# X.astype({'srcPort':'int32'}).dtypes

textCols = ['protocolName', 'ipSrc', 'ipDst']

for col in textCols:
    X.loc[X[col]=='',[col]] = "missing"
categories = [X[column].unique() for column in textCols]
cat_colwise = categories
print(categories)

categories = [item for sublist in categories for item in sublist]
categories = list(set(categories))

# i = 0
# test = map(i+1, categories)

# categories = categories[1:]
# print(categories)
# print(list(test))



# print(X[2547:2548])
# X.head(50)


from sklearn.preprocessing import OrdinalEncoder
from sklearn.impute import SimpleImputer

imp = SimpleImputer(missing_values=np.nan,strategy='constant',fill_value=-1)
imp.fit(X)
# n = imp.transform(X[textCols])
# a = 0
# for i in n:
#     print(i)
#     a+=1
#     if(a==50):
#         break



Xt = imp.transform(X)
X = pd.DataFrame(data=Xt,columns=features)



# X.head(44)



enc = OrdinalEncoder(dtype=np.float64)
enc.fit(X)
# enc.categories_
X_enc = enc.transform(X)
X = pd.DataFrame(data=X_enc,columns=features)
# X.tail(50)

from sklearn.preprocessing import LabelEncoder
le1 = LabelEncoder()
le1.fit(y1)
le1.classes_
le1.transform(y1)
le2 = LabelEncoder()
le2.fit(y2)
le2.classes_
le2.transform(y2)


# WRITING LIST TO A FILE
# list_of_array = enc.categories_
# with open('cat_list.txt','w') as fi:
#     for item in list_of_array:
#         fi.write('%s\n' %item)
pickle.dump(list_of_array,open('cat_lists.txt','wb'))