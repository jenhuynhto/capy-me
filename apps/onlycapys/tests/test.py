import dotenv
import os

#load the api key
dotenv.load_dotenv()
api_key = os.getenv('API_KEY')
print(api_key)