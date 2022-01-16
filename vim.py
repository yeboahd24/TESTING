import string
import keyboard

keys = ['cmd', 'alt', 'shift', 'tab', 'delete', 'Backspace', 'enter', 'ctrl', 'spacebar', 'insert',
        'end', 'escape', 'home', 'pageup', 'pagedown', 'numlock','pause', 'f1', 'f2', 'f3', 'f4',
        'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12'
        ]

restricted_ls = ['end', 'escape', 'home', 'pageup', 'pagedown', 'numlock', 'pause', 'capslock','spacebar',
                 'capslock', 'delete', 'Backspace', 'enter', 'tab', 'insert']# these are keys which isnt in any starting of a keyboard shortcuts


#Using keyboard module to check for chained keypresses

# Using keyboard module to check for chained keypresses

def check_chained_keys(key):
    if key in keys:
        return True
    else:
        return False
    
def check_restricted_keys(key):
    if key in restricted_ls:
        return True
    else:
        return False
    
def check_chained_keys_with_restricted_keys(key):
    if check_chained_keys(key) or check_restricted_keys(key):
        return True
    else:
        return False
    
# print(check_chained_keys_with_restricted_keys('shift'))


ls = []
for i in string.ascii_lowercase:
    keys.append(i)
    
# posible key combinations
for i in keys:
    for j in keys:
        if i != j and check_chained_keys_with_restricted_keys(i) and check_chained_keys_with_restricted_keys(j):
            ls.append(i + j)
           
           
while True:
    for i in ls:
        if keyboard.is_pressed(i):
            print(i)
            break