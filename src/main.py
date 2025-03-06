from data_generator import generate_social_services_dataset
from data_processor import process_data
from visualizer import create_tsne_visualization, print_intervention_summary

def main():
    # Generate dataset
    print("Generating dataset...")
    data = generate_social_services_dataset()
    
    # Process data
    print("Processing data...")
    X_scaled, label_encoder = process_data(data)
    
    # Create visualization
    print("Creating t-SNE visualization...")
    create_tsne_visualization(
        X_scaled,
        data['Intervention_Type_Encoded'],
        label_encoder,
        save_path='tsne_visualization.png'
    )
    
    # Print summary
    print_intervention_summary(data)

if __name__ == "__main__":
    main() 