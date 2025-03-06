from sklearn.preprocessing import StandardScaler, LabelEncoder

def process_data(df):
    """
    Process the data for t-SNE visualization
    """
    # Encode categorical variables
    le = LabelEncoder()
    df['Intervention_Type_Encoded'] = le.fit_transform(df['Intervention_Type'])
    
    # Select features for t-SNE
    features = [
        'Client_Age', 
        'Household_Income', 
        'Previous_Interventions', 
        'Intervention_Duration_Months',
        'Social_Network_Size', 
        'Mental_Health_Score', 
        'Employment_Status_Score', 
        'Life_Stability_Score', 
        'Support_Network_Quality',
        'Intervention_Success',
        'Intervention_Type_Encoded'
    ]
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])
    
    return X_scaled, le 