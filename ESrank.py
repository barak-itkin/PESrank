
def sample(P,gamma,b):
    S=[(P[i],i+1) for i in range(b)]
    i=b+1
    j=b
    while(i<len(P)):
        if (i)/(j)<=gamma and (i+1)/(j)>gamma:
            j=i
            S.append((P[j-1],j))
        i=i+1
    S.append((P[-1],len(P)))
    return S


def sampleMerge(S1,S2,gamma,b):
    
    n1=len(S1)
    n2=len(S2)

    P=[(-S1[i][0]*S2[j][0],i,j) for i in range(n1) for j in range(n2)]
    P.sort()

    U=[1]
    L=[1]
    for i in range(1,len(P)):
        (ic,jc)=(P[i][1],P[i][2])
        (ip,jp)=(P[i-1][1],P[i-1][2])
        if jp+1<n2 and ip+1<n1:
            U.append(U[-1]+(S2[jp+1][1]-S2[jp][1])*(S1[ip+1][1]-S1[ip][1]))
        elif jp+1<n2:
            U.append(U[-1]+(S2[jp+1][1]-S2[jp][1]))
        elif ip+1<n1:
            U.append(U[-1]+(S1[ip+1][1]-S1[ip][1]))
        else:
            U.append(U[-1]+1)
            
        
        if jc-1>=0 and ic-1>=0:
            L.append(L[-1]+(S2[jc][2]-S2[jc-1][2])*(S1[ic][1]-S1[ic-1][1]))
        elif jc-1>=0:
            L.append(L[-1]+(S2[jc][2]-S2[jc-1][2]))
        elif ic-1>=0:
            L.append(L[-1]+(S1[ic][1]-S1[ic-1][1]))
        else:
            L.append(L[-1]+1)
        
                
    S=[(-P[i][0],i+1,i+1) for i in range(b)]
    i=b
    j=b-1
    while(i<len(P)-1):
        if U[i]/U[j]<=gamma and U[i+1]/U[j]>gamma:
            j=i
            S.append((-P[j][0],U[j],L[j]))
        i=i+1
    S.append((-P[-1][0],U[-1],L[-1]))
    return S

def upperLower(S1,S2,p,b):
    uPrev=0
    n1=len(S1)
    n2=len(S2)
    i=0
    j=n2-1
    ub=0
    lb=0
    while(i<n1 and j>=0):
        pCurr=S1[i][0]*S2[j][0]
        if pCurr>=p:
            u=S2[j][1]
            l=S2[j][2]
            ub=ub+u
            lb=lb+l
            if i>=b:
                ub=ub+uPrev*(S1[i][1]-S1[i-1][1]-1)
                lb=lb+l*(S1[i][1]-S1[i-1][1]-1)
            i=i+1
            uPrev=u
        elif(j>=1):
            pNext=S1[i][0]*S2[j-1][0]
            if pNext<p<pCurr:
                u=S2[j][1]-1
                l=S2[j-1][2]
                ub=ub+u
                lb=lb+l
                if i>=b:
                    ub=ub+uPrev*(S1[i][1]-S1[i-1][1]-1)
                    lb=lb+l*(S1[i][1]-S1[i-1][1]-1)
                i=i+1
                uPrev=u
            else:
                j=j-1
        else:
            j=j-1
    if j<0 and i<n1:
        ub=ub+uPrev*(S1[i][1]-S1[i-1][1]-1)
    return (lb,ub)


def main(P,d,gamma,b,p):  
    S=[sample(P[i],gamma,b) for i in range(d)]
    
    Scurr=[(S[0][i][0],S[0][i][1],S[0][i][1]) for i in range(len(S[0]))]

    for i in range(1,d-1):
        Scurr=sampleMerge(S[i],Scurr,gamma,b)

    (lb,ub)= upperLower(S[d-1],Scurr,p,b)
    return (lb,ub)

def main1(P,d,gamma,b):  
    S=[sample(P[i],gamma,b) for i in range(d)]
    Scurr=[(S[0][i][0],S[0][i][1],S[0][i][1]) for i in range(len(S[0]))]

    for i in range(1,d-1):
        Scurr=sampleMerge(S[i],Scurr,gamma,b)

    return(S[d-1],Scurr)


def main2(L1,L2,p,b):  
    (lb,ub)= upperLower(L1,L2,p,b)
    return (lb,ub)
    

    
