import matplotlib.pyplot as plt

def plot_multiple(x, y):
    """Plot multiple types of graphs on the same screen."""
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))

    # Line plot
    axs[0, 0].plot(x, y, marker='o', linestyle='-', color='b')
    axs[0, 0].set_title('Line Plot')
    axs[0, 0].set_xlabel('X-axis')
    axs[0, 0].set_ylabel('Y-axis')
    axs[0, 0].grid(True)

    # Scatter plot
    axs[0, 1].scatter(x, y, color='r', marker='x')
    axs[0, 1].set_title('Scatter Plot')
    axs[0, 1].set_xlabel('X-axis')
    axs[0, 1].set_ylabel('Y-axis')
    axs[0, 1].grid(True)

    # Bar plot
    axs[0, 2].bar(x, y, color='g', edgecolor='black')
    axs[0, 2].set_title('Bar Plot')
    axs[0, 2].set_xlabel('X-axis')
    axs[0, 2].set_ylabel('Y-axis')
    axs[0, 2].grid(True)

    # Histogram
    axs[1, 0].hist(y, bins=5, color='purple', edgecolor='black')
    axs[1, 0].set_title('Histogram')
    axs[1, 0].set_xlabel('Value')
    axs[1, 0].set_ylabel('Frequency')
    axs[1, 0].grid(True)

    # Pie chart
    axs[1, 1].pie(y, labels=[f'Part {i+1}' for i in range(len(y))], autopct='%1.1f%%', colors=plt.cm.Paired(range(len(y))))
    axs[1, 1].set_title('Pie Chart')

    # Box plot
    axs[1, 2].boxplot(y, vert=False, patch_artist=True, 
                      boxprops=dict(facecolor='lightblue', color='black'),
                      whiskerprops=dict(color='black'),
                      capprops=dict(color='black'),
                      medianprops=dict(color='red'))
    axs[1, 2].set_title('Box Plot')
    axs[1, 2].set_xlabel('Value')
    axs[1, 2].grid(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]
    plot_multiple(x, y)
