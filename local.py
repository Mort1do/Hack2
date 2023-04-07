import requests

print(" 1)Get object from server", '\n', "2)Input object to the server: ")
num = int(input("input the number:"))
if num == 1:
    i = input("Input the number(index) of object: ")
    line = "http://127.0.0.1:3000/obj/" + i
    get = requests.get(line)
    print(get.json())
elif num == 2:
    adr = str(input("Input the adress of object: "))
    st = str(input("Input the state of object: "))
    adm = str(input("Input the name of admin of object: "))
    test3 = requests.post("http://127.0.0.1:3000/obj/4", json = {"adress": adr, "state": st, "admin": adm})
else:
    print("Error")

#test4 = requests.get("http://127.0.0.1:3000/obj/4")
#print(test4)

#test5 = requests.delete("http://127.0.0.1:3000/obj/2")

#test1 = requests.get("http://127.0.0.1:3000/obj/2")
#print(test1.json())



#test3 = requests.post("http://127.0.0.1:3000/name", {"problems":"some_problem33"})

#adr = input("input the adress of object: ")
#st = input("input the state of object: ")
#adm = input("input the name of administrator of object: ")
#requests.post("http://127.0.0.1:3000/", {"adress":adr, "state":st, "admin":adm})
