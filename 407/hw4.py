g=1.0
h=0.0

for i in range(100):
    h = -3*g+(9*g*g+400)**.5
    h/=2
    g = -h+(h*h+27)**.5
    #h=(14*g-16)/(g+4)
    print(i,g,h)
    #g=(6*h-14*14)/(h-22)