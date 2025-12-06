# Power BI Data Model Design
# Global Disaster Response Analysis Dashboard

## Data Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    STAR SCHEMA ARCHITECTURE                              │
│                                                                          │
│  ┌──────────────┐          ┌──────────────────────┐                    │
│  │ Date         │          │   Fact_Disasters     │                    │
│  │ Dimension    │◄─────────│   (Fact Table)       │                    │
│  └──────────────┘          └──────────────────────┘                    │
│                                      │                                  │
│  ┌──────────────┐                    │            ┌──────────────┐    │
│  │ Geography    │◄───────────────────┼────────────│ Disaster     │    │
│  │ Dimension    │                    │            │ Type Dim     │    │
│  └──────────────┘                    │            └──────────────┘    │
│                                      │                                  │
│  ┌──────────────┐                    │            ┌──────────────┐    │
│  │ Response     │◄───────────────────┘            │ Measures     │    │
│  │ Agency Dim   │                                 │ Table        │    │
│  └──────────────┘                                 └──────────────┘    │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Table Structures

### 1. Fact_Disasters (Main Fact Table)
**Source**: Global_Disaster_Response_Data_2018_2024.csv

**Purpose**: Contains all measurable disaster events and metrics

**Columns**:
- Disaster_ID (Text) - Primary Key
- Disaster_Type (Text) - Foreign Key
- Country (Text) - Foreign Key
- Region (Text) - Foreign Key
- Disaster_Date (Date) - Foreign Key
- Year (Integer)
- Quarter (Text)
- Month (Text)
- Month_Num (Integer)
- Severity_Level (Decimal)
- Casualties (Integer)
- Economic_Loss_Million_USD (Decimal)
- Response_Time_Hours (Integer)
- Aid_Amount_Million_USD (Decimal)
- Recovery_Duration_Days (Integer)
- Efficiency_Score (Decimal)
- Area_Affected_SqKm (Integer)
- People_Displaced (Integer)
- Response_Agency (Text) - Foreign Key

**Relationships**:
- Many-to-One with Dim_Date (Disaster_Date → Date)
- Many-to-One with Dim_Geography (Country → Country)
- Many-to-One with Dim_DisasterType (Disaster_Type → Disaster_Type)
- Many-to-One with Dim_ResponseAgency (Response_Agency → Agency_Name)

---

### 2. Dim_Date (Date Dimension)
**Type**: Dimension Table (Auto-generated)

**Purpose**: Enables time intelligence and temporal analysis

**Creation Method**: DAX - CALENDAR() or CALENDARAUTO()

**Columns**:
```DAX
Dim_Date = 
ADDCOLUMNS(
    CALENDAR(DATE(2018,1,1), DATE(2024,12,31)),
    "Year", YEAR([Date]),
    "Year-Month", FORMAT([Date], "YYYY-MM"),
    "Month Name", FORMAT([Date], "MMMM"),
    "Month Num", MONTH([Date]),
    "Quarter", "Q" & QUARTER([Date]),
    "Quarter Number", QUARTER([Date]),
    "Year-Quarter", YEAR([Date]) & " Q" & QUARTER([Date]),
    "Day", DAY([Date]),
    "Day of Week", FORMAT([Date], "dddd"),
    "Day of Week Num", WEEKDAY([Date]),
    "Week Number", WEEKNUM([Date]),
    "Is Weekend", IF(WEEKDAY([Date]) IN {1,7}, "Weekend", "Weekday"),
    "Month-Year", FORMAT([Date], "MMM YYYY")
)
```

**Key Columns**:
- Date (Date) - Primary Key
- Year (Integer)
- Year-Month (Text)
- Month Name (Text)
- Month Num (Integer)
- Quarter (Text)
- Quarter Number (Integer)
- Day (Integer)
- Week Number (Integer)

**Relationship**:
- One-to-Many with Fact_Disasters (Date → Disaster_Date)

---

### 3. Dim_Geography (Geography Dimension)
**Type**: Dimension Table (Created from Fact)

**Purpose**: Hierarchical geographic analysis

**Creation Method**: DAX

```DAX
Dim_Geography = 
SUMMARIZE(
    Fact_Disasters,
    Fact_Disasters[Country],
    Fact_Disasters[Region]
)
```

**Columns**:
- Country (Text) - Primary Key
- Region (Text)
- Continent (Text) - Derived
- ISO_Code (Text) - Optional enhancement

**Hierarchy**: Region → Country

**Relationship**:
- One-to-Many with Fact_Disasters (Country → Country)

---

### 4. Dim_DisasterType (Disaster Type Dimension)
**Type**: Dimension Table

**Purpose**: Categorization and classification of disasters

**Creation Method**: Manual or DAX

```DAX
Dim_DisasterType = 
ADDCOLUMNS(
    DISTINCT(Fact_Disasters[Disaster_Type]),
    "Category", 
        SWITCH(
            [Disaster_Type],
            "Earthquake", "Natural - Seismic",
            "Tsunami", "Natural - Seismic",
            "Volcano", "Natural - Seismic",
            "Flood", "Natural - Weather",
            "Hurricane", "Natural - Weather",
            "Cyclone", "Natural - Weather",
            "Drought", "Natural - Weather",
            "Wildfire", "Natural - Environmental",
            "Landslide", "Natural - Environmental",
            "Industrial Accident", "Man-Made",
            "Other"
        ),
    "Severity_Classification",
        SWITCH(
            [Disaster_Type],
            "Tsunami", "Extreme",
            "Earthquake", "Extreme",
            "Hurricane", "High",
            "Cyclone", "High",
            "Flood", "High",
            "Volcano", "High",
            "Drought", "Moderate",
            "Wildfire", "Moderate",
            "Landslide", "Moderate",
            "Industrial Accident", "Low to Moderate",
            "Moderate"
        )
)
```

**Columns**:
- Disaster_Type (Text) - Primary Key
- Category (Text) - Natural/Man-Made classification
- Severity_Classification (Text)
- Icon (Text) - Optional for visuals

**Relationship**:
- One-to-Many with Fact_Disasters (Disaster_Type → Disaster_Type)

---

### 5. Dim_ResponseAgency (Response Agency Dimension)
**Type**: Dimension Table

**Purpose**: Organization and agency classification

**Creation Method**: DAX

```DAX
Dim_ResponseAgency = 
ADDCOLUMNS(
    DISTINCT(Fact_Disasters[Response_Agency]),
    "Agency_Type",
        SWITCH(
            TRUE(),
            [Response_Agency] IN {"Red Cross", "WHO", "UNICEF", "UN OCHA"}, "International NGO",
            [Response_Agency] IN {"FEMA", "National Disaster Agency"}, "Government Agency",
            [Response_Agency] = "Military Forces", "Military",
            [Response_Agency] IN {"Local Emergency Services", "NGO Coalition"}, "Local Organization",
            "Other"
        ),
    "Scope",
        SWITCH(
            TRUE(),
            [Response_Agency] IN {"Red Cross", "WHO", "UNICEF", "UN OCHA"}, "Global",
            [Response_Agency] IN {"FEMA", "National Disaster Agency"}, "National",
            [Response_Agency] = "Military Forces", "National",
            "Local"
        )
)
```

**Columns**:
- Agency_Name (Text) - Primary Key
- Agency_Type (Text)
- Scope (Text) - Global/National/Local

**Relationship**:
- One-to-Many with Fact_Disasters (Agency_Name → Response_Agency)

---

### 6. Measures Table (Calculation Group)
**Type**: Disconnected table for DAX measures

**Purpose**: Centralized location for all calculations and KPIs

**No relationships** - Contains only measures

---

## Relationships Summary

```
Relationship Type: One-to-Many (1:*)

Dim_Date[Date] ──────────────(1:*)──────────────> Fact_Disasters[Disaster_Date]
Dim_Geography[Country] ──────(1:*)──────────────> Fact_Disasters[Country]
Dim_DisasterType[Disaster_Type] ──(1:*)─────────> Fact_Disasters[Disaster_Type]
Dim_ResponseAgency[Agency_Name] ──(1:*)─────────> Fact_Disasters[Response_Agency]
```

