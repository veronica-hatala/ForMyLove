#data setup

rooms = dict(bedroom={
    'name': 'Bedroom',
    'east': 'yoka',
    'west': 'maharu',
    'north': 'lameera',
    'south': 'riamgular',
    'contents': ['blanket'],
    'text': 'The room is cold and barren aside from your stone bed with a meager quilt.',
    'visited': False,
}, yoka={
    'name': 'Yoka Shrine',
    'west': 'bedroom',
    'contents': ['herbs', 'lilies'],
    'text': 'A statue of Yoka features prominently. Scattered herbs are left on her altar.',
    'visited': False,
}, maharu={
    'name': 'Maharu Shrine',
    'east': 'bedroom',
    'contents': ['twigs', 'shells'],
    'text': 'A statue of Maharu is at the center of the room. He hold calligraphy brushes and paper. Twigs and '
            'shells are left as offerings on his altar. ',
    'visited': False,
}, lameera={
    'name': 'Lameera Shrine',
    'south': 'bedroom',
    'contents': ['jewels', 'crown'],
    'text': 'The statue of Lameera peers into your soul. She wears a crown and her altar is covered in jewels',
    'visited': False,
}, riamgular={
    'name': 'Riamgular Shrine',
    'north': 'bedroom',
    'contents': ['bones', 'sword'],
    'text': 'The statue of Riamgular looks ready to strike.',
    'visited': False,
})
directions = ['north', 'south', 'east', 'west']
current_room = rooms['bedroom']
carrying = []

yokaAwakened = False
riamgularAwakened = False
lameeraAwakened = False
maharuAwakened = False

gameplay = True

def checkCompletion():
    global gameplay
    if yokaAwakened is True and maharuAwakened is True and lameeraAwakened is True and riamgularAwakened is True:
        gameplay = False
        print("The Rituals are complete.")

def yokaRitual():
    print("Upon placing the bones on the altar, the eyes of Yoka glow.")
    global yokaAwakened
    yokaAwakened = True
    print("CHECK:" + str(yokaAwakened))
    checkCompletion()

def maharuRitual():
    print("Upon placing the lilies on the altar, the eyes of Maharu glow.")
    global maharuAwakened
    maharuAwakened = True
    print("CHECK:" + str(maharuAwakened))
    checkCompletion()

def lameeraRitual():
    print("Upon placing the shells on the altar, the eyes of Lameera glow.")
    global lameeraAwakened
    lameeraAwakened = True
    checkCompletion()

def riamgularRitual():
    print("Upon placing the crown on the altar, the eyes of Riamgular glow.")
    global riamgularAwakened
    riamgularAwakened = True
    checkCompletion()

#game loop
while gameplay is True:
        print()

        #  print("CHECKS: " + str(lameeraAwakened) + str(riamgularAwakened) + str(yokaAwakened) + str(maharuAwakened))
        print('You are in {}.'.format(current_room['name']))
        print(current_room['text'])

        command = input('\nWhat do you do?').strip()
        if command in directions:
            if command in current_room:
                current_room = rooms[current_room[command]]
            else:
                print("You can't go that way.")
        #quit
        elif command.lower() in ('q', 'quit'):
            break
        #check bag
        elif command.lower() in ('i', 'inventory', 'contents', 'bag'):
            print(carrying)
        #check contents of room
        elif command.lower() in ('objects', 'o', 'room contents'):
            print(current_room['contents'])
        #gather objects
        elif command.lower().split()[0] == 'get':
            item = command.lower().split()[1]
            if item in current_room['contents']:
                current_room['contents'].remove(item)
                carrying.append(item)
        #drop objects
        elif command.lower().split()[0] == 'drop':
            item = command.lower().split()[1]
            if item in carrying:
                current_room['contents'].append(item)
                carrying.remove(item)
            if current_room == rooms['yoka'] and item == 'bones':
                yokaRitual()
            if current_room == rooms['maharu'] and item == 'peonies':
                maharuRitual()
            if current_room == rooms['lameera'] and item == 'shells':
                lameeraRitual()
            if current_room == rooms['riamgular'] and item == 'crown':
                riamgularRitual()
        else:
            print("Invalid command.")


