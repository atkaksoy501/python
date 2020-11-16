#encoding:utf-8

import shelve

turk_dict = "turk_dict.txt"
eng_dict = "eng_dict.txt"

turk = shelve.open(turk_dict)
eng = shelve.open(eng_dict)

print("Hoşgeldiniz.")

while True:
    print("Lütfen sözlük dilini seçiniz.")
    dil = input("Türkçe - İngilizce için T, İngilizce - Türkçe için I giriniz: ").lower()
    if dil == "t":
        kelime = input("İngilizceye çevirmek istediğiniz Türkçe kelimeyi giriniz: ").lower()
        if kelime in turk:
            print(kelime, "kelimesinin anlamı:", turk[kelime])
        else:
            a = input("Bu kelime sözlükte tanımlı değildir. Tanımlamak için 'ekle' yazınız. ").lower()
            if a == "ekle":
                eklenecek = input("Kelimenin İngilizce anlamını giriniz. ")
                turk[kelime] = eklenecek
                print(kelime, "kelimesinin anlamı", eklenecek, "olarak tanımlandı.")
    if dil == "i":
        kelime = input("Türkçeye çevirmek istediğiniz İngilizce kelimeyi giriniz: ").lower()
        if kelime in eng:
            print(kelime, "kelimesinin anlamı:", eng[kelime])
        else:
            a = input("Bu kelime sözlükte tanımlı değildir. Tanımlamak için 'ekle' yazınız. ").lower()
            if a == "ekle":
                eklenecek = input("Kelimenin Türkçe anlamını giriniz. ")
                turk[kelime] = eklenecek
                print(kelime, "kelimesinin anlamı", eklenecek, "olarak tanımlandı.")

turk.close()
eng.close()
    