import sqlite3

connection = sqlite3.connect('database.db')
cur = connection.cursor()
connection.row_factory = sqlite3.Row

while True:
    user_input = input('Enter what you want to do (add, edit, delete, exit))\n').lower()
    if user_input == 'add':
        name = str(input('Enter a name for the dish\n'))
        ingredients = str(input('Enter the ingredients for the dish in following pattern: \"i1, i2, i3, i4, ...\"\n'))
        price = int(input('Enter a price for the dish\n'))

        cur.execute('INSERT INTO menu (name, ingredients, price) VALUES (?, ?, ?)',
                    (name, ingredients, price))

        print('successfully created')

    elif user_input == 'edit':
        id = input('Enter an id of the dish you want to edit\n')
        dish = connection.execute('SELECT * FROM menu WHERE id = ?', (id,)).fetchone()

        name = input('Enter a new name for the dish\n')
        ingredients = input('Enter the new ingredients for the dish in following pattern: \"i1, i2, i3, i4, ...\"\n')
        price = input('Enter a new price for the dish\n')

        connection.execute('UPDATE menu SET name = ?, ingredients = ?, price = ? WHERE id = ?',
                           (name, ingredients, price, id))

        print('successfully edited')

    elif user_input == 'delete':
        id = input('Enter an id of the dish you want to delete\n')
        connection.execute('DELETE FROM menu WHERE id = ?', (id,))

        print('successfully deleted')

    elif user_input == 'exit':
        connection.commit()
        connection.close()
        break

    else:
        print('Error. Please try again')
