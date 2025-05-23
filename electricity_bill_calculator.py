from num2words import num2words

narx_kw = 0.45
oy_boshi = float(input("oy boshidagi kwh ni kiriting :"))
oy_oxiri = float(input("oy oxiridagi kwh ni kiriting :"))
jami = (oy_oxiri - oy_boshi) * 0.45
print(jami)

print(num2words(jami , lang="en"))
print(num2words(jami , lang="ru"))
