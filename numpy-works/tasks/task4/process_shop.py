import numpy as np
# Load the CSV and display shape
data=np.loadtxt("tasks\\task4\\task4shop.csv",delimiter=",",skiprows=1,dtype="str")
print(data)
# Calculate total number of orders
order_id=data[:,0].astype("int")
print(order_id)
print(np.max(order_id))
# Find average unit price
print(np.average(data[:,4].astype("int")))
# Calculate total revenue per order
revenue=(data[:,3].astype("int"))*(data[:,4].astype("int"))
print("revnue=",revenue)
print("revnue total=",np.sum(revenue))
# Find orders with delivery days > 5
print(data[data[:,-2].astype("int")>5])
# Count returned vs non-returned orders
returned=data[data[:,-1]=="No"]
no_returned=data[data[:,-1]!="No"]
print("returned=",len(returned),"no returned=",len(no_returned))
# Find average discount per product category
electronics=data[data[:,2]=="Electronics"]
print("electronics discount average",np.average(electronics[:,5].astype("int")))
clothing=data[data[:,2]=="Clothing"]
print("clothing discount average",np.average(clothing[:,5].astype("int")))
home=data[data[:,2]=="Home"]
print("home discount average",np.average(home[:,5].astype("int")))

"""
Create a new column:

DeliveryDays ≤ 3 → Fast

Else → Normal

"""
delivery_mode=np.where(data[:,-2].astype("int")<=3,"Fast","Normal")

print(delivery_mode)
updated_data = np.column_stack((data, delivery_mode))
print(updated_data)
