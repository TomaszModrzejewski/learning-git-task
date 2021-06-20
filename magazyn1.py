import csv

items = {
    "czekolada": {
        "name": "czekolada", "quantity": 500.0, "unit": "szt", "unit_price": 4.0},
    "tofu": {
        "name": "tofu", "quantity": 200.0, "unit": "szt", "unit_price": 7.0},
    "soczewica": {
        "name": "soczewica", "quantity": 100.0, "unit": "kg", "unit_price": 3.0},
    "mleko owsiane": {
        "name": "mleko owsiane", "quantity": 1000.0, "unit": "l", "unit_price": 5.0}    
}

param = ["Name", "Quantity", "Unit", "Unit Price(PLN)"]

def get_items():
    print()
    print(f"{param[0]:20} {param[1]:>8} {param[2]:>6} {param[3]:>10} ")
    print("=" * 56)

    for item in items:
        product_name = items[item]["name"]
        product_quantity = items[item]["quantity"]
        product_unit = items[item]["unit"]
        product_unit_price = items[item]["unit_price"]
        print(f"{product_name:20} {product_quantity:>8} {product_unit:>6} {product_unit_price:>10}")
            
    print()


def add_item():
    name = input("Please enter the name of the product: ")
    quantity = float(input("Please enter the quantity: "))
    unit = input("Please put the unit (l, kg, g, szt etc. ): ")
    unit_price = float(input("Please put price per unit in PLN: "))
    new_dict = {
        name: {"name": name, "quantity": quantity, "unit": unit, "unit_price": unit_price}
    }

    items.update(new_dict)

    get_items()


def sell_item():
    item_to_sell = input("Which item would you like to sell? ")
    if item_to_sell in items:
        sell_quantity = float(input("How much did you sell? "))
        items[item_to_sell]["quantity"] -= sell_quantity
        sell_dict = {
                "name": item_to_sell,
                "quantity": sell_quantity,
                "unit": items[item_to_sell]["unit"],
                "unit_price": items[item_to_sell]["unit_price"]
        }
        sold_items.append(sell_dict)

    else:
        print()
        print("The item is not present in the database!")
        print()

    get_items()


def get_costs():
    values_list = [items[item]["quantity"] * items[item]["unit_price"] for item in items]
    costs = round(sum(values_list), 2)

    return costs


def get_income():
    values_list = [sold_items[i]["quantity"] * sold_items[i]["unit_price"] for i in range(len(sold_items))]
    income = round(sum(values_list), 2)

    return income


def show_revenue():
    print("Income: " + str(get_income()) + " zł")
    print("Costs: " + str(get_costs()) + " zł")
    print("-" * 56)
    print("Revenue: " + str((get_income() - get_costs())) + " zł")
    print()


def export_items_to_csv():
    with open("magazyn.csv", "w") as magazyn:
        for key in items:
            ex_name = items[key]["name"]
            ex_quan = items[key]["quantity"]
            ex_unit = items[key]["unit"]
            ex_unit_price = items[key]["unit_price"]
            magazyn.write(f"{ex_name},{ex_quan},{ex_unit},{ex_unit_price}\n")  


def import_items_from_csv():
    fieldn = ["name", "quantity", "unit", "unit_price"]
    items.clear()
    with open("magazyn.csv", "r") as magazyn:
        for line in csv.DictReader(magazyn, fieldnames=fieldn):
            items[line["name"]] = {
                "name": line["name"], 
                "quantity": float(line["quantity"]),
                "unit": line["unit"],
                "unit_price": float(line["unit_price"])}

    get_items()    

sold_items = []
while True:
    choice = input("What would you like to do? ")
    if choice == "exit":
        break
    elif choice == "get":
        get_items()
    elif choice == "add":
        add_item()
    elif choice == "sell":
        sell_item()
    elif choice == "show":
        show_revenue()
    elif choice == "save":
        export_items_to_csv()
    elif choice == "load":
        import_items_from_csv()
    else:
        print("Please choose a correct action!")
        print()