from flask import Flask, render_template, request, jsonify
import base64

app = Flask(__name__)

themessage = ''

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/echo', methods=['POST'])
def echo():
    global themessage
    if not themessage:
        return jsonify({"error": "No message received"}), 400
    data = request.get_json()
    themessage = data.get('msg', '')
    return jsonify({"msg": themessage})

@app.route('/api/greet')
def greet():
    global themessage
    encrypt = base64.b64encode(themessage.encode()).decode()
    return jsonify({"message": f"Decrypted: {encrypt}"})

if __name__ == '__main__':
    app.run(debug=True)