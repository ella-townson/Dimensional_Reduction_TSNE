import numpy as np
import pandas as pd

def generate_social_services_dataset(num_samples=1000):
    """
    Generate Synthetic Social Services Dataset for t-SNE Visualization.
    """
    np.random.seed(42)
    
    intervention_types = [
        'Family Support', 
        'Youth Mentorship', 
        'Mental Health', 
        'Addiction Recovery', 
        'Domestic Violence Support',
        'Child Protection',
        'Elderly Care',
        'Homeless Support'
    ]
    
     data = {
            'Intervention_Type': np.random.choice(intervention_types, num_samples),  # Randomly assign an intervention type
            'Client_Age': np.random.normal(35, 15, num_samples),  # Normally distributed ages (mean 35, std 15)
            'Household_Income': np.random.lognormal(10, 1, num_samples),  # Log-normal income distribution
            'Previous_Interventions': np.random.poisson(1.5, num_samples),  # Poisson-distributed count of past interventions
            'Intervention_Duration_Months': np.random.gamma(5, 2, num_samples),  # Gamma-distributed intervention duration
            'Social_Network_Size': np.random.poisson(4, num_samples),  # Poisson-distributed social network size
            'Mental_Health_Score': np.random.normal(50, 10, num_samples),  # Normally distributed mental health scores
            'Employment_Status_Score': np.random.normal(60, 15, num_samples),  # Employment status score (mean 60, std 15)
            'Life_Stability_Score': np.random.normal(55, 12, num_samples),  # Life stability score (mean 55, std 12)
            'Support_Network_Quality': np.random.normal(50, 10, num_samples),  # Support network quality (mean 50, std 10)
            'Intervention_Success': np.random.normal(65, 15, num_samples)  # Intervention success score (mean 65, std 15)
    }
        
    df = pd.DataFrame(data)
    
    # Adjust data for specific intervention types
    # Add some deliberate clustering and non-linear relationship i.e. Adjust ages for specific intervention types to introduce clustering

    # For clients receiving the 'Youth Mentorship' intervention, we assume they are typically younger, so we adjust the age distribution (mean 20, std 5)
    df.loc[df['Intervention_Type'] == 'Youth Mentorship', 'Client_Age'] = np.random.normal(20, 5, sum(df['Intervention_Type'] == 'Youth Mentorship'))
    # For clients receiving the 'Elderly Care' intervention, we assume they are typically older, so we adjust the age distribution (mean 70, std 10)
    df.loc[df['Intervention_Type'] == 'Elderly Care', 'Client_Age'] = np.random.normal(70, 10, sum(df['Intervention_Type'] == 'Elderly Care'))
    
    # Additional adjustments for Family Support (younger clients, lower income) - assume family support intervention is more common among younger clients with lower income.
    df.loc[df['Intervention_Type'] == 'Family Support', 'Client_Age'] = np.random.normal(35, 10, sum(df['Intervention_Type'] == 'Family Support'))
    df.loc[df['Intervention_Type'] == 'Family Support', 'Household_Income'] = np.random.lognormal(9, 1.2, sum(df['Intervention_Type'] == 'Family Support'))  # Lower income
    
    # Additional adjustments for Addiction Recovery (middle-aged, more interventions) -  assume addiction recovery intervention is more common among middle-aged clients with more previous interventions.
    df.loc[df['Intervention_Type'] == 'Addiction Recovery', 'Client_Age'] = np.random.normal(30, 10, sum(df['Intervention_Type'] == 'Addiction Recovery'))
    df.loc[df['Intervention_Type'] == 'Addiction Recovery', 'Previous_Interventions'] = np.random.poisson(3, sum(df['Intervention_Type'] == 'Addiction Recovery'))  # More previous interventions, rate of mean occurance (lambda) = 3.
    
    return df 
