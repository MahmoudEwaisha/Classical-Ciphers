import os
import numpy as np
import time
import itertools

class Ceaser:
    def Get_Message():
        print("Enter your message: ")
        x = input().upper().replace(" ","")
        return x

    def Get_Key():
        print("Enter the key (a number between 1-26): ")
        while True:
            key = input()
            try:
                val = int(key)
                if (val >= 1 and val <= 26):
                    return val
                else:
                    print("Error: Enter a valid number")
            except ValueError:
                print("Error: Enter a valid number")

    def Encrypt(message, key):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ciphertext = []
        for character in message:
            if character.isalpha():
                num = letters.find(character) + key
                num %= len(letters)
                ciphertext.append(letters[num])
            else:
                ciphertext.append(character)
        return ''.join(ciphertext)

class Playfair:
    def Get_Message(self):
        print("Enter your message: ")
        while True:
            x = input().upper().replace(" ","")
            if x.isalpha():
                return x
            else:
                print("Error: Your message must contain letters only")

    def Get_Key(self):
        print("Enter the key(characters): ")
        while True:
            x = input().upper().replace(" ","")
            if x.isalpha():
                return x
            else:
                print("Error: Key must contain letters only")

    def create_matrix(self, key):
        letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ" #without J
        string = []

        for char in key.upper():
            if char not in string:
                if char == "J":
                    char == "I"
                string.append(char)

        # remove spaces in key
        for i in range(len(string)):
            if " " in string:
                string.remove(" ")

        # append alphabets not in key
        for char in letters:
            if char not in string:
                string.append(char)

        # put string in a 5*5 matrix form
        matrix = [None for i in range(5)] 
        matrix[0] = string[0:5]
        matrix[1] = string[5:10]
        matrix[2] = string[10:15]
        matrix[3] = string[15:20]
        matrix[4] = string[20:25]
        return matrix

    def prepare_message(self, plaintext):
        message = []
        for i in plaintext.upper():
            message.append(i)

        # remove spaces
        for i in range(len(message)):
            if " " in message:
                message.remove(" ")

        # if both letters in the digraph are the same, add an "X" between them
        i = 0
        for x in range(int(len(message)/2)):
            if message[i] == message[i+1]:
                message.insert(i+1,'X')
            i = i+2

        # append an X if len(message) is an odd number
        if len(message)%2 == 1:
            message.append("X")

        # grouping
        i = 0
        new = []
        for x in range(int(len(message)/2)):
            new.append(message[i:i+2])
            i = i+2
        return new

    def find_position(self, matrix, char):
        x=y=i=j= 0
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == char.upper():
                    x = i
                    y = j
        return x,y

    def Encrypt(self, plaintext, key):
        matrix = self.create_matrix(key)
        plaintext = self.prepare_message(plaintext)
        ciphertext = []
        for i in plaintext:
            r1, c1 = self.find_position(matrix, i[0])
            r2, c2 = self.find_position(matrix, i[1])
            if r1 == r2:
                if c1 == 4:
                    c1 = -1
                if c2 == 4:
                    c2 = -1
                ciphertext.append(matrix[r1][c1+1])
                ciphertext.append(matrix[r1][c2+1])
            elif c1 == c2:
                if r1 == 4:
                    r1 = -1;
                if r2 == 4:
                    r2 =- 1;
                ciphertext.append(matrix[r1+1][c1])
                ciphertext.append(matrix[r2+1][c2])
            else:
                ciphertext.append(matrix[r1][c2])
                ciphertext.append(matrix[r2][c1])
        return ''.join(ciphertext)
    

    
class Hill:
    def Get_Key():
        print("Enter a key:\npress 1 for 2x2 key\npress 2 for 3x3 key")
        while True:
            try:
                x = int(input())
                if x == 1 or x == 2:
                    break
                else:
                    print("Please enter a valid choice")
            except:
                print("Please enter a valid choice")
            
        while True:
            key = []
            if x == 1:
                print("Enter 4 numbers separated by a space")
                y = input().split(' ')
                for i in range(len(y)):
                    if y[i] != '':
                        try:
                            key.append(int(y[i]))
                        except:
                            break       
                if len(key) != 4:
                    print("Please enter a valid 2x2 matrix")
                    continue
                key = np.array(key)
                key = key.reshape(2,2)
                       
            elif x == 2:
                print("Enter 9 numbers separated by a space")
                y = input().split(' ')
                for i in range(len(y)):
                    if y[i] != '':
                        try:
                            key.append(int(y[i]))
                        except:
                            break 
                if len(key) != 9:
                    print("Please enter a valid 3x3 matrix")
                    continue
                key = np.array(key)
                key = key.reshape(3,3)
            return key


    def Get_Message(key_cols):
        print("Enter your message: ")
        while True:
            x = input().upper().replace(" ","")
            if x.isalpha():
                break
            else:
                print("Error: Your message must contain letters only")        

        message = []
        for i in range(0, len(x)):
            message.append(ord(x[i]) - 65)
                
        # number of rows in the message must be equal to number of columns in the key
        if len(message) % key_cols != 0:
            for i in range(0, len(message)):
                message.append(25)
                if len(message) % key_cols == 0:
                    break
        message = np.array(message)
        if key_cols == 2:
            message = np.reshape(message,(-1, 2))
        elif key_cols == 3:
            message = np.reshape(message,(-1, 3))
        return message

    def Encrypt(message, key):
        encrypt = []
        cipher = []
        for i in range(len(message)):
            encrypt.append(np.remainder(np.dot(key, message[i]), 26).tolist())
        flat = list(itertools.chain(*encrypt))
        for i in range(len(flat)):
            cipher.append(chr(flat[i] + 65))
        ciphertext = ''.join(cipher)
        return ciphertext
    
