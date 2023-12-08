barang_ali = ['peta', 'topi']
barang_budi = ['sebotol air minum', 'kamera foto']


print("Apa saja barang bawaan Ali dan Budi?")
print(f"barang Ali: {barang_ali[0]} dan {barang_ali[1]}")
print(f"barang Budi: {barang_budi[0]} dan {barang_budi[1]}\n")

print("Mengapa Ali dan Budi harus membuat pilihan antara hutan dan jalan raya?")
print("Karena mereka harus memilih jalan yang sama agar bisa bertemu\n")

print("Jika mereka memilih jalur hutan, apa yang harus mereka pilih: menyeberangi sungai atau mencari jalan di sepanjang tepi sungai?")
jalan_ali = "hutan-lebat"
jalan_budi = "hutan-lebat"
if jalan_ali == "hutan-lebat" and jalan_budi == "hutan-lebat":
    jalan_pilih = "menyeberangi-sungai" or "jalan-tepi-sungai"
    print("Jalan yang dipilih adalah", jalan_pilih + "\n")
else:
    print("Tidak ada jalan yang dipilih\n")    

print("jika mereka memilih jalan raya, apa yang harus mereka pilih: mencari jalan keluar dari jembatanan yang rusak atau mencari jalan lain di sekitar kota?")
jalan_ali = "jalan-raya"
jalan_budi = "jalan-raya"
if jalan_ali == "jalan-raya" and jalan_budi == "jalan-raya":
    jalan_pilih = "jalan-keluar" or "jalan-lain"
    print("Jalan yang dipilih adalah", jalan_pilih)   
else:
    print("Tidak ada jalan yang dipilih")     