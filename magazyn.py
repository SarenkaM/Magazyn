print("Hello, it is nice to see you. You can choose show, exit, ")
items = [{"name:": "Pomidory", "quantity:": 20, "unit:": "kg", "unit_price:": 4.2},
         {"name:": "Ogórki", "quantity:": 22, "unit:": "kg", "unit_price:": 5.0},
         {"name:": "Marchewka", "quantity:": 15, "unit:": "kg", "unit_price:": 6.5}]



odp = 0
while odp != "exit":
    odp = (input("What would you like to do? "))
    if odp == ("exit"):
        print("Exiting... Bye")
        exit()
    elif odp == ("show"):
        print("Name\tQuantity\tUnit\tPrice (PLN)")
        for i in items:
            for z in i.values():
                print(z, "\t", end = " ")
            print("")