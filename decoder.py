import sys

class Decoder:
    def __init__(self):
        self.data = None
    
    def decode(self, data):
        self.data = data
        for char in data:
            print(f"Decoding character: {char}")
            print(ord(char))

        return self.data   

    def __str__(self):
        return f"Decoder(data={self.data})"

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
            print("Decoded data:", decoder.data)
        except EOFError:
            print("\nExiting...")
            sys.exit(0)

if __name__ == "__main__":
    main()