import enigma

class Rotor:
    """
    Defines the rotor in use by the engigma machine.
    """

    def __init__(self, name, ringSetting, position, wiring=None, notches=None):
        """
        When creating a rotor, you must provide the following arguments:

        name - the name of the rotor you want to create.
        ringsetting - the initial position of the letter ring on the rotor itself.
        position - the initial position of the rotor.

        When including only the required fields, the wiring and notches are looked up in their respective 
        dictionaries in the enigma file.

        Optionally you can provide custom wiring and notches if you want to create a custom rotor.
        """
        self.name = name
        self.ringSetting = ringSetting
        self.position = position
        if (wiring is None):
            self.wiring = enigma.rotors[name]
        else:
            self.wiring = wiring
        if (notches is None):
            self.notches = enigma.knockpoints[name]
        else:
            self.notches = notches

    def onNotch(self):
        """
        returns true if the rotor's current position is on a notch, otherwise returns false
        """
        if (self.position in self.notches):
            return True
        else:
            return False

    def rotateUp(self):
        """
        Rotates the position of the rotor up one letter. 
        """
        self.position += 1
        self.position = self.safetyPos(self.position)
        return

    def rotateDown(self):
        """
        Rotates the position of the rotor down one letter.
        """
        self.position -= 1
        self.position = self.safetyPos(self.position)
        return

    def safetyPos(self, position):
        """
        Translates positions back to within 1-26 when rotor loops around.
        """
        if (position > 26):
            return position - 26
        elif (position < 1):
            return 26 + position
        else:
            return position

    def mapLetter(self, inputLetter, reverse=False):
        """
        Maps inputLetter through the wiring of the rotor.  By default, the letter passes through the rotor from right
        to left.  To map from left to right (from the reflector back through the stack), set the optional reverse parameter
        to True.
        """
        mappedChar = ""
        outputPos = None

        inputPos = enigma.plaintext.index(inputLetter)

        # adjust for position
        adjPos = inputPos + (self.position - 1)
        adjPos = self.safetyPos(adjPos)

        # adjust for Ring Setting
        adjPos = adjPos - (self.ringSetting - 1)
        adjPos = self.safetyPos(adjPos)

        if (reverse is False):
            mappedChar = self.wiring[adjPos]
            outputPos = enigma.plaintext.index(mappedChar)
        else:
            mappedChar = enigma.plaintext[adjPos]
            outputPos = self.wiring.index(mappedChar)

        # readjust for Ring Setting
        outputPos = outputPos + (self.ringSetting - 1)
        outputPos = self.safetyPos(outputPos)

        # readjust for position
        outputPos = outputPos - (self.position - 1)
        outputPos = self.safetyPos(outputPos)

        return enigma.plaintext[outputPos]