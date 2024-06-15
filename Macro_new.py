from pynput import keyboard
import pyautogui
import importlib
import time
import os
import sys

#Defino la master key, si esta no  se presiona el resto no se activan.

j_pressed_master = False

#Defino las variables inicialmente en False para evitar activaciones innecesarias.

o_pressed = False
p_pressed = False
s_pressed = False

# Variables de guardado de posiciones.

shift_pressed = False
ctrl_pressed = False

sv1 = (50,50)
sv2 = (50,50)

RUTA = "C:/Users/Public/Macro/conf.py"
CONT = f"sv1 = {str(sv1)}\nsv2 = {str(sv2)}"

# Presentacion.

print('\n===============================================================')
print('=======Macros; Desarrollo Juan Diego Bohorquez Batlle==========')
print('===============================================================\n')


print("\n\n*Recuerda*: Para activar las fuciones del programa debes \n            presionar la tecla j primero") 

print("\n* Para parar el programa pulsa la tecla q")
print("\n* Para saber la posición del mouse pulsa la tecla s")
print("\n* Para guardar la posición del mouse para luego dar click \n   en la posición deseada pulsa la tecla shift")
print("\n* Para guardar la posición del mouse para luego moverte a \n   una posición deseada pulsa la tecla ctrl")
print("\n* Para dar click en la posición deseada pulsa la tecla p")
print("\n* Para moverte a una posición deseada pulsa la tecla o\n\n")

input('presiona ENTER cuando quieras empezar')

#Declaracion de funciones.

if not os.path.exists("C:/Users/Public/Macro/"):
    os.makedirs("C:/Users/Public/Macro/")


def get_mouse_position():
    pos = pyautogui.position()
    return (pos.x, pos.y)

def write():

    global sv1, sv2
    CONT = f"sv1 = {str(sv1)}\nsv2 = {str(sv2)}"

    with open(RUTA, "w", encoding="utf-8") as archivo:
        archivo.write(CONT)

def on_press(key):
    
    '''Se define on_press como las teclas ha presionar 
    para la aparición de eventos especificados'''

    global p_pressed, o_pressed, j_pressed_master, s_pressed, sv1, sv2, ctrl_pressed, shift_pressed
    
    try:

        if key == keyboard.KeyCode.from_char('j'):
            j_pressed_master = True
        
        if key == keyboard.Key.shift:
            shift_pressed = True

        if key == keyboard.Key.ctrl_l:
            ctrl_pressed = True

        if key == keyboard.KeyCode.from_char('s'):
            s_pressed = True

        if key == keyboard.KeyCode.from_char('p'):
            p_pressed = True

        if key == keyboard.KeyCode.from_char('o'):
            o_pressed = True

        if s_pressed and j_pressed_master:
            print("Coordenadas actuales del ratón:", pyautogui.position())
            
        if key == keyboard.KeyCode.from_char('q') and j_pressed_master:
            return False
        
        if shift_pressed and j_pressed_master:
                sv1 = get_mouse_position()

                write()

        if ctrl_pressed and j_pressed_master:
                sv2 = get_mouse_position()

                write()

    except AttributeError:
        pass

def on_release(key):

    '''Se define on_relase para una vez presionadas las teclas 
    sean False para evitar bucles'''

    global j_pressed_master, s_pressed, ctrl_pressed, shift_pressed
    
    if key == keyboard.KeyCode.from_char('j'):
        j_pressed_master = False

    if key == keyboard.Key.shift:
        shift_pressed = False

    if key == keyboard.Key.ctrl_l:
        ctrl_pressed = False

    if key == keyboard.KeyCode.from_char('s'):
        s_pressed = False

escuchador = keyboard.Listener(on_press=on_press, on_release=on_release)

escuchador.start()


if os.path.exists(RUTA):
    sys.path.insert(0, "C:/Users/Public/Macro/")
    import conf


#Bucle Principal.

while escuchador.is_alive():

    if os.path.exists(RUTA):
        importlib.reload(conf)
        sv1 = conf.sv1
        sv2 = conf.sv2

    if p_pressed and j_pressed_master:
        p_pressed = False
        pyautogui.click(sv1[0], sv1[1], clicks=1)

    if o_pressed and j_pressed_master:
        o_pressed = False
        pyautogui.moveTo(sv2[0], sv2[1])

    time.sleep(0.1)

