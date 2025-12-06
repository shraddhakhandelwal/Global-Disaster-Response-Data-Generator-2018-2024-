# Sample Power BI Queries and Scenarios
# Global Disaster Response Dashboard

## BUSINESS QUESTIONS THIS DASHBOARD ANSWERS

### Executive Level Questions

1. **What is the overall disaster impact globally?**
   - View: Executive Overview page
   - KPIs: Total Disasters, Casualties, Economic Loss
   - Insight: 500 disasters, 2.7M casualties, $206B loss

2. **Which regions are most affected by disasters?**
   - View: Regional Distribution donut chart
   - Filter: By year or disaster type
   - Action: Click region to drill down

3. **How has disaster frequency changed over time?**
   - View: Trend Analysis page
   - Visual: Disaster frequency timeline
   - Measure: YoY Disasters %

4. **What is our average response performance?**
   - View: Performance Insights page
   - KPIs: Response Time, Efficiency Score
   - Benchmark: Compare against target (48 hours, 85 score)

---

### Operational Questions

5. **Which disaster types cause the most casualties?**
   - View: Disasters by Type bar chart
   - Sort: By Total Casualties
   - Filter: Specific years or regions

6. **How effective is our aid distribution?**
   - View: Performance page
   - Measure: Aid Coverage Ratio
   - Visual: Aid Effectiveness Analysis chart

7. **Which countries need priority attention?**
   - View: Top Affected Countries table
   - Sort: By Casualties or Economic Loss
   - Action: Drill through to country details

8. **What is the relationship between response time and recovery?**
   - View: Performance page
   - Visual: Response Time vs Recovery scatter plot
   - Insight: Identify outliers and best practices

---

### Strategic Planning Questions

9. **Are there seasonal patterns in disasters?**
   - View: Trend Analysis page
   - Visual: Seasonal Pattern chart
   - Analysis: Month-by-month comparison

10. **Which agencies perform best?**
    - View: Performance page
    - Visual: Agency Performance Ranking table
    - Sort: By Efficiency Score

11. **What are the fastest and slowest responses?**
    - Measure: Min/Max Response Time
    - Visual: Response Time Distribution histogram
    - Action: Investigate extreme cases

12. **Where are we underperforming?**
    - View: Performance page
    - Filter: Efficiency Score < 60
    - Visual: Low Efficiency Events count

---

## SAMPLE ANALYSIS SCENARIOS

### Scenario 1: Year-End Executive Briefing

**Objective**: Present 2024 disaster response performance

**Steps**:
1. Apply Year filter = 2024
2. Navigate to Executive Overview
3. Note key KPIs:
   - Total disasters in 2024
   - YoY change percentage
   - Total casualties and economic loss
4. Highlight most affected region
5. Show top 3 disaster types
6. Compare efficiency score vs previous year

**Export**: Save as PDF for board presentation

---

### Scenario 2: Regional Risk Assessment

**Objective**: Evaluate Asia-Pacific disaster risk

**Steps**:
1. Filter Region = Asia-Pacific
2. Geographic Analysis page
3. Review country distribution map
4. Identify top 5 affected countries
5. Analyze disaster type composition
6. Check average severity levels
7. Compare to other regions

**Action Items**:
- Increase resources in high-risk countries
- Pre-position emergency supplies
- Strengthen regional partnerships

---

### Scenario 3: Response Time Improvement

**Objective**: Reduce average response time by 20%

**Steps**:
1. Performance Insights page
2. Current: Avg Response Time = 48 hours
3. Target: 38.4 hours (20% reduction)
4. Identify delays:
   - Filter Response Time > 72 hours
   - Count critical delays
5. Analyze by:
   - Region (which regions are slowest?)
   - Disaster Type (which disasters take longest?)
   - Agency (which agencies need support?)
6. Review best performers:
   - Filter Response Time < 24 hours
   - Study their practices

**Recommendations**:
- Deploy resources closer to high-risk areas
- Improve coordination between agencies
- Invest in early warning systems

---

### Scenario 4: Budget Allocation Planning

**Objective**: Optimize aid distribution for next fiscal year

**Steps**:
1. Calculate total aid budget: $154B (historical)
2. Analyze Aid Coverage Ratio by disaster type
3. Identify underfunded disaster types:
   - Filter: Aid Coverage < 50%
4. Review economic loss trends
5. Forecast next year's needs:
   - Use disaster frequency trends
   - Apply economic loss patterns
6. Allocate budget proportionally

**Budget Distribution**:
- High severity disasters: 40%
- High frequency disasters: 30%
- Regional reserves: 20%
- Contingency fund: 10%

