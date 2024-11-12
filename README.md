# Clustering_Countries_for_Strategic_Aid_Allocation
 Clustering Countries for Strategic Aid Allocation


## Problem Statement

HELP International, a humanitarian NGO, aims to utilize its $10 million funds effectively to aid countries in dire need. To achieve this, the CEO needs to categorize countries based on socio-economic and health factors to determine which countries should receive the most aid. The goal is to use data-driven methods to strategically allocate resources and maximize the impact of the aid.

## Need and Use of Solving the Problem Statement

### Need

1. **Strategic Resource Allocation**: Optimize the utilization of $10 million by identifying countries with the highest need for aid.
2. **Data-Driven Decision Making**: Move beyond traditional methods to a more objective, evidence-based approach.
3. **Targeted Intervention**: Tailor aid efforts to address specific challenges in different regions.

### Use

1. **Country Categorization**: Group countries based on socio-economic and health factors to prioritize aid.
2. **Strategic Decision Support**: Provide insights to the CEO for informed decision-making.
3. **Resource Optimization**: Direct funds to countries where they will have the most significant impact.

### Benefits

1. **Maximized Impact**: Enhance the effectiveness of aid.
2. **Efficient Resource Utilization**: Ensure optimal use of funds.
3. **Improved Accountability**: Increase transparency and trust with stakeholders.

## Dataset

- **[Dataset Link](https://drive.google.com/file/d/1IRQWbO9m-c93XjDsbtt2nqv5RVldVPzj/view?usp=drive_link)**

### Data Description

- **Country**: Name of the country
- **Child_mort**: Death of children under 5 years of age per 1000 live births
- **Exports**: Exports of goods and services per capita (% of GDP per capita)
- **Health**: Total health spending per capita (% of GDP per capita)
- **Imports**: Imports of goods and services per capita (% of GDP per capita)
- **Income**: Net income per person
- **Inflation**: Annual growth rate of GDP
- **Life_expec**: Average life expectancy of a newborn
- **Total_fer**: Total fertility rate
- **Gdpp**: GDP per capita

## Approach

### 1. Tableau Visualization

- **Overall Development**: Heatmap and scatter plot matrix to visualize development indicators.
- **Health and Mortality**: Bar chart and scatter plot to explore health and child mortality.
- **Economic Indicators**: Histogram and scatter plot to examine income and trade data.
- **Customizable Filters**: Enable detailed exploration and drill-downs.

### 2. Exploratory Data Analysis (EDA) and Hypothesis Testing

- **Data Cleaning**: Handle missing values and outliers.
- **Univariate Analysis**: Explore distributions and categorical variables.
- **Bivariate Analysis**: Analyze correlations and relationships between variables.
- **Hypothesis Testing**:
  - Health Spending vs. Life Expectancy
  - Fertility vs. Development
  - Income vs. Child Mortality
  - Inflation vs. GDP per Capita

### 3. Machine Learning Modeling

- **Data Preprocessing**: Handle missing values, normalize data, and encode categorical variables.
- **Model Selection**:
  - **K-Means Clustering**: For predefined cluster numbers.
  - **Hierarchical Clustering**: To explore various levels of clustering.
  - **DBSCAN**: For identifying clusters of arbitrary shapes and handling outliers.
- **Model Training and Evaluation**:
  - **Choosing Clusters**: Elbow Method and Silhouette Analysis.
  - **Evaluation Metrics**: Silhouette Coefficient and visualization techniques.

### 4. Deployment

- **Setup**: Create a virtual environment and install necessary libraries.
- **Model Serialization**: Save and load the trained model using pickle or joblib.
- **API Development**: Implement a Flask API to handle data input and prediction.
  - **Endpoints**: Accept country data and return cluster/category.
  - **Response**: JSON format with predicted cluster and key factors.
- **Integration**: Optionally, develop a web interface for easier interaction.

## Why This Approach?

This approach ensures a data-driven, objective method for categorizing countries based on their need for aid. By leveraging exploratory data analysis and machine learning, we can provide precise, actionable insights to HELP International. The use of unsupervised learning techniques allows for effective grouping of countries based on their socio-economic and health characteristics, leading to optimized aid allocation and impactful resource use.