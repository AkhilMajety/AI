from sklearn import tree

x=[[160,88],[165,75],[170,77],[166,89],[150,53],[155,60],[139,57],[140,45],[155,67]]

y=['male','male','male','male','female','female','female','female','female']

clf= tree.DecisionTreeClassifier()

clf=clf.fit(x,y)

prediction=clf.predict([[185,90]])
print(prediction)