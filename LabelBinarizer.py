#veriyi kotegorik yapıdan binary matrisine çevirip bilg. tarafından anlaşılmasını kolaylaştırdık
#kısaca binary encoding diyebiliriz (aynı zamnada onehot encoding de olur ancak onehot kadar büyük bir matris olmadığı için daha avantajlıdır.)


#Tek sınıflı durum
from sklearn.preprocessing import LabelBinarizer

data = ['woman','man','woman','man','man']
lb = LabelBinarizer()
data_binarized = lb.fit_transform(data)
print(data_binarized)


#Çok sınıflı durum
from sklearn.preprocessing import LabelBinarizer

veri = ['red','blue','red','green','green']
lb = LabelBinarizer()
veri_binarized = lb.fit_transform(veri)
print(veri_binarized)
