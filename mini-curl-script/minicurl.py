import http.client
import json

def post_request():
    conn = http.client.HTTPConnection("httpbin.org", 80)
    
    data = {"name": "James", "password": "yourdad", "os": "linux", "hascoochie": "false"}
    body = json.dumps(data)

    headers = {
        "Content-Type": "application/json",
        "Content-Length": str(len(body))
    }

    conn.request("POST", "/post", body, headers)

    response = conn.getresponse()
    print(response.status, response.reason)
    print(response.read().decode())


def get_request():
    conn = http.client.HTTPConnection("httpbin.org", 80)
    conn.request("GET", "/get")

    response = conn.getresponse()
    print(response.status, response.reason)
    print(response.read().decode())



if __name__ == "__main__":
    running = True
    print("Type q or quit to cancel.")
    while running:
        methods = input("Method? GET/POST (g, p): ").strip().lower()
    
        if(methods == "g"):
            get_request()
        elif(methods == "p"):
            post_request()
        elif(methods == "quit" or methods == "q"):
            print("Goodbye...")
            running = False
        else:
            print("Please enter a valid option\n")
            continue
    
