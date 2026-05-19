import random
import math
import matplotlib.pyplot as plt

def helper(n,r):
    candidates=[i for i in range(1,n+1)]
    random.shuffle(candidates)

    actual_best = max(candidates)
    best_among_r=max(candidates[:r])
    for i in range(r,n):
        if candidates[i]>best_among_r:
            if candidates[i]==actual_best:
                return 1
            else:
                return 0
    return 0

def simulate_secretary(n, r, trials):

    c=0
    for i in range(trials):
        if helper(n,r)==1:
            c+=1
    
    return (c*100)/trials


# This function computes the exact theoretical probability
# for the secretary problem at a given threshold r.
def theoretical_probability(n, r):
    return (r / n) * sum(1 / (k - 1) for k in range(r + 1, n + 1))


# This function uses your existing simulate_secretary function
# to compute empirical probabilities for every r from 1 to n.
def empirical_curve(n, trials):
    empirical_probabilities = []

    for r in range(1, n + 1):
        # simulate_secretary returns a percentage, so divide by 100
        # to convert it into a probability between 0 and 1.
        probability = simulate_secretary(n, r, trials) / 100
        empirical_probabilities.append(probability)

    return empirical_probabilities


# This function computes the theoretical curve for every r from 1 to n.
def theoretical_curve(n):
    probabilities = []

    for r in range(1, n + 1):
        probabilities.append(theoretical_probability(n, r))

    return probabilities


# This function creates the final professional graph.
def plot_secretary_problem(n, trials):
    r_values = list(range(1, n + 1))

    empirical_probabilities = empirical_curve(n, trials)
    theoretical_probabilities = theoretical_curve(n)

    optimal_threshold = n / math.e
    label_text = "Optimal Threshold \u2248 n/e"

    # plt.figure(...) creates a fresh figure window for the graph.
    # figsize controls the width and height of the figure in inches.
    plt.figure(figsize=(12, 7))

    # plt.plot(x, y, ...) draws a line graph.
    # Here it draws the empirical probabilities from simulation.
    plt.plot(
        r_values,
        empirical_probabilities,
        color="royalblue",
        linewidth=2,
        marker="o",
        markersize=4,
        label="Empirical Probability (Monte Carlo)"
    )

    # This second plt.plot(...) draws the theoretical probability curve.
    plt.plot(
        r_values,
        theoretical_probabilities,
        color="darkorange",
        linewidth=2.5,
        label="Theoretical Probability"
    )

    # plt.axvline(...) draws a vertical line at a chosen x-value.
    # We use it to show the classical optimal threshold n/e.
    plt.axvline(
        x=optimal_threshold,
        color="seagreen",
        linestyle="--",
        linewidth=2,
        label=label_text
    )

    # Add a label next to the vertical dashed line.
    plt.text(
        optimal_threshold + 1,
        0.05,
        label_text,
        color="seagreen",
        rotation=90,
        va="bottom"
    )

    plt.title("Secretary Problem: Empirical and Theoretical Success Probabilities", fontsize=14)
    plt.xlabel("Threshold r", fontsize=12)
    plt.ylabel("Success Probability", fontsize=12)

    # plt.legend() displays the labels of all plotted lines.
    plt.legend(fontsize=11)

    # plt.grid(True) adds background grid lines for readability.
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.xlim(1, n)
    plt.ylim(0, max(max(empirical_probabilities), max(theoretical_probabilities)) + 0.05)
    plt.tight_layout()

    # plt.show() displays the completed graph on the screen.
    plt.show()

    best_empirical_r = r_values[empirical_probabilities.index(max(empirical_probabilities))]
    best_theoretical_r = r_values[theoretical_probabilities.index(max(theoretical_probabilities))]

    print("n =", n)
    print("Monte Carlo trials per r =", trials)
    print("Best empirical threshold:", best_empirical_r, "with probability", round(max(empirical_probabilities), 4))
    print("Best theoretical threshold:", best_theoretical_r, "with probability", round(max(theoretical_probabilities), 4))
    print("n/e =", round(optimal_threshold, 2))
    print()
    print("Interpretation:")
    print("The empirical curve is close to the theoretical curve because Monte Carlo simulation")
    print("approximates the exact probability, and with many trials the random fluctuations become small.")
    print("The maximum occurs near n/e because the optimal strategy balances two goals:")
    print("reject enough early candidates to learn a strong benchmark, but not so many that")
    print("the best candidate is likely to be missed.")


# # Run the full experiment and make the plot.
# plot_secretary_problem(100, 10000)