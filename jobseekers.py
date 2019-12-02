import random
import tweepy
import credentials
from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

#okay! Now we're on Twitter! Let's post something foolish.

phrase_company = ['Exciting, fast paced company', 'Brand new startup', 'Client', 'Ancient vengeful spirit', 
    'Local supervillain', 'Soulless megacorporation', 'Local mob front', 'Teenage Bitcoin multimillionaire', 
    'Shady pyramid scheme', 'Creepy quasi-religious organization', 'YouTube celebrity', 'Your middle school bully', 
    'Dumbass with a trust fund', 'Florida Man', 'Non-profit organization', 'Marketing executive', 'Busy office', 
    'Yoga studio', 'Outbound call center', 'Gourmet eatery', 'Haunted theater', 'Highly secretive government agency', 
    'Local aliens', 'Folksy war criminal', 'Aging hipster', 'White guy', 'Three small children in a trench coat', 
    'Cartoonishly evil billionaire', 'Captain Planet bad guy', 'Distinguished gentleman']
phrase_seeks = ['is seeking', 'requires', 'is now hiring', 'is most desirous of', 'looking for', 'looking to hire', 'hunting for', 
    'legally required to hire', 'is interested in hiring']
phrase_victim = ['a recent graduate', 'a useful idiot', 'a friendly individual', 'fresh meat', 'someone desperate', 
    'a basement-dwelling mutant', 'a Young Republican', 'a caring individual', 'a willing volunteer', 'a former assassin', 
    'a harmless weirdo', 'Florida Man', 'a worthy nemesis', 'a timid woodland creature', 'an unpaid intern', 
    'a detail-oriented wombat', 'a sucker', 'ten pounds of whoop-ass in a five-pound sack', 'an amiable doofus', 'a gay', 
    'a mark', 'a hardcore survivalist', 'a wizard', 'a bad enough dude', 'a yes-man', 'a manic pixie dream employee', 
    'a walking disaster', 'a masochist', 'a rigid conformist']
phrase_with = ['with a can-do attitude', 'with eleventy years experience', 'with no concept of boundaries', 'with a nice butt', 
    'with a degree in business', 'with a black belt in karate', 'with constant existential angst', 'with no social life', 
    'with nothing to lose', 'with a sunny disposition', 'with an open mind', 'with talent and ambition', 'with Christmas spirit', 
    'who knows Excel', 'with decent hygiene', 'with a high tolerance for bullshit', 'with style', 'with INT as their dump stat', 
    'with crippling student loan debt', 'with ADHD', 'with a team of plucky sled dogs', 'with a dream', 
    'with a strong immune system', 'with some sick beats', 'with attitude', 'with a perfect attendance record']
phrase_for = ['as the office snitch.', 'to dig ditches on Mars.', 'to sell cowbells to ninjas.', 'as target practice.', 
    'to manage their various offshore accounts.', 'to follow them around looking cool.', 'to mislead the IRS.', 'as code monkey.', 
    'to manage infinite monkeys on infinite typewriters.', 'for dark and mysterious occult rituals.', 'as bait.', 
    'to make their brand go viral.', 'to be the company hitman.', 'to make our dreams be memes.', 
    'to pull a miracle out of their butt.', 'to guard the office fridge.', 'to accost strangers into downloading our app.', 
    'to ghostwrite their fanfic.', 'to be all they can be.', 'to reach for the stars.', 'to fan them with palm fronds.', 
    'to kick ass and chew bubblegum.', 'as governess to a small creepy child.', 'as their new mascot.', 
    'to break the union strike and also possibly some legs.', 'for amateur taxidermy.', 
    'to make their nepotism hire look good by comparison.', 'as kabuki ninja.', 'to participate in sinister clinical trials.']
phrase_end = ['Training provided.', 'Must have own vehicle.', 'Commission only.', 'Exciting opportunity!', 
    'Masters degree preferred.', 'Learn highly marketable skills!', 'Start your new career today!', 'Suckups preferred.', 
    'Time travel opportunities available.', 'Bring donuts.', 'Must love children and animals.', 'Must be willing to relocate.', 
    'Bring a shovel.', 'Must be computer literate.', 'Must have no fear of God or death.', 'Come alone.', 'Show no fear.', 
    'Start immediately.', 'Bring a passport and a suitcase full of unmarked bills.', 'Ignore the red flags.', 
    'Must provide own bunny suit.', 'Competitive wages.', 'First aid certification helpful.', 'Subject to background check.', 
    'Up-to-date rabies vaccination required.']

def build_phrase():
    """Build the phrase we will be tweeting."""
    phrase = random.choice(phrase_company) + " " + random.choice(phrase_seeks) + " " + random.choice(phrase_victim) + " " + random.choice(phrase_with) + " " + random.choice(phrase_for) + " " + random.choice(phrase_end)
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

