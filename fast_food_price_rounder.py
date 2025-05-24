from num2words import num2words


narx_1 = float(input("narxni kiriting :"))
narx_2 = float(input("narxni kiriting :"))
narx_3 = float(input("narxni kiriting :"))

jami_narxi = narx_1 + narx_2 + narx_3 
print(jami_narxi)
print(num2words(jami_narxi , lang="en"))
print(num2words(jami_narxi , lang="ru"))
