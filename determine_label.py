def get_labels(filepath):
  file = open(filepath, 'r')
  labels = []
  for line in file:
    labels.append(line.strip())
  return labels
