#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# In[32]:


# Membaca data dari file CSV
day_df = pd.read_csv("day.csv")
day_df.head()


# In[28]:


# Memilih kolom yang ingin ditampilkan
selected_columns = ['instant', 'dteday', 'season', 'holiday', 'weekday']


# In[29]:


# Menampilkan data hanya dengan kolom yang dipilih
selected_data = day_df[selected_columns]


# In[33]:


# Konversi kolom dteday menjadi tipe data datetime
selected_data['dteday'] = pd.to_datetime(selected_data['dteday'])


# In[34]:


# Plot tren penggunaan sepeda sepanjang waktu
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(selected_data['dteday'], selected_data['instant'], marker='o', linewidth=2, color='b')
ax.set_title('Tren Penggunaan Sepeda sepanjang Waktu')
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah Penggunaan Sepeda (instant)')
ax.grid(True)
st.pyplot(fig)


# In[35]:


# Plot pola penggunaan sepeda yang berkorelasi dengan musim
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(x='season', y='instant', data=selected_data, ax=ax)
ax.set_title('Pola Penggunaan Sepeda berdasarkan Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Penggunaan Sepeda (instant)')
st.pyplot(fig)


# In[ ]:




