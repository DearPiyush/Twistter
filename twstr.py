from random import randint
from time import sleep
from TwitterFollowBot import TwitterBot
my_bot = TwitterBot()


####Automatically follow any users that have followed you
#my_bot.auto_follow_followers()

####Automatically follow any users that tweet something with a specific phrase
#my_bot.auto_follow("Rashtriya")
#my_bot.auto_follow(“#hashtag”)
#my_bot.auto_follow("hinduism dharma", count=50)

####Automatically follow any users that follow a user
#my_bot.auto_follow_followers_of_user("RSSorg", count=50)


####Automatically favorite any tweets that have a specific phrase
#my_bot.auto_fav("hinduism wellbeing", count=122)

####Post a tweet on twitter
varname = open("/root/Desktop/tweets.txt","r")
for line in varname.readlines():
	if len(line)>30:
		if len(line)<140:
			if line.find('˚') == -1:
				print (str(line))
				sleep(randint(60,90))
				my_bot.send_tweet(str(line))

####Automatically retweet any tweets that have a specific phrase
#my_bot.auto_rt("hindu spiritual", count=1000)


####Automatically unfollow any users that have not followed you back
####If there are certain users that you would like to not unfollow, add their user id to the USERS_KEEP_FOLLOWING list.
####You will need to manually edit the code if you want to add special users that you will keep following even if they don’t follow you back.
#my_bot.auto_unfollow_nonfollowers()

####Automatically unfollow all users.
#my_bot.auto_unfollow_all_followers()

####Automatically mute all users that you have followed
####You will need to manually edit the code if you want to add special users that you will not mute.
#my_bot.auto_mute_following()

####Automatically unmute everyone you have muted
####You will need to manually edit the code if you want to add special users that will remain muted.
#my_bot.auto_unmute()
