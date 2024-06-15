# Tugas Besar : Teori Bahasa dan Automata

### Kelompok:
- Baihaqi Bintang Bahana (1301223175)
- Binta Adimastama (1301223005)
- Putu Arjuna Nurgraha Eka Wana (1301223039)

<hr>

## Ketentuan Tugas Besar

Buatlah sebuah parser sederhana untuk memeriksa kevalidan struktur kalimat berbahasa Indonesia. Struktur kalimat yang dikenali adalah kalimat berita aktif dengan struktur:

S – P – O – K <br>
S – P – K <br>
S – P – O <br>
S – P <br>

Adapun jenis subyek, predikat, obyek dan keterangan yang dikenali ditentukan oleh kelompok masing-masing dengan jumlah kata masing- masing sebanyak 5.

Tugas Anda:
1. Bangunlah sebuah token recognizer menggunakan Finite Automata yang mengenali setiap kata apakah masuk ke dalam kelompok S, P, O atau K.
2. Bangunlah sebuah parser menggunakan Pushdown Automata yang mengenali apakah kalimat yang diinputkan valid berdasarkan struktur yang disebutkan di atas. Parser yang dibangun menggunakan token recognizer yang dibuat pada no 1.
   
Ketentuan:
1. Kelompok berjumlah 2-3 orang
2. Tidak diperkenankan menggunakan fungsi string matching
3. Bahasa pemrograman yang diperkenankan Go, C++, atau Python
4. Tidak wajib menggunakan GUI

Hasil pekerjaan:
1. Rancangan Finite Automata untuk masing-masing kelompok S, P, O dan K.
2. Rancangan Context Free Grammar untuk struktur kalimat yang valid.
3. Program token recognizer dan parser.
4. Video penjelasan mengenai cara kerja program yang sudah dibuat.

Tanggal pengumpulan: 18 Juni 2024 jam 23.59 di LMS

<hr>

## Pengerjaan

Disini kami membuat sebuah program parser beserta token recognizer untuk mengenali kevalidan struktur kalimat Bahasa Indonesia

Kami menggunakan bahasa pemrograman Python untuk membuat program parser dan token recognizer

### Token Recognizer dan Finite Automata:

Adapun kata-kata yang diterima pada masing-masing token adalah sebagai berikut:
- Subjek (S):
  - Aku
  - Andi
  - Budi
  - Dia
  - Dian
- Predikat (P):
  - Membaca
  - Membawa
  - Membeli
  - Menulis
  - Menukar
- Objek (O):
  - Buku
  - Kamus
  - Komik
  - Koran
  - Novel
- Keterangan (K):
  - Di_sini
  - Di_sana
  - Di_kelas
  - Di_taman
  - Di_toko

Selain kata-kata diatas, Token Recognizer akan mengeluarkan error "Token Unrecognized" dan mengembalikan token '?'

Untuk Finite Automata dari masing-masing token adalah sebagai berikut:
- Subjek: <br>
  ![image](https://github.com/baihaqibb/tubes-tba/assets/138758831/6f4a3e4c-3143-4677-b167-129b3b6f0edc)
- Predikat: <br>
  ![image](https://github.com/baihaqibb/tubes-tba/assets/138758831/1c46b0cc-f689-4027-bcb2-3353d2846768)
- Objek: <br>
  ![image](https://github.com/baihaqibb/tubes-tba/assets/138758831/fc759378-9fbb-4ca3-829c-fb9396d5af22)
- Keterangan: <br>
  ![image](https://github.com/baihaqibb/tubes-tba/assets/138758831/f454072b-8dd6-42d2-94cf-75840dcc8c4a)

### Parser dan Context Free Grammar

Untuk program parser tersebut, kami memiliki Context Free Grammar sebagai berikut dengan X sebagai Starting Symbol:
<pre>
X -> S P Y
Y -> O Z | Z
Z -> K | λ
S -> aku | andi | budi | dia | dian
P -> membaca | membawa | membeli | menulis | menukar
O -> buku | kamus | komik | koran | novel
K -> di_sana | di_sini | di_kelas | di_taman | di_toko
</pre>

Yang mana kami hasilkan first dan follow untuk setiap simbol non-terminal (ditandai dengan huruf kapital) adalah sebagai berikut:
<pre>
first(X) = {aku, andi, budi, dia, dian}
first(Y) = {buku, kamus, komik, koran, novel, di_sana, di_sini, di_kelas, di_taman, di_toko, λ}
first(Z) = {di_sana, di_sini, di_kelas, di_taman, di_toko, λ}
first(S) = {aku, andi, budi, dia, dian}
first(P) = {membaca, membawa, membeli, menulis, menukar}
first(O) = {buku, kamus, komik, koran, novel}
first(K) = {di_sana, di_sini, di_kelas, di_taman, di_toko}

follow(X) = {EOS}
follow(Y) = {EOS}
follow(Z) = {EOS}
follow(S) = {membaca, membawa, membeli, menulis, menukar}
follow(P) = {buku, kamus, komik, koran, novel, di_sana, di_sini, di_kelas, di_taman, di_toko, EOS}
follow(O) = {di_sana, di_sini, di_kelas, di_taman, di_toko, EOS}
follow(K) = {EOS}
</pre>

Dari first dan follow non-terminal diatas, kami hasilkan parse table seperti berikut: <br>
![image](https://github.com/baihaqibb/tubes-tba/assets/138758831/a4ea0fb7-d2a1-4d45-859f-423835b66653)

### Code dan Hasil Running (v1.0.2)

Program dapat dijalankan sebagaimana mestinya menjalankan program python, yaitu dengan menjalankan command
<pre>
python TBA.py
</pre>

Setelah itu, program akan meminta inputan dari pengguna berupa sebuah kalimat yang dipisah dengan spasi

<b>NOTE:<b> 
- Untuk penulisan keterangan, kata sambung 'di' dan tempat perlu dipisah menggunakan karakter '_' (garis bawah)
- Kapital tidaknya huruf pada suatu kata tidak berpengaruh (aku = Aku = aKu)

#### Contoh:

string valid: <br>
![image](https://github.com/baihaqibb/tubes-tba/assets/138758831/f1f64165-0cdc-4ccc-b517-bcfa8b740cd8)


token invalid, struktur valid: <br>
![image](https://github.com/baihaqibb/tubes-tba/assets/138758831/a20c04d7-bc48-4a6b-a6ea-af07a418bfe7)

token valid, struktur invalid: <br>
![image](https://github.com/baihaqibb/tubes-tba/assets/138758831/7667ada0-29eb-47ae-a0e6-6027becfd3ab)




