import streamlit as st

# Fungsi untuk menghitung kerapatan
def calculate_density(weight, volume):
    return weight / volume

# Fungsi untuk menghitung persamaan regresi linear
def calculate_regression(x, y):
    n = len(x)
    x_mean = sum(x) / n
    y_mean = sum(y) / n

    # Menghitung slope (m) dan intercept (c) dari persamaan regresi
    numerator = sum((x_val - x_mean) * (y_val - y_mean) for x_val, y_val in zip(x, y))
    denominator = sum((x_val - x_mean) ** 2 for x_val in x)

    # Penanganan pembagian oleh nol
    if denominator == 0:
        slope = 0
        intercept = y_mean
    else:
        slope = numerator / denominator
        intercept = y_mean - slope * x_mean

    return slope, intercept

def main():
    st.title('Kalkulator Regresi Linear untuk Kerapatan')

    # Input jumlah data konsentrasi
    num_data = st.number_input('Masukkan jumlah data konsentrasi:', min_value=1, step=1)

    # List untuk menyimpan nilai konsentrasi dan kerapatan
    x_data = []
    y_data = []
    density_data = []

    # Input data konsentrasi dan bobot
    st.write("Masukkan data konsentrasi dan bobot labu takar untuk perhitungan kerapatan:")
    for i in range(num_data):
        konsentrasi = st.number_input(f'Masukkan nilai konsentrasi data {i+1}:')
        bobot_filled = st.number_input(f'Masukkan nilai rerata bobot labu takar isi {i+1}:')
        bobot_empty = st.number_input(f'Masukkan nilai rerata bobot labu takar kosong {i+1}:')
        
        # Menghitung bobot sebenarnya
        weight = bobot_filled - bobot_empty

        # Menghitung kerapatan
        density = calculate_density(weight, 100)  # Volume larutan 100 mL
        x_data.append(konsentrasi)
        y_data.append(density)
        density_data.append((konsentrasi, density))

    # Hitung persamaan regresi
    slope, intercept = calculate_regression(x_data, y_data)

    # Tampilkan hasil persamaan regresi
    st.write(f'Persamaan Regresi: y = {slope:.2f}x + {intercept:.2f}')

    # Tampilkan hasil perhitungan kerapatan untuk setiap konsentrasi
    st.write("Hasil Perhitungan Kerapatan untuk Setiap Konsentrasi:")
    for konsentrasi, density in density_data:
        st.write(f'Konsentrasi: {konsentrasi}, Kerapatan: {density:.2f} g/mL')

    # Tampilkan kurva linear dengan range kenaikan yang diperkecil
    min_x = min(x_data)
    max_x = max(x_data)
    min_y = min(y_data)
    max_y = max(y_data)
    range_x = max_x - min_x
    range_y = max_y - min_y
    st.write("Kurva Regresi Linear:")
    st.line_chart(y_data)

if __name__ == '__main__':
    main()
