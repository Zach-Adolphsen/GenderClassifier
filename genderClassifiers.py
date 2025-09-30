from sklearn import tree
from sklearn import neighbors
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier

# [height (cm), weight (kg), shoe size (EU chart)]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37],
     [166, 65, 40], [190, 90, 47], [175,64,39], [177, 70, 40], [159, 55, 37],
     [171, 75, 42], [181, 85, 43]]

Y = ['male', 'female', 'female', 'female',
     'male', 'male', 'male', 'female', 'male',
     'female', 'male']

predictions = []
probabilities = []
algorithm_names = []

newUserDetails = [[181, 73, 44]]

# Decision Tree
clf = tree.DecisionTreeClassifier().fit(X, Y)
pred = clf.predict(newUserDetails)
predictions.append(pred[0])
prob = clf.predict_proba(newUserDetails)
probabilities.append(prob)
algorithm_names.append('Tree')
print("Tree: " + str(pred[0]))

# K Neighbors
clf = neighbors.KNeighborsClassifier().fit(X, Y)
pred = clf.predict(newUserDetails)
predictions.append(pred[0])
prob = clf.predict_proba(newUserDetails)
probabilities.append(prob)
algorithm_names.append('Neighbors')
print("K-Neighbors: " + str(pred[0]))

# Quadratic Discriminant Analysis
clf = QuadraticDiscriminantAnalysis().fit(X, Y)
pred = clf.predict(newUserDetails)
predictions.append(pred[0])
prob = clf.predict_proba(newUserDetails)
probabilities.append(prob)
algorithm_names.append('Quadratic Discriminant Analysis')
print("Quadratic Discriminant Analysis: " + str(pred[0]))

# Random Forest
clf = RandomForestClassifier().fit(X, Y)
pred = clf.predict(newUserDetails)
predictions.append(pred[0])
prob = clf.predict_proba(newUserDetails)
probabilities.append(prob)
algorithm_names.append('Random Forest')
print("Random Forest: " + str(pred[0]))

best_algo_index = 0
best_confidence = 0
for i, prob in enumerate(probabilities):
    if prob.max() > best_confidence:
        best_confidence = prob.max() * 100
        best_algo_index = i

print("Best algorithm: " + algorithm_names[best_algo_index] + " w/ confidence of " + str(best_confidence))
print("Prediction: " + str(predictions[best_algo_index]))
print(probabilities)
