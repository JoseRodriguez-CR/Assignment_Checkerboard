from flask import Flask
from flask import render_template

app = Flask(__name__)

#@app.route( '/' )
#def welcome():
#    return "Welcome!"

@app.route( '/', methods=['GET'] )  #/<int:num>
def board():
    counterList = []
    row = 8
    col = 8
    for i in range(0, row):
        counterList.append(row)
    return render_template( 'index.html', counter = counterList, row=row, col=col, color1 = "black", color2 = "red" )

@app.route( '/<int:num1>', methods=['GET'] )  #/<int:num>
def boardRow( num1):
    counterList = []
    row = num1
    col = 8
    for i in range(0, row):
        counterList.append(row)
    return render_template( 'index.html', counter = counterList, row=row, col=col, color1 = "black", color2 = "red" )

@app.route( '/<int:num1>/<int:num2>', methods=['GET'] )  #/<int:num>
def boardRowCol( num1, num2 ):
    counterList = []
    row = num1
    col = num2
    for i in range(0, row):
        counterList.append(row)
    return render_template( 'index.html', counter = counterList, row=row, col=col, color1 = "black", color2 = "red" )


@app.route( '/<int:num1>/<int:num2>/<color1>', methods=['GET'] )  #/<int:num>
def boardRowColColor1( num1, num2, color1 ):
    counterList = []
    row = num1
    col = num2
    for i in range(0, row):
        counterList.append(row)
    return render_template( 'index.html', counter = counterList, row=row, col=col, color1=color1, color2="red")

@app.route( '/<int:num1>/<int:num2>/<color1>/<color2>', methods=['GET'] )  #/<int:num>
def boardRowColColor1Color2( num1, num2, color1, color2 ):
    counterList = []
    row = num1
    col = num2
    for i in range(0, row):
        counterList.append(row)
    return render_template( 'index.html', counter = counterList, row=row, col=col, color1=color1, color2=color2)


if __name__ == "__main__":
    app.run( debug = True)
