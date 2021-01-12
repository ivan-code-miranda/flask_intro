from flask import Flask, request
from operations import add,sub, mult, div

app = Flask(__name__)

@app.route("/add")
def do_add():
  """ Add a and b """

  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = add(a, b)

  return str(result)

@app.route("/sub")
def subtratir():
  """ a minus b """

  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = sub(a, b)

  return str(result)

@app.route("/mult")
def multiplicar():
  """ Multiply a and b """

  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = mult(a, b)

  return str(result)

@app.route("/div")
def dividir():
  """ Add a and b """

  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = div(a, b)

  return str(result)

operators = {
  "add": add,
  "sub": sub,
  "mult": mult,
  "div": div
  }

@app.route("/math/<oper>")
def matematica(oper):
  """ Do Math on a and b"""

  a = int(request.args.get("a"))
  b = int(request.args.get("b"))
  result = operators[oper](a,b)

  return str(result)
