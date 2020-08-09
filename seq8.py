import numpy as np

def relu(x):
    return np.where(x > 0, x, 0)
def sigmoid(x):
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x)

if __name__=="__main__":
    STUDENT_ID = '2011121'
    print("Your ID is {}".format(STUDENT_ID))

    b_3, b_2, b_1 = [int(sid) for sid in STUDENT_ID[-3:]]
    print("b_1 = {}, b_2 = {}, b_3 = {}".format(b_1, b_2, b_3))
    w_1_1 = (b_2 + 2) / 10
    w_1_2 = -5 / 10
    w_1_3 = (b_1 - 2) / 10
    w_1_4 = -7 / 10
    w_1_5 = -b_2 / 10
    w_1_6 = -2 / 10

    w_1_a = (b_3 + 4) / 10
    w_1_b = 5 / 10
    w_1_c = -b_3 / 10
    w_1_d = -1 / 10

    w_2_1 = -(b_1 + 4) / 10
    w_2_2 = -2 / 10
    w_2_3 = (b_2 + 7) / 10
    w_2_4 = -3 / 10
    w_2_5 = (b_1 + 3)/ 10
    w_2_6 = 1 / 10
    W1 = np.array([
        [w_1_1, w_1_2],
        [w_1_3, w_1_4],
        [w_1_5, w_1_6],
    ])
    V1 = np.array([
        [w_1_a, w_1_b],
        [w_1_c, w_1_d],
    ])
    W2 = np.array([
        [w_2_1, w_2_2, w_2_3],
        [w_2_4, w_2_5, w_2_6],
    ])
    # print("{}\n {}\n {}\n".format(W1,V1,W2))
    h = np.array([0, 0])
    f = relu(h)
    for t in range(3):
        x = np.zeros(3)
        x[t] = 1
        # print("W1:\n{}\n, V1:\n{}\n".format(W1,V1))
        h = x @ W1 + f @ V1
        f = relu(h)
        # print("2agi,",x,f@W2)
        y = sigmoid(f @ W2)
        
        print(
            f"t = {t}:\n"
            f"\th = {h}\n"
            f"\tf = {f}\n"
            f"\ty = {y}\n"
        )