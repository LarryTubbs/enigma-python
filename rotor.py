import enigma

class Rotor:
    """Defines the rotor in use by the engigma machine"""

    def __init__(self, name, ringSetting, position, wiring=None, notches=None):
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
        if (self.position in self.notches):
            return True
        else:
            return False

    def rotateUp(self):
        self.position += 1
        self.position = self.safetyPos(self.position)
        return

    def rotateDown(self):
        self.position -= 1
        self.position = self.safetyPos(self.position)
        return

    def safetyPos(self, position):
        if (position > 26):
            return position - 26
        elif (position < 1):
            return 26 + position
        else:
            return position

    def mapLetter(self, inputLetter, reverse=False):
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