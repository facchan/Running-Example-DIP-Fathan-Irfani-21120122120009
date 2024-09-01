class Mouse:
    def __init__(self):
        self.name = "Menggunakan Wireless Mouse"

class Laptop:
    def __init__(self):
        self.mouse = Mouse()

    def get_mouse_name(self):
        return self.mouse.name

# main
laptop = Laptop()
print(laptop.get_mouse_name())
