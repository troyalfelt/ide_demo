from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)



@app.route('/')
def home():
    color = "black"
    return render_template('/index.html', color=color)

@app.route('/blue', methods = ['POST'])
def blue():
    if request.method == 'POST':
        color = "blue"
        return render_template('/index.html', color = color)

@app.route('/yellow', methods = ['POST'])
def yellow():
    if request.method == 'POST':
        color = "yellow"
        return render_template('/index.html', color = color)

@app.route('/red', methods = ['POST'])
def red():
    if request.method == 'POST':
        color = "red"
        return render_template('/index.html', color = color)


if __name__ == '__main__':
    app.run(debug = True)
