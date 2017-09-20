from flask import Flask

app = Flask(__name__)

@app.route("/")
def root():
  return "This is the root."

@app.route("/question")
def question():
  return "Do you have a question?"
  
@app.route("/enigma")
def enigma():
  return "This is an enigma."
  
if __name__='__main__':
  app.run()
