from pynput import mouse, keyboard

class Listener():
    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()

class Mouse(Listener):
    def __init__(self):
        self.listener = mouse.Listener(
                on_move=self.on_move,
                on_click=self.on_click,
                on_scroll=self.on_scroll)

    def on_move(self, x, y):
        print(f'Moved to: ({x}, {y})')


    def on_click(self, x, y, button, pressed):
        pressed = 'Pressed' if pressed else 'Released'
        print(f'{pressed} {button} at ({x}, {y})')


    def on_scroll(self, x, y, dx, dy):
        print(f'Scrolled {(dx, dy)} at {(x, y)}')


class Keyboard(Listener):
    def __init__(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)

    def on_press(self, key):
        print(f'{key} pressed')

    def on_release(self, key):
        print(f'{key} released')

