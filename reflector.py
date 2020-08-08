import enigma

class Reflector:
    """
    Defines the reflector in use by the engigma machine.  The name you pass into the constructor
    is looked up in the relector dictionary in the enigma module.  You can also create a custom
    reflector by passing in your own wiring.
    """

    def __init__(self, name, wiring=None):
        self.name = name
        
        if (wiring is None):
            self.wiring = enigma.reflectors[name]
        else:
            self.wiring = wiring
        
    def mapLetter(self, inputLetter):
        inputPos = enigma.plaintext.index(inputLetter)
        return self.wiring[inputPos]