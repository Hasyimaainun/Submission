import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
@st.cache_data
def load_data():
    day_url = 'https://raw.githubusercontent.com/Hasyimaainun/Analisis-Data/refs/heads/main/day.csv'
    hour_url = 'https://raw.githubusercontent.com/Hasyimaainun/Analisis-Data/refs/heads/main/hour.csv'
    
    df_day = pd.read_csv(day_url, delimiter=',')
    df_hour = pd.read_csv(hour_url, delimiter=',')
    
    df_day['dteday'] = pd.to_datetime(df_day['dteday'])
    df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])

    # Create 'year' column from 'yr'
    df_day['year'] = df_day['yr'].map({0: 2011, 1: 2012})
    return df_day, df_hour

df_day, df_hour = load_data()

# Page Layout
st.title("🚲 Bike Rental Analysis Dashboard")

# Section: Daily Rentals
st.subheader('Daily Rentals')

# Compute Metrics for Daily Rentals
daily_rent_casual = df_day['casual'].sum()
daily_rent_registered = df_day['registered'].sum()
daily_rent_total = df_day['cnt'].sum()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Casual User', value=daily_rent_casual)

with col2:
    st.metric('Registered User', value=daily_rent_registered)

with col3:
    st.metric('Total User', value=daily_rent_total)

# Insights Section
st.header("Dataset Overview")
st.subheader("Day Dataset")
st.write(df_day.head())

st.subheader("Hour Dataset")
st.write(df_hour.head())

st.subheader("Dataset Statistics")
st.write("### Day Dataset Statistics")
st.write(df_day.describe())

st.write("### Hour Dataset Statistics")
st.write(df_hour.describe())

# Visualizations
st.header("Exploratory Data Analysis")

# Correlation Heatmap
def plot_correlation(df, title):
    correlation_matrix = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title(title)
    st.pyplot(plt)

st.subheader("Correlation Heatmap")
if st.checkbox("Show Correlation for Day Dataset"):
    plot_correlation(df_day, "Correlation Matrix for Day Dataset")

if st.checkbox("Show Correlation for Hour Dataset"):
    plot_correlation(df_hour, "Correlation Matrix for Hour Dataset")

# Histogram
st.subheader("Histogram of Day Dataset")
fig, ax = plt.subplots(figsize=(12, 10))
df_day.hist(ax=ax, bins=30)
plt.suptitle('Histogram for Day Dataset', y=1.02)
st.pyplot(fig)

# Question 1: Bike Rental Trends Based on Time and Season
st.header("Question 1: Bike Rental Trends Based on Time and Season")
plt.figure(figsize=(12, 6))
sns.lineplot(x="hr", y="cnt", hue="season", data=df_hour, estimator="mean", ci=None, palette="tab10")
plt.title("Bike Rental Trend Based on Time (Hour) and Season")
plt.xlabel("Hour")
plt.ylabel("Mean of Rent (cnt)")
plt.legend(title="Season", labels=["1: Spring", "2: Summer", "3: Autumn", "4: Winter"])
st.pyplot(plt)

# Dynamic Insights for Question 1
peak_hours = df_hour.groupby('hr')['cnt'].mean().sort_values(ascending=False).head(2).index.tolist()
peak_seasons = df_hour.groupby('season')['cnt'].mean().sort_values(ascending=False).index.tolist()

st.write("**Insights:**")
st.write(f"- Bike rentals peak during rush hours: {peak_hours[0]}:00 and {peak_hours[1]}:00.")
st.write(f"- The highest rentals occur in seasons: {peak_seasons[0]} (highest) and {peak_seasons[1]} (second highest).")

# Question 2: Bike Rental Trends Between 2011 and 2012
st.header("Question 2: Bike Rental Trends Between 2011 and 2012")
total_rent_per_year = df_day.groupby('year')['cnt'].sum()
monthly_trend = df_day.groupby(['year', 'mnth'])['cnt'].mean().reset_index()

trend_2011 = monthly_trend[monthly_trend['year'] == 2011]
trend_2012 = monthly_trend[monthly_trend['year'] == 2012]

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(trend_2011['mnth'], trend_2011['cnt'], label='2011', marker='o', linestyle='-')
ax.plot(trend_2012['mnth'], trend_2012['cnt'], label='2012', marker='o', linestyle='--')
ax.set_title('Comparison of Monthly Bike Rental Trends in 2011 and 2012')
ax.set_xlabel('Month')
ax.set_ylabel('Average Number of Bike Rentals')
ax.set_xticks(range(1, 13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Dynamic Insights for Question 2
highest_month_2011 = trend_2011.loc[trend_2011['cnt'].idxmax(), 'mnth']
highest_month_2012 = trend_2012.loc[trend_2012['cnt'].idxmax(), 'mnth']
st.write("**Insights:**")
st.write(f"- Bike rentals in 2012 are significantly higher compared to 2011 across all months.")
st.write(f"- The highest rental increase is in 2012, peaking in month {highest_month_2012}. In 2011, the peak was in month {highest_month_2011}.")
