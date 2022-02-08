import os
import sys

rotors = ["DMTWSILRUYQNKFEJCAZBPGXOHV","HQZGPJTMOBLNCIFDYAWVEUSRKX","UQNTLSZFMREHDPXKIBVYGJCWOA"]
reflector = "QYHOGNECVPUZTFDJAXWMKISRBL"
alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Data:
    def __init__(self):
        self.rotor1 = int(input("Enter the first rotor: "))
        self.rotor2 = int(input("Enter the second rotor: "))
        self.rotor3 = int(input("Enter the third rotor: "))
        self.offset1 = int(input("Enter the offset of the first rotor: "))
        self.offset2 = int(input("Enter the offset of the second rotor: "))
        self.offset3 = int(input("Enter the offset of the third rotor: "))
        self.encrypt = str(input("Enter the message to encrypt: "))
        self.crypted = ""

def comeback(rotor, transit, pos):
    j = 0
    for k in rotor:
        if transit[pos] == k:
            pos = j
            break
        j += 1
    return pos

def enigma():
    data = Data()
    temp1 = rotors[data.rotor1 - 1][data.offset1 :] + rotors[data.rotor1 - 1][0: data.offset1]
    temp2 = rotors[data.rotor2 - 1][data.offset2 :] + rotors[data.rotor2 - 1][0: data.offset2]
    temp3 = rotors[data.rotor3 - 1][data.offset3 :] + rotors[data.rotor3 - 1][0: data.offset3]
    rotors[0] = temp1
    rotors[1] = temp2
    rotors[2] = temp3

    data.encrypt = data.encrypt.replace(' ', '')
    data.encrypt = data.encrypt.upper()

    for k in data.encrypt:
        pos = ord(k) - 65
        pos = ord(rotors[data.rotor1 - 1][pos]) - 65
        pos = ord(rotors[data.rotor2 - 1][pos]) - 65
        pos = ord(rotors[data.rotor3 - 1][pos]) - 65
        pos = comeback(rotors[data.rotor3 - 1], reflector, pos)
        pos = comeback(rotors[data.rotor2 - 1], alphabet, pos)
        pos = comeback(rotors[data.rotor1 - 1], alphabet, pos)
        data.crypted += alphabet[pos]

if __name__=="__main__":
    enigma()