import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

menu_list = [
    {'name': 'Margarita', 'ingredients': 'tomato sauce, mozzarella, basil leaves', 'price': 100},
    {'name': 'Hawaiian', 'ingredients': 'pizza sauce, hollandaise cheese, cooked ham, pineapple', 'price': 118},
    {'name': 'Marinara', 'ingredients': 'tomatoes, garlic, olive oil, oregano, marinara sauce', 'price': 107},
    {'name': 'Neapolitan', 'ingredients': 'tomatoes, mozzarella, parmesan, anchovies, olive oil, oregano, basil', 'price': 123},
    {'name': 'Pepperoni', 'ingredients': 'pepperoni salami, mozzarella, pizza sauce, black pepper, oregano', 'price': 109},
    {'name': 'Regina', 'ingredients': 'tomatoes, mozzarella, champignons, ham, oregano, black olives', 'price': 103},
    {'name': 'Four cheeses', 'ingredients': 'mozzarella, emmental, gorgonzola, parmesan, tomato sauce', 'price': 110},
    {'name': 'Four seasons', 'ingredients': 'olives, artichokes, salami, black pepper, tomatoes, mozzarella, mushrooms, boiled eggs', 'price': 112},
    {'name': 'Diabola', 'ingredients': 'salami, calabrian pepper, mozzarella', 'price': 102},
    {'name': 'Fungi', 'ingredients': 'mozzarella, mushrooms, sausages, tomatoes', 'price': 100},
    {'name': 'Tuna', 'ingredients': 'mozzarella, tuna, tomatoes', 'price': 114},
    {'name': 'Tomato', 'ingredients': 'olive oil, garlic, oregano, tomatoes', 'price': 97},
    {'name': 'Capricciosa', 'ingredients': 'mozzarella, baked ham, mushrooms, tomatoes, artichokes', 'price': 106},
    {'name': 'Seafood', 'ingredients': 'pizza sauce, squid, mussels, shrimps, salmon, green olives, mozzarella', 'price': 116},
    {'name': 'Stromboli (rolled pizza)', 'ingredients': 'ham, mozzarella, garlic, pizza seasoning', 'price': 100},
    {'name': 'Exotic', 'ingredients': 'salted ham, peaches, mozzarella, black olives', 'price': 103},
    {'name': 'Chicken', 'ingredients': 'baked chicken, green olives, hollandaise cheese, champignons, tomato sauce', 'price': 100},
]

cur = connection.cursor()

for menu_item in menu_list:
    cur.execute('INSERT INTO menu (name, ingredients, price) VALUES (?, ?, ?)', (menu_item['name'], menu_item['ingredients'], menu_item['price']))

connection.commit()
connection.close()
