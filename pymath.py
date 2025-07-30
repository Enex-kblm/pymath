import os
import operator

# Clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII art
def ascii_art():
    print(r"""  
  _______     ____  __       _______ _    _   
 |  __ \ \   / /  \/  |   /\|__   __| |  | |  
 | |__) \ \_/ /| \  / |  /  \  | |  | |__| |  
 |  ___/ \   / | |\/| | / /\ \ | |  |  __  |  
 | |      | |  | |  | |/ ____ \| |  | |  | |  
 |_|      |_|  |_|  |_/_/    \_\_|  |_|  |_|             
    """)
    print("            PyMath | Author : nau\n")

# Fungsi matematika

def volume_kubus():
    clear_screen()
    print("=== Volume Kubus ===")
    s = int(input("Nilai sisi (s): "))
    hasil = pow(s, 3)
    print(f"Hasil volume kubus adalah {hasil}")

def volume_balok():
    clear_screen()
    print("=== Volume Balok ===")
    p = int(input("Nilai panjang (p): "))
    l = int(input("Nilai lebar (l): "))
    t = int(input("Nilai tinggi (t): "))
    hasil = p * l * t
    print(f"Hasil volume balok adalah {hasil}")

def volume_tabung():
    clear_screen()
    print("=== Volume Tabung ===")
    r = float(input("Masukkan jari-jari (r): "))
    t = float(input("Masukkan tinggi (t): "))
    phi = 3.14
    hasil = phi * (r ** 2) * t
    print(f"Volume tabung adalah {hasil}")

def SPLDV():
    clear_screen()
    print("=== Sistem Persamaan Linear Dua Variabel (SPLDV) ===")
    print("Bentuk umum: a1x + b1y = c1 dan a2x + b2y = c2")

    a1 = float(input("Masukkan a1: "))
    b1 = float(input("Masukkan b1: "))
    c1 = float(input("Masukkan c1: "))
    a2 = float(input("Masukkan a2: "))
    b2 = float(input("Masukkan b2: "))
    c2 = float(input("Masukkan c2: "))

    faktor1 = a2
    faktor2 = a1

    new_b1 = b1 * faktor1
    new_c1 = c1 * faktor1
    new_b2 = b2 * faktor2
    new_c2 = c2 * faktor2

    elim_b = new_b1 - new_b2
    elim_c = new_c1 - new_c2

    if elim_b == 0:
        print("Tidak dapat diselesaikan (eliminasi gagal).")
        return

    y = elim_c / elim_b

    if a2 != 0:
        x = (c2 - b2 * y) / a2
    elif a1 != 0:
        x = (c1 - b1 * y) / a1
    else:
        print("Tidak dapat menyelesaikan karena koefisien x = 0 di kedua persamaan.")
        return

    print(f"Hasil: x = {x}, y = {y}")

def Cek_nilai():
    clear_screen()
    print("=== Cek Nilai ===")
    nilai = int(input("Masukkan skor: "))

    if nilai > 100 or nilai < 0:
        print("pinter atau pea")
    elif nilai >= 81:
        print("A")
    elif nilai >= 71:
        print("B")
    elif nilai >= 61:
        print("C")
    elif nilai >= 51:
        print("D")
    else:
        print("E")

def persentase():
    clear_screen()
    print("=== Persentase ===")
    total = float(input("Masukkan total nilai: "))
    bagian = float(input("Masukkan bagian nilai: "))
    persen = (bagian / total) * 100
    print(f"Hasil persentasenya: {persen:.2f}%")

def pythagoras():
    clear_screen()
    print("=== Teorema Pythagoras ===")
    print("Mencari sisi miring segitiga siku-siku")
    a = float(input("Masukkan sisi alas (a): "))
    b = float(input("Masukkan sisi tinggi (b): "))
    c = (a ** 2 + b ** 2) ** 0.5
    print(f"Panjang sisi miring (c): {c}")

def kerucut():
    clear_screen()
    print("=== Luas Permukaan & Volume Kerucut ===")
    r = float(input("Masukkan jari-jari (r): "))
    s = float(input("Masukkan panjang garis pelukis (s): "))
    t = float(input("Masukkan tinggi (t): "))
    phi = 3.14
    luas = phi * r * (r + s)
    volume = (1/3) * phi * (r ** 2) * t
    print(f"Luas Permukaan Kerucut: {luas}")
    print(f"Volume Kerucut: {volume}")

def bola():
    clear_screen()
    print("=== Luas Permukaan & Volume Bola ===")
    r = float(input("Masukkan jari-jari (r): "))
    phi = 3.14
    luas = 4 * phi * (r ** 2)
    volume = (4/3) * phi * (r ** 3)
    print(f"Luas Permukaan Bola: {luas}")
    print(f"Volume Bola: {volume}")

def kalkulator():
    def kalkulator_sederhana():
        clear_screen()
        try:
            a = float(input("Angka pertama: "))
            b = float(input("Angka kedua: "))
            op = input("Operasi (+, -, *, /): ")

            operasi = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv
            }

            if op in operasi:
                hasil = operasi[op](a, b)
                print(f"Hasil: {hasil}\n")
            else:
                print("Operasi tidak valid.\n")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}\n")

    def kalkulator_kompleks():
        clear_screen()
        try:
            ekspresi = input("Masukkan soal (contoh: 337+14*84-46): ")
            hasil = eval(ekspresi)
            print(f"Hasil: {hasil}\n")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}\n")

    while True:
        clear_screen()
        print("\n=== KALKULATOR ===")
        print("1. Kalkulator Sederhana")
        print("2. Kalkulator Kompleks")
        print("0. Kembali ke menu utama")
        pilihan = input("Pilih kalkulator (1/2/0): ")

        if pilihan == '1':
            kalkulator_sederhana()
        elif pilihan == '2':
            kalkulator_kompleks()
        elif pilihan == '0':
            break
        else:
            print("Pilihan tidak valid.\n")

# Menu utama
def main_menu():
    while True:
        clear_screen()
        ascii_art()
        print("Pilih rumus:")
        print("1. Volume Balok")
        print("2. Volume Kubus")
        print("3. Volume Tabung")
        print("4. SPLDV")
        print("5. Cek nilai")
        print("6. Bola")
        print("7. Kerucut")
        print("8. Pythagoras")
        print("9. Persentase")
        print("10. Kalkulator")
        print("0. Keluar")

        try:
            rumus = int(input("Pilih rumus (0-10): "))
        except ValueError:
            print("Masukkan angka saja.")
            input("Tekan Enter untuk lanjut...")
            continue

        if rumus == 1:
            volume_balok()
        elif rumus == 2:
            volume_kubus()
        elif rumus == 3:
            volume_tabung()
        elif rumus == 4:
            SPLDV()
        elif rumus == 5:
            Cek_nilai()
        elif rumus == 6:
            bola()
        elif rumus == 7:
            kerucut()
        elif rumus == 8:
            pythagoras()
        elif rumus == 9:
            persentase()
        elif rumus == 10:
            kalkulator()
        elif rumus == 0:
            print("Terima kasih telah menggunakan PyMath!")
            break
        else:
            print("Pilihan tidak valid!")

        input("\nTekan Enter untuk kembali ke menu utama...")

# Jalankan program
main_menu()