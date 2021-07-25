print(f'**************************************\n**    Welcome to the Snakes Cafe!   **\n**    Please see our menu below.    **\n**\n** To quit at any time, type "quit" **\n**************************************')
menue=["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"]

def orders():
    print(f'Appetizers\n---------\n{menue[0]}\n{menue[1]}\n{menue[2]}\n')
    print(f'Entrees\n---------\n{menue[3]}\n{menue[4]}\n{menue[5]}\n{menue[6]}\n')
    print(f'Desserts\n---------\n{menue[7]}\n{menue[8]}\n{menue[9]}\n')
    print(f'Drinks\n---------\n{menue[10]}\n{menue[11]}\n{menue[12]}\n')

    print(f'***********************************\n** What would you like to order? **\n***********************************')

    order=[]
    choice=input(' ')

    while choice != 'quit':
        if choice in menue:
            order.append(choice)
            print(f'**{order.count(choice)}order of {choice} have been added to your meal **')
            choice=input(' ')
        else:
            print('choose from the menue please?')
            choice=input(' ')
orders()