import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Main function
def main():
    st.title("Bike Sharing Data Dashboard")

    # Load data
    all_df = pd.read_csv(r'./dashboard/all_data.csv')

    # Pertanyaan 1: Pola Penggunaan Sepeda
    st.header("Pengaruh Musim terhadap jumlah pengguna sepeda")
    st.write("Grafik di bawah ini menunjukkan Pengaruh Musim terhadap jumlah pengguna sepeda.")
    season_data = all_df.groupby('season_x')['cnt_x'].count().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='season_x', y='cnt_x', data=season_data, palette='coolwarm', ax=ax)
    ax.set_title('Pengaruh Musim terhadap jumlah pengguna sepeda')
    ax.set_xlabel('Season (1 = Spring, 2 = Summer, 3 = Fall, 4 = Winter)')
    ax.set_ylabel('Jumlah Pengguna Sepeda')
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

    
    correlation_weather = all_df[['temp_x', 'hum_x', 'windspeed_x', 'cnt_x', 'temp_y', 'hum_y', 'windspeed_y', 'cnt_x']].corr()
    st.title('Hubungan antara Cuaca dan jumlah pengguna sepeda')
    st.write("Visuallisasi di bawah ini menunjukkan hubungan antara cuaca dan jumlah penggunaan sepeda.")
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation_weather, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap - Weather Variables vs. Bike Rental Count')
    st.pyplot(plt)

if __name__ == "__main__":
    main()
