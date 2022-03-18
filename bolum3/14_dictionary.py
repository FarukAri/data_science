
# plakalar = {"malatya" : "44", "manisa" : "45"}

# print (plakalar["malatya"])

# plakalar["ankara"] = 6 # Yeni bir değer eklenebilir.
# plakalar["manisa"] = 99 # Varolan bir değer değiştirilebilir.

# print (plakalar)

users = {
    "Faruk Arı" : {
        "Age" : 26,
        "Roles" : ["SG","C"],
        "Height" : 185,
        "Adress" : "Manisa"
    },
    
    "Stephen Curry" :{
        "Age" : 33,
        "Roles" : ["SG","PG"],
        "Height" : 191,
        "Adress" : "California",
    }
}


print(users["Stephen Curry"])
print(users["Stephen Curry"]["Height"])
print(users["Stephen Curry"]["Roles"][0])