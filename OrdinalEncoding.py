from sklearn.preprocessing import OrdinalEncoder
import numpy as np

veri = np.array([['University'],['Master'],['PhD']])

encoder = OrdinalEncoder(categories=[['University','Master','PhD']])

ordinal_encoded = encoder.fit_transform(veri)
print(ordinal_encoded)