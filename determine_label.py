def get_labels(filepath):
  file = open(filepath, 'r')
  labels = []
  for line in file:
    labels.append(line.strip())
  return labels

def max_probability(predictions):
  index = 0
  max_prob = predictions[0]
  for i in range(1, len(predictions)):
    if predictions[i] > max_prob:
      max_prob = predictions[i]
      index = i
  return index