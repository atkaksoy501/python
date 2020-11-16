#encoding: utf-8

import random

num = random.randint(0,100)

print("Hoşgeldiniz.")

for attempt in range (1, 8):
    guess = int(input("0 ile 100 arasında bir tam sayı giriniz: "))
    if guess == num:
        print("Tebrikler!", attempt, "\b'inci denemede sayıyı doğru tahmin ettiniz!")
        break
    if guess < num:
        print("Tahmininiz küçük.")
    if guess > num:
        print("Tahmininiz büyük.")

if guess != num:
    print("Sayıyı bulamadınız. Doğru cevap:", num)

