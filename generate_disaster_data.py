"""
Global Disaster Response Data Generator (2018-2024)
Generates realistic disaster response data for Power BI analysis
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Configuration
START_DATE = datetime(2018, 1, 1)
END_DATE = datetime(2024, 12, 31)
NUM_DISASTERS = 500

# Master data
COUNTRIES = {
    'Asia-Pacific': ['Japan', 'Philippines', 'Indonesia', 'India', 'Bangladesh', 'China', 'Australia', 'Nepal', 'Pakistan', 'Thailand'],
    'Americas': ['United States', 'Mexico', 'Brazil', 'Chile', 'Haiti', 'Canada', 'Colombia', 'Peru', 'Ecuador', 'Argentina'],
    'Europe': ['Italy', 'Greece', 'Spain', 'France', 'Germany', 'Turkey', 'United Kingdom', 'Portugal', 'Norway', 'Poland'],
    'Africa': ['Nigeria', 'Kenya', 'South Africa', 'Ethiopia', 'Mozambique', 'Somalia', 'Sudan', 'Madagascar', 'Zimbabwe', 'Egypt'],
    'Middle East': ['Iran', 'Iraq', 'Syria', 'Yemen', 'Afghanistan', 'Saudi Arabia', 'Israel', 'Lebanon', 'Jordan', 'UAE']
}

DISASTER_TYPES = {
    'Earthquake': {'severity_range': (5.0, 9.0), 'casualty_mult': 1000, 'economic_mult': 50},
    'Flood': {'severity_range': (3.0, 8.0), 'casualty_mult': 500, 'economic_mult': 30},
    'Hurricane': {'severity_range': (1.0, 5.0), 'casualty_mult': 800, 'economic_mult': 100},
    'Wildfire': {'severity_range': (3.0, 8.0), 'casualty_mult': 200, 'economic_mult': 40},
    'Drought': {'severity_range': (4.0, 9.0), 'casualty_mult': 300, 'economic_mult': 20},
    'Tsunami': {'severity_range': (5.0, 9.5), 'casualty_mult': 2000, 'economic_mult': 80},
    'Volcano': {'severity_range': (4.0, 8.0), 'casualty_mult': 600, 'economic_mult': 35},
    'Landslide': {'severity_range': (3.0, 7.0), 'casualty_mult': 150, 'economic_mult': 15},
    'Industrial Accident': {'severity_range': (2.0, 7.0), 'casualty_mult': 100, 'economic_mult': 25},
    'Cyclone': {'severity_range': (2.0, 5.0), 'casualty_mult': 700, 'economic_mult': 60}
}

def random_date(start, end):
    """Generate random date between start and end"""
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

def generate_disaster_data():
    """Generate realistic disaster response dataset"""
    
    data = []
    disaster_id = 1
    
    for _ in range(NUM_DISASTERS):
        # Basic info
        region = random.choice(list(COUNTRIES.keys()))
        country = random.choice(COUNTRIES[region])
        disaster_type = random.choice(list(DISASTER_TYPES.keys()))
        
        # Date
        disaster_date = random_date(START_DATE, END_DATE)
        year = disaster_date.year
        month = disaster_date.month
        quarter = f"Q{(month-1)//3 + 1}"
        
        # Severity
        severity_config = DISASTER_TYPES[disaster_type]
        severity = round(random.uniform(*severity_config['severity_range']), 1)
        
        # Impact calculations
        base_casualties = int(severity * severity_config['casualty_mult'] * random.uniform(0.3, 2.5))
        casualties = max(0, base_casualties + random.randint(-100, 500))
        
        base_economic_loss = severity * severity_config['economic_mult'] * random.uniform(0.5, 3.0)
        economic_loss_million = round(base_economic_loss, 2)
        
        # Response metrics
        response_time_hours = random.randint(2, 168)  # 2 hours to 7 days
        
        # Aid amount correlates with severity and economic loss
        aid_base = (severity * 10 + economic_loss_million * 0.5) * random.uniform(0.6, 1.8)
        aid_amount_million = round(aid_base, 2)
        
        # Recovery duration (influenced by severity and response time)
        recovery_base = severity * 15 + (response_time_hours / 24) * 5
        recovery_duration_days = int(recovery_base * random.uniform(0.7, 1.5))
        
        # Efficiency score (0-100, inversely related to response time, positively to aid)
        efficiency_base = 100 - (response_time_hours / 168 * 40)
        efficiency_bonus = min(20, aid_amount_million / economic_loss_million * 15) if economic_loss_million > 0 else 10
        efficiency_score = round(max(20, min(100, efficiency_base + efficiency_bonus + random.uniform(-10, 10))), 1)
        
        # Area affected (sq km)
        area_affected = int(severity * random.uniform(50, 500))
        
        # People displaced
        people_displaced = int(casualties * random.uniform(5, 20))
        
        # Response agency
        agencies = ['Red Cross', 'UN OCHA', 'WHO', 'UNICEF', 'National Disaster Agency', 
                   'FEMA', 'Local Emergency Services', 'Military Forces', 'NGO Coalition']
        response_agency = random.choice(agencies)
        
        data.append({
            'Disaster_ID': f'DIS{disaster_id:04d}',
            'Disaster_Type': disaster_type,
            'Country': country,
            'Region': region,
            'Disaster_Date': disaster_date.strftime('%Y-%m-%d'),
            'Year': year,
            'Quarter': quarter,
            'Month': disaster_date.strftime('%B'),
            'Month_Num': month,
            'Severity_Level': severity,
            'Casualties': casualties,
            'Economic_Loss_Million_USD': economic_loss_million,
            'Response_Time_Hours': response_time_hours,
            'Aid_Amount_Million_USD': aid_amount_million,
            'Recovery_Duration_Days': recovery_duration_days,
            'Efficiency_Score': efficiency_score,
            'Area_Affected_SqKm': area_affected,
            'People_Displaced': people_displaced,
            'Response_Agency': response_agency
        })
        
        disaster_id += 1
    
    df = pd.DataFrame(data)
    
    # Sort by date
    df = df.sort_values('Disaster_Date').reset_index(drop=True)
    
    return df

# Generate and save data
print("Generating Global Disaster Response Dataset (2018-2024)...")
disaster_df = generate_disaster_data()

# Save to CSV
output_file = 'Global_Disaster_Response_Data_2018_2024.csv'
disaster_df.to_csv(output_file, index=False)

print(f"\n✓ Dataset generated successfully!")
print(f"✓ File saved: {output_file}")
print(f"\nDataset Summary:")
print(f"  Total Disasters: {len(disaster_df)}")
print(f"  Date Range: {disaster_df['Disaster_Date'].min()} to {disaster_df['Disaster_Date'].max()}")
print(f"  Countries Covered: {disaster_df['Country'].nunique()}")
print(f"  Disaster Types: {disaster_df['Disaster_Type'].nunique()}")
print(f"  Total Casualties: {disaster_df['Casualties'].sum():,}")
print(f"  Total Economic Loss: ${disaster_df['Economic_Loss_Million_USD'].sum():,.2f} Million")
print(f"  Total Aid Distributed: ${disaster_df['Aid_Amount_Million_USD'].sum():,.2f} Million")

# Display sample records
print("\nSample Records (First 5):")
print(disaster_df.head().to_string())

# Statistical summary
print("\n\nStatistical Summary:")
print(disaster_df[['Severity_Level', 'Casualties', 'Economic_Loss_Million_USD', 
                   'Response_Time_Hours', 'Aid_Amount_Million_USD', 
                   'Recovery_Duration_Days', 'Efficiency_Score']].describe())
