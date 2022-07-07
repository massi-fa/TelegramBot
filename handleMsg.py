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
        print ("isattack")
        print (bad_words)
        for bad_ward in bad_words:
            if bad_ward in msg:
                return True

        return False; 
