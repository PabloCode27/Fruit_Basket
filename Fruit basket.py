fruits = ['Banana']

while True:
    add = input('Enter a fruit (or press Quit): ').strip().title()
    if add == 'Quit':
        print('Your final list is', fruits)
        print('Goodbye!!')
        break
    elif add == '':
        print('Invalid input')
    elif not add.replace(' ', '').isalpha():
        print('Invalid input: please use only letters')
    elif add not in fruits:
        print('New fruit discovered, Adding it...')
        fruits.append(add)
        print(fruits)
    else:
        print('That item is in the list')
        print('See', fruits)
    
    
