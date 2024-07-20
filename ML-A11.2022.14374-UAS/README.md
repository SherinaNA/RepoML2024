# Seasonal Color Classification Using RGB and HSL Features

Nama: Sherina Nur Anggraeni | 
NIM: A11.2022.14374 | 
Mata Kuliah: Machine Learning

## Ringkasan
Proyek ini bertujuan untuk mengklasifikasikan warna berdasarkan musim (Spring, Summer, Autumn, Winter) menggunakan fitur RGB dan HSL.
Dengan menggunakan algoritma machine learning yaitu menggunakan metode klasifikasi "Decision Tree Classifier", 
model ini akan belajar mengenali pola dari dataset warna dan menentukan musim yang sesuai untuk setiap warna.

## Permasalahan
Ada banyak sekali warna di dunia ini, yang awalnya hanya ada warna primer, sekunder, dan tersier sehingga dapat menghasilkan turunan warna yang berbeda dan sangat banyak sekali jumlah dan nama warnanya.

Pada eksperimen kali ini saya ingin mencoba untuk pengklasifikasian warna berdasarkan musim sangat bisa sekali untuk dibuktikan. Dengan memanfaatkan RGB dan HSL Features. Pada penentuan pola/pattern untuk menghasilkan klasifikasi warna berdasarkan musim saya mencoba beberapa kali hingga mendapatkan pola yang mendekati sesuai dengan realita.

Saya mempelajari pola klasifikasi warna pada artikel di link berikut: https://digitalcommons.aaru.edu.jo/faa-design/vol11/iss1/50/

Warna dapat mempengaruhi persepsi,emosi, serta menggambarkan personality seseorang, oleh karena itu penting untuk mengetahui bagaimana warna tertentu dapat dikategorikan ke dalam musim tertentu. Tujuannya adalah membuat model yang dapat mengklasifikasikan warna secara akurat berdasarkan musimnya.

Namun, permasalahannya ada terletak pada setelah mendapatkan kesesuaian pola, banyak warna yang ada di dalam dataset yang tidak terkategorikan atau termasuk ke dalam 'Uncategorized'. Hal ini memerlukan pendalaman eksperimen lebih lanjut mengapa hal ini bisa terjadi. Apakah warna 'Uncategorized' tersebut benar-benar tidak dapat diklasifikasikan berdasarkan kesesuaian dengan 'Seasonal Color' yang lainnya ataukah adanya penentuan pola/pattern yang tidak mencakup segala kondisi dari features yang ada.

## Tujuan
1. Membangun model machine learning untuk mengklasifikasikan warna berdasarkan kesesuaian musim.
2. Mengevaluasi performa model menggunakan metrik evaluasi yang sesuai.
3. Menganalisis hasil dan memberikan kesimpulan mengenai performa model.

## Model / Alur Penyelesaian
![Model Alur Penyelesaian](alur-modeling.png)
1. Data Collection
2. Data Preprocessing
3. Feature Engineering
4. Model Training
5. Model Evaluation

## Point 3-5 akan dijelaskan pada file Summary_Experiment.ipynb
(Summary_Experiment.ipynb)

## Diskusi Hasil
Model yang dibangun memiliki performa yang cukup baik dalam mengklasifikasikan warna berdasarkan musim walaupun masih memiliki kemungkinan terjadi overfitting.
Dari confusion matrix, kita bisa melihat bahwa beberapa kelas memiliki tingkat kesalahan yang lebih tinggi dibandingkan yang lain.

## Kesimpulan
1. Model dapat mengklasifikasikan warna ke dalam musim dengan cukup baik. Warna dapat diklasifikasikan sesuai dengan kriteria 'Seasonal Color'.
2. Performa model dapat ditingkatkan dengan menggunakan lebih banyak data dan teknik pra-pemrosesan data yang lebih baik lagi.
3. Model ini dapat digunakan dalam aplikasi yang memerlukan klasifikasi warna berdasarkan musim, seperti dalam industri fashion.

## Test Uji Model dengan input RGB
Dengan percobaan input nilai RGB suatu warna, pallete macam-macam 'Seasonal Color' dapat dilihat pada link:
* https://colorhunt.co/palettes/spring
* https://colorhunt.co/palettes/winter
* https://colorhunt.co/palettes/fall
* https://colorhunt.co/palettes/summer
Berdasarkan uji input RGB, model telah menunjukkan hasil output 'Seasonal Color' yang sudah sesuai.
Walaupun masih memungkinkan untuk terjadinya error.


