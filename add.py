app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hola Mundo!"

if __name__ == '__add.py__':
    app.run(host='0.0.0.0', port=8000)
    