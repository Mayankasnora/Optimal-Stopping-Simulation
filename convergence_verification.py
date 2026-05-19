import math
from StoppingSecProblem import simulate_secretary


def test(n):
    best_prob = 0
    best_r = None

    for i in range(1,n):
        prob = simulate_secretary(n,i,1000)

        if prob > best_prob:
            best_prob = prob
            best_r = i
    return best_r

def simulation():
    n = [10,20,50,100,200,500,1000]
    print("n                    best r                          n/e                                 max probability")
    for i in n:
        best_r=test(i)
        theoretical_best_r = i/(2.7182)
        max_emperical_probab = (best_r/i)*(math.log((i/math.e)))

        print(i,"                   ",best_r,"                   ",theoretical_best_r,"                   ",max_emperical_probab)

simulation()