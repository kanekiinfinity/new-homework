import json
import re

matn = """Welcome to our tdm tounament !
Our gamers names are:
Aslamboi:
aslamboi2244@.gmail.com
TeoTimur:
teotimurcantFly@gmail.com
Star Capitan:
starcaptanhd@gmail.com
Yakudza:
yakudzajet57@gmail.com"""

andoza = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

gmail = re.findall(andoza,matn)


with open('veb_manzil.txt','w') as m:
    json.dump(gmail,m)

