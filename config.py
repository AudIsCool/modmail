"""
    Imports
        os  - for env file, and file checks
        sys - for checking runtime args
"""
import os
import sys


"""
    Setup ENV info for importing the token 
"""
#Check if env exists
if os.path.exists("./authinfo.env") != True:
    raise ValueError("No authinfo.env file found containing token")

#Assuming we have it import env
from dotenv import load_dotenv
load_dotenv(
    dotenv_path="./authinfo.env"
)


"""
    Check run time arguments for whether we're testing or not
"""
Dev = False
if len(sys.argv) > 2:
    if sys.argv[2] == "--dev":
        Dev = True


# Bot's token
token = os.getenv("TOKEN")

# Top.gg token
topgg_token = None

# Discord Bots token
dbots_token = ""

# Discord Bot List token
dbl_token = ""

# Bots on Discord token
bod_token = ""

# Bots for Discord token
bfd_token = ""

# Discord Boats token
dboats_token = ""

# Sentry URL
sentry_url = ""

# Whether the bot is for testing, if true, stats and errors will not be posted
testing = Dev

# PUBSUB channel for Redis
ipc_channel = ""

# Postgres database credentials
database = {
    "database": "",
    "user": "",
    "password": "",
    "host": "",
    "port": 5432,
}

# Number of clusters
clusters = 1

# Additional shards to launch
additional_shards = 0

# The default prefix for commands
default_prefix = "="

# The server to send tickets to, no confirmation messages if set
default_server = 795005332945764423

# Status of the bot
activity = f"DM to Contact Staff | {default_prefix}help"

# Whether or not to fetch all members
fetch_all_members = True

# The main bot owner
owner = 237585712998907914

# Bot owners that have access to owner commands
owners = [793551719904575509]

# Bot admins that have access to admin commands
admins = [793551719904575509, 385852178063163393]

# Cogs to load on startup
initial_extensions = [
    "cogs.admin",
    "cogs.communication",
    "cogs.configuration",
    "cogs.core",
    "cogs.direct_message",
    "cogs.error_handler",
    "cogs.events",
    "cogs.general",
    "cogs.miscellaneous",
    "cogs.modmail_channel",
    "cogs.owner",
    "cogs.premium",
    "cogs.snippet",
]

# Channels to send logs
join_channel  = 795079305326624789
event_channel = 795079305326624789
admin_channel = 795079305326624789

# This is where patron roles are at
main_server = 768286301190619177    

# Patron roles for premium servers
premium1 = None
premium3 = None
premium5 = None

# The colour used in embeds
primary_colour = 0x1E90FF
user_colour    = 0x00FF00
mod_colour     = 0xFF4500
error_colour   = 0xFF0000
