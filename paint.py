import tkinter as tk


class Interface(object):
    def __init__(self):

        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._button = None
        #self._colourPicked = None
    
        #self._defaultColour = "red"

        self._root = tk.Tk()
        self._root.title("Paint")   
        self._canvas = tk.Canvas(self._root, bg="white", height=500, width=700)
        self._canvas.grid(rowspan=8, column=1)  
        self._shapeLabel  = tk.StringVar()
        tk.Label(self._root, textvariable=self._shapeLabel).grid(row=0, column=0)
        self._shapeLabel.set("Selected shape: None")

        self._colourLabel= tk.StringVar()
        tk.Label(self._root, textvariable=self._colourLabel).grid(row=1, column=0)
        self._colourLabel.set("Selected colour: None" )

        self._buttOval = tk.Button(self._root, text="Oval", command=self.makeOval)
        self._buttOval.grid(row=2, column=0, sticky="w")

        self._buttRect = tk.Button(self._root, text="Rectangle", command=self.makeRect)
        self._buttRect.grid(row=3, column=0, sticky="w")
        
        self._buttLine = tk.Button(self._root, text="Line", command=self.makeLine)
        self._buttLine.grid(row=4, column=0, sticky="w")

        self._buttRed = tk.Button(self._root, text='Red', command=self.pickRed)
        self._buttRed.grid(row=5, column=0, sticky="w")

        self._buttBlue = tk.Button(self._root, text='Blue', command=self.pickBlue)
        self._buttBlue.grid(row=6, column=0, sticky="w")

        self._buttYellow = tk.Button(self._root, text='Yellow', command=self.pickYellow)
        self._buttYellow.grid(row=7, column=0, sticky="w")

        self._canvas.bind("<Button-1>", self.noShape)

        self._root.mainloop()


    def noShape(self,event):
        print("No shape selected")

    def pickRed(self):
        #print ("red")
        self._colourPicked = "red"
        self._colourLabel.set("Selected colour: Red")

    def pickBlue(self):
        #print ("blue")
        self._colourPicked = "blue"
        self._colourLabel.set("Selected colour: Blue")

    def pickYellow(self):
        #print ("yellow")
        self._colourPicked = "yellow"
        self._colourLabel.set("Selected colour: Yellow")

    
    def makeOval(self):
        #print("oval ")
        self._button = "oval"
        self._shapeLabel.set("Selected shape: Oval")
        self._canvas.bind("<Button-1>", self.getX1Y1)

    def makeRect(self):
        #print("Make rect ")
        self._button = "rect"
        self._shapeLabel.set("Selected shape: Rectangle")
        self._canvas.bind("<Button-1>", self.getX1Y1)

    def makeLine(self):
        self._button = "line"
        self._shapeLabel.set("Selected shape: Line")
        self._canvas.bind("<Button-1>", self.getX1Y1)
        

    def paint(self):
        """ if self._colourPicked == None :
            self._colourPicked = "red" """
        try:
            if self._button == "rect":
                self._canvas.create_rectangle(self._x1,self._y1, self._x2, self._y2, fill=self._colourPicked)
                self.makeRect()

            if self._button == "oval":
                self._canvas.create_oval(self._x1,self._y1, self._x2, self._y2, fill= self._colourPicked)
                self.makeOval()

            if self._button == "line":
                self._canvas.create_line(self._x1,self._y1, self._x2, self._y2, fill= self._colourPicked)
                self.makeLine()
        except:
            print("No colour selected")
       
    def getX1Y1(self, event):
        #print("x1y1 ")
        self._x1 = event.x
        self._y1 = event.y
        self._canvas.bind("<Button-1>", self.getX2Y2)
        #self._canvas.bind("<ButtonRelease-1>", self.getX2Y2)
    
    def getX2Y2(self, event):
        #print("x2y2")
        self._x2 = event.x
        self._y2 = event.y
        self.paint()




if __name__ == '__main__':
    Interface()