---

### Scenario 5: Disaster Preparedness Audit

**Objective**: Identify preparedness gaps

**Steps**:
1. Geographic Analysis page
2. For each region, assess:
   - Disaster frequency (increasing/decreasing?)
   - Response times (meeting targets?)
   - Efficiency scores (above 80?)
3. Create risk matrix:
   - High frequency + Low efficiency = Critical Gap
   - High severity + Slow response = Priority Action
4. Develop action plans per region

**Risk Matrix**:
```
           Low Efficiency    High Efficiency
High Freq  [CRITICAL]        [MONITOR]
Low Freq   [IMPROVE]         [MAINTAIN]
```

---

## DRILL-DOWN EXAMPLES

### Example 1: Investigating High Casualties

**Starting Point**: Total Casualties KPI shows spike

**Drill Path**:
1. Click Total Casualties card
2. Cross-filters show affected visuals
3. Trends chart reveals spike month
4. Filter to that month
5. Top Countries table shows location
6. Right-click country → Drill through
7. Country detail page shows breakdown
8. Identify specific disaster events

**Root Cause**: e.g., Major earthquake in Japan, August 2023

---

### Example 2: Efficiency Score Drop

**Starting Point**: Efficiency Score = 75 (below target 85)

**Investigation**:
1. Efficiency Distribution histogram
2. Count in 60-75 range is high
3. Filter Efficiency Score: 60-75
4. Agency Performance table shows which agencies
5. Cross-reference with Response Time
6. Correlation: Slower response = Lower efficiency
7. Drill to specific disasters
8. Review common factors

**Action**: Retrain identified agencies, improve logistics

---

## POWER QUERY SCENARIOS

### Scenario: Adding New Data Column

**Requirement**: Add "Impact Category" based on casualties

**Power Query M Code**:
```m
= Table.AddColumn(
    #"Previous Step",
    "Impact Category",
    each if [Casualties] >= 10000 then "Catastrophic"
         else if [Casualties] >= 5000 then "Major"
         else if [Casualties] >= 1000 then "Significant"
         else "Minor",
    type text
)
```

---

### Scenario: Filtering Old Data

**Requirement**: Only show disasters from last 3 years

**Power Query M Code**:
```m
= Table.SelectRows(
    #"Previous Step",
    each [Year] >= Date.Year(DateTime.LocalNow()) - 3
)
```

---

## DAX SCENARIOS

### Scenario: Creating Dynamic Title

**Requirement**: Title shows selected year or "All Years"

**DAX**:
```DAX
Dynamic Title = 
"Global Disasters " & 
IF(
    HASONEVALUE(Dim_Date[Year]),
    "(" & VALUES(Dim_Date[Year]) & ")",
    "(2018-2024)"
)
```

**Usage**: Add as Card visual title

---

### Scenario: What-If Analysis

**Requirement**: Show impact if response time reduced by X%

**DAX**:
```DAX
What-If Response Time = 
[Avg Response Time (Hours)] * (1 - 'What-If Parameter'[Value] / 100)

Projected Efficiency = 
[Avg Efficiency Score] + 
    ([Avg Response Time (Hours)] - [What-If Response Time]) * 0.2
```

**Setup**: Modeling → New Parameter

---

### Scenario: Running Total Visualization

**Requirement**: Cumulative casualties over time

**DAX**:
```DAX
Cumulative Casualties = 
CALCULATE(
    [Total Casualties],
    FILTER(
        ALL(Dim_Date),
        Dim_Date[Date] <= MAX(Dim_Date[Date])
    )
)
```

**Usage**: Line chart with Date and this measure

---

## REPORTING SCENARIOS

### Scenario 1: Monthly Executive Report

**Recipients**: C-Suite, Board Members

**Content**:
1. Executive Overview page
2. Key metrics summary
3. YoY comparisons
4. Top 5 highlights
5. Areas of concern

**Format**: PDF export, 2-page max

**Schedule**: First Monday of each month

---

### Scenario 2: Regional Manager Dashboard

**Recipients**: Regional Coordinators

**Content**:
1. Filter to their region
2. Geographic Analysis page
3. Country-level details
4. Agency performance
5. Resource allocation

**Format**: Power BI Service, live updates

**Access**: Row-level security by region

---

### Scenario 3: Donor Impact Report

**Recipients**: Funding Organizations

**Content**:
1. Aid distribution charts
2. Aid coverage ratios
3. Efficiency improvements
4. Success stories (high efficiency events)
5. Future needs projection

**Format**: PowerPoint export with visuals

**Frequency**: Quarterly

---

