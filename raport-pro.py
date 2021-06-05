requefort = "requefort"
stilton = "stilton"
brie = "brie"
gouda = "gouda"
edam = "edam"
parmezan = "parmezan"
mozzarella = "mozzarella"
czechoslovakian = "czechosłowacki"

text = " {} --> mass in kg: {} --> price: {}"

requefort_weight = 2 
stilton_weight = 1
brie_weight = 1
gouda_weight = 1
edam_weight = 1
parmezan_weight = 3.5
mozzarella_weight = 1.3
czechoslovakian_weight = 2.2

requefort_price = 12.5 * requefort_weight
stilton_price = 11.24
brie_price = 9.3
gouda_price = 8.55
edam_price = 11
parmezan_price = 16.5 * parmezan_weight
mozzarella_price = 14 * mozzarella_weight
czechoslovakian_price = 122.32 * czechoslovakian_weight

print()
print("         Shopping list        ")
print()
print()

reguefort_cheese = text.format(requefort, requefort_weight, requefort_price)
stilton_cheese = text.format(stilton, stilton_weight, stilton_price)
brie_cheese = text.format(brie, brie_weight, brie_price)
gouda_cheese = text.format(gouda, gouda_weight, gouda_price)
edam_cheese = text.format(edam, edam_weight, edam_price)
parmezan_cheese = text.format(parmezan, parmezan_weight, parmezan_price)
mozzarella_cheese = text.format((mozzarella), 
                                (mozzarella_weight), 
                                (mozzarella_price))
czechoslovakian_cheese = text.format((czechoslovakian), 
                                     (czechoslovakian_weight), 
                                     (czechoslovakian_price))

print()
pantry = [
  (reguefort_cheese),
  (stilton_cheese),
  (brie_cheese),
  (gouda_cheese),
  (edam_cheese),
  (parmezan_cheese),
  (mozzarella_cheese),
  (czechoslovakian_cheese),
]
for i, (item) in enumerate(pantry):
    print('#{}: {:<10s}'.format(i + 1, item))

print()
list = [(requefort_weight), 
        (stilton_weight), 
        (brie_weight), 
        (edam_weight), 
        (gouda_weight), 
        (parmezan_weight), 
        (mozzarella_weight), 
        (czechoslovakian_weight)]

weight = sum(list)
print('The total mass is:', round(weight), 'kg')
print() 
list = [(requefort_price), 
        (stilton_price), 
        (brie_price), 
        (edam_price), 
        (gouda_price), 
        (parmezan_price), 
        (mozzarella_price), 
        (czechoslovakian_price)]
price = sum(list)
print('Your entire cost is:', price, 'zł')
