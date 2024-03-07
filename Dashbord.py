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
    # BIKE DATASET
    Berdasakan Bike Dataset yang ada dapat menjawab 2 permasalahan dalam bentuk pertanyaan berikut:
    1. Bagaimana tren penggunaan sepeda di sepanjang waktu?
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
st.markdown(
    """
    Berdasakan grafik diatas dapat dilihat bahwa selama rentang tahun 2011 hingga 2013, terjadi peningkatan yang konsisten dalam penggunaan sepeda menurut dataset Bike Sharing. Kenaikan tersebut cukup signifikan setiap tahunnya, mencerminkan minat yang terus meningkat dari masyarakat untuk menggunakan sepeda sebagai moda transportasi. Puncak penggunaan sepeda tercatat pada bulan Oktober 2012 dan September 2013, menunjukkan adanya periode tertentu di mana minat bersepeda mencapai titik tertinggi. Meskipun demikian, tidak terdapat tren musiman yang jelas dalam pola penggunaan sepeda, menandakan bahwa faktor-faktor lain mungkin turut memengaruhi fluktuasi tersebut selain musim.
)
st.markdown(
    """
    2. Apakah ada pola penggunaan sepeda yang berkorelasi dengan musim (season)?
    """
)
# Plot pola penggunaan sepeda yang berkorelasi dengan musim
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(x='season', y='instant', data=selected_data, ax=ax)
ax.set_title('Pola Penggunaan Sepeda berdasarkan Musim')
ax.set_xlabel('Musim')
ax.set_ylabel('Jumlah Penggunaan Sepeda (instant)')
st.pyplot(fig)


# In[ ]:

st.markdown(
    """
    Berdasarkan gambar diatas dapat dilihat bahwa pola penggunaan sepeda dalam Bike Sharing Dataset menunjukkan variasi yang signifikan berdasarkan musim, musim panas menjadi periode dengan rata-rata penggunaan sepeda tertinggi, menandakan bahwa cuaca hangat dan cerah cenderung mendorong masyarakat untuk lebih banyak menggunakan sepeda. Sementara itu, musim semi dan musim gugur menunjukkan rata-rata penggunaan sepeda yang hampir sama, mencerminkan kestabilan aktivitas bersepeda di kedua musim tersebut. Sebaliknya, musim dingin memiliki rata-rata penggunaan sepeda terendah, menandakan bahwa cuaca yang lebih dingin dan kondisi jalan yang mungkin tidak sesuai dapat mengurangi minat masyarakat untuk bersepeda. Perbedaan yang cukup signifikan antara rata-rata penggunaan sepeda pada musim panas dan musim dingin menegaskan pengaruh kuat cuaca terhadap kegiatan bersepeda.
    """
)


