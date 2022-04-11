from tkinter import *
root=Tk()
root.title("Fibonacci series")
root.geometry("400x400")
label_series=Label(root,text="Fibonacci Series")
label_flower=Label(root)
label_sum=Label(root)
def Show():
    num=10
    firstnum=0
    secondnum=1
    counter=1
    sum=0
    while (counter<=num):
        label_series["text"]+=str(sum)+" "
        counter=counter+1
        firstnum=secondnum
        secondnum=sum
        sum=firstnum+secondnum
    label_flower["text"]="flower is fully bloomed"
    label_sum["text"]="spiral's in right direction are "+str(firstnum)+"spiral's in left direction are "+str(secondnum)+"\ntotal spirals"+str(sum)

btn=Button(root,text="Show Fibonacci Series",command=Show)
btn.pack()
label_series.pack()
label_flower.pack()
label_sum.pack()
root.mainloop()