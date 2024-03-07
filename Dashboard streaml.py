import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style="dark")

all_df = pd.read_csv('day.csv')
datetime_columns = ["datetime"]
all_df.sort_values(by="datetime", inplace=True)
all_df.reset_index(inplace=True)
 
for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

min_date = all_df["datetime"].min()
max_date = all_df["datetime"].max()

with st.sidebar:
    st.title("Dashboard", )
    st.image("dashboard/Logo.png", width=300, use_column_width=True)

    start_date, end_date = st.date_input(
        "Select date range",
        [min_date, max_date]
    )

    st.selectbox("Select a station", all_df["station"].unique())

st.header('PRSA Water Quality :sparkles:')

# Water Quality Over Time
st.subheader('Overall Water Quality')

col1, col2 = st.columns(2)

with col1:
    overall_quality = round(all_df["Overall_Air_Quality"].max(), 1)
    st.metric("Rata-rata partikel Tertinggi (Buruk)", value=overall_quality)

with col2:
    overall_quality = round(all_df["Overall_Air_Quality"].min(), 1)
    st.metric("Rata-rata partikel Terendah (Bagus)", value=overall_quality)
    
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    all_df["datetime"],
    all_df["Overall_Air_Quality"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)

# Water Quality by City
st.subheader('Overall City Water Quality')
fig, ax = plt.subplots(figsize=(16, 8))
colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    y = "Overall_Air_Quality",
    x = "station",
    data = all_df.sort_values(by="Overall_Air_Quality", ascending=True),
    palette = colors,
    legend = True,
    ci=None,
    ax=ax
)

ax.set_title("Water Quality in China", fontsize=20)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=12)
st.pyplot(fig)

# Rainfall and Preesure Analysis
st.subheader('Rainfall and Temperature Analysis')

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(16, 8))
    sns.barplot(
        y = "RAIN",
        x = "year",
        data = all_df,
        hue= "station",
        legend = True,
        ax=ax,
        ci=None
    )

    ax.set_title("Rainfall Analysis", fontsize=20)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=12)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(16, 8))
    sns.barplot(
        y = "TEMP",
        x = "year",
        data = all_df,
        hue = "station",
        legend = True,
        ax=ax,
        ci=None
    )

    ax.set_title("Temperature Analysis", fontsize=20)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=12)
    st.pyplot(fig)


# Dataframe Table
st.subheader('Dataframe Table')
st.dataframe(all_df[["station", "datetime", "PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "Overall_Air_Quality"]], width=1000, height=500)
    
# Analisis lanjutan : Timeanalysis
st.subheader('Time Analysis')
all_df['datetime'] = pd.to_datetime(all_df['datetime'])
all_df.set_index('datetime', inplace=True)

col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(all_df['PM2.5'], color='blue')
    ax.set_title('Time Series Plot of PM2.5')
    ax.set_xlabel('Date')
    ax.set_ylabel('PM2.5 Level')
    ax.grid(True)
    st.pyplot(fig)
    st.markdown("<h6 style='text-align: center;'>PM2.5 plot</h6>", unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(all_df['PM10'], color='purple')
    ax.set_title('Time Series Plot of PM10')
    ax.set_xlabel('Date')
    ax.set_ylabel('PM10 Level')
    ax.grid(True)
    st.pyplot(fig)
    st.markdown("<h6 style='text-align: center;'>PM10 plot</h6>", unsafe_allow_html=True)
    
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(all_df['SO2'], color='green')
    ax.set_title('Time Series Plot of SO2')
    ax.set_xlabel('Date')
    ax.set_ylabel('SO2 Level')
    ax.grid(True)
    st.pyplot(fig)
    st.markdown("<h6 style='text-align: center;'>SO2 plot</h6>", unsafe_allow_html=True)

with col2:
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(all_df['NO2'], color='orange')
    ax.set_title('Time Series Plot of NO2')
    ax.set_xlabel('Date')
    ax.set_ylabel('NO2 Level')
    ax.grid(True)
    st.pyplot(fig)
    st.markdown("<h6 style='text-align: center;'>NO2 plot</h6>", unsafe_allow_html=True)


    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(all_df['CO'], color='red')
    ax.set_title('Time Series Plot of CO')
    ax.set_xlabel('Date')
    ax.set_ylabel('CO Level')
    ax.grid(True)
    st.pyplot(fig)
    st.markdown("<h6 style='text-align: center;'>CO plot</h6>", unsafe_allow_html=True)

    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(all_df['O3'], color='black')
    ax.set_title('Time Series Plot of O3')
    ax.set_xlabel('Date')
    ax.set_ylabel('O3 Level')
    ax.grid(True)
    st.pyplot(fig)
    st.markdown("<h6 style='text-align: center;'>O3 plot</h6>", unsafe_allow_html=True)






