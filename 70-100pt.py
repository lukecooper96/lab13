#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="blue")
circle = drawpad.create_oval(55,100,50,50, fill="purple")
circle2 = drawpad.create_oval(35,400,100,500, fill="green")
circle3 = drawpad.create_oval(200,200,310,360, fill="yellow")
# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
     
	
	        #button 2
	    self.button2 = Button(self.myContainer1)
	    self.button2.configure(text="Right", background= "yellow")
	    self.button2.grid(row=1,column=3)
	    self.button2.bind("<Button-1>", self.button2Click)
		
		#button 3
	    self.button3 = Button(self.myContainer1)
	    self.button3.configure(text="left", background= "red")
	    self.button3.grid(row=1,column=0)
	    self.button3.bind("<Button-1>", self.button3Click)	
		
		#button 4
	    self.button4 = Button(self.myContainer1)
	    self.button4.configure(text="down", background= "magenta")
	    self.button4.grid(row=3,column=1)
	    self.button4.bind("<Button-1>", self.button4Click)	
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	 # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
            self.animate1()
            self.animate2()
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    global circle
            x1, y1, x2, y2 = drawpad.coords(circle)
            if x2 > drawpad.winfo_width(): 
                drawpad.move(circle, -800, 0)
                   
            drawpad.move(circle,6,0)
  
            drawpad.after(10, self.animate)
	def animate1(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    global circle2
            x1, y1, x2, y2 = drawpad.coords(circle2)
            if x2 > drawpad.winfo_width(): 
                drawpad.move(circle2, -800, 0)
        
            drawpad.move(circle2,5,0)
  
            drawpad.after(10, self.animate1)
            
        def animate2(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    global circle3
            x1, y1, x2, y2 = drawpad.coords(circle3)
            if x2 > drawpad.winfo_width(): 
                drawpad.move(circle3, -800, 0)

        
            drawpad.move(circle3,5,0)
  
            drawpad.after(10, self.animate2)
	   
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	   
	#button 2	
	def button2Click(self, event):
	    global oval
	    global drawpad
	    drawpad.move(player,25,0)
	#button 3
	def button3Click(self, event):
	    global oval
	    global drawpad
	    drawpad.move(player,-25,0)
	#button 4
	def button4Click(self, event):
	    global oval
	    global drawpad
	    drawpad.move(player,0,10)
	    
	  
	
	
		

app = MyApp(root)
root.mainloop()