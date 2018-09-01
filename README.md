# Fake Legends Bot #

This bot uses a trained neural net (made with textgenrnn) to generate new
items, check them against its input, and toot out the new item if it passes
the test. 

# Dependencies #

textgenrnn for the neural net

pawopy for tooting (publishing to mastodon) 

tweepy if you prefer to tweet - code is there but commented out

# Setup - training the neural net #

1. You'll need a list of input items. Included here is a list of legendary
creatures and their descriptions (from Wikipedia)

2. Use *train.py* to create a neural network trained on this input. Training
a neural net can take a while - this is a small one, only took me about an
hour. You can run it for a longer or shorter time if you like, and stop when
it gives you appropriately wacky output. 

This creates a file called *textgenrnn_weights.hdf5*. This is the brains of
your neural net. 

3.  Use *peek.py 0.5* to see what kind of output the neural net is able to
produce.  This step is optional, just for your own curiousity.

Any questions? Check the docs for textgenrnn! :) 

# Setup part 2 - creating the bot #

1. Create a mastodon account for your bot (recommended: http://botsin.space )

2. In the settings of that account: 
	
	a. Go to Development 

	b. Create an app 

	c. Click on the app you just created 

	d. Highlight and copy the access token.

3. Add the access token to the toot_secrets.py file included here.

4. Run the *make_creature.py* script from the command line to make sure it does the right thing. (This provides some command line feedback and also makes it toot its first toot!)

5. Set up a cron job to run make_creature.py on your desired interval.
Optionally you can supply a temperature argument: 0.1 gives boring output,
1.0 gives output so creative it may not make sense.

Any issues with the tooting, check the docs for pawopy. 

(If you prefer to publish to twitter instead of mastodon, uncomment the code
for tweepy and make sure to set up the access tokens for your twitter
account) 
