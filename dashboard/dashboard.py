import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Main function
def main():
    st.title("Bike Sharing Data Dashboard")

    # Load data
    all_df = pd.read_csv('all_data.csv')

    # Pertanyaan 1: Pola Penggunaan Sepeda
    st.header("Pola Penggunaan Sepeda")
    st.write("Grafik di bawah ini menunjukkan pola penggunaan sepeda selama periode waktu yang diamati.")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(x='dteday', y='cnt_x', data=all_df, ax=ax)
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Penggunaan Sepeda')
    ax.set_title('Pola Penggunaan Sepeda')
    st.pyplot(fig)

    # Pertanyaan 2: Hubungan antara Kondisi Cuaca dan Penggunaan Sepeda
    st.header("Hubungan antara Kondisi Cuaca dan Penggunaan Sepeda")
    st.write("Grafik di bawah ini menunjukkan hubungan antara suhu dan jumlah penggunaan sepeda.")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(x='temp_x', y='cnt_x', data=all_df, ax=ax)
    ax.set_xlabel('Suhu (Celsius)')
    ax.set_ylabel('Jumlah Penggunaan Sepeda')
    ax.set_title('Hubungan antara Suhu dan Penggunaan Sepeda')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
