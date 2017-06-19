from sklearn import tree
x = [[0, 0], [2, 8], [3, 11], [5, 12], [7, 15]]
y = [0, 8, 11, 12, 15]
clf = tree.DecisionTreeClassifier()
clf.fit(x, y)
print (clf.predict([8, 19]))
t = input()