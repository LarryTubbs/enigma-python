import enigma
from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard

class Machine():
    """
    This is the Machine class.  It is the main entry point for setting up an Enigma 
    machine and evaluating text with it.  For example:

    >>> m3 = Machine("M3", "B", "III", "II", "I", [("A", "B"), ("C", "D")])
    >>> m3.evaluate("m")
    'C'
    >>> m3.evaluate("i")
    'O'
    >>> m3.evaluate("k")
    'M'
    >>> m3.evaluate("e")
    'W'
    >>> m3.evaluate("l")
    'U'
    >>> m3.evaluate("a")
    'Y'
    >>> m3.evaluate("r")
    'N'
    >>> m3.evaluate("r")
    'T'
    >>> m3.evaluate("y")
    'G'

    >>> m4 = Machine("M4", "b_thin", "III", "II", "I", [("A", "B"), ("C", "D")], "g")
    >>> m4.evaluate("M")
    'D'
    >>> m4.evaluate("I")
    'S'
    >>> m4.evaluate("K")
    'S'
    >>> m4.evaluate("E")
    'H'
    >>> m4.evaluate("L")
    'W'
    >>> m4.evaluate("A")
    'S'
    >>> m4.evaluate("R")
    'A'
    >>> m4.evaluate("R")
    'O'
    >>> m4.evaluate("Y")
    'D'
    """
    def __init__(self, type, reflector, r, m, l, pb=None, z=None, rSetting=1, mSetting=1, lSetting=1, zSetting=1, rPosition=1, mPosition=1, lPosition=1, zPosition=1):
        """
        To create an enigma machine, you must supply its minimum components.  Required parameters are:
        
            type - either 'M3' or 'M4'. For M4 machines, a z rotor is also required
            reflector - the reflector type for the machine you want to create, matching a key in the enigma.reflectors dictionary.
                        To be historically accurate, you should use the "*_thin" variants with the M4 machine.  They had to create 
                        thinner reflectors to make space for the 4th rotor.  The code will allow any reflector with any machine.
            r - the type of rotor you want in the right position in the stack, matching a key value in the enigma.rotors dictionary
            m - the same for the middle rotor
            l - and the left rotor
            
        If you are creating an "M4 machine, you must also provide:

            z - the type of z-rotor you want in the rotor stack.  There are only two rotors that are valid z rotors, "b" and "g", the
                beta rotors.  The library will accept any rotor matching a key value in the engima.rotors dictionary however and the 
                machine function as expected.  Rotors in the z or beta position do not rotate however, as per the design of the M4 
                Enigma machine.

        Optional parameters allow you to further configue the inital setup of the machine.  They are:

            pb - A list of tuples listing the pairs of letters jumped by the plugboard.  Each letter can only be jumped once, and you
                 can't jump a leter to itself.

        Ring settings:

            rSetting, lSetting, mSetting, zSetting - these default to 1 (A), but can be setup to any value from 1-26 (A-Z)

        Inital rotor positions:

            rPosition, lPosition, mPosition, zPosition - these also default to 1 (A), but can also be setup to any value from 1-26 (a-Z)
        
        """
        self.type = type
        # Implement validation for machine to ensure inputs meet requirements
        # if M4, must include a z rotor
        if type == "M4" and z is None:
            raise ValueError("M4 Enigma machines requires a z rotor.")

        self.reflector = Reflector(reflector)
        self.r = Rotor(r, rSetting, rPosition)
        self.m = Rotor(m, mSetting, mPosition)
        self.l = Rotor(l, lSetting, lPosition)

        # Implement plugboard class and wire it up here
        self.pb = Plugboard(pb)

        if z is not None:
            self.z = Rotor(z, zSetting, zPosition)
        else:
            self.z = None

    def __str__(self):
        rtn = f"{self.type}: "
        if self.z is not None:
            rtn += f"{self.z.name}({enigma.plaintext[self.z.position]}) -> "
        rtn += f"{self.l.name}({enigma.plaintext[self.l.position]}) -> "
        rtn += f"{self.m.name}({enigma.plaintext[self.m.position]}) -> "
        rtn += f"{self.r.name}({enigma.plaintext[self.r.position]})"
        return rtn

    def __repr__(self):
        rtn = f"machine.Machine(type='{self.type}',"
        rtn += f"reflector='{self.reflector.name}', "
        rtn += f"r='{self.r.name}', "
        rtn += f"m='{self.m.name}', "
        rtn += f"l='{self.l.name}', "
        if self.z is not None:
            rtn += f"z='{self.z.name}', "
        else:
            rtn += f"z=None, "
        rtn += f"rSetting={self.r.ringSetting}, "
        rtn += f"mSetting={self.m.ringSetting}, "
        rtn += f"lSetting={self.l.ringSetting}, "
        if self.z is not None:
            rtn += f"zSetting={self.z.ringSetting}, "
        else:
            rtn += f"zSetting=None, "
        rtn += f"rPosition={self.r.position}, "
        rtn += f"mPosition={self.m.position}, "
        rtn += f"lPosition={self.l.position}, "
        if self.z is not None:
            rtn += f"zPosition={self.z.position})"
        else:
            rtn += f"zPosition=None)"
        return rtn        

    def evaluate(self, inputLetter):
        """
        emulates handling a keypress on the enigma machine
        """
        # rotate the rotors
        self.rotateRotors()

        l = inputLetter.upper()

        # map through the plugboard
        l = self.pb.mapLetter(l)

        # map the path through the rotor stack
        l = self.r.mapLetter(l)
        l = self.m.mapLetter(l)
        l = self.l.mapLetter(l)

        # if there is a r rotor, map through it
        if self.z is not None:
            l = self.z.mapLetter(l)
        
        # map through the relector
        l = self.reflector.mapLetter(l)

        # reverse the process on the other side
        
        # if there is a r rotor, map through it
        if self.z is not None:
            l = self.z.mapLetter(l, True)

        # map back through the rotor stack in reverse
        l = self.l.mapLetter(l, True)
        l = self.m.mapLetter(l, True)
        l = self.r.mapLetter(l, True)
        
        # Map back through the plubboard on the way out
        l = self.pb.mapLetter(l)

        # return the resulting letter
        return l

    def evaluateMessage(self, msg, blockCount=0):
        """
        evaluateMessage emulates an enigma machine operator encoding an entire message.  For example,

        >>> m3 = Machine("M3", "B", "III", "II", "I", [("A", "B"), ("C", "D")])
        >>> m3.evaluateMessage("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", 4)
        'PIXW HLIF PVWH EDGC YIUY YXFB SFXW POBL ERUR HDZJ CTNK GZBF BIHF GOSG IYWR MEEZ HQAZ WRKY ZJBV WFDA TOHG EURN NYPX CADE DTHB DB'
        >>> m3 = Machine("M3", "B", "III", "II", "I", [("A", "B"), ("C", "D")])
        >>> m3.evaluateMessage('PIXW HLIF PVWH EDGC YIUY YXFB SFXW POBL ERUR HDZJ CTNK GZBF BIHF GOSG IYWR MEEZ HQAZ WRKY ZJBV WFDA TOHG EURN NYPX CADE DTHB DB')
        'LOREMIPSUMDOLORSITAMETCONSECTETURADIPISCINGELITSEDDOEIUSMODTEMPORINCIDIDUNTUTLABOREETDOLOREMAGNAALIQUA'
        """
        
        cypherText = ""
        charCount = 0
        for c in msg:
            if c.upper() in enigma.plaintext[1:]:
                if blockCount > 0 and charCount > 0 and charCount % blockCount == 0:
                    cypherText += " "
                try:
                    cypherText += self.evaluate(c)
                except:
                    pass
                charCount += 1
        return cypherText


    def rotateRotors(self):
        """
        emulates the rotation of the rotors when a key is pressed on the enigma machine.  This should only be called internally
        by the class when the evaluate() method is invoked.
        """
        # if middle rotor is on a notch, rotate all three notched rotors
        if (self.m.onNotch() is True):
            self.l.rotateUp()
            self.m.rotateUp()
            self.r.rotateUp()
        # if right rotor on notch, rotate right and middle rotors
        elif (self.r.onNotch() is True):
            self.m.rotateUp()
            self.r.rotateUp()
        # else rotate only the right rotor
        else:
            self.r.rotateUp()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
