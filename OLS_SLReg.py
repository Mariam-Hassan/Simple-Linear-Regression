class Mariamz_sim_lin_reg:   
 
    def __init__(self, X,Y):
        self.X=X
        self.Y=Y
    def mean_X(self):
        from functools import reduce
        return (reduce(lambda x,y: x+y,self.X))/len(self.Y)
    def mean_Y(self):
        from functools import reduce
        return (reduce(lambda x,y: x+y,self.Y))/len(self.Y)
    def var_X(self):
        from functools import reduce
        return ((reduce(lambda x,y: x+y,(list(map(lambda x:((x-self.mean_X())**2),self.X)))))/len(self.Y))
    def var_Y(self):
        from functools import reduce
        return ((reduce(lambda x,y: x+y,(list(map(lambda x:((x-self.mean_Y())**2),self.Y)))))/len(self.Y))
    
    def cov(self):
        from functools import reduce
        return ((reduce(lambda x,y: x+y,(list(map(lambda x,y:((x-self.mean_X())*(y-self.mean_Y())),self.X,self.Y)))))/len(self.Y))
    
    def B1(self): #slope
        return self.cov()/self.var_X()
    def B0(self): #intercept
        return self.mean_Y()-self.B1()*self.mean_X()   

    def Y_pred(self): #Predicted values
        return list(map(lambda x: self.B0()+self.B1()*x,self.X))
    def MSE(self):    #Mean square error
        from functools import reduce
        return (reduce(lambda x,y:x+y,(list(map(lambda yhat,y:(yhat-y)**2,self.Y_pred(),self.Y)))))/len(self.Y)

    def equation(self): #linear equation   
        print ("{}+{}X".format(self.B0(),self.B1()))
        
