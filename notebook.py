import os

#clears terminal
def userClear():
    os.system('cls' if os.name == 'nt' else 'clear')


def addNote():
    note = input('Please enter your note: ')
    if note == 'secret':
        print('Holy Moly, you went above and beyond for this one! Props!')
    while True:
        sure = input('Are you sure you want to add this note? (y/n only)').lower().strip()
        if sure.startswith('y'):
            with open('my_notes.txt', 'a') as file:
                file.write(note + '\n')
                print('Note added successfully!')
                break
        elif sure.startswith('n'):
            print('You cancelled your note addition...')
            break
        else:
            print('You entered an unrecognized input, please try again.')

def showHelp():   
    print('''exit - to quit program
note - add note
read - read all notes
delete - remove a selected note from your list
clear - clear the terminal
''')

def readNote():
    try:           
        with open('my_notes.txt', 'r') as file:
            my_notes = file.readlines()
            if not my_notes:
                print('You have no notes saved so far.')
                return
            else:
                print('Here are your notes so far:')
                for i, note in enumerate(my_notes, start=1):
                    print(f'{i}. {note.strip()}')
    except FileNotFoundError:
        print('You have not added any notes yet.')

def deleteNote():
    try:
        with open('my_notes.txt', 'r') as file:
            my_notes = file.readlines()
        for i, note in enumerate(my_notes, start=1):
            print(f'{i}. {note.strip()}')
        delete_selection = int(input('Please type the number of note you want to delete: '))           
        if delete_selection >= 1 and delete_selection <= len(my_notes):
            print(f'Are you sure to delete selected note: {delete_selection}')
            confirm_deletion = input('> ').lower().strip()
            if confirm_deletion == 'y':
                del my_notes[delete_selection - 1]
                with open('my_notes.txt', 'w') as file:
                    file.writelines(my_notes)
                print('Note successfully deleted!')
            elif confirm_deletion == 'n':
                print('You have cancelled the operation.')
            else:
                print('Please try again and enter a valid input. (Y/N)')
        else:
            print('You entered an invalid number, please try again.')
    except ValueError:
        print('You did something wrong, please try again.')
    except FileNotFoundError:
        print('You have not made a note yet.')


print('Your personal notepad, type "help" for a list of commands. Do not worry, there are no SECRETs here...')
user_command = ''

while True:
    user_command = input('> ').lower().strip()
    if user_command == 'help':
        showHelp()
    elif user_command == 'note':
        addNote()
    elif user_command == 'read':
       readNote()
    elif user_command == 'delete':
        deleteNote()
    elif user_command in ['exit', 'quit']:
        print('Signing off...')
        break
    elif user_command == 'clear':
        userClear(user_command)
        print('Terminal successfully cleared!')
    elif user_command == 'secret':
        print('Wow, you really are desperate for easter eggs are you not?')
    else:
        print('Sorry, I do not understand that... Try something else')

    
    

