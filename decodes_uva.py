import sys

class Decoder:
    def __init__(self):
        self.new = ""

    def decode(self, data):
        self.new = ""
        for char in data:
            if 32 <= ord(char) <= 126:
                self.new += chr(ord(char) - 7)
            else:
                self.new += char

def main():
    for line in sys.stdin:
        decoder = Decoder()
        decoder.decode(line)
        print(decoder.new, end='')  

if __name__ == "__main__":
    main()
