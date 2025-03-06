# Social Services Intervention Analysis

This project analyzes and visualizes social services intervention data using t-SNE (t-Distributed Stochastic Neighbor Embedding) to identify patterns in intervention outcomes.

## Project Overview

The project generates synthetic social services data and visualizes relationships between different types of interventions and their outcomes. It includes:

Synthetic data generation for social services interventions
    - Data processing and standardization
    - t-SNE visualization
    - Statistical summary of intervention outcomes


This will:
1. Generate a synthetic dataset
2. Process the data
3. Create a t-SNE visualization (saved as 'tsne_visualization.png')
4. Print intervention outcome summaries

## Data Features

The synthetic dataset includes:

    - Intervention Type (8 different categories)
    - Client Age
    - Household Income
    - Previous Interventions
    - Intervention Duration
    - Social Network Size
    - Mental Health Score
    - Employment Status Score
    - Life Stability Score
    - Support Network Quality
    - Intervention Success

## Visualization

The t-SNE visualization shows clustering patterns among different intervention types, helping to identify:

    - Similar intervention outcomes
    - Groupings of client characteristics
    - Patterns in service delivery effectiveness

## Output

The program generates:

    1. A t-SNE visualization plot (tsne_visualization.png)
    2. Summary statistics for each intervention type, including:
        - Average success rates
        - Average life stability scores
        - Mental health scores
        - Income levels
        - Intervention duration
        - Social network size


## Notes

- The data is synthetic and generated for demonstration purposes
- The random seed is set to 42 for reproducibility
- The t-SNE parameters are optimized for this specific dataset
