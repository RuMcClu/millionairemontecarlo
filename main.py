import random
import statistics
import numpy as np
import matplotlib.pyplot as plt


def simulate(audience_correctness, runs):
    results = []
    results2 = []
    for x in range(runs):
        answers = []
        answers_two = []
        possible_answers = ['a', 'b', 'c', 'd']
        answer = random.choice(possible_answers)
        # print('Answer is = ' + answer)

        random_answers = [random.choice(possible_answers) for aud in range(100 - audience_correctness)]
        right_answers = [answer for aud in range(audience_correctness)]
        answers = right_answers + random_answers

        # after 50/50
        k1 = random.choice([i for i in possible_answers if i != answer])
        k2 = random.choice([i for i in possible_answers if i not in [k1, answer]])

        answers_50 = list(filter(lambda a: a != k2, list(filter(lambda a: a != k1, answers))))

        possible_two = [answer, 'other']
        random_two = [random.choice(possible_two) for aud in range(100 - audience_correctness)]
        answers_two = random_two + right_answers

        results.append(answer == statistics.mode(answers_50))
        results2.append(answer == statistics.mode(answers_two))

    strategy = np.mean(results)
    strategy2 = np.mean(results2)
    # print(strategy)
    # print(strategy2)

    return [strategy, strategy2]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    runs = 10000
    graph_data = [[x, simulate(x, runs)] for x in range(21)]
    print(graph_data)

    x = []
    y1 = []
    y2 = []

    for each_result in graph_data:
        x.append(each_result[0])
        y1.append(each_result[1][0])
        y2.append(each_result[1][1])
    plt.plot(x, y1, label='50/50 after poll')
    plt.plot(x, y2, '-.', label='50/50 before poll')
    plt.xlabel('people in the know')
    plt.ylabel('P(audience correct)')
    plt.title(str(runs) + ' runs')
    plt.legend(loc="lower right")
    plt.show()

