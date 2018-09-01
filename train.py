
from textgenrnn import textgenrnn

#t=textgenrnn()
t = textgenrnn('textgenrnn_weights.hdf5')
t.train_from_file('legendary_creatures.txt', num_epochs=10)



