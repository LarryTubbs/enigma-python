"""main entry point for the engima module."""

plaintext = '.ABCDEFGHIJKLMNOPQRSTUVWXYZ'

rotors = {}
rotors["I"] = ".EKMFLGDQVZNTOWYHXUSPAIBRCJ"    # Rotor I
rotors["II"] = ".AJDKSIRUXBLHWTMCQGZNPYFVOE"   # Rotor II
rotors["III"] = ".BDFHJLCPRTXVZNYEIWGAKMUSQO"  # Rotor III
rotors["IV"] = ".ESOVPZJAYQUIRHXLNFTGKDCMWB"   # Rotor IV
rotors["V"] = ".VZBRGITYUPSDNHLXAWMJQOFECK"    # Rotor V
rotors["VI"] = ".JPGVOUMFYQBENHZRDKASXLICTW"   # Rotor VI
rotors["VII"] = ".NZJHGRCXMYSWBOUFAIVLPEKQDT"  # Rotor VII
rotors["VIII"] = ".FKQHTLXOCBJSPDZRAMEWNIUYGV" # Rotor VIII
rotors["b"] = ".LEYJVCNIXWPBQMDRTAKZGFUHOS"    # M4 Greek Rotor "b" (beta)
rotors["g"] = ".FSOKANUERHMBTIYCWLQPZXVGJD"    # M4 Greek Rotor "g" (gama)

knockpoints = {}
knockpoints["I"] = (17, 17)    # Q - one knockpoint (R I)
knockpoints["II"] = (5, 5)     # E - one knockpoint (R II)
knockpoints["III"] = (22, 22)  # V - one knockpoint (R III)
knockpoints["IV"] = (10, 10)   # J - one knockpoint (R IV)
knockpoints["V"] = (26, 26)    # Z - one knockpoint (R V)
knockpoints["VI"] = (26, 13)   # Z/M - two knockpoints (R VI)
knockpoints["VII"] = (26, 13)  # Z/M - two knockpoints (R VII)
knockpoints["VIII"] = (26, 13) # Z/M - two knockpoints (R VIII)

reflectors = {}
reflectors["B"] = ".YRUHQSLDPXNGOKMIEBFZCWVJAT"      # M3 B
reflectors["C"] = ".FVPJIAOYEDRZXWGCTKUQSBNMHL"      # M3 C
reflectors["b_thin"] = ".ENKQAUYWJICOPBLMDXZVFTHRGS" # M4 thin B
reflectors["c_thin"] = ".RDOBJNTKVEHMLFCWZAXGYIPSUQ" # M4 thin C

