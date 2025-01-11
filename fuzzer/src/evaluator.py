import matplotlib.pyplot as plt


def plot_coverage(coverage_data):
    plt.plot(coverage_data)
    plt.title('Coverage Over Time')
    plt.xlabel('Time')
    plt.ylabel('Coverage')
    plt.savefig('results/coverage.png')
