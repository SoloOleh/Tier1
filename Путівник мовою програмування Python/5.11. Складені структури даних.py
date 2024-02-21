dairy_products = ['butter', 'cheese', 'yoghurt']
vegetables = ['potatoes', 'broccoli', 'carrot', 'cucumber', 'onion']
light_snacks = ['biscuits', 'chocolate', 'nuts']

tuple_of_lists = dairy_products, vegetables, light_snacks
print (tuple_of_lists) # (['butter', 'cheese', 'yoghurt'], ['potatoes', 'broccoli', 'carrot', 'cucumber', 'onion'], ['biscuits', 'chocolate', 'nuts'])

list_of_lists = [dairy_products, vegetables, light_snacks]
print (list_of_lists) #[['butter', 'cheese', 'yoghurt'], ['potatoes', 'broccoli', 'carrot', 'cucumber', 'onion'], ['biscuits', 'chocolate', 'nuts']]

dict_of_lists = {'Dairy': dairy_products, 'Vegetables': vegetables, 'Snacks': light_snacks}
print (dict_of_lists) #{'Snacks': ['biscuits', 'chocolate', 'nuts'], 'Vegetables': ['potatoes', 'broccoli', 'carrot', 'cucumber', 'onion'], 'Dairy': ['butter', 'cheese', 'yoghurt']}


sports_equipment = {
('1500 metres', 'high jump', 'shot put'): 'Athletics',
('goalkeeper', 'foul', 'corner'): 'Football',
('handlebars', 'wheels', 'bicycle pump'): 'Cycling'
}
print (sports_equipment) #{('1500 metres', 'high jump', 'shot put'): 'Athletics', ('handlebars', 'wheels', 'bicycle pump'): 'Cycling', ('goalkeeper', 'foul', 'corner'): 'Football'}