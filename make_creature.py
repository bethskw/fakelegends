# get temperature from arg
import sys 
args = [float(x) for x in sys.argv[1:]]

# load the neural network
from textgenrnn import textgenrnn
textgen = textgenrnn('textgenrnn_weights.hdf5')

# load the list of "real" creatures
fh = open('real_creature_names.txt', 'r')
realcreatures = {}
for line in fh.readlines():
    creaturename = line.rstrip()
    realcreatures[creaturename] = 1


# temperature
tempy = 0.5
if len(args) > 0:
    tempy = args[0] # TODO defaulting doesn't work 

hmm = 0
while hmm == 0:

    # get a legendary creature
    creaturelist= textgen.generate(1, temperature=tempy, return_as_list = True)
    mycreature = creaturelist[0]

    # TODO
    # split on first '-' or '('
    creaturestuff = mycreature.split('(')
    firstname = creaturestuff[0].rstrip()
    pieces = firstname.split('-')
    if len(pieces) > 1:
        firstname = pieces[0].rstrip()

    print("Checking " + firstname + "...")

    if firstname in realcreatures:
#	# DEBUG print
        print("NOPE, " + mycreature + " is real") # DEBUG
        next
    else:
        hmm = 1

# DEBUG print
print("Success! Your creature is: " + mycreature)


### TWEET
#import tweepy
#from tweet_secrets import *
#auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
#auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
#api = tweepy.API(auth)
#api.update_status(mycreature)

### TOOT
import pawopy
from toot_secrets import *
auth = pawopy.OAuthHandler('https://botsin.space')
auth.set_access_token(A_TOKEN)
api = pawopy.API(auth)
api.update_status(mycreature)


