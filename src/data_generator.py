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
        'Intervention_Type': np.random.choice(intervention_types, num_samples),
        'Client_Age': np.random.normal(35, 15, num_samples),
        'Household_Income': np.random.lognormal(10, 1, num_samples),
        'Previous_Interventions': np.random.poisson(1.5, num_samples),
        'Intervention_Duration_Months': np.random.gamma(5, 2, num_samples),
        'Social_Network_Size': np.random.poisson(4, num_samples),
        'Mental_Health_Score': np.random.normal(50, 10, num_samples),
        'Employment_Status_Score': np.random.normal(60, 15, num_samples),
        'Life_Stability_Score': np.random.normal(55, 12, num_samples),
        'Support_Network_Quality': np.random.normal(50, 10, num_samples),
        'Intervention_Success': np.random.normal(65, 15, num_samples)
    }
    
    df = pd.DataFrame(data)
    
    # Adjust data for specific intervention types
    df.loc[df['Intervention_Type'] == 'Youth Mentorship', 'Client_Age'] = np.random.normal(20, 5, sum(df['Intervention_Type'] == 'Youth Mentorship'))
    df.loc[df['Intervention_Type'] == 'Elderly Care', 'Client_Age'] = np.random.normal(70, 10, sum(df['Intervention_Type'] == 'Elderly Care'))
    df.loc[df['Intervention_Type'] == 'Family Support', 'Client_Age'] = np.random.normal(35, 10, sum(df['Intervention_Type'] == 'Family Support'))
    df.loc[df['Intervention_Type'] == 'Family Support', 'Household_Income'] = np.random.lognormal(9, 1.2, sum(df['Intervention_Type'] == 'Family Support'))
    df.loc[df['Intervention_Type'] == 'Addiction Recovery', 'Client_Age'] = np.random.normal(30, 10, sum(df['Intervention_Type'] == 'Addiction Recovery'))
    df.loc[df['Intervention_Type'] == 'Addiction Recovery', 'Previous_Interventions'] = np.random.poisson(3, sum(df['Intervention_Type'] == 'Addiction Recovery'))
    
    return df 