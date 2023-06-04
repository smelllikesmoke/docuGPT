from deta import Deta

DETA_KEY = "d0n7zfhjqd9_4dq6oynzAFmbLhrGwn8hij26CH3jRbSf"
db = Deta(DETA_KEY) 
db = db.Base("feedback")

def add_feedback(feedback):
    db.put({"feedback": feedback})
