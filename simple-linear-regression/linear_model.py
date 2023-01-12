import numpy as np

class LinearRegression:
    def __init__(self):
        self.x:np.array
        self.y:np.array
        self.a:np.array
        self.b:np.array
        self.n:np.int16
    
    
    def fit(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        self.n = len(self.x)
        #coeficiente angular
        self.b = self.coef_()
        #intercepto
        self.a = self.intercept_()
        print('Sucess')
    
    
    def predict(self, x):
        return self.a + self.b * np.array(x)
    
    
    def coef_(self):
        return (self.n * np.sum(self.x * self.y) - np.sum(self.x) * np.sum(self.y)) / (self.n * np.sum(self.x ** 2) - (np.sum(self.x) ** 2))
    
    
    def intercept_(self):
        return (np.sum(self.y) - self.b * np.sum(self.x)) / self.n