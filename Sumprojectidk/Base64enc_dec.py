import base64

msg = input("Your message: ")
encodedmsg = ""

def encodeit():
    global encodedmsg
    encodedmsg = base64.b64encode(msg.encode())
    print("Encoded:", encodedmsg.decode())  # Optional: decode for readable output

def decodeit():
    decodedmsg = base64.b64decode(encodedmsg).decode()
    print("Encoded:", encodedmsg.decode())
    print("Decoded:", decodedmsg)

encodeit()

question = input("Do you want to decode it? (y/n): ").lower()

if question == "y":
    decodeit()
elif question == "n":
    print("Goodbye.")
else:
    print("Invalid input. Please rerun the program.")




