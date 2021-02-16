"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 0):
        self.next = start
        self.start = start

    def __repr__(self):
         return f"<SerialGenerator start={self.start} next={self.next}>"
    
    def generate(self):
        self.next += 1 
        return self.next 

    def reset(self):
        return self.start

serial = SerialGenerator(start=100)
print(serial.generate())
print(serial.generate())
print(serial.reset())
    

    

