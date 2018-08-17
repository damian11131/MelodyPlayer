from pynput.keyboard import Key, Listener, KeyCode
from serial import Serial
from serial import SerialException
from time import sleep

SERIAL_NAME = "COM3"
BAUD_RATE = 115200

key_already_pressed = False
arduino_serial = None


def on_release(key):
    global key_already_pressed
    key_already_pressed = False
    data = b'a'
    arduino_serial.write(data)


def on_press(key):
    global key_already_pressed

    if not key_already_pressed:
        key_already_pressed = True
    else:
        return

    frequency = ''
    if key == Key.esc:
        # Stop listener
        return False
    elif key == Key.f1:
        frequency = b"0\n"
    elif key == Key.f2:
        frequency = b"31\n"
    elif key == Key.f3:
        frequency = b"33\n"
    elif key == Key.f4:
        frequency = b"35\n"
    elif key == Key.f5:
        frequency = b"37\n"
    elif key == Key.f6:
        frequency = b"39\n"
    elif key == Key.f7:
        frequency = b"41\n"
    elif key == Key.f8:
        frequency = b"44\n"
    elif key == Key.f9:
        frequency = b"46\n"
    elif key == Key.f10:
        frequency = b"49\n"
    elif key == Key.f11:
        frequency = b"52\n"
    elif key == Key.f12:
        frequency = b"55\n"
    elif key == Key.print_screen:
        frequency = b"8\n"
    elif key == Key.scroll_lock:
        frequency = b'62\n'
    elif key == Key.pause:
        frequency = b'65\n'
    elif key == KeyCode(char='`'):
        frequency = b'69\n'
    elif key == KeyCode(char='1'):
        frequency = b'73\n'
    elif key == KeyCode(char='2'):
        frequency = b'78\n'
    elif key == KeyCode(char='3'):
        frequency = b'82\n'
    elif key == KeyCode(char='4'):
        frequency = b'87\n'
    elif key == KeyCode(char='5'):
        frequency = b'93\n'
    elif key == KeyCode(char='6'):
        frequency = b'98\n'
    elif key == KeyCode(char='7'):
        frequency = b'104\n'
    elif key == KeyCode(char='8'):
        frequency = b'110\n'
    elif key == KeyCode(char='9'):
        frequency = b'117\n'
    elif key == KeyCode(char='0'):
        frequency = b'123\n'
    elif key == KeyCode(char='-'):
        frequency = b'131\n'
    elif key == key == KeyCode(char='='):
        frequency = b'139\n'
    elif key == Key.backspace:
        frequency = b'147\n'
    elif key == Key.insert:
        frequency = b'156\n'
    elif key == Key.home:
        frequency = b'165\n'
    elif key == Key.page_up:
        frequency = b'175\n'
    elif key == Key.tab:
        frequency = b'185\n'
    elif key == KeyCode(char='q'):
        frequency = b'196\n'
    elif key == KeyCode(char='w'):
        frequency = b'208\n'
    elif key == KeyCode(char='e'):
        frequency = b'220\n'
    elif key == KeyCode(char='r'):
        frequency = b'233\n'
    elif key == KeyCode(char='t'):
        frequency = b'247\n'
    elif key == KeyCode(char='y'):
        frequency = b'262\n'
    elif key == KeyCode(char='u'):
        frequency = b'277\n'
    elif key == KeyCode(char='i'):
        frequency = b'294\n'
    elif key == KeyCode(char='o'):
        frequency = b'311\n'
    elif key == KeyCode(char='p'):
        frequency = b'330\n'
    elif key == KeyCode(char='['):
        frequency = b'349\n'
    elif key == KeyCode(char=']'):
        frequency = b'370\n'
    elif key == Key.enter:
        frequency = b'392\n'
    elif key == Key.delete:
        frequency = b'415\n'
    elif key == Key.end:
        frequency = b'440\n'
    elif key == Key.page_down:
        frequency = b'466\n'
    elif key == KeyCode(char='+'):
        frequency = b'494\n'
    elif key == Key.caps_lock:
        frequency = b'523\n'
    elif key == KeyCode(char='a'):
        frequency = b'554\n'
    elif key == KeyCode(char='s'):
        frequency = b'587\n'
    elif key == KeyCode(char='d'):
        frequency = b'622\n'
    elif key == KeyCode(char='f'):
        frequency = b'659\n'
    elif key == KeyCode(char='g'):
        frequency = b'698\n'
    elif key == KeyCode(char='h'):
        frequency = b'740\n'
    elif key == KeyCode(char='j'):
        frequency = b'784\n'
    elif key == KeyCode(char='k'):
        frequency = b'831\n'
    elif key == KeyCode(char='l'):
        frequency = b'880\n'
    elif key == KeyCode(char=';'):
        frequency = b'932\n'
    elif key == KeyCode(char="'"):
        frequency = b'988\n'
    elif key == KeyCode(char='\\'):
        frequency = b'1047\n'
    elif key == Key.shift_l:
        frequency = b'1109\n'
    elif key == KeyCode(char='z'):
        frequency = b'1175\n'
    elif key == KeyCode(char='x'):
        frequency = b'1245\n'
    elif key == KeyCode(char='c'):
        frequency = b'1319\n'
    elif key == KeyCode(char='v'):
        frequency = b'1397\n'
    elif key == KeyCode(char='b'):
        frequency = b'1480\n'
    elif key == KeyCode(char='n'):
        frequency = b'1568\n'
    elif key == KeyCode(char='m'):
        frequency = b'1661\n'
    elif key == KeyCode(char=','):
        frequency = b'1760\n'
    elif key == KeyCode(char='.'):
        frequency = b'1865\n'
    elif key == KeyCode(char='/'):
        frequency = b'1976\n'
    elif key == Key.shift_r:
        frequency = b'2093\n'
    elif key == Key.ctrl_l:
        frequency = b'2217\n'
    elif key == Key.cmd_l:
        frequency = b'2349\n'
    elif key == Key.alt_l:
        frequency = b'2489\n'
    elif key == Key.space:
        frequency = b'2637\n'
    elif key == Key.alt_r:
        frequency = b'2794\n'
    elif key == Key.cmd_r:
        frequency = b'2960\n'
    elif key == Key.menu:
        frequency = b'3136\n'
    elif key == Key.ctrl_r:
        frequency = b'3322\n'
    elif key == Key.up:
        frequency = b'3520\n'
    elif key == Key.left:
        frequency = b'3729\n'
    elif key == Key.down:
        frequency = b'3951\n'
    elif key == Key.right:
        frequency = b'4186\n'
    # elif key.char == *: frequency = b'4435\n'
    # elif key.char == *: frequency = b'4699\n'
    # elif key.char == *: frequency = b'4978\n'
    try:
        arduino_serial.write(frequency)
    except SerialException:
        return False

def wait_for_arduino():
    global arduino_serial

    while True:
        try:
            arduino_serial = Serial(SERIAL_NAME, BAUD_RATE)
            break
        except SerialException:
            info = "Oczekiwanie na Arduino..."
            print(info)
            sleep(1)


def main():
    wait_for_arduino()

    print("Ready")

    with Listener(
            on_release=on_release, on_press=on_press) as listener:
        listener.join()
    print("Do widzenia :)")


if __name__ == "__main__":
    main()
