#!/usr/bin/env python
# coding: utf-8

# In[7]:


import math

class Triangle():
    
    def __init__(self, a, b, c):
        self.side1 = a
        self.side2 = b
        self.side3 = c
        
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def area(self):
        return 1/4(sqrt(-self.side1^4 + 2*(self.side1*self.side2)^2-self.side2^4+2*(self.side2*self.side3)^2-self.side3^4))
    
    def scale(self, scale_factor):
        return Triangle(scale_factor*self.side1, scale_factor*self.side2, scale_factor*self.side3)
    
    def is_valid(self):
        if self.side1 + self.side2 > self.side3 and self.side2+self.side3>self.side1 and self.side3+self.side1>self.side2:
            return True
        else:
            return False
        
    def is_right(self):
        if self.side1^2 == self.side2^2 + self.side3^2:
            return True
        else:
            False

test_triangle = Triangle(3,4,5)
test_triangle.perimeter()
test_triangle.area()
test_triangle.scale(3)
test_triangle.is_valid()


# In[ ]:




