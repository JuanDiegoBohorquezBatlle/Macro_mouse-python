from pynput.mouse import Listener, Button, Controller
from pynput import keyboard

def on_click(key2):

    if key2 == keyboard.KeyCode.from_char('l'):
        print(f'Coordenadas x, y = {mouse.position}')

def on_press(key):
    if key == keyboard.KeyCode.from_char('q'):
        print(f'Coordenadas x, y = {mouse.position}')
        mouse_listener.stop()
        return False
        

mouse = Controller()
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()
keyboard_listener2 = keyboard.Listener(on_click=on_click)
keyboard_listener2.start()

with Listener(on_click=on_click) as mouse_listener:
    mouse_listener.join()



