print("Hello, it is nice to see you. You can choose show, exit, ")
items = [{"name:": [1], "quantity:": [2], "unit:": [3], "unit_price:": [4]},
         {"name:": [11], "quantity:": [22], "unit:": [33], "unit_price:": [44]},
         {"name:": [111], "quantity:": [222], "unit:": [333], "unit_price:": [444]}]



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
                print(z, "\t")