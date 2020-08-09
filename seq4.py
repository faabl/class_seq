import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

class LinerDyanamicSysytem:
    def __init__(self,gamma,sigma):
        self.gamma = gamma
        self.sigma = sigma

        self.log_p_x_history = []
        self.cov6list=[]
        self.klist=[]#カルバックゲイン
        self.mu_history = []
        self.pred_mu_history = []
        self.p_history = []
        self.pred_p_history = []

    

    def fit(self,obs,mu,p,flag=False):
        self._filter(obs,mu,p,flag)
        
        
    def _filter(self,observations,mu,p,flag):
        _mu,_p=mu,p
        likelihood=0
        for i,obs in enumerate(observations):
            #1~4
            pred_mu,pred_p,log_p_x = self._predict(_mu,_p,obs)
            #7
            self.log_p_x_history.append(log_p_x)
            likelihood+=log_p_x
            #5=1
            #6
            self.cov6list.append(_p+self.sigma)

            #9,10=12,11=13
            _mu, _p = self._update(obs, pred_mu, pred_p)

            self.pred_mu_history.append(pred_mu)
            self.pred_p_history.append(pred_p)

            self.mu_history.append(_mu)
            self.p_history.append(_p)

            if flag:
                print("=================={}回目==============".format(i+1))
                print("1=3:",pred_mu)
                print("2=4:",pred_p,"\n")

                print("5:",pred_mu)
                print("6:",pred_p+self.sigma)
                print("7:",log_p_x)
                print("8:",likelihood,"\n")

                print("9:",self.klist[i])
                print("10=12:",_mu)
                print("11=13:",_p)
            
            else:
                print("Answer {}: ".format(i+1))
                if i > 0:
                    print("predicted p.d.f. of latent variable: mu = {:.3f}, sigma = {:.3f}, joint_prob. = {:.3f}"
                        .format(pred_mu, pred_p, np.sum(self.log_p_x_history)))

                print("log-scaled likelihood = {:.3f}, "
                    "updated p.d.f. of latent value: mu = {:.3f}, sigma = {:.3f}"
                    .format(log_p_x, _mu, _p))





    
    #遷移確率が1だからA=1.
    def _predict(self,mu,p,obs):
        pred_mu = mu
        pred_p = p+self.gamma
        
        log_p_x = norm.logpdf(x=obs, loc=pred_mu, scale=(pred_p + self.sigma))
        return pred_mu,pred_p,log_p_x
    
    #p68
    def _kalman_gain(self,p,sigma):
        return p/(p+sigma)
    
    #p68
    def _update(self, obs, mu, p):
        k = self._kalman_gain(p, self.sigma)

        self.klist.append(k)
        new_mu = mu + k * (obs - mu)
        new_p = (1 - k) * p
        return new_mu, new_p


    



def generation_obserbation(b):
    return 10*b+20




def main():
    STUDENT_ID = "2011121"  #input("please, input a your id:")
    print("Your ID is {}".format(STUDENT_ID))

    INIT_P=50
    INIT_MU=200
    INIT_SIGMA=10
    INIT_GAMMA=20

    # variable to calculate x_t
    b = np.array([int(sid) for sid in STUDENT_ID[-4:]])
    x=generation_obserbation(b)
    print("x1~x4:,",x,"\n")

    lds=LinerDyanamicSysytem(INIT_GAMMA,INIT_SIGMA)
    lds.fit(x,INIT_MU,INIT_P,True)




if __name__=="__main__":
    main()

#What is Kalman Smoothing? What is the difference with Kalman Filtering?
#Is there any relation with the Forward or Backward Algorithm? Please explain!

# カルマン平滑化は、時点tの平滑化分布(p(x_t | y_{1:T}) )を求める手法である．
# カルマンフィルターの場合，現在の状態z_tを過去のt-1までの状態を用いて推定し，その後，t+1を推定するような前向きアルゴリズムをおこなうが，
# 平滑化の場合，状態tを予測するのに，観測されいる全ての状態を用いてtを推定し，その後，t-1を推定するような後ろ向きアルゴリズムを行う違いがある．