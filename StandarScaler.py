#standart sapmalrı 1 veri ortalamasını 0 yapar böylece geniş ölçekli feature ları eşit ağırlıkta dağıtır.

from sklearn.preprocessing import StandardScaler

data = [[-1,2],[-0.5, 6], [0, 10], [1, 18]]

scaler = StandardScaler()

scaled_data = scaler.fit_transform(data)
print(scaled_data)