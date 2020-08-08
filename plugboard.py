import enigma

class Plugboard():
    def __init__(self, pairs):
        self.wiring = "."

        for pair in pairs:
            # TODO Add validation logic!

            # append pair to the wiring
            self.wiring += pair[0].upper()
            self.wiring += pair[1].upper()

    def mapLetter(self, inputLetter):
        # if the letter isn't found in the wiring, return input letter
        try:
            letterPos = self.wiring.index(inputLetter)
        except:
            return inputLetter

        if (letterPos % 2 == 0):
            return self.wiring[letterPos - 1]
        else:
            return self.wiring[letterPos + 1]

        

