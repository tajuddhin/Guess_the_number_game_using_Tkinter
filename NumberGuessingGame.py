
import tkinter as tk
import random


LARGE_FONT= ("Verdana", 12)
l=("Times 10 bold",19)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)


        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, pagethree,pagefour,pagefive,pagesix,finalpage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Guess game", font=LARGE_FONT,bg='lightgreen')
        label.pack(pady=100,padx=100)

        button = tk.Button(self, text="Start Game",bg='lightblue',
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Imagine a Number",bg='pink', font=LARGE_FONT)
        label.pack(pady=100,padx=100)
      


        button2 = tk.Button(self, text="NEXT",bg='lightblue',
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Multiply the number by 2",bg='lightgreen', font=LARGE_FONT)
        label.pack(pady=100,padx=100)
    


        button2 = tk.Button(self, text="NEXT",bg='lightblue',
                            command=lambda: controller.show_frame(pagethree))
        button2.pack()
        button2 = tk.Button(self, text="BACK",bg='orange',
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        
        
class pagethree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        global n
        n=random.randint(10,90)
        label = tk.Label(self, text="Add "+str(n)+" to result", font=LARGE_FONT,bg='lightgreen')
        label.pack(pady=100,padx=100)

        button = tk.Button(self, text="NEXT",bg='lightblue',
                            command=lambda: controller.show_frame(pagefour))
        button.pack()
        button2 = tk.Button(self, text="BACK",bg='purple',command=lambda: controller.show_frame(pageTwo))
        button2.pack()

class pagefour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Divide the result by 2",bg='lightgreen',font=LARGE_FONT)
        label.pack(pady=100,padx=100)

        button = tk.Button(self, text="NEXT",bg='lightblue',activebackground='lightpink',
                            command=lambda: controller.show_frame(pagefive))
        button.pack()
        button2 = tk.Button(self, text="BACK",bg='purple',
                            command=lambda: controller.show_frame(pagethree))
        button2.pack()
class pagefive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Substract the first imagine number from result", font=LARGE_FONT,bg='lightgreen')
        label.pack(pady=100,padx=100)

        button = tk.Button(self, text="NEXT",bg='lightblue',
                            command=lambda: controller.show_frame(pagesix))
        button.pack()
        button2 = tk.Button(self, text="BACK",bg='purple',
                            command=lambda: controller.show_frame(pagefour))
        button2.pack()
class pagesix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Click Next to get Answer", font=LARGE_FONT,bg='lightgreen')
        label.pack(pady=100,padx=100)

        button = tk.Button(self, text="NEXT",bg='lightblue',
                            command=lambda: controller.show_frame(finalpage))
        button.pack()
        button2 = tk.Button(self, text="BACK",bg='purple',
                            command=lambda: controller.show_frame(pagefive))
        button2.pack()
class finalpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        ans=n/2

        label = tk.Label(self, text="WOW !"+"Answer is ", font=LARGE_FONT,bg='lightgreen')
        label.pack(pady=10,padx=100)
        label = tk.Label(self, text=str(ans), font=l,bg='lightblue')
        label.pack(pady=10,padx=100)
       



app = SeaofBTCapp()
app.mainloop()
