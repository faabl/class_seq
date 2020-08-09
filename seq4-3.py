import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


class LinearDynamicSystem:
    def __init__(self, gamma, sigma, A, W):
        self.gamma = gamma
        self.sigma = sigma
        self.A = A
        self.W = W
    
        self.log_p_x_history = []
        self.pred_mu_history = []
        self.mu_history = []
        self.pred_mu_history = []
        self.p_history = []
        self.pred_p_history = []

    def fit(self, observations, mu, p):
        #self._filter(observations, mu, p)
        i=1
        for i in range(4):
            mu,p=self._calc(observations,mu,p,i+1)

    def _calc(self,observations,mu,p,i):
        pred_mu=self._pred_mean(mu)
        pred_p=self._pred_covariance(p)
       
        print("\n Answer {}:".format(i))
        print("Predicted mean: mu_{}|{} = {}".format(i,i-1,pred_mu))
        print("Predicted covariance: P_{}|{} = {}".format(i,i-1,pred_p))
        print("p(z_{}) = p(z_{}|x_{}) = N(z_{};{},{}) \n".format(i,i,i-1,i,pred_mu,pred_p))
        
        Mean=self._Mean(pred_mu)
        Covariance=self._Covariance(pred_p)
        ln_p=self._predict(Mean, Covariance, observations[i-1])
        
        print("Mean: Wmu{}|{} = {}".format(i,i-1,Mean))
        print("Covariance: WP_{}|{}W^T+sigma = {}".format(i,i-1,Covariance))
        print("lnp(x_{}) = {}".format(i,ln_p))
        print("")
        print()
        K=self._Kalman_gain_matrix(pred_p)
        up_mu=self._Update_mu(pred_mu,K,observations[i-1])
        up_p=self._Update_p(K,pred_p)
        print("kalman gain matrix: K_{} = {}".format(i,K))
        print("Updated mean: mu_{} = {}".format(i,up_mu))
        print("Update covariance: P_{} = {}".format(i,up_p))
        print("p(z_{}|x_{}) = N(z_{};{},{})".format(i,i,i,up_mu,up_p))

        return up_mu,up_p

    def _pred_mean(self, mu):
        return self.A*mu
            
    def _pred_covariance(self, p):
        return self.A*p*self.A+self.gamma
              
    def _Mean(self, mu):
        return self.W*mu
              
    def _Covariance(self, p):
        tmp=self.W*p*self.W+self.sigma
        print("===========================")
        print("wagi",p," ",tmp)
        return tmp

    def _predict(self, mu, p, obs):
        
        log_p_x = norm.logpdf(x=obs, loc=mu, scale=(p + self.sigma))
        return log_p_x
    
    def _Kalman_gain_matrix(self, p):
        return p*self.W/(self.W*p*self.W+self.sigma)
    

    def _kalman_gain(self, p, s):
        return p / (p + s)

    def _Update_mu(self, mu, K, x):
        return mu + K*(x-self.W*mu)

    def _Update_p(self, K, p):
        return (1-K*self.W)*p
    

def generate_observation(b):
    return 10 * b + 20


STUDENT_ID =  "2011121"#input("please, input a your id:")
print("Your ID is {}".format(STUDENT_ID))

b_1, b_2, b_3, b_4 = [int(sid) for sid in STUDENT_ID[-4:]]
print("b_1 = {}, b_2 = {}, b_3 = {}, b_4 = {}".format(b_1, b_2, b_3, b_4))

INPUT_X = np.array([generate_observation(b) for b in [b_1, b_2, b_3, b_4]])
INIT_P = 50
INIT_MU = 200
INIT_GAMMA = 20
INIT_SIGMA = 10
INIT_A=1
INIT_W=1

print("initialized value...: A = {}, W = {}, X = {}, P_0 = {}, μ_0 = {}, Γ = {}, Σ = {}"
      .format(INIT_A,INIT_W,INPUT_X, INIT_P, INIT_MU, INIT_GAMMA, INIT_SIGMA))

lds_model = LinearDynamicSystem(INIT_GAMMA, INIT_SIGMA, INIT_A,INIT_W)
lds_model.fit(INPUT_X, INIT_MU, INIT_P)