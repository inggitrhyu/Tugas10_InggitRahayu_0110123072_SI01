buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
def list_buah(buah) :
    list_terbalik = []

    for i in range(len(buah)-1, -1, -1):
        list_terbalik.append(buah[i])
    return list_terbalik

hasil = list_buah(buah)
print(hasil)