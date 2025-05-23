from num2words import num2words
from decimal import Decimal

boshlangin_narxi = Decimal("3.00")
km_1 = Decimal("1.20")
km = Decimal(input("km ni kiriting :"))
taxi_narxi = (km * km_1) + boshlangin_narxi

print(taxi_narxi)

print(num2words( taxi_narxi , lang='ru') )

print(num2words( taxi_narxi , lang='en') )