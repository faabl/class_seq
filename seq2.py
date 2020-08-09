from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN #四捨五入用
from itertools import permutations 

import numpy as np 

def make_prob(n1,n2,n3,flag=False):
    t_prob={} #transition probabilty
    e_prob={} #emission probability
    
    t_prob['in']={'M':n1/10,'F':(10-n1)/10}
    e_prob['M']={'H':n3/10,'S':(10-n3)/10}
    e_prob['F']={'H':n2/10,'S':(10-n2)/10}
    t_prob['M']={'M':(2+n3)/20,'F':n1/20,'fin':(18-n1-n3)/20}
    t_prob['F']={'F':(n1+n2)/20 ,'M':(10-n1)/20,'fin':(10-n2)/20}


    print('==========問1=========')
    if(flag==True):
        print('[1-1 : {0}, 1-2 : {1} ]'.format(t_prob['in']['M'],t_prob['in']['F']))
        print('[1-3 : {0}, 1-4 : {1} ]'.format(e_prob['M']['H'],e_prob['M']['S']))
        print('[1-5 : {0}, 1-6 : {1} ]'.format(e_prob['F']['H'],e_prob['F']['S']))
        print('[1-7 : {0}, 1-8 : {1}, 1-9 : {2} ]'.format(t_prob['M']['M'],t_prob['M']['F'],t_prob['M']['fin']))
        print('[1-10 : {0}, 1-11 : {1}, 1-12 : {2} ]\n'.format(t_prob['F']['F'],t_prob['F']['M'],t_prob['F']['fin']))
    else:
        
        print('遷移確率:',t_prob)
        print("排出確率:",e_prob)
    print('\n')

    return t_prob,e_prob

#全ての入力パスを考慮した上で排出を考える
# def viterbi(t_prob,e_prob,flag = False):
#     prob={'x1':{'M':0,'F':0},'x2':{'M':0,'F':0},'x3':{'M':0,'F':0},'fin':0}
#     afters=['x2','x3'] #　in と fin だけ別処理
#     before='x1'
#     prob['x1']['M'] = t_prob['in']['M']
#     prob['x1']['F'] = t_prob['in']['F']
#     #遷移行列でも書けるね
#     for after in afters:
#         prob[after]['M']=t_prob['M']['M']*prob[before]['M'] + t_prob['F']['M'] * prob[before]['F']
#         prob[after]['F']= t_prob['M']['F']*prob[before]['M'] + t_prob['F']['F'] * prob[before]['F']

#         before=after
    
#     prob['fin']= t_prob['M']['fin']*prob[before]['M'] + t_prob['F']['fin'] * prob[before]['F']

    
#     if(e_prob['M']['H']>e_prob['M']['S']):
#         mother_p=e_prob['M']['H']
#         mother_e='H'
#     else:
#         mother_p=e_prob['M']['S']
#         mother_e='S'
    
#     if(e_prob['F']['H']>e_prob['F']['S']):
#         father_p=e_prob['F']['H']
#         father_e='H'
#     else:
#         father_p=e_prob['F']['S']
#         father_e='S'

# #2-1~2-7まで
#     afters=['x1','x2','x3']
#     ans={'x1':{},'x2':{},'x3':{}}
#     for after in afters:
#         m_tmp=mother_p*prob[after]['M']
#         f_tmp=father_p*prob[after]['F']
#         ans[after]['M']=m_tmp
#         ans[after]['F']=f_tmp
#     ans['fin']=prob['fin']

#     for key1 in ans:
#         if type(ans[key1]) == dict:
#             for key2 in ans[key1]:
#                 ans[key1][key2]=float(Decimal(ans[key1][key2]).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)) 
#         else :
#             ans[key1]=float(Decimal(ans[key1]).quantize(Decimal('0.001'), rounding=ROUND_HALF_UP)) 
#     seq=[]
#     # afters.reverse()
#     # seq.append('fin')
#     seq.append('start')
#     for tmp in afters:
#         if ans[tmp]['M']>ans[tmp]['F']:
#             seq.append({'M':mother_e})
#         else:
#             seq.append({'F':father_e})
#     seq.append('fin')

        

#     print("==========問2=========")
#     if(flag==True):
#         print('各確率(2-1~2-7):',ans)
#         # print('latent確率:',prob)
#         print('系列:',seq)
#         print('\n')


#直前の確率で高い方を選択する場合．
# def viterbi(t_prob,e_prob,flag = False):
#     #独立事象なので先に計算
#     if(e_prob['M']['H']>e_prob['M']['S']):
#         mother_p=e_prob['M']['H']
#         mother_e='H'
#     else:
#         mother_p=e_prob['M']['S']
#         mother_e='S'
    
