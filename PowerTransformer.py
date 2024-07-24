#genelde çok çarpık veriler içerdiği için normal (Gaussian) dağılıma yakınlaştırmaya çalışılır
from sklearn.preprocessing import PowerTransformer

data = [[1, 2], [3, 2], [2, 3], [4, 4], [5, 6]]

pt = PowerTransformer(method="yeo-johnson") #burada verilerimiz>0 old. için box-cox da kullanılabilir

transformed_data = pt.fit_transform(data)

print(transformed_data)