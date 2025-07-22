import base64

msg = input("Your message: ")
encodedmsg = ""
sum = input("Do you want to encode this message? (y/n)")

def encodeit():
    global encodedmsg
    encodedmsg = base64.b64encode(msg.encode())
    print("Encoded:", encodedmsg.decode())  # Optional: decode for readable output

def decodeit():
    decodedmsg = base64.b64decode(encodedmsg).decode()
    print("\n\nEncoded:", encodedmsg.decode())
    print("Decoded:", decodedmsg)

question1 = sum.lower()
if(question1 == "y"):
    encodeit()
elif(question1 =="n"):
    print("Goodbye.")
else:
    print("Invalid input. Please rerun the program.")

question = input("Do you want to decode it? (y/n): ").lower()

if question == "y":
    decodeit()
elif question == "n":
    print("Goodbye.")
else:
    print("Invalid input. Please rerun the program.")




