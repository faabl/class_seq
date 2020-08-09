from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN #四捨五入用
from itertools import permutations 

import numpy as np 

#xはlenが3のリストを想定．
#要素は文字列を想定
def make_input(x):
    ans = [["h","h",x[0]],[x[0],"h",x[1]],[x[1],"s",x[2]],[x[2],"s","s"],["s","h","h"]]
    return ans


#inputに自分の場合の事象を入れたら，8個の確率がでるよ．
#確率は一つ目のkeyが条件,二つ目がそれが与えられた事象
#ex) p(b|a)のとき，対応する確率はprob[a][b] 
def make_prob(input):
   
    
    e_counts={} #事象数のカウンター
     
    for events in input:
        events.append("fin")
        before = "in"
        for event in events:
            if not(before in e_counts):
                e_counts[before]={}
            if not(event in e_counts[before]):
                e_counts[before][event]=1
            else :
                e_counts[before][event] += 1
            
            before = event
            
    prob={}
    print(e_counts)
    for count in e_counts :
        e_sum = sum(e_counts[count][tmp] for tmp in e_counts[count])
        # prob[count]={tmp:e_counts[count][tmp]/e_sum for tmp in e_counts[count]}
        prob[count]={ tmp:float(Decimal((e_counts[count][tmp]/e_sum)).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)) for tmp in e_counts[count]}
    
    return prob

#求めたい尤度の事象とmake_prob()で求めた確率から，尤度を出す．
#c_flag　は
def get_likelihood(input,prob,c_flag=False,digit='0.0001'):
    before = "in"
    input.append("fin")
    ans = 1
    process=""
    for tmp in input:
        ans *= prob[before][tmp]
        
        process+=str(prob[before][tmp])+" * "
        before=tmp
    process=process.rstrip(" * ")
    if c_flag:
        print(process)
    return float(Decimal(ans).quantize(Decimal(digit)))

        

def start(id=["s","s","h"]):
    # input1=[["h","h","s"],["s","h","s"],["s","s","h"],["h","s","s"],["s","h","h"]]
    
    
    input1=make_input(id)
    print(input1)
    prob_a= make_prob(input1)
    prob_b={"in":{"h":0.6,"s":0.4},"s":{"s":0.4,"h":0.4,"fin":0.2 },"h":{"s":0.1,"h":0.6,"fin":0.3}}
    print("------問1-----")
    print(prob_a,"\n")

    print("------問2-----")
    like_a=get_likelihood(["s","s","h"],prob_a)
    like_b=get_likelihood(["s","s","h"],prob_b)
    print("尤度A: {0} , 尤度B: {1} , 答え* {2} \n".format(like_a,like_b,"a" if like_a>like_b else "b") )

    print("------問3-----")
    l=["s","s","s","h","h","h"]
    list3=list(set(permutations(l,3))) # 問3の全ての並びを列挙
    
    max_tmp=0
    ans3=[]
    for tmp in list3:
        print(tmp)
        tmp2=get_likelihood(list(tmp),prob_a,c_flag=True,digit='0.00001')
        if tmp2 > max_tmp : 
            ans3=list(tmp)
            max_tmp=tmp2
        print("尤度 :{} \n".format(tmp2))
    
    print("答え:{}\n".format(ans3))

    print("------問4-----")
    l=["s","s","s","h","h","h"]
    list4=list(set(permutations(l,3))) # 問3と同じく全ての並びを列挙
    max_tmp=0
    ans4=[]
    for tmp in list4:
        if (tmp[0]==id[1]) and( tmp[2]==id[2]):
            print(tmp)
            tmp=list(tmp)
            tmp2=get_likelihood(list(tmp),prob_b,c_flag=True,digit='0.00001')
        
            if tmp2 > max_tmp : 
                ans3=list(tmp)
                max_tmp=tmp2
            print("尤度 :{} \n".format(tmp2))
    
    print("答え:{}\n".format(ans3))


def main():
    # l=["s","s","s","h","h","h"]
    # list3=list(set(permutations(l,3))) # 問3の全ての並びを列挙
    # for tmp in list3:
    #     print("----------------------------\n",tmp)
    #     start(tmp)
    start(['s','h','s'])



if __name__ == "__main__":
    main()