#     if(e_prob['F']['H']>e_prob['F']['S']):
#         father_p=e_prob['F']['H']
#         father_e='H'
#     else:
#         father_p=e_prob['F']['S']
#         father_e='S'
    
#     prob={'x1':{'M':0,'F':0},'x2':{'M':0,'F':0},'x3':{'M':0,'F':0},'fin':0}
#     afters=['x2','x3'] #　in と fin だけ別処理
#     before='x1'
#     prob['x1']['M'] = t_prob['in']['M']
#     prob['x1']['F'] = t_prob['in']['F']
#     seq_matrix={'x1':{'F':'in','M':'in'},'x2':{},'x3':{},'fin':{}}
#     #遷移行列でも書けるね
#     for after in afters:
#         # prob[after]['M']=t_prob['M']['M']*prob[before]['M'] + t_prob['F']['M'] * prob[before]['F']
        
        
#         if t_prob['M']['M']*prob[before]['M'] >= t_prob['F']['M']*prob[before]['F']:
#             prob[after]['M']=t_prob['M']['M']*prob[before]['M']
#             seq_matrix[after]['M']='M'
#         else:
#             prob[after]['M']=t_prob['F']['M'] * prob[before]['F']
#             seq_matrix[after]['M']='F'





#         # prob[after]['F']= t_prob['M']['F']*prob[before]['M'] + t_prob['F']['F'] * prob[before]['F']
#         # prob[after]['F']= t_prob['M']['F']*prob[before]['M'] if t_prob['M']['F']*prob[before]['M'] >= t_prob['F']['F'] * prob[before]['F'] else t_prob['F']['F'] * prob[before]['F']
#         if t_prob['M']['F']*prob[before]['M'] >= t_prob['F']['F']*prob[before]['F']:
#             prob[after]['F']=t_prob['M']['F']*prob[before]['M']
#             seq_matrix[after]['F']='M'
#         else:
#             prob[after]['F']=t_prob['F']['F'] * prob[before]['F']
#             seq_matrix[after]['F']='F'
#         before=after
    
#     # prob['fin']= t_prob['M']['fin']*prob[before]['M'] if t_prob['M']['fin']*prob[before]['M']>t_prob['F']['fin'] * prob[before]['F'] else t_prob['F']['fin'] * prob[before]['F']
#     if t_prob['M']['fin']*prob[before]['M']>t_prob['F']['fin'] * prob[before]['F'] :
#         prob['fin']=t_prob['M']['fin']*prob[before]['M']
#         seq_matrix['fin']='M'
#     else:
#         prob['fin']=t_prob['F']['fin']*prob[before]['F']
#         seq_matrix['fin']='F'

    
    

#     #2-1~2-7まで
#     afters=['x1','x2','x3']
#     ans={'x1':{},'x2':{},'x3':{}}
#     for after in afters:
#         m_tmp=mother_p*prob[after]['M']
#         f_tmp=father_p*prob[after]['F']
#         ans[after]['M']=m_tmp
#         ans[after]['F']=f_tmp
#     ans['fin']=prob['fin']

#     for key1 in ans:
#         if type(ans[key1]) == dict:
#             for key2 in ans[key1]:
#                 ans[key1][key2]=float(Decimal(ans[key1][key2]).quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)) 
#         else :
#             ans[key1]=float(Decimal(ans[key1]).quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)) 
#     # seq=['fin',seq_matrix['fin']]
#     # afters=['x3','x2']
#     # for after in afters:
#     #     tmp = seq[len(seq)-1]
#     #     seq.append(seq_matrix[after][tmp])
#     # seq.append('in')
#     # seq.reverse()

#     seq=[]
#     seq.append('start')
#     afters=['x1','x2','x3']
#     for tmp in afters:
#         if ans[tmp]['M']>ans[tmp]['F']:
#             seq.append({'M':mother_e})
#         else:
#             seq.append({'F':father_e})
#     seq.append('fin')

        

#     print("==========問2=========")
#     if(flag==True):
#         print('各確率(2-1~2-7):',ans)
#         # print('latent確率:',prob)
#         print('系列:',seq)
#         print('M_emo:{} F_emo{}'.format(mother_e,father_e))
#         print('\n')

def viterbi(t_prob,e_prob,flag = False):
    #独立事象なので先に計算
    if(e_prob['M']['H']>e_prob['M']['S']):
        mother_p=e_prob['M']['H']
        mother_e='H'
    else:
        mother_p=e_prob['M']['S']
        mother_e='S'
    
    if(e_prob['F']['H']>e_prob['F']['S']):
        father_p=e_prob['F']['H']
        father_e='H'
    else:
        father_p=e_prob['F']['S']
        father_e='S'
    
    prob={'x1':{'M':0,'F':0},'x2':{'M':0,'F':0},'x3':{'M':0,'F':0},'fin':0}
    afters=['x2','x3'] #　in と fin だけ別処理
    before='x1'
    prob['x1']['M'] = t_prob['in']['M']*mother_p
    prob['x1']['F'] = t_prob['in']['F']*father_p
    seq_matrix={'x1':{'F':'in','M':'in'},'x2':{},'x3':{},'fin':{}}
    #遷移行列でも書けるね
    for after in afters:
        # prob[after]['M']=t_prob['M']['M']*prob[before]['M'] + t_prob['F']['M'] * prob[before]['F']
        
        
        if t_prob['M']['M']*prob[before]['M'] >= t_prob['F']['M']*prob[before]['F']:
            prob[after]['M']=t_prob['M']['M']*prob[before]['M']*mother_p
            seq_matrix[after]['M']='M'
        else:
            prob[after]['M']=t_prob['F']['M'] * prob[before]['F']*mother_p
            
            seq_matrix[after]['M']='F'



        # prob[after]['F']= t_prob['M']['F']*prob[before]['M'] + t_prob['F']['F'] * prob[before]['F']
        # prob[after]['F']= t_prob['M']['F']*prob[before]['M'] if t_prob['M']['F']*prob[before]['M'] >= t_prob['F']['F'] * prob[before]['F'] else t_prob['F']['F'] * prob[before]['F']
        if t_prob['M']['F']*prob[before]['M'] >= t_prob['F']['F']*prob[before]['F']:
            prob[after]['F']=t_prob['M']['F']*prob[before]['M']*father_p
            seq_matrix[after]['F']='M'
        else:
            prob[after]['F']=t_prob['F']['F'] * prob[before]['F']*father_p
            seq_matrix[after]['F']='F'
        before=after
    
    # prob['fin']= t_prob['M']['fin']*prob[before]['M'] if t_prob['M']['fin']*prob[before]['M']>t_prob['F']['fin'] * prob[before]['F'] else t_prob['F']['fin'] * prob[before]['F']
    if t_prob['M']['fin']*prob[before]['M']>t_prob['F']['fin'] * prob[before]['F'] :
        prob['fin']=t_prob['M']['fin']*prob[before]['M']
        seq_matrix['fin']='M'
    else:
        prob['fin']=t_prob['F']['fin']*prob[before]['F']
        seq_matrix['fin']='F'

    
    

    #2-1~2-7まで
    afters=['x1','x2','x3']
    ans={'x1':{},'x2':{},'x3':{}}
    for after in afters:
        m_tmp=prob[after]['M']
        f_tmp=prob[after]['F']
        ans[after]['M']=m_tmp
        ans[after]['F']=f_tmp
    ans['fin']=prob['fin']

    for key1 in ans:
        if type(ans[key1]) == dict:
            for key2 in ans[key1]:
                ans[key1][key2]=float(Decimal(ans[key1][key2]).quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)) 
        else :
            ans[key1]=float(Decimal(ans[key1]).quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP)) 
    # seq=['fin',seq_matrix['fin']]
    # afters=['x3','x2']
    # for after in afters:
    #     tmp = seq[len(seq)-1]
    #     seq.append(seq_matrix[after][tmp])
    # seq.append('in')
    # seq.reverse()

    seq=[]
    seq.append('start')
    afters=['x1','x2','x3']
    for tmp in afters:
        if ans[tmp]['M']>ans[tmp]['F']:
            seq.append({'M':mother_e})
        else:
            seq.append({'F':father_e})
    seq.append('fin')

        

    print("==========問2=========")
    if(flag==True):
        print('各確率(2-1~2-7):',ans)
        # print('latent確率:',prob)
        print('系列:',seq)
        print('M_emo:{} F_emo:{}'.format(mother_e,father_e))
        print('\n')



#digit　はテキスト
def round_number(num,digit):
    return  float(Decimal(num).quantize(Decimal(digit), rounding=ROUND_HALF_UP))

#二重辞書を想定
def round_dict(dic,digit):
    for key in dic:
        if(type(dic[key]) == dict):
            for key2 in dic[key]:
                dic[key][key2]=round_number(dic[key][key2],"0.00001")
        else :
            dic[key]=round_number(dic[key],"0.00001")
    

    #o_argは観測変数の引数．つまり，観測データ
def make_forward(t_prob,e_prob,o_arg,flag=False):
    prob={'x1':{'M':0,'F':0},'x2':{'M':0,'F':0},'x3':{'M':0,'F':0},'fin':0}
    afters=['x2','x3'] #　in と fin だけ別処理
    before='x1'
    #====遷移確率計算======
    prob['x1']['M'] = t_prob['in']['M'] *e_prob['M'][o_arg['x1']] 
    # prob['x1']['M']=float(Decimal(prob['x1']['M']).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))
    prob['x1']['F'] = t_prob['in']['F'] *e_prob['F'][o_arg['x1']]
    # prob['x1']['F']=float(Decimal(prob['x1']['F']).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))
    #遷移行列でも書けるね
    for after in afters:
        prob[after]['M']=(t_prob['M']['M']*prob[before]['M'] + t_prob['F']['M'] * prob[before]['F'])*e_prob['M'][o_arg[after]]
        # prob[after]['M']=float(Decimal(prob[after]['M']).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))
        prob[after]['F']= (t_prob['M']['F']*prob[before]['M'] + t_prob['F']['F'] * prob[before]['F'])*e_prob['F'][o_arg[after]]
        # prob[after]['F']=float(Decimal(prob[after]['F']).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))

        before=after
    
    prob['fin']= t_prob['M']['fin']*prob[before]['M'] + t_prob['F']['fin'] * prob[before]['F']
    # prob['fin']=float(Decimal(prob['fin']).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))

    #四捨五入
    round_dict(prob,"0.00001")
    
    #======終了========
    #====以下表示======
    if(flag==True):
        print("==========問3=========")
        print("3-1 ~ 3-7: ",prob)
        print("3-8 : ",prob['fin'])
        print("3-9 : ",prob['x2']['M'])
        print("3-10 : ",prob['x2']['F'])
    
    return prob

def make_backward(t_prob,e_prob,o_arg,flag=False):
    prob={'in':0,'x1':{'M':0,'F':0},'x2':{'M':0,'F':0},'x3':{'M':0,'F':0}}
    afters=['x2','x1'] #　in と fin だけ別処理
    before='x3'
     #====遷移確率計算======
    prob['x3']['M'] = t_prob['M']['fin'] 
    # prob['x3']['M']=float(Decimal(prob['x3']['M']).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))
    prob['x3']['F'] = t_prob['F']['fin'] 
    # prob['x3']['F']=float(Decimal(prob['x3']['F']).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))
    #遷移行列でも書けるね
    for after in afters:
        prob[after]['M']=(t_prob['M']['M']*prob[before]['M']*e_prob['M'][o_arg[before]] + t_prob['M']['F'] * prob[before]['F']*e_prob['F'][o_arg[before]])
        # prob[after]['M']=float(Decimal(prob[after]['M']).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))
        prob[after]['F']= (t_prob['F']['M']*prob[before]['M']*e_prob['M'][o_arg[before]] + t_prob['F']['F'] * prob[before]['F']*e_prob['F'][o_arg[before]])
        # prob[after]['F']=float(Decimal(prob[after]['F']).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))

        before=after
    
    prob['in']= t_prob['in']['M']*prob[before]['M']*e_prob['M'][o_arg[before]] + t_prob['in']['F'] * prob[before]['F']*e_prob['F'][o_arg[before]]

    #四捨五入
    round_dict(prob,"0.00001")
    # prob['in']=float(Decimal(prob['in']).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))

    
    
    #======終了========
    #====以下表示======

    if(flag==True):
        print("==========問4=========")
        print("4-1 ~ 4-7: ",prob)
        print("4-8 : ",prob['in'])
        print("4-9 : ",prob['x2']['M'])
        print("4-10 : ",prob['x2']['F'])
    
    return prob



def q5(f_prob,b_prob,flag=False):
    ans=[]
    #5-1
    ans.append(f_prob['x2']['M']*b_prob['x2']['M'])
    #5-2
    ans.append(f_prob['x2']['F']*b_prob['x2']['F'] )
    #5-3
    ans.append(ans[0]/(ans[0]+ans[1]))

    for index,tmp in enumerate(ans):
        ans[index]=round_number(tmp,"0.000001")



    #=======以下表示========
    if(flag==True):
        print("==========問5=========")
        print("5-1: {}".format(ans[0]))
        print("5-2: {}".format(ans[1]))
        print("5-3: {}".format(ans[2]))



def main():
    x=[9,3,0]
    
    #問1
    t_prob,e_prob=make_prob(x[0],x[1],x[2],True)
    
    #問2
    viterbi(t_prob,e_prob,True)

    #問3,4で使う入力
    input_3={'x1':'S','x2':'S','x3':'H'}

    #問3
    f_prob=make_forward(t_prob,e_prob,input_3,True)

    #問4
    b_prob=make_backward(t_prob,e_prob,input_3,True)

    #問5
    q5(f_prob,b_prob,True)

    # print(t_prob['in']['M'])

    # print(t_prob)
    # print(e_prob)

if __name__=='__main__':
    main()
    