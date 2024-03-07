#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# In[37]:
with st.sidebar:
    st.title("Proyek Analisi Bike Dataset", )
    st.image("Logo.png", width=300, use_column_width=True)

# Membaca data dari file CSV
day_df = pd.read_csv("day.csv")
day_df.head()


# In[38]:
st.markdown(
    """
    # My first app
    Berdasakan Bike Dataset yang ada dapat menjawab 2 permasalahan dalam bentuk pertanyaan berikut:
    1. Bagaimana tren penggunaan sepeda di sepanjang waktu (dalam instant atau dteday)?
    """
)

# Memilih kolom yang ingin ditampilkan
selected_columns = ['instant', 'dteday', 'season', 'holiday', 'weekday']


# In[39]:


# Menampilkan data hanya dengan kolom yang dipilih
selected_data = day_df[selected_columns]


# In[40]:


# Konversi kolom dteday menjadi tipe data datetime
selected_data['dteday'] = pd.to_datetime(selected_data['dteday'])


# In[41]:


# Plot tren penggunaan sepeda sepanjang waktu
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(selected_data['dteday'], selected_data['instant'], marker='o', linewidth=2, color='b')
ax.set_title('Tren Penggunaan Sepeda sepanjang Waktu')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penggunaan Sepeda (instant)')
ax.grid(True)
st.pyplot(fig)


# In[42]:


# Plot pola penggunaan sepeda yang berkorelasi dengan musim
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(x='season', y='instant', data=selected_data, ax=ax)
ax.set_title('Pola Penggunaan Sepeda berdasarkan Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Penggunaan Sepeda (instant)')
st.pyplot(fig)


# In[ ]:




