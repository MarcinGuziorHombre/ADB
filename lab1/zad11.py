class Quaternion:
    def __init__(self, real, i, j, k):
        self.real = real
        self.i = i
        self.j = j
        self.k = k

    def __add__(self, rhs):
        return Quaternion(self.real + rhs.real,
                          self.i + rhs.i,
                          self.j + rhs.j,
                          self.k + rhs.k)
        
    def __sub__(self, rhs):
        return Quaternion(self.real - rhs.real,
                          self.i - rhs.i,
                          self.j - rhs.j,
                          self.k - rhs.k)