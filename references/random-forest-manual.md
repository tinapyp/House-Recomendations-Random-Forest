Tentu, berikut adalah penjelasan singkat tentang bagaimana kode bekerja dalam `dokumentasi.md`:

# Dokumentasi Kode Random Forest Tanpa Library

## DecisionTree Class

Kelas `DecisionTree` bertanggung jawab untuk membangun dan melakukan prediksi menggunakan sebuah pohon keputusan.

- **Metode `fit(X, y)`**: Metode ini digunakan untuk melatih pohon keputusan menggunakan data latih `X` dan label `y`.
  
- **Metode `_build_tree(X, y, depth)`**: Metode ini secara rekursif membangun pohon keputusan dengan menggunakan pembagian berdasarkan fitur dan ambang batas terbaik yang ditemukan.
  
- **Metode `_find_best_split(X, y, feature_indices)`**: Metode ini mencari pembagian terbaik berdasarkan gain informasi dengan memeriksa semua kombinasi fitur dan ambang batas.
  
- **Metode `_information_gain(parent, left_child, right_child)`**: Metode ini menghitung gain informasi berdasarkan impurity Gini.
  
- **Metode `_gini(y)`**: Metode ini menghitung impurity Gini dari sebuah himpunan data.
  
- **Metode `predict(X)`**: Metode ini digunakan untuk melakukan prediksi pada sekumpulan data `X` menggunakan pohon keputusan yang telah dilatih.

- **Metode `_predict_tree(tree, x)`**: Metode ini secara rekursif melakukan prediksi untuk sebuah sampel `x` menggunakan pohon keputusan.

## RandomForest Class

Kelas `RandomForest` bertanggung jawab untuk membangun dan melakukan prediksi menggunakan sekumpulan pohon keputusan.

- **Metode `fit(X, y)`**: Metode ini digunakan untuk melatih model random forest menggunakan data latih `X` dan label `y`.
  
- **Metode `predict(X)`**: Metode ini digunakan untuk melakukan prediksi pada sekumpulan data `X` menggunakan model random forest yang telah dilatih.

## Contoh Penggunaan

```python
import numpy as np
from random_forest import RandomForest

# Generate some sample data
np.random.seed(42)
X = np.random.rand(100, 2)  # Features
y = np.random.randint(0, 2, 100)  # Labels (0 or 1)

# Instantiate and fit the random forest
random_forest = RandomForest(n_estimators=10, max_depth=3)
random_forest.fit(X, y)

# Make predictions
new_data = np.array([[0.1, 0.5], [0.8, 0.2]])
predictions = random_forest.predict(new_data)
print("Predictions:", predictions)
```

Dalam contoh di atas, kita menghasilkan data sampel sebagai fitur `X` dan label `y`. Kemudian, kita melatih model random forest dengan 10 pohon keputusan dan kedalaman maksimum 3. Akhirnya, kita melakukan prediksi pada data baru `new_data` menggunakan model yang telah dilatih.