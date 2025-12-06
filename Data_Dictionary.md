# Data Dictionary - Global Disaster Response Dataset (2018-2024)

## Overview
This dataset contains comprehensive information about global disaster events from 2018 to 2024, including disaster characteristics, impact metrics, and response performance indicators.

---

## Field Definitions

### Identification Fields

| Field Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| **Disaster_ID** | Text | Unique identifier for each disaster event | DIS0001, DIS0002 |
| **Disaster_Type** | Text | Category of disaster | Earthquake, Flood, Hurricane, Wildfire, etc. |

### Geographic Fields

| Field Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| **Country** | Text | Country where disaster occurred | Japan, United States, Brazil |
| **Region** | Text | Geographic region | Asia-Pacific, Americas, Europe, Africa, Middle East |

### Temporal Fields

| Field Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| **Disaster_Date** | Date | Date when disaster occurred | 2023-05-15 |
| **Year** | Integer | Year of disaster | 2023 |
| **Quarter** | Text | Quarter of the year | Q1, Q2, Q3, Q4 |
| **Month** | Text | Month name | January, February |
| **Month_Num** | Integer | Month number (1-12) | 1, 2, 3 |

### Severity & Impact Metrics

| Field Name | Data Type | Description | Range/Unit | Business Meaning |
|------------|-----------|-------------|------------|------------------|
| **Severity_Level** | Decimal | Disaster intensity scale | 1.0 - 9.5 | Higher values indicate more severe disasters |
| **Casualties** | Integer | Number of deaths and injuries | 0 - 50,000+ | Total human casualties from the disaster |
| **Economic_Loss_Million_USD** | Decimal | Financial damage in millions USD | 0 - 5,000+ | Total economic impact including property damage |
| **Area_Affected_SqKm** | Integer | Geographic area impacted | 50 - 5,000+ | Size of disaster zone in square kilometers |
| **People_Displaced** | Integer | Number of people displaced | 500 - 100,000+ | Population forced to evacuate |

### Response Performance Metrics

| Field Name | Data Type | Description | Range/Unit | Business Meaning |
|------------|-----------|-------------|------------|------------------|
| **Response_Time_Hours** | Integer | Hours from disaster to first response | 2 - 168 hours | Speed of emergency response deployment |
| **Aid_Amount_Million_USD** | Decimal | Financial aid provided in millions USD | 5 - 1,000+ | Total humanitarian and recovery aid distributed |
| **Recovery_Duration_Days** | Integer | Days until recovery completion | 20 - 250+ | Time to restore basic services and infrastructure |
| **Efficiency_Score** | Decimal | Response effectiveness rating | 20 - 100 | Calculated performance score (higher is better) |

### Organizational Fields

| Field Name | Data Type | Description | Example |
|------------|-----------|-------------|---------|
| **Response_Agency** | Text | Primary responding organization | Red Cross, FEMA, UN OCHA, WHO |

---

## Disaster Type Categories

### 1. **Earthquake**
- Severity Range: 5.0 - 9.0 (Richter scale equivalent)
- Typical Casualties: High (1,000 - 40,000+)
- Economic Impact: Very High

### 2. **Flood**
- Severity Range: 3.0 - 8.0
- Typical Casualties: Moderate to High (500 - 15,000)
- Economic Impact: High

### 3. **Hurricane/Cyclone**
- Severity Range: 1.0 - 5.0 (Category scale)
- Typical Casualties: High (800 - 20,000)
- Economic Impact: Very High

### 4. **Wildfire**
- Severity Range: 3.0 - 8.0
- Typical Casualties: Low to Moderate (200 - 5,000)
- Economic Impact: Moderate to High

### 5. **Drought**
- Severity Range: 4.0 - 9.0
- Typical Casualties: Moderate (300 - 8,000)
- Economic Impact: Moderate

### 6. **Tsunami**
- Severity Range: 5.0 - 9.5
- Typical Casualties: Very High (2,000 - 50,000+)
- Economic Impact: Very High

