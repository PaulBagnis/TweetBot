import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = "n4QQQaLtC70dsi54adwRuFMCW"
    consumer_secret = "GrsLdf2drgLFkT8FpFzPeLrBrFTFlHY4LN6h7EiVamY7GefiHE"
    access_token = "1377622154683019265-wB6k2RuIfNGcth52wDEO6bGPnzyXYw"
    access_token_secret = "8RTqizUFIrmg7LAAawJXDwZF7w1qHoPdypvpIRYd6ji5B"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api