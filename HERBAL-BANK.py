#Authon: Felicia Loprete
# Class: SDEV140
# Date: July 29 2022
# Assignment: Final project Submission
# Herb Bank

# Summary: This is an app that tells you what herbs you can use that would be appropriate for various ailments you may have. You press
#the buttons on the screen and the appropriate herbs pop up in the dialog box.You can use the clear button to clear the screen.



    #imports
from ast import Delete
from cgitb import text
from tkinter import *
from tkinter.tix import PopupMenu


    #Window settings
window=Tk()
window.title("Herb Bank")
window.configure(bg='lightslategray',)

    #Images

icon1 = PhotoImage(file = "/home/felicia/Desktop/FINALPROJECT2/labelHERB.png") #Image file 
smaller_image1 = icon1.subsample(2,2)

label1 = Label(window, image = smaller_image1) #Label for first image
label1.grid( column=3, row=0)


icon2 = PhotoImage(file = "/home/felicia/Desktop/FINALPROJECT2/herbs.png") #herbs image
smaller_image2 = icon2.subsample(3,4)

label2 = Label(window, image = smaller_image2)
label2.grid( column=1, row=0, columnspan=2)



    #Function for closing the second window

def close_win(top): #function to close the window
   top.destroy()


    #functions that opens second window when pain or cold is pressed on main screen. 

def open_popup(): #function to open the popup window
   top= Toplevel()

   Hope=Label(top,text="Ouch! Hope you feel better soon!", font=("arial 16 bold")) #text label for Hope you feel better label.
   Hope.grid(padx=30, pady=30)

    #button that is pressed on popup window
   Button(top,)
   button1=Button(top,text=" Okay, thank you.", command=lambda:close_win(top)) #button text for popup window.  
   button1.grid( padx=10, pady=10  )


def coldpop():
    top=Toplevel() #function for opening popupwindow for pressing cold button on main screen.

    cold=Label(top, text="Awe man, having a cold sucks. Feel better soon!", font=("arial 16 bold"))
    cold.grid(padx=30, pady=30)

    #button that is pressed on popup window
    Button(top,)
    button1=Button(top,text=" Okay, thank you.", command=lambda:close_win(top)) #text for button for popup window. 
    button1.grid( padx=10, pady=10  )
   
    
    
    
    #Label for main screen that tells user what to do.

Label(window, text=" Click the Button to see what herbs to use", bg=("lightcyan4") ,font=('Arial 16 bold' )).grid(pady=20, row=0, )

    #Entry window

ent=Entry(window, width=40,  font=('garamond', 22 ) ) #entry window for button entry. 
ent.grid (row=9, column=1, columnspan=3, padx=10, pady=10,)



    #Functions that are called when buttons are pressed


def stomachic():
    firstLabel=Label(window, font="garamond",  bg="darkseagreen4") #Labels labeled from first to tenth labels. The functions are herb classifications and are appropriately named based on the button that is pressed. 
    firstLabel.grid(padx=10)

def analgesic():
    secondLabel=Label(window, font="garamond",  bg="darkseagreen4")
    secondLabel.grid

def aperient():
    thirdLabel=Label(window, font="garamond",  bg="darkseagreen4")
    thirdLabel.grid(padx=10)

def antianemic():
    forthLabel=Label(window, font="garamond",  bg="darkseagreen4", )
    forthLabel.grid(pady=10)

def immune():
    fifthLabel=Label(window, font="garamond",  bg="darkseagreen4")
    fifthLabel.grid(padx=10)

def diuretic():   
    sixthLabel=Label(window, font="garamond",  bg="darkseagreen4" )
    sixthLabel.grid(padx=10)
    
def antihistamine():
    seventhLabel=Label(window, font="garamond",  bg="darkseagreen4")
    seventhLabel.grid(padx=10)

def anti_inflammatory():
    eighthLabel=Label(window, font="garamond", bg="darkseagreen4")
    eighthLabel.grid()

def hypoglycemic():
    ninthLabel=Label(window, font="garamond",  bg="darkseagreen4")
    ninthLabel.grid()

def antiitussive():
    tenthLabel=Label(window, font="garamond",  bg="darkseagreen4")
    tenthLabel.grid()


    
       
       
       
       #funtion that clears the screen when the clar button is pressed
    
def buttonClear(): # a clear button that clears the screen. 
    ent.delete (0,END)
    


def click(herb):
    ent.delete(0,END)
    ent.insert(0, herb)

    
    
    
    #buttons that get pressed on main screen

firstButton=Button(window, text="Pain", command=lambda:[click("Sage, stinging nettle, solomons seal"), analgesic(), open_popup() ], bg="lightpink4", fg="White", width=20)
firstButton.grid(row=8, column=0, padx=20)

secondButton=Button(window, text= "Cold",  bg="lightpink4", fg="White", width=20,command=lambda:[click("Linden, golden seal, elder, horehound"), immune, coldpop()])
secondButton.grid(row=6, column=1, padx=20, )

thirdButton=Button(window, text="Nausea", bg="lightpink4", fg="White", width=20,command=lambda:[stomachic,click("Aloe, Lemonbalm")] )
thirdButton.grid(row=6, column=2, padx=5, pady=10)

forthButton=Button(window, text= "Edema", bg="lightpink4", fg="White", width=20,command=lambda:[diuretic, click("Broom, hemlock, iris") ])
forthButton.grid(row=7, column=1, padx=20, pady=10)

fifthButton=Button(window, text= "Constipation", bg="lightpink4", fg="White", width=20,command=lambda:[aperient, click("Balomy, chickweed, white ash, fennel seed") ])
fifthButton.grid(row=6, column=0, padx=20, pady=10)

sixthButton=Button(window, text= "Allergies", bg="lightpink4", fg="White", width=20,command=lambda:[antihistamine, click("Goldenseal, plantains, stinging nettle, basil") ])
sixthButton.grid(row=7, column=2, padx=5, pady=10)

seventhButton=Button(window, text= "Diabetes", bg="lightpink4", fg="White", width=20,command=lambda:[hypoglycemic,click("Alum root")] )
seventhButton.grid(row=8, column=2, padx=5, pady=10)

eighthButton=Button(window, text= "Inflammation", bg="lightpink4", fg="White", width=20,command=lambda:[anti_inflammatory,click("Cayenne, sarsaparilla, lobelia, Slippery elm")] )
eighthButton.grid(row=8, column=1, padx=20, pady=10)

ninthButton=Button(window, text= "Anemia", bg="lightpink4", fg="White", width=20,command=lambda:[antianemic,click("Dandelion, raspberry leaves, comfrey, fenugreek")] )
ninthButton.grid(row=7, column=0, pady=10, padx=20, )

tenthButton=Button(window, text="Clear screen",command=buttonClear)
tenthButton.grid(row=9, column=0, pady=30, padx=30, columnspan=1)






window.mainloop()
