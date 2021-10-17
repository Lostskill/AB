from tkinter import * 
import pickle 
import os

os.chdir(r'C:\Users\User\Documents\Programms\Reserv')


class slovar: 

    def __init__(self,name,email) : 
        self.name = name 
        self.email = email
        
    
    def add(self): 
        with open('it.data', 'rb') as f :
            b = pickle.load(f)  
            b[self.name] = self.email
            self.b = b

        with open('it.data', 'wb') as f :
            pickle.dump(b,f) 
            print(b) 
            del b 
            f.close
            
    def open(self): 
        global a 
        f = open('it.data', 'rb') 
        a = pickle.load(f) 
        self.a = a
        f.close()
    
    def delete(self): 
        with open('it.data', 'rb') as f :
            c = pickle.load(f)  
            print(c)
            del c[self.name] 
        
        with open('it.data', 'wb') as f : 
            pickle.dump(c,f) 
            print(c) 
            del c 
            f.close
    
    def delall(self) : 
        with open('it.data', 'wb') as f : 
          kofds = {} 
          pickle.dump(kofds, f) 
          f.close()   






window = Tk() 
window.title("Адресная книга") 
window.geometry('1000x700')

def get_entry(): 
    value2 = txt.get()
    value1 = txt2.get()
    adrees = slovar(value1,value2) 
    adrees.add()

def get_all(): 
    adrees = slovar(name=None,email=None)  
    adrees.open()   
    text.insert(1.0,a) 

def deladd(): 
    adrees = slovar(name=None,email=None) 
    adrees.delall() 

def delname() : 
    jo = txt3.get()
    adrees = slovar(jo,email=None) 
    adrees.delete()    
    text.insert(1.0,a)
lbl = Label(window,text="Адресная книга",font=('Arial Bold',50))
lbl.grid(column=3, row=0)


txt = Entry(window,width=20) 
txt.grid(column=3,row=1)
txt2 = Entry(window,width=20) 
txt2.grid(column=2,row=1)
txt3 = Entry(window,width=20) 
txt3.grid(column=3,row=3)
text = Text(window, wrap=WORD)  
text.grid(column=3,row=6)

btn = Button(window,text="Добавить Контакт",command=get_entry) 
btn.grid(column=4,row=1)
btn2 = Button(window,text="Очистить всё",command=deladd) 
btn2.grid(column=3,row=2) 
btn3 = Button(window,text='Удалить контакт(По имени)',command=delname) 
btn3.grid(column=4,row=3)
btn4 = Button(window,text='Показать все контакты', command =get_all)
btn4.grid(column=3,row=4)


lbl2 = Label(window,text="Список контактов",font=('Arial Bold',30))
lbl2.grid(column=3, row=5)




window.mainloop()
