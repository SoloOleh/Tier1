clothes = ['shirt', 'hat', 'jeans', 'trainers']
sorted_clothes = sorted(clothes)
print (sorted_clothes) #['hat', 'jeans', 'shirt', 'trainers']
print (clothes) #['shirt', 'hat', 'jeans', 'trainers']
#sorted_clothes - це копія списку clothes, її створення не змінило оригінальний список clothes. А використання функції sort() змінює сам список clothes:
clothes.sort()
print (clothes) #['hat', 'jeans', 'shirt', 'trainers']