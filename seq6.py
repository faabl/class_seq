import numpy as np
import copy

#https://ahcweb01.naist.jp/lecture/2014/sdm/sdm-20140729.pdf
#コメントアウトしてる方はこのP21の例の確認用．
# '#'で囲ってる箇所はスライドの上記の例を確認するときに，コメントアウトを解除し，
# 同じ名前のもの(下にあるやつ)とpath_scoreをコメントアウト
class Perceptron:
    def __init__(self,n):
        #スライドの例を用いた確認用
        ##############################################
        # self.nodes=[['s'],['N','V'],['N','V'],['e']]
         ##############################################
        self.nodes=[['s'],['A','V','N'],['N','V'],['e']]
        
        #遷移確率，排出確率,大文字確率
        self.t_weight,self.e_weight,self.c_weight=self._generate_weight(n)
        self.t_w_history=[]
        tmp=copy.deepcopy(self.t_weight)
        self.t_w_history.append(tmp)
        #前向きスコア(α)と，後ろ向きスコア(β)出した後，確率化
        self.prob=self._make_prob()
        
        #スライドの時は削除
         ##############################################
        self.path_score = self._make_path_score()
         ##############################################
        


                
    
    def _make_prob(self):
        alpha=self._make_forward_score()
        beta=self._make_backward_score()
        #前向きスコアと後ろ向きスコアが同じになる必要がある．
        # print(alpha)
        # print(beta)
        path_score=[]
        prob=[]
        for i in range(len(self.nodes)-1):
            prob.append({})
            path_score.append({})
            node_sum=0
            for key1 in self.nodes[i]:
                prob[i][key1]={}
                path_score[i][key1]={}
                for key2 in self.nodes[i+1]:
                    prob[i][key1][key2]=alpha[i][key1]*beta[i+1][key2]*np.exp(self.t_weight[key1][key2])*np.exp(self.e_weight[i+1][key2])
                    path_score[i][key1][key2] = prob[i][key1][key2]
                    # if (key1=='s') and(key2=='N'):
                    #     print("s , N ,{} {} {}".format(alpha[i][key1],beta[i+1][key2],self.t_weight[key1][key2]))
                    
                    node_sum+=prob[i][key1][key2]
            
            for key1 in self.nodes[i]:
                for key2 in self.nodes[i+1]:
                    prob[i][key1][key2]/=node_sum

       
        # print(prob) 
        return prob


        

    #前向きスコアの計算
    #alpha[i][k]とあれば，深さi+1のノード'k'の前向きスコア
    def _make_forward_score(self):
        alpha=[]
        alpha.append({'s': 1})
        for i in range(len(self.nodes)-1):
            alpha.append({})
            
            if not(i+1 in self.e_weight):
                        self.e_weight[i+1]={}
            for after in self.nodes[i+1]:
                tmp=0
                for before in self.nodes[i]:
                    if not(after in self.t_weight[before]):
                        self.t_weight[before][after]=0
                    if not(after in self.e_weight[i+1]):
                        self.e_weight[i+1][after]=0
                    

                    tmp+=alpha[i][before]*np.exp(self.t_weight[before][after]+self.e_weight[i+1][after])
                    # print("{} {} {}".format(before,after,np.exp(self.t_weight[before][after]+self.e_weight[i+1][after])))
                    
                       
                    
                alpha[i+1][after]=tmp
                # print("i:{} ,after:{} ,alpha:{}".format(i+1,after,tmp))
        print(alpha[-1])
        return alpha

    #後ろ向きスコアの計算
    #リストの向きがややこしい
    def _make_backward_score(self):
        beta=[]
        beta.append({'e':1})
        back_nodes=list(reversed(self.nodes))
        for i in range(len(back_nodes)-1):
            beta.append({})
            for after in back_nodes[i+1]:
                tmp=0
                for before in back_nodes[i]:
                    if not(before in self.t_weight[after]):
                        self.t_weight[after][before]=0
                    if not(before in self.e_weight[len(back_nodes)-1 -i]):
                        self.e_weight[len(back_nodes)-1 -i][before]=0
                    tmp+=beta[i][before]*np.exp(self.t_weight[after][before]+self.e_weight[len(back_nodes)-1 -i][before])
                    # print("{} {} {} {}".format(before,after,np.exp(self.t_weight[after][before]+self.e_weight[len(back_nodes)-1 -i][before])\
                    # ,beta[i][before]))
                       
                beta[i+1][after]=tmp
        beta.reverse()
        return beta

    
            


    #スライド用
     ##############################################
    # def _generate_weight(self,n):
    #     trans_wegiht={}
    #     trans_wegiht['s']={'N':1}
    #     trans_wegiht['N']={}
    #     trans_wegiht['V']={'e':1}
    #     emission_weight={1:{'N':1}}
    #     caps_weight={}
    #     return trans_wegiht,emission_weight,caps_weight
     ##############################################

    def _generate_weight(self,n):
        trans_wegiht={}
        trans_wegiht['s']={'A':(n[0]+9)/20 ,'V':(n[1]+10)/20 ,'N':(n[2]+11)/20 }
        trans_wegiht['A']={'N':(n[0]+n[1])/ 20, 'V': (n[1]+n[2])/20}
        trans_wegiht['V']={'N':(n[0]+n[2])/ 20, 'V': (n[0]+4)/20 ,'e': (n[1]+n[2])/20}
        trans_wegiht['N']={'N':(n[1]+5)/ 20, 'V': (n[2]+6)/20 ,'e': (n[0]+1)/20}
        emission_weight={}
        caps_weight={}
        
        return trans_wegiht,emission_weight,caps_weight
    
    def _make_path_score(self):
        paths=[['A','N'],['A','V'],['V','N'],['V','V'],['N','N'],['N','V']]
        path_score={}
        for path in paths:
            

            path.insert(0,'s')
            path.append('e')
            tmp =0
            for i in range(len(path)-1):
                before = path[i]
                after = path[i+1]
                tmp += self.t_weight[before][after]

            if not(path[1] in path_score):
                path_score[path[1]]={}
            path_score[path[1]][path[2]] = tmp
        
        #以下確認
        #後ほど削除
        # tmp2=0
        # for tmp in paths:
        #     # print(tmp[1],tmp[2])
        #     path_score[tmp[1]][tmp[2]]=np.exp(path_score[tmp[1]][tmp[2]])
        #     tmp2+=path_score[tmp[1]][tmp[2]]
        
        # for tmp in paths:
        #     path_score[tmp[1]][tmp[2]]/=tmp2

        
        return path_score

    def update(self,sentence):
        for i in range(len(sentence)-1):
            for after in self.nodes[i+1]:
                for before in self.nodes[i]:

                    # 遷移確率の更新
                    phi=1 if (sentence[i][0]==before) and (sentence[i+1][0]==after) else 0
                    self.t_weight[before][after] += ( phi - self.prob[i][before][after])

                    #emissionの更新はやってないので
        
        tmp=copy.deepcopy(self.t_weight)
        self.t_w_history.append(tmp)
        






