import base64

sum = input("Decode / Encode? (d/e) (q to quit): ").lower()


def encodeit():
    msg = input("Your message: ")
    encodedmsg = base64.b64encode(msg.encode())
    print("Encoded:", encodedmsg.decode())  # Optional: decode for readable output

def decodeit():
    msg = input("Your base64 string to decode: ")
    if(msg.lower() == "q"):
        print("Goodbye.")
        return
    else:
        try:
            decodedmsg = base64.b64decode(msg).decode()
            print("\n\nEncoded:", msg)
            print("Decoded:", decodedmsg)
            print("Goodbye.")
        except Exception as e:
            print(f"An error occurred while decoding: {e}")

question1 = sum.lower()
if(question1 == "d"):
    decodeit()
elif(question1 == "e"):
    encodeit()
elif(question1 == "q"):
    print("Goodbye.")
else:
    print("Invalid input. Please rerun the program.")


