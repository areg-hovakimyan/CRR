import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Plot 1: Distribution of RFM Scores

def plot_rfm_distributions(data):
    # Load the data from the given CSV file path
    

    # Set up the plotting environment
    fig, ax = plt.subplots(1, 3, figsize=(18, 6))

    # Plot for Recency Scores
    sns.histplot(data=data, x='R_Score', bins=5, kde=False, ax=ax[0])
    ax[0].set_title('Distribution of Recency Scores')
    ax[0].set_xlabel('Recency Score')
    ax[0].set_ylabel('Count')

    # Plot for Frequency Scores
    sns.histplot(data=data, x='F_Score', bins=5, kde=False, ax=ax[1])
    ax[1].set_title('Distribution of Frequency Scores')
    ax[1].set_xlabel('Frequency Score')
    ax[1].set_ylabel('Count')

    # Plot for Monetary Scores
    sns.histplot(data=data, x='M_Score', bins=5, kde=False, ax=ax[2])
    ax[2].set_title('Distribution of Monetary Scores')
    ax[2].set_xlabel('Monetary Score')
    ax[2].set_ylabel('Count')

    plt.tight_layout()
    plt.show()

# Plot 2: Distribution of RFM Scores
def cluster_p(data):
    # Load the data from the given CSV file path

    plt.figure(figsize=(10, 6))
    sns.countplot(x='Cluster', data=data)
    plt.title('Customer Distribution by Cluster')
    plt.xlabel('Cluster')
    plt.ylabel('Number of Customers')
    plt.show()


# Plot 3: Age Distribution per Cluster
def age_dist_per_cluster(data):
    # Load the data from the given CSV file path
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Cluster', y='Age', data=data)
    plt.title('Age Distribution per Cluster')
    plt.xlabel('Cluster')
    plt.ylabel('Age')
    plt.show()


# Plot 4
def rfm_plots(data):
# Load the data
    

    # Filter out any rows with missing values in the columns you're interested in

    # Setting up the plot
    fig, ax = plt.subplots(figsize=(8, 6))

    # Recency vs Monetary
    scatter = ax.scatter(data['Recency'], data['Monetary'], c=data['Cluster'], cmap='viridis', alpha=0.6, edgecolors='w')
    ax.set_xlabel('Recency')
    ax.set_ylabel('Monetary')
    ax.set_title('Recency vs Monetary')

    # Create a legend
    legend = ax.legend(*scatter.legend_elements(), title="Clusters")
    ax.add_artist(legend)

    plt.tight_layout()
    plt.show()

