class Device:
    def __init__(self, name, connected_by, connected=True):
        self.name = name
        self.connected_by = connected_by
        self.connected = connected

    def __str__(self):
        return f"{self.name!r} {self.connected_by}"

    def disconnect(self):
        self.connected = False
        print(f"Disconnected {self.name}")


class Printer(Device):
    def __init__(self, name, connected_by, capacity, connected=True):
        super().__init__(name, connected_by, connected)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} {self.remaining_pages} pages remaining"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 100)
print(printer)
printer.print(1)
print(printer)
printer.disconnect()
printer.print(1)
