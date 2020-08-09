from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN #四捨五入用
from numpy.linalg import inv

import numpy as np 



def make_input(n):
        x=[]
        x.append([n[2]+n[3],n[0]])
        x.append([n[3],n[1]+n[3]])
        x.append([n[1],n[0]+n[3]])
        x.append([n[0]+n[1],n[2]])
        x.append([n[1]+n[2],n[0]+n[2]])

        return np.array(x)



class FA:
    def __init__(self,W,mu,sigma):
        self.W=W.reshape(1,-1).T
        self.mu=mu
        self.sigma=sigma
    
    def fit(self,n):
        # q1
        self.mu,X=self._q1(n,True)
        #q2
        Z,ZZ_n=self._q2(X,True)

        #q3
        XX,ZZ,XZ=self._q3(X,Z,ZZ_n,True)

        #q4
        W2,sigma2=self._q4(X.shape[0],XX,ZZ,XZ,True)

        #q5
        self._q5(W2,sigma2,True)






        


    def _q1(self,n,flag=False):
        x=make_input(n)
        
        mu,x2=self._update_input(x)

        if(flag==True):
            print("=================問1=================")
            
            print("1-1~1-10 \n",x,"\n")
            print("mean \n",mu,"\n")
            print("1-13~1-22 \n",x2,"\n")
        return mu,x2
    
    # P67
    def _q2(self,X,flag=False):
        ans2_1=self._calc_cov_of_Z()
        Z=ans2_1 @  self.W.T @ inv(self.sigma) 
        
        Z=Z@X.T
        print(Z.shape)
        ZZ= self._calc_ZZ(Z)
        if(flag==True):
            print("=================問2=================")
            print("2-1 : {} \n".format(ans2_1))
            print("Z 2-2~2-6 :  \n",Z,"\n")
            print("ZZ 2-7~2-11 :  \n",ZZ,"\n")
        return Z,ZZ

    def _q3(self,X,Z,ZZ_n,flag=False):
        XX=self._diag(X.T@X)
        ZZ=ZZ_n.sum()
        
        XZ=X.T@Z.T

        if(flag ==True):
            print("=================問3=================")
            print("3-1 : {} \n".format(X.shape[0]))
            print("<XX> 3-2~3-5:  \n",XX,"\n")
            print("<ZZ>  3-6:",ZZ)
           
            print("<XZ>3-7,3-8 : ",XZ)
        
        return XX,ZZ,XZ

    def _q4(self,N,XX,ZZ,XZ,flag=False):
        #W2=W^
        W2=XZ /ZZ
        
        sigma2=1/N*(self._diag(XX-XZ@W2.T))
        if flag==True:
            print("=================問4=================")
            print("4-1,4-2 :\n",XZ)
            print("4-3 ",ZZ)
            print("4-4,4-5:",W2)
            print("4-6 ~ 4-9:\n",XX)
            print("4-10.4-11:\n",XZ)
            print("4-12,4-13:\n",W2)
            print("4-14~4-17:\n",sigma2)

        return W2,sigma2
    
    def _q5(self,W2,sigma2,flag=False):
        before_cov = self.W @self.W.T + self.sigma
        after_cov = W2 @ W2.T + sigma2

        if flag==True:
            print("=================問5=================")
            print("----before----")
            print("5-1,5-2:\n",self.W )
            print("5-3,5-4:\n",self.W.T)
            print("5-5~5-8: \n",self.sigma)
            print("5-9~5-12: \n",before_cov,"\n")
            
            print("----after----")
            print("5-13,5-14:\n",W2)
            print("5-15,5-16:\n",W2.T)
            print("5-17~5-20:\n",sigma2)
            print("5-21~5-24:\n",after_cov)

        








    

    def _update_input(self,x):
        mu=np.mean(x,axis=0)
        x2=x-mu
        
        return mu,x2
    
    
    def _calc_cov_of_Z(self):
        i_size=self.W.shape[1]
        ans=inv(self.W.T @ inv(self.sigma) @self.W + np.eye(i_size))
        return ans
    
    def _calc_ZZ(self,Z):
        return np.multiply(Z, Z) + self._calc_cov_of_Z()
    
    def _diag(self,A):
        return np.diag(np.diag(A))






    



def  main():
    n=[9,3,0,1]
    print("n0: {} ,n1: {} ,n2: {} ,n3: {}".format(n[0],n[1],n[2],n[3]))
    
    INIT_W = np.array([1, 0], dtype=np.float)
    INIT_MU = np.array([0, 0], dtype=np.float)
    INIT_SIGMA = np.matrix([[1, 0], [0, 1]], dtype=np.float)


    # print("initialized value...: X = {}, W = {}, μ = {}, Σ = {}"
    #   .format(INPUT_X, INIT_W, INIT_MU, INIT_SIGMA))

    


    # STUDENT_ID = "2011039"
    # print("Your ID is {}".format(STUDENT_ID))

    # n_3, n_2, n_1, n_0 = [int(sid) for sid in STUDENT_ID[-4:]]
    # print("n_0 = {}, n_1 = {}, n_2 = {}, n_3 = {}".format(n_0, n_1, n_2, n_3))

    # x_1 = [n_0,       n_2 + n_3], dtype=np.float)
    # x_2 = [n_1 + n_3, n_3],       dtype=np.float)
    # x_3 = [n_0 + n_3, n_1],       dtype=np.float)
    # x_4 = [n_2,       n_0 + n_1], dtype=np.float)
    # x_5 = [n_0 + n_2, n_1 + n_2], dtype=np.float)
    # print("x_1 = {}, x_2 = {}, x_3 = {}, x_4 = {}, x_5 = {}"
    #     .format(x_1, x_2, x_3, x_4, x_5))

    # INPUT_X = np.vstack((x_1, x_2, x_3, x_4, x_5))
    # print(type(INPUT_X))
    

    fac_model = FA(INIT_W, INIT_MU, INIT_SIGMA)
    fac_model.fit(n)

    
    

if __name__=='__main__':
    main()