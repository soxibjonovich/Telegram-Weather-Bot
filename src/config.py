from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
OPENWEATHER_API_KEY = env.str('OPENWEATHER_API_KEY')

assert BOT_TOKEN is not None, "BOT_TOKEN is not set in environment variables."
assert OPENWEATHER_API_KEY is not None, "OPENWEATHER_API_KEY is not set in environment variable."
