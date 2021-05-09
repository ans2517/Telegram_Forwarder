from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "1846818308:AAFwPLq5-N7oOUaCeG8neq8E2yXoxbD5bfU"  # Your bot API key
    OWNER_ID = 1253966183  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    FROM_CHATS = [-1001378573071]  # List of chat id's to forward messages from.
    TO_CHATS = [-1001361042967,-1001357055226,-1001179396735,-1001257364379]  # List of chat id's to forward messages to.
    
    WORKERS = 10