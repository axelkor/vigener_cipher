
class VigenereCipher():
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def lenght(self,text):
        l = len(self.key)
        while True:
            if len(self.key) < len(text):
                for i in range(0, l, 1):
                    self.key = self.key + self.key[i]
                    if len(self.key) == text:
                        break
            else:
                break
    def encode(self, text):
        word = ""
        self.lenght(text)
        for i in range(0,len(text),1):
            if text[i] in self.alphabet:
                a = self.alphabet.index(text[i])
                b = self.alphabet.index(self.key[i])
                if a + b >= len(self.alphabet):
                    word = word + self.alphabet[a + b - len(self.alphabet)]
                else:
                    word = word + self.alphabet[a + b]
            else:
                if text[i].lower() in self.alphabet:
                    a = self.alphabet.index(text[i].lower())
                    b = self.alphabet.index(self.key[i])
                    if a + b >= len(self.alphabet):
                        word = word + self.alphabet[a + b - len(self.alphabet)].upper()
                    else:
                        word = word + self.alphabet[a + b].upper()
                else:
                    word = word + text[i]
        return word

    def decode(self, text):
        word = ""
        self.lenght(text)
        for i in range(len(text)):
            if text[i] in self.alphabet:
                c = self.alphabet.index(text[i])
                d = self.alphabet.index(self.key[i])
                if c - d < 0:
                    word = word + self.alphabet[c - d + len(self.alphabet)]
                else:
                    word = word + self.alphabet[c    - d]
            else:
                if text[i].lower() in self.alphabet:
                    c = self.alphabet.index(text[i].lower())
                    d = self.alphabet.index(self.key[i])
                    if c - d < 0:
                        word = word + self.alphabet[c - d + len(self.alphabet)].upper()
                    else:
                        word = word + self.alphabet[c-d].upper()
                else:
                    word = word + text[i]

        return word