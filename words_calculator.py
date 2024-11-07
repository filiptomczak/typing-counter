class Calculator:
    def __init__(self):
        self.deltas=[]
        self.lens=[]

    def chars_per_minute(self,word,delta):
        self.lens.append(word)
        self.deltas.append(delta)
        
        return 60 / self.get_avg(self.deltas) * self.get_avg(self.lens)

    def get_avg(self, arr):
        sum=0
        for a in arr:
            sum += a
        return sum / len(arr)