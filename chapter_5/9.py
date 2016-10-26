class CaesarCipher:
    def __init__(self,  roation=3):
        self._rot = roation
        
    def encrypt(self, string):
        return self._trans(self._rot, string)

    def decrypt(self, string):
        return self._trans(-self._rot, string)

    def _trans(self, roation, string):
        return "".join([ chr((ord(s)+roation)%256) for s in string ])
        
       
if __name__ == "__main__":
    plain_text = "a;slkdrtuhkldsfn;askjt";
    engin = CaesarCipher(7)
    print plain_text
    print engin.encrypt(plain_text)
    print engin.decrypt(engin.encrypt(plain_text))
