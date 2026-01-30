import numpy as np
'''fname=input("insert file name ")
data=np.loadtxt(fname)
abu=data[:,2]
elem=data[:,1]
abuFe=abu[elem==26.00]
abuCa=abu[elem==20.00]
abuMg=abu[elem==12.00]
print("Fe mean absolute abundance",np.mean(abuFe))
print("Ca mean absolute abundance",np.mean(abuCa))
print("Mg mean absolute abundance",np.mean(abuMg))'''
up=np.loadtxt("up_rv.fit")
low=np.loadtxt("low_rv.fit")
abu_up=up[:,2]
elem_up=up[:,1]
abuFe_up=abu_up[elem_up==26.00]
abu_low=low[:,2]
elem_low=low[:,1]
abuFe_low=abu_low[elem_low==26.00]
print("Fe mean absolute abundance",np.mean(np.concatenate((abuFe_up,abuFe_low))))



