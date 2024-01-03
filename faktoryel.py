# Faktöriyel hesaplayan bir fonksiyon tanımlayın
def faktoriyel(sayi):
    # Sayı sıfır veya bir ise 1 döndürün
    if sayi == 0 or sayi == 1:
        return 1

    # Sayı negatif ise hata mesajı verin
    elif sayi < 0:
        print("Negatif sayıların faktöriyeli hesaplanamaz.")
        return None

    # Sayı pozitif ise, sayı ile fonksiyonun bir azaltılmış değeri için çağrısının çarpımını döndürün
    else:
        return sayi * faktoriyel(sayi - 1)

# Kullanıcıdan bir sayı alın
sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))

# Fonksiyonu çağırın ve sonucu ekrana yazdırın
print(f"{sayi}! = {faktoriyel(sayi)}")
