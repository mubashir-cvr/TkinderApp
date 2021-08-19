from tkinter import * 
from tkinter import ttk

def createCustomerTreeview(frame):
    customerlist = ttk.Treeview(frame, selectmode ='browse')
    customerlist["columns"] = ("1", "2", "3","4")
    customerlist['show'] = 'headings'
    customerlist.heading("1", text ="Cust ID")
    customerlist.heading("2", text ="Name")
    customerlist.heading("3", text ="Mobile")
    customerlist.heading("4", text ="Address")
    customerlist.column("1", width = 50, anchor ='w')
    customerlist.column("2", width = 100, anchor ='w')
    customerlist.column("3", width = 100, anchor ='w')
    customerlist.column("4", width = 100, anchor ='w')
    return customerlist
def CreateItemsListTreeView(frame):
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview", background="#a3cff7", 
                fieldbackground="#a3cff7", foreground="black")
    style.configure("Treeview.Heading", font=(None, 14))
    # style = ttk.Style(frame)
    style.configure('Treeview', rowheight=30)
    treeView = ttk.Treeview(frame, selectmode ='browse')
    treeView["columns"] = ("1", "2", "3","4")
    treeView['show'] = 'headings'
    treeView.heading("1", text ="Bar Code")
    treeView.heading("2", text ="Name")
    treeView.heading("3", text ="Type")
    treeView.heading("4", text ="Stock")
    treeView.column("1", width = 100, anchor ='c')
    treeView.column("2", width = 200, anchor ='c')
    treeView.column("3", width = 200, anchor ='c')
    treeView.column("4", width = 200, anchor ='c')
    return treeView