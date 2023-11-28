import json
import re

matn = """Welcome to our tdm tounament !
Our gamers names are:
Aslamboi-email:aslamboi2244@.gmail.com
TeoTimur-email:teotimurcantFly@gmail.com
Star Capitan-email:starcaptanhd@gmail.com
Yakuda-email:yakudzajet57@gmail.com"""

andoza = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

gmail = re.findall(andoza,matn)


with open('veb_manzil.txt','w') as m:
    json.dump(gmail,m)

