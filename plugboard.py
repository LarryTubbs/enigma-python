import enigma

class Plugboard():
    def __init__(self, pairs):
        self.wiring = "."

        if pairs is not None:
            for pair in pairs:
                # each character in the pair must be exactly one character
                if len(pair[0]) != 1 or len(pair[1]) != 1:
                    raise ValueError("You can only map pairs of letters into the plugboard")

                # each character must be valid
                if pair[0].upper() not in enigma.plaintext[1:] or pair[1].upper() not in enigma.plaintext[1:]:
                    raise ValueError("Only alpha characters can be mapped into the plugboard")

                # characters can't already be in the wiring
                if pair[0].upper() in self.wiring or pair[1].upper() in self.wiring:
                    raise ValueError("Letters can't be mapped into the plugboard more than once")
                
                # characters can't match each other
                if pair[0].upper() == pair[1].upper():
                    raise ValueError("Letters can't be mapped to themselves in the plugboard")

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

        

