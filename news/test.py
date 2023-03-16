
from dotenv import load_dotenv
import os
load_dotenv()

NEWSAPI_KEY=os.environ.get("NEWSAPI_KEY")
print(NEWSAPI_KEY)

