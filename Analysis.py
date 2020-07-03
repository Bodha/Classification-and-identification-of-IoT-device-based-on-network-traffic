import matplotlib.pyplot as plt
import matplotlib.cm as cm

from sklearn.metrics import plot_confusion_matrix

mac_to_device = {'00:16:6c:ab:6b:88':'Samsung SmartCam', '00:24:e4:11:18:a8':'Withings Smart Baby Monitor', '00:24:e4:1b:6f:96':'Withings Smart scale',
                '08:21:ef:3b:fc:e3':'Samsung Galaxy Tab', '14:cc:20:51:33:ea':'TPLink Router', '18:b4:30:25:be:e4':'NEST Protect smoke alarm',
                 '18:b7:9e:02:20:44':'Triby Speaker', '30:8c:fb:2f:e4:b2':'Dropcam','44:65:0d:56:cc:d3':'Amazon Echo', 
                 '50:c7:bf:00:56:39':'TP-Link Smart plug', '70:5a:0f:e4:9b:c0':'HP Printer', '70:ee:50:03:b8:ac':'Netatmo weather station', 
                 '70:ee:50:18:34:43':'Netatmo Welcome',  'd0:52:a8:00:67:5e':'Smart Things', 'e0:76:d0:33:bb:85':'PIX-STAR Photo-frame',
                 'ec:1a:59:79:f4:89':'Belkin Wemo switch', 'ec:1a:59:83:28:11':'Belkin wemo motion sensor', 'f4:f2:6d:93:51:f1':'TP-Link Day Night Cloud camera', 
                    }
devices = [d for d in mac_to_device.values()]
plot_confusion_matrix(classifier, X_test, y1_test, normalize='pred', display_labels=devices, include_values=True)

###########      Y2       ##############
plot_confusion_matrix(classifier, X_test, y1_test, normalize='pred')

CMd = pd.DataFrame(CM, columns=devices, index=le1.classes_)
CMd.head(18)

classifier.feature_importances_
classifier.score(X_test,y_test)

classifier.predict_proba(X_test)[0:33]

from sklearn.model_selection import cross_val_score
import numpy as np
cv = cross_val_score(classifier, X_train, y_train, cv=10)
print(cv)
print(np.mean(cv))
# scores
print("CV")

from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report

print ('Confusion Matrix :') 
CM = confusion_matrix(y_test, predicted, normalize="pred")
CM_not = confusion_matrix(y_test,predicted)
print(CM) 
# print('le1 classes:', le1.classes_)

print ('Accuracy Score :',accuracy_score(y_test, predicted)) 

print ('Report : ') 
print (classification_report(y_test, predicted))

# X_train, X_test, y2_train, y2_test = train_test_split(X, y2, test_size=0.3, random_state=0)
# classifier2 = RandomForestClassifier()
# classifier2.fit(X_train, y2_train)
# predicted2 = classifier2.predict(X_test)

# print ('Confusion Matrix :') 
# print(confusion_matrix(y2_test, predicted2)) 
# print ('Accuracy Score :',accuracy_score(y2_test, predicted2)) 
# print ('Report : ') 
# print (classification_report(y2_test, predicted2)) 


%matplotlib inline
import seaborn as sn
plt.figure(figsize=(18,9))
sn.heatmap(CM, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

import pandas as pd# CMd = pd.DataFrame(CM, columns=devices, index=le1.classes_)

CMd = pd.DataFrame(CM_not, columns=devices, index=devices)

CMd.head(18)

from sklearn.metrics import precision_recall_fscore_support
precision, recall, f1Score, support = precision_recall_fscore_support(y_test, predicted)
print(precision, recall, f1Score, support)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.scatter(f1Score, support)

from sklearn.metrics import balanced_accuracy_score
balanced_accuracy_score(y_test, predicted)

