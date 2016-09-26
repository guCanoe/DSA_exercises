class Human:
    def __init__(self, message=''):
        self._msg = message

    def send(self, message=''):
        self._msg = message

    def get_msg(self):
        return self._msg

    def check(self, Computer):
        if Computer.get_msg():
            self.read(Computer)
            
    def read(self, Computer);
        Computer.clean()


class Broadcast:
    def __init__(self, message=None, Human=None):
        self._msg = message
        

    def check(self, Human):
        if Human.get_msg():
            self.msg = Human.get_msg()
            
            
    def trans(self, Computer)
        Computer.set_message(self._msg)
        
class Computer:
    def __init__(self, message=''):
        self._msg = message

    def set_message(self, message):
        self._msg = message
        
    def get_msg(self):
        return self._msg

    def clean(self):    
        self._msg = ''
        


if __name__ == "__main__":
    Alice = Human()
    Bob = Human()
    Internet = Broadcast()
    com = Computer()
    for t in range(10):
        Alice.send("dsdfdf")
        if Internet.check(Alice)
        Internet.trans(Com)
        Bob.check


