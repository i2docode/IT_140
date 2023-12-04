#!/usr/bin/python3
# Aaron Bevans

def player_instructions():
    # displays main menu and commands.
    print('\n** Rogue Alien Hunter **\n')
    print('[ Objective ]: Successfully collect 6 items to defeat the Alien, or meet your doom!\n')
    print('[ Mobility Commands ]: go north, go south, go east, go west\n')
    print("[ Add to your inventory ]: get 'item name'\n")
    print("[ To Exit ]: exit")
player_instructions()

def main():
    pass
    """
    a dictionary that links rooms within the space-craft.
    this dictionary also links an item/weapon to its assigned room, & Alien's location.
    starting poing/corridor does not contain an item/weapon.
    """
    rooms_and_items = {
        'Corridor': {'South':'Flight Deck', 'East':'Medical Bay', 'West':'Engineering Lab', 'item':'night-vision goggles'},

        'Fight Deck':{'North':'Corridor', 'East':'Kennel', 'West':'Boiler Room', 'item':'Alien'},

        'Kennel':{'North':'Medical Bay', 'West':'Flight Deck', 'item':'Jet Pack'},

        'Medical Bay':{'North':'Mess Hall', 'West':'Corridor', 'South':'Kennel', 'item':'Attack Dog'},

        'Engineering Lab':{'East':'Corridor', 'North':'Server Room', 'item':'holographic tablet'},

        'Server Room':{'South':'Engineering Lab', 'East':'Armory', 'item':'laser cannon'},

        'Armory':{'West':'Server Room', 'East':'Mess Hall', 'item':'roast beef'},

        'Mess Hall':{'West':'Armory', 'South':'Medical Bay', 'item':'anti-venom'},

        'Boiler Room':{'East':'flight deck', 'item':'Alien'}
    }


    inventory = []
    user_input = \
    """
    \n
    You are in the Corridor

    your move: [ 1. go south, 2. go east, 3. go west ]\n
    """
    
    start = input(f'{user_input}')

    while start != '':

        location = ''

        # first start option from the Corridor location.
        if start == 'go east':

            inventory = []

            location = \
            """
            'You are in the Medical Bay'
            """

            print(location)

            print(f'\t\tinventory = {inventory}')
            
            east_move = \
            """
            your move: [ 1. go north, 2. go south, 3. go west, 4. get item ]\n
            """
            
            med_bay_move = input(f'{east_move}')

            
            if med_bay_move == 'get item':

                med_bay_item = 'Anti-Venom'

                inventory.append(med_bay_item)

                print(f'\t\tinventory = {inventory}')
            
            elif med_bay_move == 'go north':
                location = \
                """
                'You are in the Mess Hall'
                """
                print(location)



            else:
                exit()
        else:
            exit()


        
        
        






    

main()
