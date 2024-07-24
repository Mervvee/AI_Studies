# tamamen lineer bağımsız

from sklearn.preprocessing import OneHotEncoder
import numpy as np 
#encoderlar kategorik veriler olduğu için arraye çeviririz.
data = np.array([['Apricot'],['Watermelon'],['Cherry']])

encoder = OneHotEncoder(categories=[['Apricot','Watermelon','Cherry']]) 
# category saves the queue of the items as we gave, otherwise it gets alphabetical

onehot_encoded = encoder.fit_transform(data).toarray()
print(onehot_encoded)