from num2words import num2words


km = float(input("kmni kiriting :"))
boshlangich_tolov = 5.00
har_bir_km_uchun = 0.80
jami = km * har_bir_km_uchun+ boshlangich_tolov

print("$" ,jami)
print(num2words(jami , lang="ru"))
print(num2words(jami , lang="en"))

