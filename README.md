# Fake Legends Bot #

This bot uses a trained neural net (made with textgenrnn) to generate new
items, check them against its input, and toot out the new item if it passes
the test. 

# Dependencies #

textgenrnn for the neural net

pawopy for tooting (publishing to mastodon) 

tweepy if you prefer to tweet - code is there but commented out

# Setup #

1. Get your things (in this case, I used a list of legendary creatures and
their descriptions) 

2. Train a neural net to make more of them

3. Create a list of the items' names (the legendary creatures' names, minus
their descriptions) - the bot will check this list to make sure it's not
reinventing something real

4. Adjust the code as needed (input of a different format may require
slightly different parsing/checking) 

5. Create an account and app for your bot. Copy the access token into the secrets
file. 

6. Run the make_creature script from the command line and/or set up a cron
job.