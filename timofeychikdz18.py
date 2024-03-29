from flask import Flask

app = Flask(__name__)

counter = 0

@app.route('/', methods=['GET'])
def get_counter():
    return str(counter)

@app.route('/plus', methods=['POST'])
def increment_counter():
    global counter
    counter += 1
    return 'Counter incremented.'

@app.route('/minus', methods=['POST'])
def decrement_counter():
    global counter
    counter -= 1
    return 'Counter decremented.'

if __name__ == '__main__':
    app.run()

#curl http://127.0.0.1:5000/
#curl -X POST http://127.0.0.1:5000/plus
#curl -X POST http://127.0.0.1:5000/minus

    
