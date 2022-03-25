from flask import Flask
from keras.models import load_model

app = Flask(__name__)

model = load_model('./models/abnormality_model')

@app.route("/", methods=["GET"])
def evaluate():
  pass

if __name__ == '__main__':
  app.debug = True
  app.run()