import tweepy
import time as

print ('This is a Twitter Bot')

consumer_key = 'q9DGMddPdDTUCgvzNFnUH8ZmP'
consumer_secret = 'xvg87ZDrQvMLbKvCvdPV9MMt1MY0krqEpoVUmBJoKb7NzwB8Pb'
access_key = '1218455156334956544-WM1HCqIvtT8AphbajB56D7Imy8vVdJ'
access_secret = 'xnakBhPKUscAYoKBrTrvDmssUHtQTvaiP7A8e3u0U1SRn'

stream = tweepy.Stream(
  "q9DGMddPdDTUCgvzNFnUH8ZmP", "xvg87ZDrQvMLbKvCvdPV9MMt1MY0krqEpoVUmBJoKb7NzwB8Pb",
  "1218455156334956544-WM1HCqIvtT8AphbajB56D7Imy8vVdJ", "xnakBhPKUscAYoKBrTrvDmssUHtQTvaiP7A8e3u0U1SRn"
)

stream.filter(track=["Tweepy"])


class IDPrinter(tweepy.Stream):

    def on_status(self, status):
        print(status.id)


printer = IDPrinter(
  "Consumer Key here", "Consumer Secret here",
  "Access Token here", "Access Token Secret here"
)
printer.sample()

thread = stream.filter(follow=[1072250532645998596], threaded=True)

class ConnectionTester(tweepy.Stream):

    def on_connection_error(self):
        self.disconnect()

auth = tweepy.oauthhandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.api(auth, wait_on_rate_limit= True)