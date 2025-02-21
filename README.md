# **Bank Marketing Campaign Analysis**

`Created by : Syafiq Basmallah`

## **Overview**
Proyek ini bertujuan untuk menganalisis kampanye pemasaran Bank Sigma yang berfokus pada promosi produk deposito berjangka. Dengan memanfaatkan data historis, kita akan mengidentifikasi karakteristik nasabah yang lebih mungkin untuk berpartisipasi dalam kampanye.

## **Table of Contents**

1. Business Problem
2. Data Understanding
3. Data Preparation
4. Modeling & Evaluation
5. Conclusion & Recommendation

## **1. Business Problem Understanding**

### **Context**
Bank Sigma secara berkala mengadakan kampanye pemasaran langsung kepada pelanggan potensial. Tujuan dari analisis ini adalah:
- Meningkatkan efisiensi dalam menargetkan nasabah yang relevan
- Mengoptimalkan efektivitas strategi kampanye
- Meminimalkan pemborosan anggaran pemasaran

### **Problem Statement**
Dapatkah kita membangun model prediksi yang mampu mengidentifikasi pelanggan yang kemungkinan besar akan berlangganan produk deposito berjangka?

### **Metrics**
- **Accuracy** : Untuk menilai sejauh mana model dapat memprediksi dengan benar
- **Precision & Recall** : Untuk memahami keseimbangan antara pelanggan yang benar-benar tertarik dengan yang tidak
- **F1-score** : Menggabungkan precision dan recall untuk evaluasi menyeluruh

## **2. Data Understanding**
Dataset yang digunakan berasal dari kampanye pemasaran sebelumnya yang berisi informasi demografi pelanggan, interaksi sebelumnya, serta hasil akhir kampanye.

Fitur utama dalam dataset:
- `age` : Usia pelanggan
- `job` : Jenis pekerjaan pelanggan
- `marital` : Status pernikahan
- `education` : Tingkat pendidikan
- `default` : Status gagal bayar
- `balance` : Saldo rata-rata pelanggan
- `contact` : Jenis kontak yang digunakan
- `campaign` : Jumlah kontak yang dilakukan selama kampanye
- `previous` : Jumlah kontak sebelumnya
- `y` : Label target (apakah pelanggan berlangganan produk deposito berjangka atau tidak)

## **3. Data Preparation**
Langkah-langkah yang dilakukan:
- Menghapus missing values
- Melakukan encoding pada variabel kategori
- Normalisasi fitur numerik
- Pembagian dataset menjadi training dan testing set

## **4. Modeling & Evaluation**
Beberapa model machine learning yang diuji:
- **Logistic Regression**
- **Random Forest Classifier**
- **Gradient Boosting**

Evaluasi dilakukan menggunakan:
- Confusion Matrix
- ROC Curve
- Classification Report

## **5. Conclusion & Recommendation**
- Model terbaik berdasarkan evaluasi adalah `XXXXX` (akan disesuaikan dari hasil model)
- Bank Sigma dapat meningkatkan efektivitas kampanye dengan menargetkan pelanggan berdasarkan hasil analisis model
- Rekomendasi selanjutnya mencakup pengujian dengan dataset yang lebih besar dan eksplorasi fitur tambahan

## **How to Run**
1. Clone repository ini
   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan notebook
   ```bash
   jupyter notebook
   ```

## **Dependencies**
- Python 3.x
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn
- Jupyter Notebook

---

README ini dapat disesuaikan dengan detail tambahan sesuai kebutuhan proyek!


link streamlit: https://capstone3syafiq.streamlit.app/
