def duplikasi(daftar_buah):
    list_baru = []
    for buah in daftar_buah:
        list_baru.append(buah)
        list_baru.append(buah)
    return list_baru

daftar_buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
hasil_duplikasi = duplikasi(daftar_buah)
print(hasil_duplikasi)