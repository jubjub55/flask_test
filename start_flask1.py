from flask import Flask

app = Flask(__name__)

@app.route('/')
def hellowolrd():
    return 'Hello Flask !!!'

@app.route('/robot')
def robot():
    return '<H1>Hello ROBOT !!!</H1>'

@app.route('/profile/<name>')
def profile(name):
    return 'Name is %s'% name


#if __name__ == '__main__':
    # app.run();
app.run();