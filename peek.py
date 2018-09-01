import sys
import sys 
args = [float(x) for x in sys.argv[1:]]

from textgenrnn import textgenrnn
textgen = textgenrnn('textgenrnn_weights.hdf5')
#textgen.generate(20, temperature=0.5)
textgen.generate(5, temperature=args[0])