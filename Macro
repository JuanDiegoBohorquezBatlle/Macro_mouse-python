from pynput import keyboard
import pyautogui

#Defino la master key, si esta no  se presiona el resto no se activan.

j_pressed_master = False

#Defino las variables inicialmente en False para evitar activaciones innecesarias.

o_pressed = False
p_pressed = False
s_pressed = False

print('\n===============================================================')
print('=======Macros; Desarrollo Juan Diego Bohorquez Batlle==========')
print('===============================================================\n')


print("\n\n*Recuerda*: Para activar las fuciones del programa debes \n            presionar la tecla j antes que nada") 

print("\n* Para parar el programa pulsa la tecla q")
print("\n* Para saber la posición del mouse pulsa la tecla s")
print("\n* Para dar click en la posición deseada pulsa la tecla p")
print("\n* Para moverte a una zona deseada de la pantalla pulsa la tecla o\n\n")

input('presiona ENTER cuando quieras empezar')

def on_press(tecla):
    
    '''Se define on_press como las teclas ha presionar 
    para la aparición de eventos especificados'''

    global p_pressed, o_pressed, j_pressed_master, s_pressed
    
    if tecla == keyboard.KeyCode.from_char('j'):
        j_pressed_master = True

    if tecla == keyboard.KeyCode.from_char('s'):
        s_pressed = True

    if tecla == keyboard.KeyCode.from_char('p'):
        p_pressed = True

    if tecla == keyboard.KeyCode.from_char('o'):
        o_pressed = True

    if s_pressed and j_pressed_master:
        print("Coordenadas actuales del ratón:", pyautogui.position())
        
    if tecla == keyboard.KeyCode.from_char('q') and j_pressed_master:
        return False
    


def on_release(key):

    '''Se define on_relase para una vez presionadas las teclas 
    sean False para evitar bucles'''

    global j_pressed_master, s_pressed
    
    if key == keyboard.KeyCode.from_char('j'):
        j_pressed_master = False

    if key == keyboard.KeyCode.from_char('s'):
        s_pressed = False

escuchador = keyboard.Listener(on_press=on_press, on_release=on_release)

escuchador.start()



while escuchador.is_alive():
    
    if p_pressed and j_pressed_master:
        p_pressed = False
        pyautogui.click(x=880, y=146, clicks=1)

    if o_pressed and j_pressed_master:
        o_pressed = False
        pyautogui.moveTo(600, 400)



