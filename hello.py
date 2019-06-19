from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

## RBP 2018-09-13
## Adding the following line outputs the value
## of '__name__' on the command line.
print()
print("Value of '__name__' = ", __name__)
print ()

@app.route("/")
def hello():
    return render_template('hello.html', 
    message1 = "Hello World!",
    message2 = "Hello World!")

@app.route("/noknok")
def nok():
    return "<h1>Knock! Knock! Who's there?</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
