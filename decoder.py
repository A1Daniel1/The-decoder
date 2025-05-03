import sys

class Decoder:
    def __init__(self):
        self.data = None
        self.new = ""
    
    def decode(self, data):
        self.data = data
        for char in data:
            if ord(char) < 32 or ord(char) > 126:
                print(f"Invalid character: {char} (ASCII: {ord(char)})")
                continue
            else:
                self.new += (chr(ord(char) - 7))
    
        return self.data  

    def __str__(self):
        return f"Decoder(data={self.new})"

def main():
    # printable ascci characters
    # 32-126
    while True:
        try:
            decoder = Decoder()
            data = input("Enter a string to decode: ")

            if not data:
                print("No data provided.")
                sys.exit(1)
            
            decoder.decode(data)
            print("Decoded data:", decoder.new)
        except EOFError:
            print("\nExiting...")
            sys.exit(0)

if __name__ == "__main__":
    main()