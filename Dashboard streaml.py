import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#create_day_df()
st.subheader("Season")
 
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(35, 15))
 
colors = ["#90CAF9", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
 
sns.barplot(x="quantity_x", y="product_name", data=day_df.head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel("Number of Sales", fontsize=30)
ax[0].set_title("Best Performing Product", loc="center", fontsize=50)
ax[0].tick_params(axis='y', labelsize=35)
ax[0].tick_params(axis='x', labelsize=30)
 
sns.barplot(x="quantity_x", y="product_name", data=day_df.sort_values(by="quantity_x", ascending=True).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel("Number of Sales", fontsize=30)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Product", loc="center", fontsize=50)
ax[1].tick_params(axis='y', labelsize=35)
ax[1].tick_params(axis='x', labelsize=30)
 
st.pyplot(fig)


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
