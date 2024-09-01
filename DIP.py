# Abstraksi untuk Peripheral
class Peripheral:
    def get_name(self):
        pass

# Implementasi Mouse
class Mouse(Peripheral):
    def get_name(self):
        return "Menggunakan Wireless Mouse"

# Implementasi Keyboard
class Keyboard(Peripheral):
    def get_name(self):
        return "Menggunakan Mechanical Keyboard"

class Laptop:
    def __init__(self, peripheral: Peripheral):
        self.peripheral = peripheral

    def get_peripheral_name(self):
        return self.peripheral.get_name()

# main
mouse = Mouse()
keyboard = Keyboard()

laptop_with_mouse = Laptop(mouse)
print(laptop_with_mouse.get_peripheral_name())  

laptop_with_keyboard = Laptop(keyboard)
print(laptop_with_keyboard.get_peripheral_name())  
