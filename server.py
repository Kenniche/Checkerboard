from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', rows = 8, columns = 8)

@app.route('/<num>')
def callDown(num):
    return render_template('index.html', rows = 8, columns = int(num))

@app.route('/<num1>/<num2>')
def acrossDown(num1,num2):
    return render_template('index.html', rows = int(num1), columns = int(num2) )

@app.route('/<num1>/<num2>/<col1>/<col2>')
def hellaColors(num1, num2, col1, col2):
    return render_template('index.html', rows = int(num1), columns = int(num2), color1= col1, color2 = col2)

if __name__ == "__main__":
    app.run(debug=True)