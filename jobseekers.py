import random
import tweepy
import credentials

# Authenticate to Twitter
auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_KEY, credentials.ACCESS_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

#okay! Now we're on Twitter! Let's post something foolish.

phrase_company = ['Exciting, fast paced company', 'Brand new startup', 'Client', 'Ancient vengeful spirit', 
    'Local supervillain', 'Soulless megacorporation', 'Local mob front', 'Teenage Bitcoin multimillionaire', 
    'Shady pyramid scheme', 'Creepy quasi-religious organization', 'YouTube celebrity', 'Your middle school bully', 
    'Dumbass with a trust fund', 'Florida Man', 'Non-profit organization']
phrase_seeks = ['is seeking', 'requires', 'is now hiring', 'is most desirous of', 'looking for', 'looking to hire', 'hunting for']
phrase_victim = ['a recent graduate', 'a useful idiot', 'a friendly individual', 'fresh meat', 'someone desperate', 
    'a basement-dwelling mutant', 'a Young Republican', 'a caring individual', 'a willing volunteer', 'a former assassin', 
    'a harmless weirdo', 'Florida Man', 'a worthy nemesis', 'a timid woodland creature', 'an unpaid intern', 
    'a detail-oriented wombat', 'a sucker']
phrase_with = ['with a can-do attitude', 'with eleventy years experience', 'with no concept of boundaries', 'with a nice butt', 
    'with a degree in business', 'with a black belt in karate', 'with constant existential angst', 'with no social life', 
    'with nothing to lose', 'with a sunny disposition', 'with an open mind', 'with talent and ambition', 'with Christmas spirit', 
    'who knows Excel']
phrase_for = ['as the office snitch.', 'to dig ditches on Mars.', 'to sell cowbells to ninjas.', 'as target practice.', 
    'to manage their various offshore accounts.', 'to follow them around looking cool.', 'to mislead the IRS.', 'as code monkey.', 
    'to manage infinite monkeys on infinite typewriters.', 'for dark and mysterious occult rituals.', 'as bait.', 
    'to make our brand go viral.', 'to be the company hitman.', 'to make our dreams be memes.', 
    'to pull a miracle out of their butt.', 'to guard the office fridge.', 'to accost strangers into downloading our app.']
phrase_end = ['Training provided.', 'Must have own vehicle.', 'Commission only.', 'Exciting opportunity!', 
    'Masters degree preferred.', 'Learn highly marketable skills!', 'Start your new career today!', 'Suckups preferred.', 
    'Time travel opportunities available.', 'Bring donuts.', 'Must love children and animals.', 'Must be willing to relocate.', 
    'Bring a shovel.', 'Must be computer literate.', 'Must have no fear of God or death.']

def build_phrase():
    """Build the phrase we will be tweeting."""
    phrase = random.choice(phrase_company) + " " + random.choice(phrase_seeks) + " " + random.choice(phrase_victim) + " " +
        random.choice(phrase_with) + " " + random.choice(phrase_for) + " " + random.choice(phrase_end)
    return phrase

def count_chara(phrase):
    """Count the number of characters."""
    total = 0
    for i in phrase:
        total = total + 1
    return total

#Make sure the tweet is within the word count.
myphrase = build_phrase()
while count_chara(myphrase) > 280:
    myphrase = build_phrase()

#Post that shit.
try: 
    api.update_status(myphrase)
    print ("Tweet sent!")
except:
    print ("Tweet failed.")

