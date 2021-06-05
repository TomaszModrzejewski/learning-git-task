requefort = "requefort"
stilton = "stilton"
brie = "brie"
gouda = "gouda"
edam = "edam"
parmezan = "parmezan"
mozzarella = "mozzarella"
czechoslovakian = "czechosłowacki"

requefort_price = 12.5 
stilton_price = 11.24
brie_price = 9.3
gouda_price = 8.55
edam_price = 11
parmezan_price = 16.5
mozzarella_price = 14
czechoslovakian_price = 122.32

pantry = [
  (requefort, requefort_price),
  (stilton, stilton_price),
  (brie, brie_price),
  (gouda, gouda_price),
  (edam, edam_price),
  (parmezan, parmezan_price),
  (mozzarella, mozzarella_price),
  (czechoslovakian, czechoslovakian_price),
]

for i, (item, count) in enumerate(pantry):
    print('#{}: {:<10s} = {}'.format(i + 1, item, count))
list = [(requefort_price), 
        (stilton_price), 
        (brie_price), 
        (edam_price), 
        (gouda_price), 
        (parmezan_price), 
        (mozzarella_price), 
        (czechoslovakian_price)]
price = sum(list)
print('#9: Your entire cost is:', price, "zł")
