import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def ascii_art():
    print(r"""
  _______     ____  __       _______ _    _ 
 |  __ \ \   / /  \/  |   /\|__   __| |  | |
 | |__) \ \_/ /| \  / |  /  \  | |  | |__| |
 |  ___/ \   / | |\/| | / /\ \ | |  |  __  |
 | |      | |  | |  | |/ ____ \| |  | |  | |
 |_|      |_|  |_|  |_/_/    \_\_|  |_|  |_|         
 """)

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

clear_screen()
ascii_art()
print("Pilih rumus:")
print("1. Volume Balok")
print("2. Volume Kubus")
print("3. Volume Tabung")

rumus = int(input("Pilih rumus (1, 2, 3): "))

if rumus == 1:
    volume_balok()
elif rumus == 2:
    volume_kubus()
elif rumus == 3:
    volume_tabung()
else:
    print("Pilihan tidak valid!")
