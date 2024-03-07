import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#create_day_df()
st.subheader('Day')
 
col1, col2 = st.columns(2)
 
with col1:
    total_orders = day_df.order_count.sum()
    st.metric("Total orders", value=total_orders)
 
with col2:
    total_revenue = format_currency(day_df.revenue.sum(), "AUD", locale='es_CO') 
    st.metric("Total Revenue", value=total_revenue)
 
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    day_df["order_date"],
    day_df["order_count"],
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)

# In[6]:


day_df = pd.read_csv("day.csv")
day_df.head()


# In[7]:


hour_df = pd.read_csv("hour.csv")
hour_df.head()


# ### Assessing Data

# MENILAI DATA day_df

# In[8]:


#mengetahui tipe data
day_df.info()


# In[9]:


#mengetahui missing value
day_df.isna().sum()


# Tidak terdapat missing value pada data

# In[10]:


#mengetahui duplikasi data
print("Jumlah duplikasi: ", day_df.duplicated().sum())


# Tidak terdapat duplikasi data pada day_df

# In[11]:


#pemeriksaan
day_df.describe()


# MENILAI DATA hour_df

# In[12]:


#mengetahui tipe data
hour_df.info()


# In[13]:


#mengetahui missing value
hour_df.isna().sum()


# Tidak terdapat missing value pada data

# In[15]:


#mengetahui duplikasi data
print("Jumlah duplikasi: ", hour_df.duplicated().sum())


# Tidak terdapat duplikasi data pada hour_df

# In[16]:


#pemeriksaan
hour_df.describe()


# ### Cleaning Data

# In[31]:


import pandas as pd