### 7. **Volcano**
- Severity Range: 4.0 - 8.0
- Typical Casualties: Moderate to High (600 - 15,000)
- Economic Impact: Moderate to High

### 8. **Landslide**
- Severity Range: 3.0 - 7.0
- Typical Casualties: Low to Moderate (150 - 4,000)
- Economic Impact: Low to Moderate

### 9. **Industrial Accident**
- Severity Range: 2.0 - 7.0
- Typical Casualties: Low (100 - 2,500)
- Economic Impact: Moderate

### 10. **Cyclone**
- Severity Range: 2.0 - 5.0
- Typical Casualties: High (700 - 18,000)
- Economic Impact: High

---

## Key Performance Indicators (KPIs)

### Primary KPIs
1. **Total Disasters**: Count of all disaster events
2. **Countries Affected**: Number of unique countries
3. **Total Casualties**: Sum of all casualties
4. **Total Economic Loss**: Sum of economic damage (Million USD)
5. **Average Response Time**: Mean response time in hours
6. **Total Aid Distributed**: Sum of aid amounts (Million USD)
7. **Average Recovery Duration**: Mean recovery time in days
8. **Average Efficiency Score**: Mean response effectiveness

### Secondary Metrics
- **Deadliest Disaster Type**: Type with highest total casualties
- **Costliest Disaster Type**: Type with highest economic loss
- **Fastest Response**: Minimum response time
- **Slowest Response**: Maximum response time
- **Aid Coverage Ratio**: Aid Amount / Economic Loss

---

## Data Relationships & Calculations

### Efficiency Score Formula
```
Base Efficiency = 100 - (Response_Time_Hours / 168 * 40)
Aid Effectiveness Bonus = min(20, Aid_Amount / Economic_Loss * 15)
Efficiency_Score = Base Efficiency + Aid Effectiveness Bonus + Random Variance(-10, +10)
Range: 20 - 100
```

### Recovery Duration Factors
- Positively correlated with severity level
- Positively correlated with response time (delayed response = longer recovery)
- Inversely correlated with aid amount

### Economic Loss Patterns
- Scales with severity level
- Varies by disaster type (hurricanes/earthquakes typically costlier)
- Influenced by country's economic development level

---

## Regional Coverage

### Asia-Pacific (10 countries)
Japan, Philippines, Indonesia, India, Bangladesh, China, Australia, Nepal, Pakistan, Thailand

### Americas (10 countries)
United States, Mexico, Brazil, Chile, Haiti, Canada, Colombia, Peru, Ecuador, Argentina

### Europe (10 countries)
Italy, Greece, Spain, France, Germany, Turkey, United Kingdom, Portugal, Norway, Poland

### Africa (10 countries)
Nigeria, Kenya, South Africa, Ethiopia, Mozambique, Somalia, Sudan, Madagascar, Zimbabwe, Egypt

### Middle East (10 countries)
Iran, Iraq, Syria, Yemen, Afghanistan, Saudi Arabia, Israel, Lebanon, Jordan, UAE

---

## Data Quality Notes

- **Date Range**: January 2018 - December 2024
- **Total Records**: 500 disaster events
- **Data Completeness**: 100% (no missing values)
- **Data Source**: Synthetically generated for analysis purposes
- **Update Frequency**: Historical dataset (static)

---

## Usage Guidelines

### For Power BI Dashboard
1. Import CSV file as data source
2. Set correct data types for each column
3. Create date hierarchy using Disaster_Date
4. Build relationships if using dimension tables
5. Apply filters for interactive analysis

### Recommended Visualizations
- **KPI Cards**: Summary metrics
- **Line Charts**: Trends over time
- **Bar Charts**: Comparison by disaster type, country, region
- **Scatter Plots**: Response time vs. recovery duration
- **Maps**: Geographic distribution
- **Tables**: Detailed drill-down data
- **Slicers**: Year, Region, Disaster Type filters

---

## Version Information
- **Version**: 1.0
- **Created**: December 2024
- **Dataset Size**: 500 records
- **File Format**: CSV (UTF-8)
