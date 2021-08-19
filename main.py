from tkinter import *
import widgetHelper as Widgets
from ValuesHelper import defaultValues
from tkinter import ttk
import bindings as binds
import MinPageHelper as helper
import mockDB
root = Tk()
root.geometry("1250x680")
root.title("My Desktop App")
topFrame = LabelFrame(root,text="Entry Details",width=1245,height=110,bg='#327ba8',fg='white')
topFrame.place(x=0,y=0)
#Widgets in top Frame >

#<Middle frame Start
middleFrame = LabelFrame(root,text="Quotation",width=1245,height=500,bg='#327ba8',fg='white')
middleFrame.place(x=0,y=110)
TempFrame = Frame(root,width=1245,height=500)
itemList=Widgets.CreateItemsListTreeView(middleFrame)
#itemList.place(x=0,y=0,width=1245)
#Middle Frame End>
# Frames >
# < Widgets in top Frame
CustomerName = Entry(topFrame)
CustomerName.insert(0,defaultValues[0])
CustomerName.place(x=10,y=10,height=30)
CustomerName.bind("<FocusIn>", helper.handle_focus)

CustomerId = Entry(topFrame,width=10)
CustomerId.insert(0,defaultValues[1])
CustomerId.bind("<FocusIn>", helper.handle_focus)

custAddFrame=Frame(topFrame,width=600,bg='#327ba8')

CustomerPhone = Entry(custAddFrame)
CustomerPhone.insert(0,defaultValues[2])
CustomerPhone.place(x=200,y=10,height=30)
CustomerPhone.bind("<FocusIn>", helper.handle_focus)
CustomerPhone.place(x=5,y=0)

CustomerAddress = Entry(custAddFrame)
CustomerAddress.insert(0,defaultValues[3])
CustomerAddress.place(x=200,y=10,height=30)
CustomerAddress.bind("<FocusIn>", helper.handle_focus)
CustomerAddress.place(x=205,y=0)
AddCustContext={
    'CustomerName':CustomerName,
    'CustomerPhone':CustomerPhone,
    'CustomerAddress':CustomerAddress,
    'custAddFrame':custAddFrame
    }
AddCust = Button(custAddFrame,text='Add Customer',bg="#3ea832",fg='black',command=lambda:helper.addCustomer(AddCustContext))
AddCust.place(x=405,y=5)

ItemSearchFrame = Frame(topFrame,width=1245,padx=10,pady=10,bg='#327ba8')

barcode = Entry(ItemSearchFrame)
barcode.insert(0,defaultValues[4])
barcode.place(x=0,y=0,width=240)
barcode.bind("<FocusIn>", helper.handle_focus)

ItemName = Entry(ItemSearchFrame)
ItemName.insert(0,defaultValues[5])
ItemName.place(x=245,y=0,width=330)
ItemName.bind("<FocusIn>", helper.handle_focus)

ItemType = Entry(ItemSearchFrame)
ItemType.insert(0,defaultValues[6])
ItemType.place(x=580,y=0,width=300)
ItemType.bind("<FocusIn>", helper.handle_focus)

ItemSearchFrame.place(x=0,y=40,height=300)
barcode.bind(
    "<KeyRelease>",lambda event,context=[itemList]:
    helper.listItemsbyBarcode(
    event,
    context
    ))
ItemName.bind(
    "<KeyRelease>",lambda event,context=[itemList]:
    helper.listItemsbyItemName(
    event,
    context
    ))
ItemType.bind(
    "<KeyRelease>",lambda event,context=[itemList]:
    helper.listItemsbyItemType(
    event,
    context
    ))
    #<frame in top frame
customerFrame = Frame(root,width=500)
customerlist=Widgets.createCustomerTreeview(customerFrame)
customerlist.bind("<ButtonRelease-1>",lambda event,frame=customerFrame,entry=CustomerName,custId=CustomerId: helper.selectcustomer(event,entry,frame,custId))
listCustomerContext={
    'custframe':customerFrame,
    'custlist':customerlist,
    'CustomerId':CustomerId,
    'custAddFrame':custAddFrame
    }
CustomerName.bind(
    "<KeyRelease>",lambda event,context=listCustomerContext:
     helper.listCustomer(
         event,context
         ))
customerlist.pack()
root.mainloop()