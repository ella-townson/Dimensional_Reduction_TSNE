import matplotlib.pyplot as plt
from openTSNE import TSNE

def create_tsne_visualization(X_scaled, intervention_types, label_encoder, save_path=None):
    """
    Create t-SNE visualization
    """
    # Initialize and fit t-SNE
    tsne = TSNE(
        n_components=2,          # Keep 2D for visualization
        perplexity=40,           # Test a different perplexity value
        learning_rate=500,       # Set learning rate to 300 (experiment with values between 100-1000)
        n_jobs=-1,               # Use all cores for faster computation
        random_state=42          # Ensure reproducibility
    )
    
    X_embedded = tsne.fit(X_scaled)
    
    # Create plot
    plt.figure(figsize=(16, 10))
    scatter = plt.scatter(
        X_embedded[:, 0], X_embedded[:, 1],
        c=intervention_types, cmap='viridis',
        alpha=0.7, edgecolors='black', linewidth=0.5
    )
    
    # Add colorbar and labels
    plt.colorbar(scatter, label='Intervention Types', 
                ticks=range(len(label_encoder.classes_)),
                format=plt.FuncFormatter(lambda val, loc: label_encoder.inverse_transform([int(val)])[0]))

    # Set title and labels
    plt.title('t-SNE Visualization of Social Services Intervention Outcomes')
    plt.xlabel('t-SNE Dimension 1')
    plt.ylabel('t-SNE Dimension 2')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    
    plt.close()

def print_intervention_summary(df):
    """
    Print summary statistics for each intervention type
    """
    print("\nIntervention Outcomes Summary:")
    for intervention in df['Intervention_Type'].unique():
        subset = df[df['Intervention_Type'] == intervention]
        print(f"\n{intervention}:")
        print(f"Avg Success: {subset['Intervention_Success'].mean():.2f}, "
              f"Avg Life Stability: {subset['Life_Stability_Score'].mean():.2f}")
        print(f"Avg Mental Health: {subset['Mental_Health_Score'].mean():.2f}, "
              f"Avg Income: ${subset['Household_Income'].mean():.2f}")
        print(f"Avg Duration: {subset['Intervention_Duration_Months'].mean():.2f} months, "
              f"Avg Network Size: {subset['Social_Network_Size'].mean():.2f}") 
