#Code i made for Genetics Lab Ex9 - Simulation of Hardy-Weinberg Equilibrium

import random


A_dom = 50
A_rec = 50
n = A_dom + A_rec

masterlist = list('A'*A_dom) +  list('a'*A_rec)


def withSubstitution(count): #try to verify accuracy of this part
    matinglist = list()

    for i in range(count):
        A = masterlist.pop(random.randint(0,len(masterlist)-1))
        B = masterlist.pop(random.randint(0,len(masterlist)-1))
        
        #displays the result
        mating = A+B
        #print('{}'.format(mating),end='')

        #returns the beads back to the tray
        masterlist.append(A)
        masterlist.append(B)

        #appends the result to matinglist
        matinglist.append(mating)

    print(matinglist)

    AA = matinglist.count('AA')
    Aa = matinglist.count('Aa') + matinglist.count('aA')
    aa = matinglist.count('aa')
    print('\nAA = {}\nAa = {}\naa = {}\nTotal={}'.format(AA,Aa,aa,(AA+Aa+aa)))

    countlist = [AA,Aa,aa]
    return(countlist)

    #there's a pop index out of range error that occurs once in a while.
    #fixit

def chisquare(lista):
    # with the data from the WithSubstitution, return a 0 and a 1 for accept,reject
    #H-W model
    #p^2 + 2pq + q^2 = 1
    #where p = A_dom, q =A_rec
    p = A_dom/n
    q = A_rec/n
    
    ExpRatioAA = p*p*1.00
    ExpRatioAa = p*q*2.00
    ExpRatioaa = q*q*1.0

    ExpRatios = [ExpRatioAA,ExpRatioAa,ExpRatioaa]
    ObservedValue = lista
    ExpValue = list()
    DevValues = list()
    ChiValues = list()

    for i in range(len(ExpRatios)):
        ExpValue.append(ExpRatios[i] * countt)

    for i in range(len(ExpRatios)):
        DevValues.append(abs(ExpValue[i]-ObservedValue[i]))

    for i in range(len(ExpRatios)):
        ChiValues.append(DevValues[i]*DevValues[i]/ExpValue[i])

    chicrit = 5.991
    chicalc = sum(ChiValues)
    print('Chisq(0.05, df2) ={}'.format(chicalc))
    return(chicalc<chicrit) #if True, Accept HO, if False, Reject HO




countt = 50
# withSubstitution(countt)
AcceptReject = list()

for i in range(25):
    AcceptReject.append(chisquare(withSubstitution(countt)))


print(AcceptReject.count(True))
print(AcceptReject.count(False))

# print(chisquare([17,20,13]))



