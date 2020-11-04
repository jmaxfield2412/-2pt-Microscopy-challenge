#Microscopy problem
#Calculate the magnification
C = 4
u = 80
#Subroutine to calculate magnification
def Magnif(C):
  return ((C * 10000) / 80)
#Main Program
M = Magnif(C)
print("The magnification is",M,"X")