import json

with open("twitterdev.json") as f:
    load1= json.loads(f.read())
print (load1)
    
print ()

def get_tweets():
    with open ("tweetj.json") as f2:
        load2= json.loads(f2.read())
    return (load2)
print (get_tweets())

print()

def add_tweets(text, username):
    tweets = get_tweets()
    tweets["tweets"].append ({"text": text, "username": username})
    return tweets
tweets= add_tweets(input("Input a text "), input("Input your username "))

def save_tweets(tweets):
    with open ("tweetj.json", "w") as f3:
        json.dump(tweets,f3, indent= 4)
save_tweets(tweets)
    