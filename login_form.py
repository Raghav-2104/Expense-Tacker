from tkinter import*  
base = Tk()  
base.geometry('500x500')  
base.title("Login Form") 





labl_0 = Label(base, text="Login form",width=20,font=("bold", 20))  
labl_0.place(x=90,y=53)  


labl_1 = Label(base, text="Username",width=17,font=("bold", 10))  
labl_1.place(x=80,y=130) 

entry_1 = Entry(base)  
entry_1.place(x=240,y=130)  

labl_2 = Label(base, text="Password",width=17,font=("bold", 10))  
labl_2.place(x=68,y=170)  

entry_2 = Entry(base)  
entry_2.place(x=240,y=170)  


  

 
Button(base, text='Forgot Password?',width=20,bg='black',fg='white').place(x=155,y=250)  
Button(base, text='Submit',width=20,bg='black',fg='white').place(x=155,y=300)  
Button(base, text='Back',width=15,bg='black',fg='white').place(x=50,y=450)

base.mainloop()  
 