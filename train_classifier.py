

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import numpy as np

data_dict = pickle.load(open('./data.pickle', 'rb'))
data = data_dict['data']
labels = data_dict['labels']
data_clean=[]
label_clean=[]

for i in range(len(data)):
    if len(data[i])==42:
        data_clean.append(data[i])
        label_clean.append(labels[i])

data = np.asarray(data_clean)
labels = np.asarray(label_clean)

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.80, shuffle=True, stratify=labels)

model = RandomForestClassifier()

print("Training Model")
model.fit(x_train, y_train)

y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly !'.format(score * 100))

f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()