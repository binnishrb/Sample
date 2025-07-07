from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print("Flask app is running!")
    return "Hello from Flask in VS Code!"

def home():
    print("Flask app is running!")
    return "Hello from Flask in VS Code!"

if __name__ == '__main__':
    app.run(debug=True)
