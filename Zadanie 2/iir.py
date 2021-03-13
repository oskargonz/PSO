# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 21:11:21 2020

@author: Asus
"""



class systemIIR():
    
    def __init__(self,wspolczynniki_a, wspolczynniki_b):
        self.wspolczynniki_a = wspolczynniki_a
        self.wspolczynniki_b = wspolczynniki_b
        self.dane_x = []
        self.dane_y = []
        
        for i in range(len(wspolczynniki_a)):
            self.dane_x.append(0)
        
        for i in range(len(wspolczynniki_b)):
            self.dane_y.append(0)
            
            
    def MnozISumuj_x(self):
        
        suma = 0
        
        for i in range(len(self.wspolczynniki_a)):
            a = self.wspolczynniki_a[i]
            x = self.dane_x[i]
            suma += (a * x)
        
        return suma
    
    def MnozISumuj_y(self):
        
        suma = 0
        
        for i in range(len(self.wspolczynniki_b)):
            b = self.wspolczynniki_b[i]
            y = self.dane_y[i]
            suma += (b * y)
        
        return suma
    
            
    def WpiszNowa_x(self,x):
        
        indeks = len(self.wspolczynniki_a) - 1
        
        for i in range(len(self.wspolczynniki_a)):
            if(i < len(self.wspolczynniki_a)):
                self.dane_x[indeks] = self.dane_x[indeks - 1]
                indeks -= 1
                
        self.dane_x[0] = x
        
    def WpiszNowa_y(self,y):
        
        indeks = len(self.wspolczynniki_b) - 1
        
        for i in range(len(self.wspolczynniki_b)):
            if(i < len(self.wspolczynniki_b)):
                self.dane_y[indeks] = self.dane_y[indeks - 1]
                indeks -= 1
                
        self.dane_y[0] = y
            
            

        
    def WyliczIIR(self, x):
        self.WpiszNowa_x(x)
        wynik_x = self.MnozISumuj_x()
        wynik_y = self.MnozISumuj_y()
        self.WpiszNowa_y(wynik_x - wynik_y)
        
        return wynik_x - wynik_y
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        
    
        