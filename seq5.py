import numpy as np

class Perceptron:
    def __init__(self,n):
        #遷移確率，排出確率,大文字確率
        self.t_weight,self.e_weight,self.c_weight=self._generate_weight(n)

        
    
    def _generate_weight(self,n):
        trans_wegiht={}
        trans_wegiht['s']={'A':(n[0]+9)/20 ,'V':(n[1]+10)/20 ,'N':(n[2]+11)/20 }
        trans_wegiht['A']={'N':(n[0]+n[1])/ 20, 'V': (n[1]+n[2])/20}
        trans_wegiht['V']={'N':(n[0]+n[2])/ 20, 'V': (n[0]+4)/20 ,'e': (n[1]+n[2])/20}
        trans_wegiht['N']={'N':(n[1]+5)/ 20, 'V': (n[2]+6)/20 ,'e': (n[0]+1)/20}
        emission_weight={}
        caps_weight={}

        

        return trans_wegiht,emission_weight,caps_weight
    
    #パスの形成
    def _make_path(self,depth):
        dep=depth-1
        path=['e']
        while path[-1] != 's':
            path.append(self.t_prob[dep][path[-1]][1])
            dep -=1
        path.reverse()
        
        self.path=path


    def viterbi(self,roots):
        #最大の尤度とその尤度のための親ノード
        self.t_prob=[]
        self.t_prob.append({'s':[1,'non']})
        # {0:{'s':[1,'']}}

        #初めのノードは一つだと仮定
        before=roots[0][0]

        #'i'が木の深さ
        #'before' が矢印の出るノード，'after'が矢印の向かうノード
        for i in range(len(roots)-1):
            self.t_prob.append({})
            for after in roots[i+1]:
                for before in roots[i]:
                    #初めて訪れるノードなら，辞書に確率を作成．
                    if not(after in self.t_prob[i+1] ):
                        self.t_prob[i+1][after]=[self.t_prob[i][before][0] * self.t_weight[before][after] , before]
                    #以前の経路より起こりやすかったら，確率を更新
                    elif  self.t_prob[i][before][0] * self.t_weight[before][after] >= self.t_prob[i+1][after][0]:
                        # print("i:{} before:{} after:{}".format(i,before,after))
                        self.t_prob[i+1][after]=[self.t_prob[i][before][0] * self.t_weight[before][after] , before]
        
        self._make_path(len(roots))
    


    
    #sentenceは[[x_1,y_1],[x_2,y_2]・・・・]のタプルのリストを想定する．xが潜在変数(PoSタグ)で，yが観測変数(word)
    def update(self,sentence):

        for i in range(len(self.path)):
            if i==len(sentence)-1:
                break
            if (sentence[i+1][0] != self.path[i+1]) or (sentence[i][0] != self.path[i]):
                
                self.t_weight[self.path[i]][self.path[i+1]] -= 1
                self.t_weight[sentence[i][0]][sentence[i+1][0]] -= 1

            



def main():
    flag=True
    STUDENT_ID = "2011039"  #input("please, input a your id:")
    print("Your ID is {}".format(STUDENT_ID))

    # n1==n[0] ・・・
    n = list([int(sid) for sid in STUDENT_ID[-3:]])
    n.reverse()
    print("n:",n)

    roots=[['s'],['A','V','N'],['N','V'],['e']]
    for i in range(1):
        print(i,"回目")
        per=Perceptron(n)
        per.viterbi(roots)
        print("path: ",per.path)
        if flag :
            print("=====================問1=====================")
            print("1-1:{}, 1-2:{}, 1-3:{}".format(per.t_weight['s']['A'],per.t_weight['s']['V'],per.t_weight['s']['N']))
            print("1-4:{}, 1-5:{}, 1-6:{}, 1-7:{}, 1-8:{}, 1-9:{}".format(per.t_weight['A']['N'],per.t_weight['A']['V'], \
            per.t_weight['V']['N'],per.t_weight['V']['V'],per.t_weight['N']['N'],per.t_weight['N']['V']))
            print("1-10:{}, 1-11:{}\n".format(per.t_weight['N']['e'],per.t_weight['V']['e']))
        sentence=[("s",""),("A","Blue"),("N","leaves"),("e","")]
        per.update(sentence)
       
    
    
    
    
  

    if flag:

        
        

        print("=====================問2=====================")
        print("2-1:{}, 2-2:{}, 2-3:{}".format(per.t_prob[1]['A'][0],per.t_prob[1]['V'][0],per.t_prob[1]['N'][0]))
        print("2-4:{}, 2-5:{}".format(per.t_prob[2]['N'][0],per.t_prob[2]['V'][0]))
        print("2-6:{}\n".format(per.t_prob[3]['e'][0]))

        print("=====================問3=====================")
        print("3-1:{}, 3-2:{}, 3-3:{}".format(per.t_weight['s']['A'],per.t_weight['s']['V'],per.t_weight['s']['N']))
        print("3-4:{}, 3-5:{}, 3-6:{}, 3-7:{}, 3-8:{}, 3-9:{}".format(per.t_weight['A']['N'],per.t_weight['A']['V'], \
        per.t_weight['V']['N'],per.t_weight['V']['V'],per.t_weight['N']['N'],per.t_weight['N']['V']))
        print("3-10:{}, 3-11:{}\n".format(per.t_weight['N']['e'],per.t_weight['V']['e']))
    
    print("path: ",per.path)
    print("weight: ",per.t_prob)

        
    


if __name__=='__main__':
    main()