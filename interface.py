import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def list(list_items, numbered=True, clear_screen=False):
    
    if clear_screen:
        clear()
    
    if numbered:
        number = 1
        for item in list_items:
            print(number, item)
            number = number + 1
    else:
        for item in list_items:
            print(item)