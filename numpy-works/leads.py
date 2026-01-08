import numpy as np

leads = np.array([
    # s  m    t  w   th
    [12, 18, 10, 15, 5],   # facebook
    [20, 25, 22, 18, 8],   # insta
    [18, 30, 25, 22, 10],  # youtube
    [25, 28, 30, 26, 12],  # refferal
    [30, 35, 28, 32, 15],  # walkin
    [40, 45, 38, 40, 20],  # reddit
    [35, 50, 42, 45, 25]   # camp
    
])

# task1 total leads generated each day
total_lead=np.sum(leads,axis=0)
print(total_lead)
# task2 total leads from each source 
print(np.sum(leads,axis=1))
# task3 highst lead day
day_wisde_total=np.sum(leads,axis=0)
print(day_wisde_total)
max_total=np.max(day_wisde_total) # to get max value
max_total_index=np.argmax(day_wisde_total)  # to get index of max
print(max_total)
print(max_total_index)
# task4 average leads per source
print(np.average(leads,axis=1))
# task5 avrage leads per day
print(np.average(leads,axis=0))
# highest lead sourse
leads_total=np.sum(leads,axis=1)
print(leads_total)
print(np.max(leads_total))
print(np.argmax(leads_total))

