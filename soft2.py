def pay(d,r):
    if d<=1500 and d>=0:
        fare=500-500*r/100
    elif d<0 or d >=10000000:
        fare=0
    else:
       
        if ((d-1800)%300)==0:
            tmp2=(d-1800)/300
        else :
            tmp2=int((d-1800)/300) +1
            
        tmp=int(tmp2)*100 + 500
        fare=tmp-tmp*r/100
    return [d,r,int(round(fare,-1))]


def main():
    d=[-1,0,1500,1799,99999000,9999999,10000000]
    r=[-1,0,50,51]
    ans=[]
    for tmp in d:
        for tmp2 in r:
            ans.append(pay(tmp,tmp2))
    
    print(ans)


if __name__ == "__main__":
    main()
