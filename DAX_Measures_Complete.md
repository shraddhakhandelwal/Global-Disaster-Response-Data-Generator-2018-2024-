# DAX Measures & Calculations
# Global Disaster Response Analysis Dashboard

## TABLE OF CONTENTS
1. [Primary KPI Measures](#primary-kpi-measures)
2. [Advanced Analytical Measures](#advanced-analytical-measures)
3. [Time Intelligence Measures](#time-intelligence-measures)
4. [Comparison & Ranking Measures](#comparison-ranking-measures)
5. [Conditional Formatting Measures](#conditional-formatting-measures)
6. [Helper Measures](#helper-measures)

---

## PRIMARY KPI MEASURES

### 1. Total Disasters
```DAX
Total Disasters = COUNTROWS(Fact_Disasters)
```
**Usage**: Main KPI card  
**Description**: Total count of disaster events

---

### 2. Countries Affected
```DAX
Countries Affected = DISTINCTCOUNT(Fact_Disasters[Country])
```
**Usage**: KPI card  
**Description**: Number of unique countries with disasters

---

### 3. Total Casualties
```DAX
Total Casualties = SUM(Fact_Disasters[Casualties])
```
**Usage**: KPI card, charts  
**Description**: Sum of all casualties (deaths + injuries)

**Formatted Version**:
```DAX
Total Casualties (Formatted) = 
FORMAT([Total Casualties], "#,##0")
```

---

### 4. Total Economic Loss
```DAX
Total Economic Loss = SUM(Fact_Disasters[Economic_Loss_Million_USD])
```
**Usage**: KPI card, financial analysis  
**Description**: Total economic damage in millions USD

**Formatted Version**:
```DAX
Total Economic Loss (Formatted) = 
"$" & FORMAT([Total Economic Loss], "#,##0.00") & "M"
```

---

### 5. Average Response Time
```DAX
Avg Response Time (Hours) = AVERAGE(Fact_Disasters[Response_Time_Hours])
```
**Usage**: KPI card, performance tracking  
**Description**: Average time to respond to disasters

**Alternative in Days**:
```DAX
Avg Response Time (Days) = 
DIVIDE([Avg Response Time (Hours)], 24, 0)
```

---

### 6. Total Aid Distributed
```DAX
Total Aid Distributed = SUM(Fact_Disasters[Aid_Amount_Million_USD])
```
**Usage**: KPI card, aid analysis  
**Description**: Total humanitarian aid in millions USD

**Formatted Version**:
```DAX
Total Aid (Formatted) = 
"$" & FORMAT([Total Aid Distributed], "#,##0.00") & "M"
```

---

### 7. Average Recovery Duration
```DAX
Avg Recovery Duration (Days) = AVERAGE(Fact_Disasters[Recovery_Duration_Days])
```
**Usage**: KPI card, recovery analysis  
**Description**: Average days to complete recovery

---

### 8. Average Efficiency Score
```DAX
Avg Efficiency Score = AVERAGE(Fact_Disasters[Efficiency_Score])
```
**Usage**: KPI card, performance evaluation  
**Description**: Average response effectiveness rating (0-100)

---

## ADVANCED ANALYTICAL MEASURES

### 9. Aid Coverage Ratio
```DAX
Aid Coverage Ratio = 
DIVIDE(
    [Total Aid Distributed],
    [Total Economic Loss],
    0
)
```
**Usage**: Performance evaluation  
**Description**: Proportion of economic loss covered by aid

**Percentage Version**:
```DAX
Aid Coverage % = 
FORMAT([Aid Coverage Ratio], "0.0%")
```

---

### 10. Casualties per Disaster
```DAX
Avg Casualties per Disaster = 
DIVIDE(
    [Total Casualties],
    [Total Disasters],
    0
)
```
**Usage**: Severity comparison  
**Description**: Average casualties per event

---

### 11. Economic Loss per Disaster
```DAX
Avg Economic Loss per Disaster = 
DIVIDE(
    [Total Economic Loss],
    [Total Disasters],
    0
)
```
**Usage**: Financial impact analysis  
**Description**: Average economic damage per event

---

### 12. Total People Displaced
```DAX
Total People Displaced = SUM(Fact_Disasters[People_Displaced])
```
**Usage**: Humanitarian impact  
**Description**: Total population displaced

---

### 13. Total Area Affected
```DAX
Total Area Affected (SqKm) = SUM(Fact_Disasters[Area_Affected_SqKm])
```
**Usage**: Geographic impact  
**Description**: Total geographic area affected

---

### 14. Average Severity Level
```DAX
Avg Severity Level = AVERAGE(Fact_Disasters[Severity_Level])
```
**Usage**: Disaster intensity tracking  
**Description**: Average disaster severity rating

---

### 15. High Severity Disasters
```DAX
High Severity Disasters = 
CALCULATE(
    [Total Disasters],
    Fact_Disasters[Severity_Level] >= 7
)
```
**Usage**: Risk assessment  
**Description**: Count of disasters with severity ≥ 7

---

### 16. Critical Response Delays
```DAX
Critical Delays = 
CALCULATE(
    [Total Disasters],
    Fact_Disasters[Response_Time_Hours] > 72
)
```
**Usage**: Performance monitoring  
**Description**: Disasters with >72 hour response time

---

### 17. Low Efficiency Events
```DAX
Low Efficiency Events = 
CALCULATE(
    [Total Disasters],
    Fact_Disasters[Efficiency_Score] < 60
)
```
**Usage**: Quality control  
**Description**: Disasters with poor response efficiency

---

### 18. Deadliest Disaster Type
```DAX
Deadliest Disaster Type = 
VAR MaxCasualties = 
    MAXX(
        SUMMARIZE(
            Fact_Disasters,
            Fact_Disasters[Disaster_Type],
            "TotalCasualties", [Total Casualties]
        ),
        [TotalCasualties]
    )
RETURN
    CALCULATE(
        VALUES(Fact_Disasters[Disaster_Type]),
        FILTER(
            SUMMARIZE(
                Fact_Disasters,
                Fact_Disasters[Disaster_Type],
                "TotalCasualties", [Total Casualties]
            ),
            [TotalCasualties] = MaxCasualties
        )
    )
```
**Usage**: Risk identification  
**Description**: Disaster type with highest casualties

---

### 19. Costliest Disaster Type
```DAX
Costliest Disaster Type = 
VAR MaxLoss = 
    MAXX(
        SUMMARIZE(
            Fact_Disasters,
            Fact_Disasters[Disaster_Type],
            "TotalLoss", [Total Economic Loss]
        ),
        [TotalLoss]
    )
RETURN
    CALCULATE(
        VALUES(Fact_Disasters[Disaster_Type]),
        FILTER(
            SUMMARIZE(
                Fact_Disasters,
                Fact_Disasters[Disaster_Type],
                "TotalLoss", [Total Economic Loss]
            ),
            [TotalLoss] = MaxLoss
        )
    )
```
**Usage**: Financial risk assessment  
**Description**: Disaster type with highest economic loss

---

### 20. Most Affected Region
```DAX
Most Affected Region = 
VAR MaxDisasters = 
    MAXX(
        SUMMARIZE(
            Fact_Disasters,
            Fact_Disasters[Region],
            "Count", [Total Disasters]
        ),
        [Count]
    )
RETURN
    CALCULATE(
        VALUES(Fact_Disasters[Region]),
        FILTER(
            SUMMARIZE(
                Fact_Disasters,
                Fact_Disasters[Region],
                "Count", [Total Disasters]
            ),
            [Count] = MaxDisasters
        )
    )
```
**Usage**: Geographic risk analysis  
**Description**: Region with most disasters

---

## TIME INTELLIGENCE MEASURES

### 21. Year-over-Year Disasters
```DAX
YoY Disasters = 
VAR CurrentYear = [Total Disasters]
VAR PreviousYear = 
    CALCULATE(
        [Total Disasters],
        DATEADD(Dim_Date[Date], -1, YEAR)
    )
RETURN
    CurrentYear - PreviousYear
```
**Usage**: Trend analysis  
**Description**: Change in disaster count vs previous year

---

### 22. YoY Disasters % Change
```DAX
YoY Disasters % = 
VAR CurrentYear = [Total Disasters]
VAR PreviousYear = 
    CALCULATE(
        [Total Disasters],
        DATEADD(Dim_Date[Date], -1, YEAR)
    )
RETURN
    DIVIDE(
        CurrentYear - PreviousYear,
        PreviousYear,
        0
    )
```
**Usage**: Percentage change tracking  
**Format**: 0.0%

---

### 23. YoY Casualties Change
```DAX
YoY Casualties Change = 
VAR CurrentYear = [Total Casualties]
VAR PreviousYear = 
    CALCULATE(
        [Total Casualties],
        DATEADD(Dim_Date[Date], -1, YEAR)
    )
RETURN
    CurrentYear - PreviousYear
```

---

### 24. YoY Economic Loss % Change
```DAX
YoY Economic Loss % = 
VAR CurrentYear = [Total Economic Loss]
VAR PreviousYear = 
    CALCULATE(
        [Total Economic Loss],
        DATEADD(Dim_Date[Date], -1, YEAR)
    )
RETURN
    DIVIDE(
        CurrentYear - PreviousYear,
        PreviousYear,
        0
    )
```

---

### 25. Running Total Disasters
```DAX
Running Total Disasters = 
CALCULATE(
    [Total Disasters],
    FILTER(
        ALL(Dim_Date[Date]),
        Dim_Date[Date] <= MAX(Dim_Date[Date])
    )
)
```
**Usage**: Cumulative trend charts  
**Description**: Cumulative disaster count over time

---

### 26. Running Total Casualties
```DAX
Running Total Casualties = 
CALCULATE(
    [Total Casualties],
    FILTER(
        ALL(Dim_Date[Date]),
        Dim_Date[Date] <= MAX(Dim_Date[Date])
    )
)
```

---

### 27. MTD Disasters (Month-to-Date)
```DAX
MTD Disasters = 
CALCULATE(
    [Total Disasters],
    DATESMTD(Dim_Date[Date])
)
```

---

### 28. QTD Disasters (Quarter-to-Date)
```DAX
QTD Disasters = 
CALCULATE(
    [Total Disasters],
    DATESQTD(Dim_Date[Date])
)
```

---

### 29. YTD Disasters (Year-to-Date)
```DAX
YTD Disasters = 
CALCULATE(
    [Total Disasters],
    DATESYTD(Dim_Date[Date])
)
```

---

### 30. Previous Year Same Period
```DAX
PY Disasters = 
CALCULATE(
    [Total Disasters],
    SAMEPERIODLASTYEAR(Dim_Date[Date])
)
```

---

## COMPARISON & RANKING MEASURES

### 31. Disaster Type Rank by Casualties
```DAX
Rank by Casualties = 
RANKX(
    ALL(Fact_Disasters[Disaster_Type]),
    [Total Casualties],
    ,
    DESC,
    DENSE
)
```
**Usage**: Top N analysis  
**Description**: Ranking of disaster types by casualties

---

### 32. Country Rank by Economic Loss
```DAX
Country Rank by Loss = 
RANKX(
    ALL(Fact_Disasters[Country]),
    [Total Economic Loss],
    ,
    DESC,
    DENSE
)
```

---

### 33. Response Performance Score
```DAX
Response Performance = 
VAR AvgResponseTime = [Avg Response Time (Hours)]
VAR TargetResponseTime = 48
VAR AvgEfficiency = [Avg Efficiency Score]
VAR AidCoverage = [Aid Coverage Ratio]

RETURN
    (
        (1 - MIN(AvgResponseTime / TargetResponseTime, 1)) * 30 +
        (AvgEfficiency / 100) * 50 +
        (MIN(AidCoverage, 1)) * 20
    )
```
**Usage**: Composite performance metric  
**Range**: 0-100  
**Components**: Response speed (30%), Efficiency (50%), Aid coverage (20%)

---

### 34. Top 5 Countries by Disasters
```DAX
Top 5 Countries = 
CALCULATE(
    [Total Disasters],
    TOPN(
        5,
        ALL(Fact_Disasters[Country]),
        [Total Disasters],
        DESC
    )
)
```

---

### 35. Bottom 5 Efficiency Agencies
```DAX
Bottom 5 Agencies = 
CALCULATE(
    [Avg Efficiency Score],
    TOPN(
        5,
        ALL(Fact_Disasters[Response_Agency]),
        [Avg Efficiency Score],
        ASC
    )
)
```

---

## CONDITIONAL FORMATTING MEASURES

### 36. Response Time Status
```DAX
Response Time Status = 
VAR ResponseTime = [Avg Response Time (Hours)]
RETURN
    SWITCH(
        TRUE(),
        ResponseTime <= 24, "Excellent",
        ResponseTime <= 48, "Good",
        ResponseTime <= 72, "Fair",
        "Poor"
    )
```
**Usage**: Color coding  
**Values**: Excellent | Good | Fair | Poor

---

### 37. Response Time Color
```DAX
Response Time Color = 
VAR ResponseTime = [Avg Response Time (Hours)]
RETURN
    SWITCH(
        TRUE(),
        ResponseTime <= 24, "#2E7D32",      // Green
        ResponseTime <= 48, "#FFA726",       // Orange
        ResponseTime <= 72, "#EF6C00",       // Dark Orange
        "#C62828"                             // Red
    )
```

---

### 38. Efficiency Score Color
```DAX
Efficiency Color = 
VAR Score = [Avg Efficiency Score]
RETURN
    SWITCH(
        TRUE(),
        Score >= 90, "#2E7D32",      // Green
        Score >= 75, "#66BB6A",      // Light Green
        Score >= 60, "#FFA726",      // Orange
        "#EF5350"                     // Red
    )
```

---

### 39. Severity Level Indicator
```DAX
Severity Indicator = 
VAR SeverityLevel = [Avg Severity Level]
RETURN
    SWITCH(
        TRUE(),
        SeverityLevel >= 8, "🔴 Extreme",
        SeverityLevel >= 6, "🟠 High",
        SeverityLevel >= 4, "🟡 Moderate",
        "🟢 Low"
    )
```

---

### 40. Aid Gap Indicator
```DAX
Aid Gap = 
VAR Gap = [Total Economic Loss] - [Total Aid Distributed]
RETURN
    IF(
        Gap > 0,
        "⚠️ Underfunded: $" & FORMAT(Gap, "#,##0.0") & "M",
        "✓ Fully Funded"
    )
```

---

## HELPER MEASURES

### 41. Disaster Count (Non-Zero)
```DAX
Disaster Count Non-Zero = 
IF([Total Disasters] > 0, [Total Disasters], BLANK())
```
**Usage**: Remove zeros from charts

---

### 42. Selected Year
```DAX
Selected Year = 
IF(
    HASONEVALUE(Dim_Date[Year]),
    VALUES(Dim_Date[Year]),
    "All Years"
)
```
**Usage**: Dynamic titles

---

### 43. Selected Region
```DAX
Selected Region = 
IF(
    HASONEVALUE(Fact_Disasters[Region]),
    VALUES(Fact_Disasters[Region]),
    "All Regions"
)
```

---

### 44. Max Casualties in Single Event
```DAX
Max Single Event Casualties = 
MAX(Fact_Disasters[Casualties])
```

---

### 45. Min Response Time
```DAX
Fastest Response = 
MIN(Fact_Disasters[Response_Time_Hours]) & " hours"
```

---

### 46. Max Response Time
```DAX
Slowest Response = 
MAX(Fact_Disasters[Response_Time_Hours]) & " hours"
```

---

### 47. Disaster Trend Indicator
```DAX
Trend Arrow = 
VAR YoYChange = [YoY Disasters %]
RETURN
    SWITCH(
        TRUE(),
        YoYChange > 0.1, "↗️ Increasing",
        YoYChange < -0.1, "↘️ Decreasing",
        "→ Stable"
    )
```

---

### 48. Recovery Efficiency
```DAX
Recovery Efficiency = 
DIVIDE(
    1,
    [Avg Recovery Duration (Days)],
    0
) * 1000
```
**Usage**: Higher is better  
**Description**: Inverse of recovery time, scaled

---

### 49. Impact Severity Score
```DAX
Impact Severity Score = 
VAR NormCasualties = DIVIDE([Total Casualties], MAXX(ALL(Fact_Disasters), [Total Casualties]), 0)
VAR NormEconomic = DIVIDE([Total Economic Loss], MAXX(ALL(Fact_Disasters), [Total Economic Loss]), 0)
VAR NormSeverity = DIVIDE([Avg Severity Level], 10, 0)

RETURN
    (NormCasualties * 0.4 + NormEconomic * 0.4 + NormSeverity * 0.2) * 100
```
**Range**: 0-100  
**Description**: Composite impact score

---

### 50. Disaster Frequency Rate
```DAX
Disaster Frequency (per Year) = 
DIVIDE(
    [Total Disasters],
    DISTINCTCOUNT(Dim_Date[Year]),
    0
)
```

---

## IMPLEMENTATION NOTES

### Creating Measures in Power BI:
1. Open Power BI Desktop
2. Go to "Modeling" tab
3. Click "New Measure"
4. Paste DAX formula
5. Name the measure
6. Set appropriate format:
   - Whole Number: 0
   - Decimal: 0.00
   - Currency: $#,##0.00
   - Percentage: 0.0%

### Organization:
- Create a "_Measures" table
- Group measures by category using Display Folders:
  - KPIs
  - Time Intelligence
  - Comparisons
  - Conditional Formatting
  - Helpers

### Testing:
- Verify calculations with known values
- Test with different filter contexts
- Validate time intelligence measures
- Check performance on large datasets

---

**Total Measures**: 50+  
**Categories**: 6  
**Complexity**: Beginner to Advanced  
**Ready for Production**: Yes