**Cardinality**: One-to-Many  
**Cross Filter Direction**: Single (from dimension to fact)  
**Active Relationships**: All active

---

## Data Model Best Practices Applied

### 1. **Star Schema Design**
✓ Fact table at center with dimensions around it  
✓ Denormalized dimensions for performance  
✓ Clear separation of facts and dimensions

### 2. **Optimized Relationships**
✓ One-to-Many relationships only  
✓ Single direction filtering  
✓ Proper key selection

### 3. **Data Types**
✓ Whole numbers for counts  
✓ Decimal for measures  
✓ Text for dimensions  
✓ Date for temporal data

### 4. **Performance Optimization**
✓ Separate date table for time intelligence  
✓ Calculated columns minimized  
✓ Measures used instead of calculated columns where possible  
✓ Proper indexing through relationships

### 5. **Usability**
✓ Clear naming conventions  
✓ Hierarchies defined  
✓ Measures grouped logically  
✓ Hidden technical columns

---

## Implementation Steps in Power BI

### Step 1: Import Data
```
1. Get Data → Text/CSV
2. Select: Global_Disaster_Response_Data_2018_2024.csv
3. Transform Data (Power Query)
   - Verify data types
   - Check for nulls
   - Validate ranges
4. Close & Apply
```

### Step 2: Create Date Dimension
```
1. Modeling tab → New Table
2. Paste Dim_Date DAX formula
3. Mark as Date Table
4. Set Date column as the date identifier
```

### Step 3: Create Other Dimensions
```
1. Create Dim_Geography (DAX formula)
2. Create Dim_DisasterType (DAX formula)
3. Create Dim_ResponseAgency (DAX formula)
```

### Step 4: Create Relationships
```
1. Model View → Manage Relationships
2. Create relationships as per schema
3. Verify cardinality (1:*)
4. Set cross-filter direction (Single)
```

### Step 5: Create Measures Table
```
1. Enter Data → Create blank table named "_Measures"
2. Delete default columns
3. Add all DAX measures to this table
```

### Step 6: Create Hierarchies
```
Geography Hierarchy:
  - Region
  - Country

Date Hierarchy:
  - Year
  - Quarter
  - Month
  - Date

Disaster Classification:
  - Category
  - Disaster_Type
```

### Step 7: Hide Technical Columns
```
Hide from report view:
  - All foreign keys in fact table
  - Technical/ID columns
  - Intermediate calculation columns
```

---

## Data Refresh Strategy

**Refresh Type**: Manual (Historical data)  
**Incremental Refresh**: Not required (static dataset)  
**Schedule**: On-demand only

**For Live Implementation**:
- Set up incremental refresh for date ranges
- Configure gateway for scheduled refresh
- Implement data source credentials

---

## Security Considerations

**Row-Level Security (RLS)**:
```DAX
// Region-based security
[Region] = USERPRINCIPALNAME()

// Country-based security
[Country] IN VALUES(UserCountryMapping[Country])
```

**Object-Level Security**:
- Hide sensitive measures
- Restrict report access by role

---

## Model Size Optimization

**Expected Model Size**: ~2-5 MB (for 500 records)

**Optimization Techniques**:
1. Remove unnecessary columns
2. Use integer encoding for text where possible
3. Disable auto date/time
4. Use SUMMARIZE for dimension tables
5. Archive old data if dataset grows

---

## Testing & Validation Checklist

- [ ] All relationships working correctly
- [ ] Date table marked as date table
- [ ] Measures calculating accurately
- [ ] Hierarchies drill down properly
- [ ] Filters cascade correctly
- [ ] Cross-filtering behaves as expected
- [ ] No circular dependencies
- [ ] Performance is acceptable (<3 sec for visuals)

---

This data model provides a robust foundation for comprehensive disaster response analysis with optimal performance and usability.
