class Game:
    def __init__(self,id):
        self.p1Sign = False
        self.p2Sign = False
        self.ready = False
        self.card = []
        self.id = id
        self.wins = [0,0]
        self.ties = 0

    def connected(self):
        return self.ready
    
    def play(self, player, position):
      pass
    
    def bothWent(self):
        return self.p1Sign and self.p2Sign
    
    def reset(self):
        self.p1Sign = False
        self.p2Sign = False