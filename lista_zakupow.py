print("Shopping list")
shopping_dict = {
      "Bakery": ["bread", "donut", "rolls"],
      "Vegetables store": ["carrots", "celery", "arugula"]
      
}

shopping_count = 0
text = "I go to {}, buy the following things here: "
text_a = "In total, I buy {} products."

for shop in shopping_dict:
    store = text.format(shop.capitalize())
    for article in shopping_dict[shop]:
        store += "," + article.capitalize()  
    print(store)                                                             
    shopping_count += len(shopping_dict[shop])
print(text_a.format(shopping_count))
print()

five = list(range(5, 101, 5))
print(five)
print()
five_to_the_third = [i**3 for i in five]
print(five_to_the_third)
