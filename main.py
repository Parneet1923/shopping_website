from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    with open('States.csv', mode='r') as data:
        states = data.readlines()
        for i in range(len(states)):
            states[i] = states[i].replace('\n', '')
    return render_template('signup.html', states=states)


if __name__ == '__main__':
    app.run(debug=True)

