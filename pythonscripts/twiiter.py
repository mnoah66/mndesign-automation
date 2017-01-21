import tweepy, datetime
from datetime import datetime
from pytz import timezone

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "xvvbz3tcgoOfSzLPKDD3T4i8F",
    "consumer_secret"     : "bUmFKSsg0upDcHAYwrCWy99yJ4yiw8vlJSxfbxxKn73IhO9qSd",
    "access_token"        : "1067132768-OYYNwqYPNo2yAZ31WonlY6aQCF10Gu6ogxYmtM3",
    "access_token_secret" : "ogYDi58JELwDZoNfujQLN3IUlv7zC5TskVMKmTZDYyGwG"
    }
  now_utc = datetime.now(timezone('UTC'))
  now_eastern = now_utc.astimezone(timezone('US/Eastern'))
  api = get_api(cfg)
  tweet = "@MixMasterMartin The date and time is " + now_eastern.strftime("%A, %D, %I:%M%p")
  status = api.update_status(status=tweet)
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()