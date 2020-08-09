import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


class LinearDynamicSystem:
    def __init__(self, gamma, sigma):
        self.gamma = gamma
        self.sigma = sigma

        self.log_p_x_history = []
        self.pred_mu_history = []
        self.mu_history = []
        self.pred_mu_history = []
        self.p_history = []
        self.pred_p_history = []

    def fit(self, observations, mu, p):
        self._filter(observations, mu, p)
        smoothed_mu_list = self._smoothing()

        plt.plot(observations, label="Observation")
        plt.plot(self.pred_mu_history, label="Predicted Latent Variable")
        plt.plot(self.mu_history, label="Updated Latent Variable")
        plt.plot(smoothed_mu_list, label="Smoothed Latent Variable")
        plt.legend()
        plt.show()

    def _filter(self, observations, mu, p):
        _mu, _p = mu, p
        for i, obs in enumerate(observations):
            pred_mu, pred_p, log_p_x = self._predict(_mu, _p, obs)
            self.log_p_x_history.append(log_p_x)
            _mu, _p = self._update(obs, pred_mu, pred_p)

            self.pred_mu_history.append(pred_mu)
            self.pred_p_history.append(pred_p)

            self.mu_history.append(_mu)
            self.p_history.append(_p)

            print("Answer {}: ".format(i+1))

            if i > 0:
                print("predicted p.d.f. of latent variable: mu = {:.3f}, sigma = {:.3f}, joint_prob. = {:.3f}"
                      .format(pred_mu, pred_p, np.sum(self.log_p_x_history)))

            print("log-scaled likelihood = {:.3f}, "
                  "updated p.d.f. of latent value: mu = {:.3f}, sigma = {:.3f}"
                  .format(log_p_x, _mu, _p))

    def _predict(self, mu, p, obs):
        pred_mu = mu
        pred_p = p + self.gamma
        log_p_x = norm.logpdf(x=obs, loc=pred_mu, scale=(pred_p + self.sigma))
        return pred_mu, pred_p, log_p_x

    def _kalman_gain(self, p, s):
        return p / (p + s)

    def _update(self, obs, mu, p):
        k = self._kalman_gain(p, self.sigma)
        new_mu = mu + k * (obs - mu)
        new_p = (1 - k) * p
        return new_mu, new_p

    def _smoothing(self):
        smoothed_mu_list = []
        smoothed_p_list = []

        last_smoothed_mu = self.mu_history[-1]
        last_smoothed_p = self.p_history[-1]

        smoothed_mu_list.append(last_smoothed_mu)
        smoothed_p_list.append(last_smoothed_p)

        for i in reversed(range(len(self.mu_history)-1)):
            current_mu = self.mu_history[i]
            pred_mu = self.pred_mu_history[i+1]

            current_p = self.p_history[i]
            pred_p = self.pred_p_history[i+1]

            j = current_p / pred_p

            last_smoothed_mu = current_mu + j * (last_smoothed_mu - pred_mu)
            last_smoothed_p = current_p + j ** 2 * (last_smoothed_p - pred_p)

            smoothed_mu_list.insert(0, last_smoothed_mu)
            smoothed_p_list.insert(0, last_smoothed_p)

        for mu, p in zip(smoothed_mu_list, smoothed_p_list):
            print("smoothed μ = {:.3f}, smoothed P = {:.3f}".format(mu, p))

        return smoothed_mu_list


def generate_observation(b):
    return 10 * b + 20


STUDENT_ID = "2011039"
print("Your ID is {}".format(STUDENT_ID))

b_1, b_2, b_3, b_4 = [int(sid) for sid in STUDENT_ID[-4:]]
print("b_1 = {}, b_2 = {}, b_3 = {}, b_4 = {}".format(b_1, b_2, b_3, b_4))

INPUT_X = np.array([generate_observation(b) for b in [b_1, b_2, b_3, b_4]])
INIT_P = 50
INIT_MU = 200
INIT_GAMMA = 20
INIT_SIGMA = 10
print("initialized value...: X = {}, P_0 = {}, μ_0 = {}, Γ = {}, Σ = {}"
      .format(INPUT_X, INIT_P, INIT_MU, INIT_GAMMA, INIT_SIGMA))

lds_model = LinearDynamicSystem(INIT_GAMMA, INIT_SIGMA)
lds_model.fit(INPUT_X, INIT_MU, INIT_P)