def main():
    flag=True
    STUDENT_ID = "2011238"  #input("please, input a your id:")
    print("Your ID is {}".format(STUDENT_ID))

    # n1==n[0] ・・・
    n = list([int(sid) for sid in STUDENT_ID[-3:]])
    n.reverse()
    print("n:",n)
    per=Perceptron(n)
    #スライド
     ##############################################
    # sentence=[['s',0],['N',1],['V',2],['e',0]]
     ##############################################
    sentence=[['s',0],['A',1],['N',2],['e',0]]

    per.update(sentence)
    # print(per.t_w_history[0])
    # print(per.t_w_history[1])
    # print(per.prob)

    # tmp=17/20+1-(np.exp(1)+1)/(np.exp(37/20) + np.exp(17/20) + 2*np.exp(9/20) +2)
    # print(tmp)
    

    if flag ==True:
        print("========================問1========================")
        print("1-1: {} ,1-2: {}, 1-3:{} ".format(per.t_w_history[0]['s']['A'] ,per.t_w_history[0]['s']['V'],\
        per.t_w_history[0]['s']['N'] ))
        print("1-4:{} ,1-5:{} ,1-6:{} ,1-7:{}".format(per.t_w_history[0]['A']['N'], per.t_w_history[0]['A']['V'],per.t_w_history[0]['V']['N'], \
        per.t_w_history[0]['V']['V']))
        print("1-8:{} ,1-9:{} ,1-10:{} ,1-11:{}\n".format(per.t_w_history[0]['N']['N'],per.t_w_history[0]['N']['V'],per.t_w_history[0]['N']['e'],\
            per.t_w_history[0]['V']['e']))
        print("1-12:{} ,1-13:{} ,1-14:{} ,1-15:{} ,1-16:{} ,1-17:{}".format(per.path_score['A']['N'],per.path_score['A']['V'],\
        per.path_score['V']['N'],per.path_score['V']['V'],per.path_score['N']['N'],per.path_score['N']['V'] ))
        
        print("========================問2========================")
        print("2-1:{} ,2-2:{} ,2-3:{} ".format(per.prob[1]['A']['N'],per.prob[1]['A']['V'],per.prob[1]['V']['N']))
        print("2-4:{} ,2-5:{} ,2-6:{}\n".format(per.prob[1]['V']['V'],per.prob[1]['N']['N'],per.prob[1]['N']['V']))

        print("========================問3========================")
        print("3-1:{} ,3-2:{} ,3-3:{}".format(per.prob[0]['s']['A'],per.prob[0]['s']['V'],per.prob[0]['s']['N']))
        print("3-4:{} ,3-5:{}\n".format(per.prob[2]['N']['e'],per.prob[2]['V']['e']))

        print("========================問4========================")
        print("4-1: {} ,4-2: {}, 4-3:{} ".format(per.t_w_history[1]['s']['A'] ,per.t_w_history[1]['s']['V'],\
        per.t_w_history[1]['s']['N'] ))
        print("4-4:{} ,4-5:{} ,4-6:{} ,4-7:{}".format(per.t_w_history[1]['A']['N'], per.t_w_history[1]['A']['V'],per.t_w_history[1]['V']['N'], \
        per.t_w_history[1]['V']['V']))
        print("4-8:{} ,4-9:{} ,4-10:{} ,4-11:{}\n".format(per.t_w_history[1]['N']['N'],per.t_w_history[1]['N']['V'],per.t_w_history[1]['N']['e'],\
            per.t_w_history[1]['V']['e']))




    



if __name__=='__main__':
    main()