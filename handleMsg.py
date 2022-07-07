class Message:
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    
    def __repr__(self):
        return self.msg

    def isAttack(self,bad_words):
        msg = self.msg.lower()
        msg = msg.replace(" ", "")
        
        for bad_ward in bad_words:
            if bad_ward in msg:
                return True

        return False; 

class User:
    def __init__(self, id, username = None):
        self.id = id
        if(username == None):
            self.username = "Unknown"
        else:
            self.username = username
        self.n_badWords = 0
        self.n_goodWords = 0

    def __str__(self):
        return self.username

    def addBadWord(self):
        self.n_badWords += 1
        self.n_goodWords = 0
    
    def addGoodWord(self):
        self.n_goodWords += 1

    