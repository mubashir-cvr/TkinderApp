import mockDB as dB
import ValuesHelper as vHelper
from tkinter import *
from tkinter import ttk

def listCustomer(e,context):
    context['custframe'].place(x=10,y=60)
    context['CustomerId'].place(x=205,y=10,height=30)
    customerDetails= dB.getCustomersList()
    typed = e.widget.get()
    if typed == ' ' or typed == '':
        data = customerDetails
    else:
        data=[]
        for item in customerDetails:
            if typed.lower() in item[1].lower() or typed.lower() in item[2].lower() or typed.lower() in item[3].lower():
                data.append(item)
        count=0
        for item in data:
            count=+1
        if count==0:
            context['custframe'].place(x=10,y=-1000)
            context['CustomerId'].place_forget()
            context['custAddFrame'].place(x=200,y=10,height=30)
        else:
            context['custAddFrame'].place_forget()
    updateList(data,context['custlist'])


def updateList(data,widget):
    for item in widget.get_children():
        widget.delete(item)
    count=0
    for item in data:
        count+=1
        widget.insert("", 'end', text ="L"+str(count),
             values =item)


def selectcustomer(e,entry,frame,custId):
    val = e.widget.focus()
    custId.delete(0,END)
    entry.delete(0,END)
    entry.insert(0,e.widget.item(val)['values'][1])
    custId.insert(0,e.widget.item(val)['values'][0])
    frame.place(x=10,y=-1000)


def handle_focus(event):
    if event.widget.get() in vHelper.defaultValues:
        event.widget.delete(0,END)


def addCustomer(context):
    [a,b,c]=[context['CustomerPhone'],context['CustomerName'],context['CustomerAddress']]
    if(a.get()!='' and b.get() !='' and c.get()!=''):
        value=[(100,b.get(),a.get(),c.get())]
        dB.addCustomer(value)
        clearEntryText([a,b,c])
        a.insert(0,'Phone Number')
        b.insert(0,'Customer Name')
        c.insert(0,'Address ')
        context['custAddFrame'].place_forget()


def clearEntryText(context):
    for entry in context:
        entry.delete(0,END)


def listItemsbyBarcode(event,context):
    context[0].place(x=0,y=0,width=1245)
    typed = event.widget.get()
    itemlist = dB.getStockItems()
    if typed == '' or typed == ' ':
        data=itemlist
    else:
        data=[]
        for item in itemlist:
            if typed.lower() in item[0].lower():
                data.append(item)
    count=0
    for item in data:
        count=+1
    if count==0:
        print("Not Found")
        context[0].place_forget()
    updateList(data,context[0])


def listItemsbyItemName(event,context):
    context[0].place(x=0,y=0,width=1245)
    typed = event.widget.get()
    itemlist = dB.getStockItems()
    if typed == '' or typed == ' ':
        data=itemlist
    else:
        data=[]
        for item in itemlist:
            if typed.lower() in item[1].lower():
                data.append(item)
    count=0
    for item in data:
        count=+1
    if count==0:
        context[0].place_forget()
    updateList(data,context[0])

def listItemsbyItemType(event,context):
    context[0].place(x=0,y=0,width=1245)
    typed = event.widget.get()
    itemlist = dB.getStockItems()
    if typed == '' or typed == ' ':
        data=itemlist
    else:
        data=[]
        for item in itemlist:
            if typed.lower() in item[2].lower():
                data.append(item)
    count=0
    for item in data:
        count=+1
    if count==0:
        context[0].place_forget()
    updateList(data,context[0])