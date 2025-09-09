import http.client
import json

def post_request(url = "httpbin.org"):
    conn = http.client.HTTPConnection(url, 80)
    
    data = {"name": "User", "password": "12345"}
    body = json.dumps(data)

    headers = {
        "Content-Type": "application/json",
        "Content-Length": str(len(body))
    }

    conn.request("POST", "/post", body, headers)

    response = conn.getresponse()
    print(response.status, response.reason)
    print(response.read().decode())


def get_request(url = "httpbin.org"):
    conn = http.client.HTTPConnection(url, 80, timeout=16)
    headers = {"Connection": "close"}
    conn.request("GET", "/get", headers=headers)
    
    response = conn.getresponse()
    print(response.status, response.reason)
    print(response.read().decode())



if __name__ == "__main__":
    running = True
    print("Type q or quit to cancel.")
    while running:
        methods = input("Method? GET/POST (g, p): ").strip().lower()
        if(methods == "quit" or methods == "q"):
            print("Goodbye..")
            running = False
            exit()
        get_url_input = input("What URL do you want to use?\ninfo: only use the domain name ('example.com')\n(Press 'Enter' for default): ").strip().lower()
        url = get_url_input or "httpbin.org"

        if(methods == "g"):
            print("GET on:", url)
            get_request(url)
        elif(methods == "p"):
            print("POST on:",url)
            post_request(url)
        else:
            print("Please enter a valid option\n")
            continue
    