class Vernam:
    def Get_Message():
        print("Enter your message: ")
        while True:
            x = input().upper().replace(" ","")
            if x.isalpha():
                return x
            else:
                print("Error: Your message must contain letters only")

    def Get_Key():
        print("Enter the key(characters): ")
        while True:
            x = input().upper().replace(" ","")
            if x.isalpha():
                return x
            else:
                print("Error: Key must contain letters only")
        

    def Encrypt(message, key):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while True:
            if len(message) != len(key):
                print("Error: Message and key must have the same size")
                key = Vernam.Get_Key()
                continue
            else:
                break
        msg = []
        k = []
        for i in range(len(message)):
            msg.append(letters.find(message[i].upper()))
            k.append(letters.find(key[i].upper()))
        out = ""
        for i in range(len(msg)):
            out += letters[(msg[i] + k[i]) % 26]
        return out
    
    
class Vigenere:
    def Get_Message():
        print("Enter your message: ")
        while True:
            x = input().upper().replace(" ","")
            if x.isalpha():
                return x
            else:
                print("Error: Your message must contain letters only")        

    def Get_Key():
        print("Enter the key(characters): ")
        while True:
            x = input().upper().replace(" ","")
            if x.isalpha():
                return x
            else:
                print("Error: Key must contain letters only")
                

    def Get_Mode():
        print("Enter desired mode\n1 for auto\n0 for repeating mode: \n")
        while True:
            x = int(input())
            if x == 0 or x == 1:
                return x
            else:
                print("Error: Enter a valid choice")

    def Encrypt(message, key, mode):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ciphertext = []
        key_index = 0

        if mode == 1:  # auto mode
            new_key = key
            for i in range(len(key), len(message)):
                new_key += message[i - len(key)]
            key = new_key

        for character in message:
            if character.isalpha():
                num = letters.find(character) + letters.find(key[key_index])
                num %= len(letters)
                ciphertext.append(letters[num])
                key_index += 1 # move to the next letter in the key
                if key_index == len(key):
                    key_index = 0
            else:
                ciphertext.append(character)
        return ''.join(ciphertext)




def screen():
    print("Please enter the classical ciphering technique you'd like to use\n\
1- Ceaser cipher\n\
2- Playfair cipher\n\
3- Hill cipher\n\
4- Vigenere cipher\n\
5- Vernam cipher\n\
6- Exit\n")
    
    
def main():
    while True:
        os.system('cls')
        screen()
        while True:
            try:
                choice = int(input())
                break
            except:
                print("Please enter valid number")
                time.sleep(1)
                os.system('cls')
                screen()
                continue
        
        if choice == 1:
            msg = Ceaser.Get_Message()
            key = Ceaser.Get_Key()
            cipher = Ceaser.Encrypt(msg, key)
            print("ciphertext : ", cipher)
            print("\nDo you wish to continue (y/n)")
            while True:
                ans = input()
                if ans == 'y':
                    break
                elif ans == 'n':
                    print("Bye Bye")
                    time.sleep(2)
                    return
                else:
                    print("Enter a valid choice")
            
        elif choice == 2:
            p = Playfair()
            msg = p.Get_Message()
            key = p.Get_Key()
            cipher = p.Encrypt(msg, key)
            print("ciphertext : ", cipher)
            print("\nDo you wish to continue (y/n)")
            while True:
                ans = input()
                if ans == 'y':
                    break
                elif ans == 'n':
                    print("Bye Bye")
                    time.sleep(2)
                    return
                else:
                    print("Enter a valid choice")
            
        elif choice == 3:
            key = Hill.Get_Key()
            print("Entered key:\n", key)
            msg = Hill.Get_Message(key.shape[1])
            cipher = Hill.Encrypt(msg, key)
            print("ciphertext : ", cipher)
            print("\nDo you wish to continue (y/n)")
            while True:
                ans = input()
                if ans == 'y':
                    break
                elif ans == 'n':
                    print("Bye Bye")
                    time.sleep(2)
                    return
                else:
                    print("Enter a valid choice")
            
        elif choice == 4:
            msg = Vigenere.Get_Message()
            key = Vigenere.Get_Key()
            mode = Vigenere.Get_Mode()
            cipher = Vigenere.Encrypt(msg, key, mode)
            print("ciphertext : ", cipher)
            print("\nDo you wish to continue (y/n)")
            while True:
                ans = input()
                if ans == 'y':
                    break
                elif ans == 'n':
                    print("Bye Bye")
                    time.sleep(2)
                    return
                else:
                    print("Enter a valid choice")
            
        elif choice == 5:
            msg = Vernam.Get_Message()
            key = Vernam.Get_Key()
            cipher = Vernam.Encrypt(msg, key)
            print("ciphertext : ", cipher)
            print("\nDo you wish to continue (y/n)")
            while True:
                ans = input()
                if ans == 'y':
                    break
                elif ans == 'n':
                    print("Bye Bye")
                    time.sleep(2)
                    return
                else:
                    print("Enter a valid choice")
            
        elif choice == 6:
            print("Bye Bye")
            time.sleep(2)
            return
        
        else:
            print("Please enter valid number")
            time.sleep(1)


if __name__ == "__main__":
    main()

