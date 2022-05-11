from flask import Flask, request, jsonify
from keras.models import load_model
from determine_label import get_labels, max_probability

app = Flask(__name__)

model = load_model('./models/abnormality_model')

@app.route("/", methods=["POST"])
def evaluate():
  if request.method == "POST":
    tensor = request.json['tensor']
    modelType = request.json['modelType']
    
    labels = None
    if modelType == 'abnormality':
      labels = get_labels('./labels/abnormality_labels.txt')
    else:
      labels = get_labels('./labels/condition_labels.txt')

    predictions = model.predict(tensor)
    index = max_probability(predictions)
    return jsonify(prediction=labels[index])

if __name__ == '__main__':
  app.debug = True
  app.run()