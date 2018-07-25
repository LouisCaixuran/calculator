import tkinter as tk
import sys
from calculator import main
root=tk.Tk()
 
topString=tk.StringVar()
topEntry=tk.Entry(root)
topEntry['width']=40
topEntry['textvariable']=topString
topEntry['width']=40
topEntry.grid(row=0,column=0,columnspan=7)
 

buttonCaptions=['/','*','+','-',\
                '7','8','9',\
                '4','5','6',\
                '1','2','3',\
                '0','=','C']

def edit(caption):
    topString.set(topString.get()+ caption) 
 
buttons={}
for i in range(4):
    for j in range(4):
        t=tk.Button(root,text=buttonCaptions[i*4+j])
        t['width']=5
        t['command']=lambda :edit(buttonCaptions[i*4+j])
        t.grid(row=i+1,column=j)
        buttons[buttonCaptions[i*4+j]]=t                                    
 


buttons['/']['command']=lambda : topString.set(topString.get()+'/')
buttons['*']['command']=lambda : topString.set(topString.get()+'*')
buttons['7']['command']=lambda : topString.set(topString.get()+'7')
buttons['8']['command']=lambda : topString.set(topString.get()+'8')
buttons['9']['command']=lambda : topString.set(topString.get()+'9')
buttons['-']['command']=lambda : topString.set(topString.get()+'-')
buttons['5']['command']=lambda : topString.set(topString.get()+'5')
buttons['6']['command']=lambda : topString.set(topString.get()+'6')
buttons['+']['command']=lambda : topString.set(topString.get()+'+')
buttons['1']['command']=lambda : topString.set(topString.get()+'1')
buttons['2']['command']=lambda : topString.set(topString.get()+'2')
buttons['3']['command']=lambda : topString.set(topString.get()+'3')
buttons['0']['command']=lambda : topString.set(topString.get()+'0')


def clear():
    topString.set('')
buttons['C']['command']=clear

def cct():
     topString.set(main.calculate(topString.get()))
buttons['=']['command']=cct 

 
root.mainloop()