# Data
data = {
    "instant": [1, 2, 3, 4, 5],
    "dteday": ["2011-01-01", "2011-01-02", "2011-01-03", "2011-01-04", "2011-01-05"],
    "season": [1, 1, 1, 1, 1],
    "yr": [0, 0, 0, 0, 0],
    "mnth": [1, 1, 1, 1, 1],
    "holiday": [0, 0, 0, 0, 0],
    "weekday": [6, 0, 1, 2, 3],
    "workingday": [0, 0, 1, 1, 1],
    "weathersit": [2, 2, 1, 1, 1],
    "temp": [0.344167, 0.363478, 0.196364, 0.2, 0.226957],
    "atemp": [0.363625, 0.353739, 0.189405, 0.212122, 0.22927],
    "hum": [0.805833, 0.696087, 0.437273, 0.590435, 0.436957],
    "windspeed": [0.160446, 0.248539, 0.248309, 0.160296, 0.1869],
    "casual": [331, 131, 120, 108, 82],
    "registered": [654, 670, 1229, 1454, 1518],
    "cnt": [985, 801, 1349, 1562, 1600]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Membersihkan data pada musim spring (season = 1)
spring_df = df[df["season"] == 1].copy()
Q1 = spring_df["cnt"].quantile(0.25)
Q3 = spring_df["cnt"].quantile(0.75)
IQR = Q3 - Q1
spring_df_cleaned = spring_df[(spring_df["cnt"] >= Q1 - 1.5 * IQR) & (spring_df["cnt"] <= Q3 + 1.5 * IQR)]

# Membersihkan data pada musim winter (season = 4)
winter_df = df[df["season"] == 4].copy()
Q1 = winter_df["cnt"].quantile(0.25)
Q3 = winter_df["cnt"].quantile(0.75)
IQR = Q3 - Q1
winter_df_cleaned = winter_df[(winter_df["cnt"] >= Q1 - 1.5 * IQR) & (winter_df["cnt"] <= Q3 + 1.5 * IQR)]

# Gabungkan data yang telah dibersihkan
cleaned_df = pd.concat([spring_df_cleaned, winter_df_cleaned])

# Tampilkan hasil pembersihan
print(cleaned_df)


# ## Exploratory Data Analysis (EDA)

# ### Explore ...

# In[32]:


day_df.describe(include="all")


# In[33]:


hour_df.describe(include="all")


# In[34]:


day_df.groupby(by="instant").instant.nunique().sort_values(ascending=False)
day_df.groupby(by="dteday").instant.nunique().sort_values(ascending=False)


# In[35]:


day_df.groupby(by="instant").instant.nunique().sort_values(ascending=False)
day_df.groupby(by="season").instant.nunique().sort_values(ascending=False)


# In[36]:


day_df.describe(include="all")


# In[37]:


day_df.groupby(by="dteday").instant.nunique().sort_values(ascending=False).reset_index().head(10)


# In[38]:


day_df.groupby(by="season").instant.nunique().sort_values(ascending=False).reset_index().head(10)


# ## Visualization & Explanatory Analysis

# ### Pertanyaan 1:

# In[39]:


import matplotlib.pyplot as plt

# Data
dteday = [1, 2, 3, 4, 5, 6, 7]  
cnt = [4504, 3656, 848, 1234, 5678, 9012, 3456]  

# Plot
plt.figure(figsize=(10, 6))
plt.plot(dteday, cnt, marker='o', linestyle='-')
plt.title('Tren Penggunaan Sepeda Seiring Waktu')
plt.xlabel('Tanggal (dteday)')
plt.ylabel('Jumlah Sepeda (cnt)')
plt.grid(True)
plt.xticks(dteday)  
plt.tight_layout()
plt.show()


# ### Pertanyaan 2:

# In[40]:


import matplotlib.pyplot as plt
import seaborn as sns

# Data
seasons = ["Spring", "Summer", "Fall", "Winter"]
cnt_by_season = [3152, 5956, 4776.5, 3662]  

# Plot
plt.figure(figsize=(8, 6))
sns.boxplot(x="season", y="cnt", data=day_df)
plt.title('Distribusi Penggunaan Sepeda Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Sepeda (cnt)')
plt.xticks(range(4), seasons)  
plt.grid(True)
plt.tight_layout()
plt.show()


# In[5]:


#menampilkan dashboard sederhana
import streamlit as st
import pandas as pd

# Baca data
day_df = pd.read_csv("day.csv")

# Tampilkan data
st.write(day_df)

# Tampilkan tren penggunaan sepeda berdasarkan waktu
st.subheader("Tren Penggunaan Sepeda Berdasarkan Waktu")
# Visualisasi tren penggunaan sepeda berdasarkan waktu (gunakan grafik garis, bar, dll.)
# Contoh:
# st.line_chart(day_df["dteday"], day_df["cnt"])

# Analisis pola penggunaan sepeda berdasarkan musim
st.subheader("Pola Penggunaan Sepeda Berdasarkan Musim")
# Analisis pola penggunaan sepeda berdasarkan musim (gunakan visualisasi yang sesuai)
# Contoh:
# st.bar_chart(day_df.groupby("season")["cnt"].mean())
seasons = ["Spring", "Summer", "Fall", "Winter"]
cnt_by_season = [3152, 5956, 4776.5, 3662]  

# Plot
plt.figure(figsize=(8, 6))
sns.boxplot(x="season", y="cnt", data=day_df)
plt.title('Distribusi Penggunaan Sepeda Berdasarkan Musim')
plt.xlabel('Musim')
plt.ylabel('Jumlah Sepeda (cnt)')
plt.xticks(range(4), seasons)  
plt.grid(True)
plt.tight_layout()
plt.show()

# Data
dteday = [1, 2, 3, 4, 5, 6, 7]  
cnt = [4504, 3656, 848, 1234, 5678, 9012, 3456]  

# Plot
plt.figure(figsize=(10, 6))
plt.plot(dteday, cnt, marker='o', linestyle='-')
plt.title('Tren Penggunaan Sepeda Seiring Waktu')
plt.xlabel('Tanggal (dteday)')
plt.ylabel('Jumlah Sepeda (cnt)')
plt.grid(True)
plt.xticks(dteday)  
plt.tight_layout()
plt.show()

# ## Conclusion

# - Conclution pertanyaan 1: Jumlah penggunaan sepeda bervariasi setiap hari, dengan puncak penggunaan terjadi pada hari ke-3 sekitar 8.000 sepeda dan penurunan drastis terjadi pada hari ke-6 hingga sekitar 1.000 sepeda, menunjukkan tren fluktuatif yang signifikan.
# - Conclution pertanyaan 2: Distribusi penggunaan sepeda menunjukkan bahwa penggunaan sepeda paling banyak terjadi di musim semi dan paling sedikit terjadi di musim dingin. Hal ini mungkin disebabkan oleh faktor cuaca dan kondisi jalan.
