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