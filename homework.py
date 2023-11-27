import datetime as dt

bugun = dt.date.today()
for i in range(1, 11):
    sana = bugun + dt.timedelta(weeks=i*2)
    print(sana)




import datetime as dt

hozir = dt.datetime.today()
yosh = dt.datetime(2009, 6, 16, 00, 00, 00)
farq= hozir-yosh

kun = farq.days
soat = kun*60
minut = soat*60
sekund = minut*60
print(f"Meni tug'ilganimga {kun} kun bolibdi")
print(f"Meni tug'ilganimga {soat} soat bolibdi")
print(f"Meni tug'ilganimga {minut} minut bolibdi")
print(f"Meni tug'ilganimga {sekund} sekund bolibdi")




