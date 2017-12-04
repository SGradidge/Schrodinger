#Simon Gradidge
#Please note: This program runs in VIDLE as coded from in the WinLab

from visual import *
from visual.graph import *

L = float(input("Please input the size of the well (L):"))
E = float(input("Please input the starting energy (E):"))
dx = float(input("Please input the size increment (dx):"))
V0 = float(input("Please input the depth of the well (V0):"))
Lp = L
Ep = E
dxp = dx
V = 0
hc = 1
psi = 0
psip = psi
x = -(L/2) - 0.1
xp = x
dpsi = 1/sqrt(0.0508895)
dpsip = dpsi
dE = 0.02
find = False

graph2 = gdisplay(title='Find the Energy value')
funct1 = gcurve(color=color.blue)

while not find:
    rate(1000)
    x = 0
    dpsi = 1/sqrt(0.0508895)
    psi = 0
    while x <= ((L/2)+0.1):
        if(x < -L/2 or x > L/2):
            V = V0
        else:
            V = 0
        rate(100000)
        ddpsi = -2*hc*(E-V)*psi
        dpsi = dpsi+ddpsi*dx
        psi = psi+dpsi*dx
        x = x+dx
        funct1.plot(pos = (x,psi))
        
    if abs(psi)<0.002:
        find = true
        print "\nCalculated Energy value",E
    E = E+dE

graph2 = gdisplay(title='Graph of Psi vs Poistion', xtitle='Position', ytitle='Psi')
funct2 = gcurve(color=color.red)

while xp <= L:
    if(x < -L/2 or x > L/2):
        V = V0
    else:
        V = 0
    ddpsi=-2*hc*(E-V)*psip
    dpsip=dpsip+ddpsi*dxp
    psip=psip+dpsip*dxp
    xp=xp+dxp
    funct2.plot(pos = (xp,psip))
    
print "Possible energy levels:"
for n in range (1,11):
    print ((n**2)*((1.0976201*10**-67)/(2*(9.1*10**-31)*L**2)))
