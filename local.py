import requests

test1 = requests.get("http://127.0.0.1:3000/obj/0")
print(test1.json())


test3 = requests.post("http://127.0.0.1:3000/obj/4", json = {"adress": "qwert1", "state": "qwert2", "admin": "qwert3"})

#test4 = requests.get("http://127.0.0.1:3000/obj/4")
#print(test4)

test5 = requests.delete("http://127.0.0.1:3000/obj/2")

test1 = requests.get("http://127.0.0.1:3000/obj/0")
print(test1.json())



#test3 = requests.post("http://127.0.0.1:3000/name", {"problems":"some_problem33"})

#adr = input("input the adress of object: ")
#st = input("input the state of object: ")
#adm = input("input the name of administrator of object: ")
#requests.post("http://127.0.0.1:3000/", {"adress":adr, "state":st, "admin":adm})
