import numpy as np

class LinearRegression:
    def __init__(self):
        self.x:np.array
        self.y:np.array
        self.a:np.array
        self.b:np.array
        self.n:np.int16
        self.coef_:np.float32
        self.intercept_:np.float32
    
    
    def fit(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        self.n = len(self.x)
        self.b = self.coef_()
        self.a = self.intercept_()
        print('Sucess')
    
    
    def predict(self, x):
        return self.a + self.b * np.array(x)
    
    
    def coef_(self):
        self.coef_ = (self.n * np.sum(self.x * self.y) - np.sum(self.x) * np.sum(self.y)) / (self.n * np.sum(self.x ** 2) - (np.sum(self.x) ** 2))
        return self.coef_
    
    
    def intercept_(self):
        self.intercept_ = (np.sum(self.y) - self.b * np.sum(self.x)) / self.n
        return self.intercept_