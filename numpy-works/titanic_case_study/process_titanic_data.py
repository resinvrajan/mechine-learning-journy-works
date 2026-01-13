"""
np.genfromtxt -> is used to add default value in empty column when importing time  

"""
import numpy as np
data=np.genfromtxt("titanic_case_study\\passengers_data.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")
print(data.shape)
# survival analysis
print("survival =",np.sum (data[:,1].astype("int")))
print("survival num by another method =",np.count_nonzero(data[:,1]=="1"))


# print(len(data[data[:,1]=="1"]))  this is not numpy way "len" is slow down the process
# print("total number of death =",len(data[data[:,1]=="0"]))

# total number of death
print("death =",np.count_nonzero(data[:,1]=="0"))

# survival analysis

# survival rate
total=np.count_nonzero(data[:,1])
print(total)
count_of_survival=np.count_nonzero(data[:,1]=="1")
print("survival rate =",(count_of_survival/total)*100)


# survival rate using another method
survived_unsurvived=data[:,1].astype("int")
survived=survived_unsurvived[survived_unsurvived==1]
print("total number of survived=",survived.size)
print("survived rate =",(survived.size/survived_unsurvived.size)*100)

# unsrvived rate
unsurvived=survived_unsurvived[survived_unsurvived==0]
print("unsrvived rate =",(unsurvived.size/survived_unsurvived.size)*100)


# gender analysis

# total number of males
male_female=data[:,3]
male=male_female[male_female=="male"]
print("male count=",male.size)
# total number of female
female=male_female[male_female=="female"]
print("female count=",female.size)
# male survived count
data[data[:,3]=="male"]
male_survived=data[(data[:,3]=="male")&(data[:,1]=="1")]
print("male survived count=",male_survived[:,0].size)
# female survived count
female_survived=data[(data[:,3]=="female")&(data[:,1]=="1")]
print("female survived count=",female_survived[:,0].size)


# male survival rate
print("male survival rate=",(male_survived[:,0].size/male.size)*100)
# female survival rate

print("female survival rate=",(female_survived[:,0].size/female.size)*100)


# age analysis

# max age
print("max age",np.max(data[:,4].astype("int")))
print(data[data[:,4].astype("int")==np.max(data[:,4].astype("int"))])
# min age
print("min age",np.min(data[:,4].astype("int")))
# average age
print("average age",np.mean(data[:,4].astype("int")))

# fare analysis
fare=data[:,5].astype("float")
print("min fare=",np.min(fare))
print("max fare=",np.max(fare))
print("aveerage fare=",np.mean(fare))

# sort 
# =====

# np.argsort()

# sort fare
print(data[np.argsort(data[:,-2].astype("float"))])

