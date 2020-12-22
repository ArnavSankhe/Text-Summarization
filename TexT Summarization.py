from tkinter import *

from gensim.summarization import summarize, keywords

root1= Tk()

root = Frame(root1)
root.pack()


label1 = Label(root, text='TEXT SUMMARISATION')
label1.config(font=('helvetica', 14))
label1.pack(pady=10)

label2 = Label(root, text='ENTER YOUR TEXT:')
label2.config(font=('helvetica', 10))
label1.pack(pady=10)


text = Text(root, width=50, height=10,  padx=10, pady=10, bd=5, selectbackground="blue")
text.pack(pady=10)

##root.geometry("300x300+120+120")



def txtsummarise():

    txt = text.get('1.0', END)
    
    text1.delete('1.0', END)
    text1.insert(END, summarize(txt, ratio=0.3))

    text2.delete('1.0', END)
    text2.insert(END, keywords(txt, ratio=0.3))

    

button1 = Button(root, text='SUMMARIZE', command=txtsummarise, bg='brown', fg='white', font=('helvetica', 9, 'bold'))
button1.pack(pady=10)


text1 = Text(root, width=33, height=10,  padx=10, pady=10, bd=5, selectbackground="blue")
text1.pack(side='left', pady=10)


text2 = Text(root, width=14, height=10,  padx=10, pady=10, bd=5, selectbackground="blue")
text2.pack(side='left', pady=10)

##root.resizable(width=False, height=False)

root1.mainloop()
