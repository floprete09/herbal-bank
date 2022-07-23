from tkinter import *

window=Tk()
window.title("Herb Bank")
window.configure(bg='lightslategray',)


def stomachic():
    firstLabel=Label(window, font="garamond", text="Aloe, Lemonbalm", bg="darkseagreen4")
    firstLabel.grid(padx=10)
def analgesic():
    secondLabel=Label(window, font="garamond", text="Sage", bg="darkseagreen4")
    secondLabel.grid(padx=10, pady=10)

def purgative():
    thirdLabel=Label(window, font="garamond", text="Bitterroot", bg="darkseagreen4")
    thirdLabel.grid(padx=10)

def inflammation():
    twelthLabel=Label(window, font="garamond", text="Cayenne",bg="darkseagreen4")
    twelthLabel.grid()
    
def antianemic():
    forthLabel=Label(window, font="garamond", text="Dandilion", bg="darkseagreen4", image="/media/felicia/My Passport/WEB DEVELOPMENT/SUMMER 2022/SDEV 140/FINAL PROJECT/dandelion.png")
    forthLabel.grid(pady=10)

def hypoglycemic():
    thirteenthLabel=Label(window, font="garamond", text="Alum Root", bg="darkseagreen4")
    thirteenthLabel.grid()


def antiitussive():
    fourteenthLabel=Label(window, font="garamond", text="Goldenseal, Alum root, elecampane", bg="darkseagreen4")
    fourteenthLabel.grid()






    fifthLabel=Label(window, font="garamond", text="Linden")
    fifthLabel.pack(padx=10)
    
    sixthLabel=Label(window, font="garamond", text="Basil")
    sixthLabel.pack(padx=10)

    seventhLabel=Label(window, font="garamond", text="Goldenseal")
    seventhLabel.pack(padx=10)
    
    eighthLabel=Label(window, font="garamond", text="Alum root")
    eighthLabel.pack()

    ninthLabel=Label(window, font="garamond", text="Elecampane")
    ninthLabel.pack()
    
    tenthLabel=Label(window, font="garamond", text="Camphor", bg="green")
    tenthLabel.pack()

    eleventhLabel=Label(window, font="garamond", text="White lilly")
    eleventhLabel.pack()

firstButton=Button(window, text="Pain", command=lambda:[stomachic(), analgesic()], bg="lightpink4", fg="White", width=20)
firstButton.grid(row=3, column=0, padx=25)

secondButton=Button(window, text= "Cold", command=antiitussive, bg="lightpink4", fg="White", width=20)
secondButton.grid(row=3, column=1, padx=25, pady=5)

thirdButton=Button(window, text="Nausea", command=stomachic, bg="lightpink4", fg="White", width=20)
thirdButton.grid(row=3, column=2, padx=25, pady=10)

forthButton=Button(window, text= "Swelling", command=purgative, bg="lightpink4", fg="White", width=20)
forthButton.grid(row=5, column=1)

fifthButton=Button(window, text= "Constipation", command=purgative, bg="lightpink4", fg="White", width=20)
fifthButton.grid(row=5, column=0,)

sixthButton=Button(window, text= "Allergies", command=analgesic, bg="lightpink4", fg="White", width=20)
sixthButton.grid(row=5, column=2)

seventhButton=Button(window, text= "Diabetes", command=hypoglycemic, bg="lightpink4", fg="White", width=20)
seventhButton.grid(row=6, column=2)

eighthButton=Button(window, text= "Inflammation", command=analgesic, bg="lightpink4", fg="White", width=20)
eighthButton.grid(row=6, column=1)

ninthButton=Button(window, text= "Anemia", command=antianemic, bg="lightpink4", fg="White", width=20)
ninthButton.grid(row=6, column=0, pady=10)







window.mainloop()
