data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

print("Seluruh Data Panen")
for i, d in data_panen.items():
    print(f"{i}:\nNama Lokasi: {d['nama_lokasi']}, Hasil Panen: {d['hasil_panen']}")


jagung_lokasi2=data_panen['lokasi2']['hasil_panen']['jagung']
print(f'Jumlah panen jagung dari lokasi2 :{jagung_lokasi2}')

nama_lokasi3=data_panen['lokasi3']['nama_lokasi']
print(f'Nama dari lokasi3 :{nama_lokasi3}')

jumlah_padi = {i: d['hasil_panen']['padi'] for i, d in data_panen.items()}
jumlah_kedelai = {i: d['hasil_panen']['kedelai'] for i, d in data_panen.items()}
print(f'Jumlah hasil panen padi dari setiap lokasi :\n{jumlah_padi}')
print(f'Jumlah hasil panen kedelai dari setiap lokasi :\n{jumlah_kedelai}')

print("Status perhatian tiap lokasi:")
for i, d in data_panen.items():
    padi = d['hasil_panen']['padi']
    jagung = d['hasil_panen']['jagung']
    nama = d['nama_lokasi']
    
    if padi > 1300 or jagung > 800:
        print(f'Lokasi {nama} memerlukan perhatian khusus')
    else:
        print(f'Lokasi {nama} dalam kondisi baik')

# commit ke dua testing
# menambahkan branch baru
# branch Baru