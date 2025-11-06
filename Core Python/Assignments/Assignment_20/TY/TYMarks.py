

class TYMarks:
    
    
    def __init__(self, theory, practical):
        self.theory = theory
        self.practical = practical

    def __str__(self):
        return f"{self.theory}, {self.practical}"
    
if __name__=="__main__":
    ty=TYMarks(87,92)
    print(ty)