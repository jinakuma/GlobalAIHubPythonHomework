print("Lütfen 5 adet sayı giriniz:")
sayilar=[]
for i in range(5):
    sayi = input()
    sayilar.append(sayi)
for i in range(1,6):
	print(f"{i}. sayı: {sayilar[i-1]}, {i}. sayı veri tipi: {type(sayilar[i-1])}" )
