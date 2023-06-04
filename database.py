from deta import Deta
from dotenv import load_dotenv
import os
load_dotenv()

DETA_KEY = os.environ["DETA_PROJECT_KEY"]

db = Deta(DETA_KEY) 
db = db.Base("feedback")

def add_feedback(feedback):
    db.put({"feedback": feedback})
