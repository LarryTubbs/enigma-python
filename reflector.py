import enigma

class Reflector:
    """Defines the rotor in use by the engigma machine"""

    def __init__(self, name, wiring=None):
        self.name = name
        
        if (wiring is None):
            self.wiring = enigma.reflectors[name]
        else:
            self.wiring = wiring
        
    def mapLetter(self, inputLetter):
        inputPos = enigma.plaintext.index(inputLetter)
        return self.wiring[inputPos]