## ADVANCED ANALYSIS EXAMPLES

### Correlation Analysis

**Question**: Does higher aid lead to faster recovery?

**Analysis**:
1. Create scatter plot
2. X-axis: Aid Amount
3. Y-axis: Recovery Duration
4. Add trend line
5. Calculate R-squared

**DAX for Correlation** (simplified):
```DAX
Aid-Recovery Correlation = 
// Use external tools like Python visual
// Or export data for statistical analysis
```

---

### Predictive Modeling

**Question**: Forecast disaster frequency for 2025

**Approach**:
1. Use built-in Analytics pane
2. Add Forecast to timeline
3. Set confidence interval: 95%
4. Forecast length: 12 months

**Interpretation**:
- Upward trend → Increase preparedness
- Seasonal peaks → Pre-position resources

---

### Outlier Detection

**Question**: Which disasters had unusual characteristics?

**Method**:
1. Calculate statistical bounds
2. Identify outliers
3. Investigate causes

**DAX**:
```DAX
Is Outlier = 
VAR Mean = AVERAGE(Fact_Disasters[Casualties])
VAR StdDev = STDEV.P(Fact_Disasters[Casualties])
VAR CurrentValue = SUM(Fact_Disasters[Casualties])
RETURN
    IF(
        CurrentValue > Mean + (2 * StdDev) ||
        CurrentValue < Mean - (2 * StdDev),
        "Outlier",
        "Normal"
    )
```

---

## INTERACTIVE SCENARIOS

### Scenario: Side-by-Side Comparison

**Requirement**: Compare 2023 vs 2024

**Setup**:
1. Duplicate Overview page
2. Page 1: Filter Year = 2023
3. Page 2: Filter Year = 2024
4. Add navigation buttons
5. Sync slicers for other filters

**Usage**: Click between pages to compare

---

### Scenario: Drill-Through with Context

**Requirement**: Click country to see details

**Setup**:
1. Create "Country Details" page
2. Add drill-through field: Country
3. Add visuals:
   - Country KPIs
   - Disaster timeline
   - Type breakdown
   - Response metrics
4. Add Back button

**Usage**: Right-click country → Drill through

---

## EXPORT SCENARIOS

### Scenario 1: Executive Summary PDF

**Steps**:
1. File → Export → Export to PDF
2. Select: Current Page (Overview)
3. Optimize for: Quality
4. Save as: Disaster_Summary_2024.pdf

---

### Scenario 2: Data Export for Further Analysis

**Steps**:
1. Click visual (e.g., table)
2. More options (...)
3. Export data
4. Format: .xlsx with underlying data
5. Open in Excel for pivot analysis

---

### Scenario 3: PowerPoint Integration

**Steps**:
1. File → Export → Export to PowerPoint
2. Include: Current Page / All Pages
3. Embed actual report or Create image
4. Add narrative slides in PowerPoint

---

## REAL-WORLD USE CASES

### Use Case 1: Emergency Response Planning

**User**: National Disaster Management Agency

**Workflow**:
1. Weekly: Review new disaster trends
2. Monthly: Analyze response performance
3. Quarterly: Update preparedness plans
4. Annually: Budget allocation based on patterns

---

### Use Case 2: Humanitarian Aid Distribution

**User**: International NGO

**Workflow**:
1. Identify underfunded disasters
2. Calculate aid gap
3. Allocate resources by priority
4. Track distribution efficiency
5. Report to donors

---

### Use Case 3: Risk Assessment

**User**: Insurance Company

**Workflow**:
1. Analyze disaster frequency by region
2. Calculate expected loss per disaster type
3. Adjust premiums based on risk
4. Identify high-risk areas for policy adjustments

---

### Use Case 4: Academic Research

**User**: University Disaster Research Center

**Workflow**:
1. Export historical data
2. Statistical analysis of trends
3. Publish findings on response effectiveness
4. Develop predictive models

---

## TROUBLESHOOTING COMMON QUERIES

**Q**: Why are some countries missing from the map?

**A**: Check:
- Country name spelling in data
- Map visual settings (auto-detect off?)
- Data category set to "Country"

**Q**: Why doesn't time intelligence work?

**A**: Verify:
- Date table marked as date table
- Relationship between date tables active
- Continuous date range (no gaps)

**Q**: Why are totals incorrect?

**A**: Review:
- Measure formula (CALCULATE context?)
- Relationships (many-to-many?)
- Filters applied at visual/page level

---

**Document Version**: 1.0  
**Use Cases**: 30+  
**Scenarios**: 15+  
**Target Users**: All levels (Executive to Analyst)
