
import numpy as np
import matplotlib.pyplot as plt


def roll_dice():
    return np.random.randint(1, 7)


if __name__ == "__main__":
    fig = plt.figure(tight_layout=True, figsize=(10, 8), dpi=80)
    dice1_rolls = np.array([roll_dice() for _ in range(100)])
    dice2_rolls = np.array([roll_dice() for _ in range(100)])

    sums = np.array([int(dice1_rolls[i] + dice2_rolls[i]) for i in range(100)])
    trials = np.array([int(i) for i in range(100)])
    column = np.array(sums[:])
    row = np.array(trials[:])

    scatter = fig.add_subplot(2, 2, 1)
    scatter.set_title("Scatter Plot")
    scatter.set_ylabel('Sums', fontsize=8)
    scatter.set_xlabel('Trials', fontsize=8)
    scatter.set_yticks(np.arange(2, 13, 1))
    scatter.scatter(row, column, s=1, color='Red')

    line = fig.add_subplot(2, 2, 2)
    line.set_title("Line Plot")
    line.set_ylabel('Sums', fontsize=8)
    line.set_xlabel('Trials', fontsize=8)
    line.set_yticks(np.arange(2, 13, 1))
    line.plot(row, column)

    bar = fig.add_subplot(2, 2, 3)
    bar.set_title("Pie Chart")
    occurrences = np.array([sums.tolist().count(i) for i in range(2, 13)])

    bar.pie(occurrences, labels=[i for i in range(
        2, 13)], radius=1.2, autopct='%1.1f%%', textprops={'fontsize': 10})

    histogram = fig.add_subplot(2, 2, 4)
    histogram.set_title("Histogram")
    histogram.set_ylabel('Occurrences', fontsize=8)
    histogram.set_xlabel('Sums', fontsize=8)
    histogram.hist(column, bins=11, color='Green')

    plt.show()
