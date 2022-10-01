from cmath import pi


def area(b,h):
    return b*h

def per(B,H):
    return 2*B + 2*H 

def areaS(r):
    return  4*pi*r**2  

def volumeS(r):
    return 4/3*pi*r**3 

base = float(input('give base: '))
height = float(input('give height: '))

print('Area= ', round(area(base, height),1))
print('Perímetro= ', round(per(base, height),1))

print('===========================================')

print('Now lets find area and volume of a sphere')
radius = float(input('Give radius: '))

print('area of sphere with radius of %d has %d and a volume of %d' %(radius, areaS(radius), volumeS(radius)) )  #why roound bro.

