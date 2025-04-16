import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "11073994"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ecf4c3a7f7bafab1c5b0e47fae0db217")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6073523936"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb://vijayetc15:TjrWQPWJTIZDUtit@ac-9rcwyp7-shard-00-00.k5tqk7n.mongodb.net:27017,ac-9rcwyp7-shard-00-01.k5tqk7n.mongodb.net:27017,ac-9rcwyp7-shard-00-02.k5tqk7n.mongodb.net:27017/?replicaSet=atlas-5y953h-shard-0&ssl=true&authSource=admin&retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
