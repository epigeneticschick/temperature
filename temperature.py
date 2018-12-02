'''Lorrayya Williams
Homework 11
April 18, 2018 '''

import unittest
from tkinter import *

class Temperature:
    def __init__(self, f_temp = 0.0):
        self._f_temp = float(f_temp)
        if self._f_temp < -459.67:
            raise ValueError("The temperature cannot be below absolute zero!")
        else:
            self._f_temp = f_temp
            self._c_temp = (float(self._f_temp) - 32) / 1.8
    
    def get_temp_f (self):
        return float(self._f_temp)
    
    def get_temp_c (self):
        return float(self._c_temp)

if __name__== '__main__':
    
    try:
        #tests if it will run temperatures below absolute 0
        Temperature(-500)
        print("Test one failed")
    
    except:
        print("Test one passed")
    
    try:
        #tests if it will run  strings
        Temperature("One hundred degrees")
        print("Test two failed")
        
    except:
        print("Test two passed")
   
    try:
        #tests if it will run proper values
        Temperature(50.0)
        print("Test three passed")
        
    except:
        print("Test three failed")
        
    try:
        #tests if it intially sets temperature f_temp to 0
        t = Temperature()
        t.get_temp_f == 0.0
        print("Test four passed.")
    except:
        print("Test four failed")
        
        
    try:
        #tests whether or not the vonversions are done properly 
        t = Temperature(50)
        assert t.get_temp_c() == 10
        assert t.get_temp_f() == 50
        print("Test five passed.")
    except:
        print("Test five failed")
  
    
class User_interface:
    def __init__(self,window):
        self._convert = Temperature()
        
        window.title("Farenheit to Celisius Converter")
        
        #accepts user input of temperature in Fahrenheit
        self._input = StringVar()
        input1_label = Label(window, text="Temperature (in Fahrenheit):")
        input1_label.grid(row=0, column=0, sticky=E)
        input1_entry = Entry(window, width=6, textvariable = self._input)
        input1_entry.grid(row=0, column=1, sticky=W)
        
        #creates converter button
        convert_frame = Frame(window)
        convert_frame.grid(row=3, column=0, columnspan=2)
        add_button = Button(convert_frame, text = 'Convert', command=self.convert)
        add_button.pack()
      
        #prints Conversion
        self._convert = StringVar()
        self.result_label = Label(window, textvariable = self._convert, width=20)
        self.result_label.grid(row=3, column=1, columnspan =20)
        
        #prints error or greeting
##        self._greetingname = 'Welcome!'
##        error_frame = Frame(window)
##        error_frame.grid(row =4, column =0, columnspan =5)
##        self.error_label = Label(error_frame, text =self._greetingname , width=30)
##        self.error_label.pack()
        
        
    #converts temperature in farenheit to Celsius  
    def convert(self):
        try:
            result = Temperature(self._input.get())
            self._convert.set(result.get_temp_c())
        except:
             self.error_label.config(text= "Sorry, there has been an error.")
            
        
        

        
if __name__ == '__main__':
    root = Tk()
    root.title('Temperature')
    app = User_interface(root)
    root.mainloop()        
    
        
