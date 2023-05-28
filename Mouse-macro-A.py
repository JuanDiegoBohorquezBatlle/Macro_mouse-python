# # # # import time
# # # # # import os
# # # # # import sys
# # # # from pynput.mouse import Button, Controller, Listener
# # # # from pynput import keyboard
# # # # from pynput.mouse import Listener

# # # # mouse = Controller()

# # # # # def on_press(tecla):
# # # # #     if tecla == keyboard.KeyCode.from_char('q'):
# # # # #         return False
# # # # # escuchador = keyboard.Listener(on_press)
# # # # # escuchador.start()




# # # # # def on_press(tecla):
# # # # # 	print('Se ha pulsado la tecla ' + str(tecla))
# # # # # escuchador = Listener.join(on_press)
# # # # # #escuchador = mouse.Listener(on_press)
# # # # # escuchador.start()

# # # # # while escuchador.is_alive():
# # # # #     # mouse.click(Button.left)
# # # # #     time.sleep(0.1)

# # # # #from pynput.mouse import Listener


# # # # def on_click(x, y, button, pressed):
# # # #     if button == Button.x1 and pressed:
# # # #         target_x = 575
# # # #         target_y = 429
# # # #         mouse.position = (target_x, target_y)
# # # #         if keyboard.KeyCode.from_char('q') == True:
# # # #             return False



# # # # with Listener(on_click=on_click) as listener:
# # # #     listener.join()

# # # # # # from pynput.mouse import Listener, Button, Controller
# # # # # # from pynput import keyboard

# # # # # # def on_click(x, y, button, pressed):
# # # # # #     if button == Button.x1 and pressed:
# # # # # #         # Coordenadas a las que se desea mover el cursor
# # # # # #         target_x = 500
# # # # # #         target_y = 300

# # # # # #         mouse.position = (target_x, target_y)

# # # # # # def on_press(key):
# # # # # #     if key == keyboard.Key.q:
# # # # # #         return False

# # # # # # mouse = Controller()
# # # # # # keyboard_listener = keyboard.Listener(on_press=on_press)
# # # # # # keyboard_listener.start()

# # # # # # with Listener(on_click=on_click) as mouse_listener:
# # # # # #     mouse_listener.join()
# # # # # #     if on_press == False:
# # # # # #         mouse_listener.qstop()

# # # # from pynput.mouse import Listener, Button, Controller
# # # # from pynput import keyboard

# # # # def on_click(x, y, button, pressed):
# # # #     if button == Button.x1 and pressed:
# # # #         # Coordenadas a las que se desea mover el cursor
# # # #         target_x = 500
# # # #         target_y = 300

# # # #         mouse.position = (target_x, target_y)

# # # # def on_press(key):
# # # #     if key == keyboard.KeyCode.from_char('q'):
# # # #         return False

# # # # mouse = Controller()
# # # # keyboard_listener = keyboard.Listener(on_press=on_press)
# # # # keyboard_listener.start()

# # # # with Listener(on_click=on_click) as mouse_listener:
# # # #     mouse_listener.join()
# # # #     keyboard_listener.stop()



# # # # from pynput.mouse import Listener, Button, Controller
# # # # from pynput import keyboard

# # # # def on_click(x, y, button, pressed):
# # # #     if button == Button.x1 and pressed:
# # # #         # Coordenadas a las que se desea mover el cursor
# # # #         target_x = 500
# # # #         target_y = 300

# # # #         mouse.position = (target_x, target_y)
        
# # # #         current_x, current_y = mouse.position
# # # #         if current_x == target_x and current_y == target_y:
# # # #             mouse.click(Button.left, 1)

# # # # def on_press(key):
# # # #     if key == keyboard.KeyCode.from_char('q'):
# # # #         mouse_listener.stop()
# # # #         return False

# # # # mouse = Controller()
# # # # keyboard_listener = keyboard.Listener(on_press=on_press)
# # # # keyboard_listener.start()

# # # # with Listener(on_click=on_click) as mouse_listener:
# # # #     mouse_listener.join()

# from pynput.mouse import Button, Controller as MouseController
# from pynput.keyboard import Key, Listener as KeyboardListener
# from pynput import keyboard

# mouse = MouseController()

# def on_click(x, y, button, pressed):
#     if button == Button.x1:
#         mouse.position = (100, 200)
#         mouse.click(Button.left)

# def on_press(key):
#     if key == keyboard.KeyCode.from_char('q'):
#         return False

# with KeyboardListener(on_press=on_press) as listener:
#     with mouse.Listener(on_click=on_click) as listener:
#         listener.join()

# # # # from pynput.mouse import Button, Controller as MouseController
# # # # from pynput.keyboard import Key, Listener as KeyboardListener
# # # # from pynput import keyboard

# # # # mouse = MouseController()

# # # # def on_click(x, y, button, pressed):
# # # #     if button == Button.x1:
# # # #         mouse.position = (100, 200)
# # # #         mouse.click(Button.left)

# # # # def on_press(key):
# # # #     if key == keyboard.KeyCode.from_char('q'):
# # # #         return False

# # # # with KeyboardListener(on_press=on_press) as listener:
# # # #     with mouse.Listener(on_click=on_click) as mouselistener:
# # # #         mouselistener.join()

from pynput.mouse import Listener, Button, Controller
from pynput import keyboard

def on_click(x, y, button, pressed):

    if button == Button.x1 and pressed:
            mouse.position = (100, 200)
            mouse.click(Button.left)



def on_press(key):
    if key == keyboard.KeyCode.from_char('q'):
        mouse_listener.stop()
        return False
        

mouse = Controller()
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

with Listener(on_click=on_click) as mouse_listener:
    mouse_listener.join()




"""Button.x1 = boton 4
Button.x2 = boton 5"""

