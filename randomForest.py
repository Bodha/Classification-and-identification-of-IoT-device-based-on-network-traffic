from sklearn.model_selection import train_test_split

X_train, X_test, y1_train, y1_test = train_test_split(X, y1, test_size=0.3, random_state=0)

from sklearn.ensemble import RandomForestClassifier

classifier=RandomForestClassifier() 
classifier=classifier.fit(X_train,y1_train) 
predicted=classifier.predict(X_test)

from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report

print ('Confusion Matrix :') 
CM = confusion_matrix(y1_test, predicted)
print(CM) 
print('le1 classes:', le1.classes_)

print ('Accuracy Score :',accuracy_score(y1_test, predicted)) 

print ('Report : ') 
print (classification_report(y1_test, predicted))





##############    FOR Y2    #################

# X_train, X_test, y2_train, y2_test = train_test_split(X, y2, test_size=0.3, random_state=0)
# classifier2 = RandomForestClassifier()
# classifier2.fit(X_train, y2_train)
# predicted2 = classifier2.predict(X_test)

# print ('Confusion Matrix :') 
# print(confusion_matrix(y2_test, predicted)) 
# print ('Accuracy Score :',accuracy_score(y2_test, predicted)) 
# print ('Report : ') 
# print (classification_report(y2_test, predicted)) 


import pickle
filename = 'final_model.sav'
pickle.dump(classifier,open(filename,'wb'))