
# Example of a confusion matrix in Python
#pip install -U scikit-learn scipy matplotlib
#pip3 install -U scikit-learn scipy matplotlib
#https://www.geeksforgeeks.org/confusion-matrix-machine-learning/
from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 

expected = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0,1, 0,  0, 1, 0, 0, 1, 0, 0, 0,1, 0, 0, 1, 0, 0, 1, 1, 1, 0,1, 0, 0, 1, 0, 0, 1, 0, 1, 0,1, 0, 0, 1, 0, 0, 1, 1, 1, 0,1, 0, 0, 1, 0, 0, 1, 1, 1, 0,1, 0, 0, 1, 0, 0, 0, 1, 1, 0,1, 0, 0, 1, 0, 0, 1, 1, 1, 0,1, 0, 0, 1, 0, 0, 1, 1, 1, 0,1, 0, 0, 1, 0, 0, 0, 1, 1, 0]
predicted = [1, 1, 0, 1, 0, 0, 1, 0, 0, 0,1, 0,  0, 1, 0, 0, 1, 1, 1, 0,1, 0, 0, 1, 0, 0, 1, 1, 1, 0,1, 0, 0, 1, 0, 0, 0, 1, 1, 0,1, 0, 0, 1, 0, 0, 1, 1, 1, 0,1, 0, 0, 1, 0, 0, 1, 1, 1, 0,1, 0, 0, 1, 0, 0, 0, 1, 1, 0,1, 0, 0, 1, 0, 0, 1, 1, 1, 0,1, 0, 0, 1, 0, 0, 1, 1, 1, 0,1, 0, 0, 1, 0, 0, 0, 1, 1, 0]
results = confusion_matrix(expected, predicted)

print ("Confusion Matrix : " )
print(results) 
print ("Accuracy Score : ")
print(accuracy_score(expected, predicted) )
print ("Report :  ")
print (classification_report(expected, predicted) )