import os, requests
import matplotlib.pyplot as plt


def plot_willingness(a_w,b_w,c_w):
    plt.plot(a_w, label = "Alice")
    plt.plot(b_w, label = "Ben")
    plt.plot(c_w, label = "Charle")
    plt.ylabel('willingness')
    plt.xlabel('number of tick (round)')
    # plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

def plot_competence(a_c,b_c,c_c):
    plt.plot(a_c, label = "Alice")
    plt.plot(b_c, label = "Ben")
    plt.plot(c_c, label = "Charlie")
    plt.ylabel('willingness')
    plt.xlabel('number of tick (round)')
    # plt.title('Interesting Graph\nCheck it out')
    plt.legend()
    plt.show()

if __name__ == "__main__":

    c_w = []
    c_c= []
    a_w = []
    a_c = []
    b_w = []
    b_c = []

    fold = os.getcwd()
    file = fold+'\\beliefs\\trustLog.csv'
    f = open(file, "r")

    for x in f:

        if x != "\n":
            result = x.split(";")
            if result[0] == "Alice":
                a_w.append(result[2])
                a_c.append(result[1])
            elif result[0] == "Ben":
                b_w.append(result[2])
                b_c.append(result[1])
            elif result[0] == "Charlie":
                b_w.append(result[2])
                b_c.append(result[1])

    print(a_w)
    f.close()
    plot_willingness(a_w,b_w,c_w)






