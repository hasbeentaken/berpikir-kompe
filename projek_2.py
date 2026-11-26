import os
import random
import time

slotIl = 10
barisIl = 2
slotOr = 10
barisOr = 5
antreanMobil = []
antreanMotor = []
persenramaiMobil = 10
persenramaiMotor = 80
persenkeluarMobil = 5
persenkeluarMotor = 5

lapanganMobil = [[0 for _ in range(slotIl)] for _ in range(barisIl)]
lapanganMotor = [[0 for _ in range(slotOr)] for _ in range(barisOr)]
kapasitasMaxIl = barisIl * slotIl
kapasitasMaxOr = barisOr * slotOr
batasSimulasi = 100

kapasitasMobil = 15
isiMobil = 0
kapasitasMotor = 60
isiMotor = 0

KampusBuka = True

def cekKosongMobil():
  kosong = 0
  for i in lapanganMobil:
    for j in i:
      if j == 0:
        kosong += 1
  return kosong

def cekKosongMotor():
  kosong = 0
  for i in lapanganMotor:
    for j in i:
      if j == 0:
        kosong += 1
  return kosong

for _ in range(1, random.randint(1,batasSimulasi)):
  os.system("cls" if os.name == "nt" else "clear")

  # 1. Kedatangan mobil baru ke antrean
  if random.randint(1, 100) <= persenramaiMobil:
    antreanMobil.append(1)
  
  if random.randint(1, 100) <= persenramaiMotor:
    antreanMotor.append(1)

  # 2. Pengecekan setiap slot dari depan (c = 0) sampai ujung dalam (c = slot - 1) untuk Mobil
  for r in range(barisIl):
    for c in range(slotIl):
      terisi = kapasitasMaxIl - cekKosongMobil()

      # Bobot berdasarkan kedalaman (c + 1) ditambah tingkat kepadatan parkiran
      peluang_parkir = (c + 1) + int((terisi / kapasitasMaxIl) * slotIl)

      # Jika slot kosong, ada antrean, dan peluang terpenuhi -> Parkir
      # Catatan: Saat di ujung (c = slot - 1), peluang_parkir selalu >= slot (100% parkir)
      if (
          lapanganMobil[r][c] == 0
          and len(antreanMobil) > 0
          and random.randint(1, slotIl) <= peluang_parkir
      ):
        antreanMobil.pop(0)
        lapanganMobil[r][c] = 1

      # Jika slot terisi -> Peluang acak mobil keluar
      elif lapanganMobil[r][c] == 1 and random.randint(1, 100) <= persenkeluarMobil:
        lapanganMobil[r][c] = 0

  for i in range(barisIl):
    print(lapanganMobil[i])
  print("Antrean:", antreanMobil)
  print("Slot Mobil Kosong:", cekKosongMobil())


  for r in range(barisOr):
    for c in range(slotOr):
      terisi = kapasitasMaxOr - cekKosongMotor()

      # Bobot berdasarkan kedalaman (c + 1) ditambah tingkat kepadatan parkiran
      peluang_parkir = (c + 1) + int((terisi / kapasitasMaxOr) * slotOr)

      # Jika slot kosong, ada antrean, dan peluang terpenuhi -> Parkir
      # Catatan: Saat di ujung (c = slot - 1), peluang_parkir selalu >= slot (100% parkir)
      if (
          lapanganMotor[r][c] == 0
          and len(antreanMotor) > 0
          and random.randint(1, slotIl) <= peluang_parkir
      ):
        antreanMotor.pop(0)
        lapanganMotor[r][c] = 1

      # Jika slot terisi -> Peluang acak mobil keluar
      elif lapanganMotor[r][c] == 1 and random.randint(1, 100) <= persenkeluarMotor:
        lapanganMotor[r][c] = 0

  # 3. Tampilkan visualisasi parkiran
  
  for i in range(barisOr):
    print(lapanganMotor[i])
  print("Antrean:", antreanMotor)
  print("Slot Motor Kosong:", cekKosongMotor())

  #time.sleep(0.1)

while KampusBuka:
  Kegiatan = input("Kendaraan akan masuk atau keluar : ").lower()
  jenisKendaraan = input("Apa jenis kendaraan yang masuk ke tempat parkir : ").lower()

  if Kegiatan == "masuk":
    if jenisKendaraan == "mobil":
      isiMobil += 1
    elif jenisKendaraan == "motor":
      isiMotor += 1
  elif Kegiatan == "keluar":
    if jenisKendaraan == "mobil":
      isiMobil -= 1
    elif jenisKendaraan == "motor":
      isiMotor -= 1
  
  if input("apakah ada kegiatan lain?").lower() == "tidak":
    KampusBuka = False