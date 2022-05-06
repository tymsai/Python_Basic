#%%
#Lambda function
KE = lambda m, v: (m*v**2)/2
a=int(input("Enter the weight in kilograms"))
b=int(input("Enter the speed in meters per second"))
print("Kinetic Energy : ", KE(a,b), "joules")
