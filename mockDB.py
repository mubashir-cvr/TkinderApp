from tkinter import *
from tkinter import ttk
customerData =[("001","Nidhi", "9656248731", "VKD"),("002","Suman", "12389898s", "OMR")]
stockItems =[("001","Glass", "Cooling", "3"),("002","Glass", "Plane", "4"),("001","Glass", "Cooling", "3"),("002","Glass", "Plane", "4"),("001","Glass", "Cooling", "3"),("002","Glass", "Plane", "4"),("001","Glass", "Cooling", "3"),("002","Glass", "Plane", "4"),("001","Glass", "Cooling", "3"),("002","Glass", "Plane", "4"),("001","Glass", "Cooling", "3"),("002","Glass", "Plane", "4")]
def getCustomersList():
    return customerData
def getStockItems():
    return stockItems
def addCustomer(context):
    global customerData
    customerData+=context
    print(customerData)

