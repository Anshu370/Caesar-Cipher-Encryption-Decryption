# Caesar Cipher Encryption and Decryption

class Caesar_Cipher:

    def __init__(self, shiftValue):
        self.shiftValue = shiftValue
        self.alphabets = 'abcdefghijklmnopqrstuvwxyz'
        self.caesercipher_alphabets = self.alphabets[self.shiftValue:]+self.alphabets[:self.shiftValue]

    def encryption(self, text):
        ''' This will Encrypt your text into caesar cipher string '''

        givenText = text.lower()

        caesarcipher = ''
        for i in givenText:
            if i not in self.alphabets:
                caesarcipher += i
            else:
                index_alphabet = self.alphabets.index(i)
                caesarcipher += self.caesercipher_alphabets[index_alphabet]
        return caesarcipher

    def decryption(self, text):
        ''' This will Decrypt your caesar cipher string into normal text '''

        caesercipherText = text
        normal_Text = ''

        for i in caesercipherText:
            if i not in self.caesercipher_alphabets:
                normal_Text += i
            else:
                index_alphabet = self.caesercipher_alphabets.index(i)
                normal_Text += self.alphabets[index_alphabet]
        return normal_Text



if __name__ == '__main__':
    a = Caesar_Cipher(10)
    print(a.caesercipher_alphabets)
    print(a.encryption("Anshu"))
    print(a.decryption("kxcre"))