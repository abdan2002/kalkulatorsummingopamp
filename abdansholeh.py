import streamlit as st
from streamlit_option_menu import option_menu
import math
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
    
selected = option_menu ("Kalkulator Summing OP-AMP",
    ["Home",
    "Rangkaian Penjumlahan Op-Amp",],
    default_index=0)

if(selected == "Home") :
    st.header("Kalkulator Perhitungan Rangkaian Penjumlah Op-Amp")
    st.subheader("By Abdan Reza Raihan (11-2021-006)")
    st.write("Program ini dibuat untuk memenuhi Tugas Besar Elektronika Analog\nDosen Pengampu : Ir. Rustamaji M.T")

if(selected == "Rangkaian Penjumlahan Op-Amp") :
    st.title("Contoh Rangkaian Penjumlah Op-Amp")
    st.image("a.jpg", width = 500)
    st.title("Rumus Rangkain Penjumlah Op-Amp")
    st.image("b.jpg", width = 500)
    st.subheader("Perhitungan Vo pada Rangkaian Penjumlahan Op-Amp dan Simulasi Sinyal Output")

    a=st.number_input("Masukkan Nilai VCC (Volt)",0.00)
    b=st.number_input("Masukkan Nilai R1 (Ohm)",0.00)
    c=st.number_input("Masukkan Nilai R2 (Ohm)",0.00)
    d=st.number_input("Masukkan Nilai R3 (Ohm)",0.00)
    h=st.number_input("Masukan Nilai Rf (Ohm)",0.00)
    e=st.number_input("Masukkan Nilai V1 (Volt)",0.00)
    h=st.number_input("Masukkan nilai frekuensi V1 (Hz)")
    f=st.number_input("Masukkan Nilai V2 (Volt)",0.00)
    i=st.number_input("Masukkan nilai frekuensi V2 (Hz)")
    g=st.number_input("Masukkan Nilai V3 (Volt)",0.00)
    j=st.number_input("Masukkan nilai frekuensi V3 (Hz)")
    perhitungan = st.button("Vo dan Sinyal Output")

    if perhitungan :
        vo=-(((h/b)*e)+((h/c)*f)+((h/d)*g))
        
        st.write("Hasil Vo dan Hasil Simulasi Output")

        def sinusoidal():
            t = np.linspace(-0.05, 0.05, 1000)
            phase_shift = 180  # Phase shift in degrees
            
            # Calculate the sinusoidal signal
            hasil_Vi1 = e * np.sin(2 * np.pi * h * t + np.deg2rad(phase_shift))
            hasil_Vi2 = f * np.sin(2 * np.pi * i * t + np.deg2rad(phase_shift))
            hasil_Vi3 = g * np.sin(2 * np.pi * j * t + np.deg2rad(phase_shift))
            hasil_Vo = vo*((np.sin(2 * np.pi * h * t + np.deg2rad(phase_shift)))+(np.sin(2 * np.pi * i * t + np.deg2rad(phase_shift)))+(np.sin(2 * np.pi * j * t + np.deg2rad(phase_shift))))
            if perhitungan:

                fig, (ax1, ax2,ax3,ax4) = plt.subplots(4, 1, figsize=(20, 15))
                
                ax1.plot(t, hasil_Vi1)
                ax1.set_xlabel('Waktu (s)')
                ax1.set_ylabel('Amplitudo (V)')
                ax1.set_title('Sinyal Vi1')
                ax1.grid(True)
                ax1.set_xlim(-0.05, 0.05)

                ax2.plot(t, hasil_Vi2)
                ax2.set_xlabel('Waktu (s)')
                ax2.set_ylabel('Amplitudo (V)')
                ax2.set_title('Sinyal Vi2')
                ax2.grid(True)
                ax2.set_xlim(-0.05, 0.05)

                ax3.plot(t, hasil_Vi3)
                ax3.set_xlabel('Waktu (s)')
                ax3.set_ylabel('Amplitudo (V)')
                ax3.set_title('Sinyal Vi3')
                ax3.grid(True)
                ax3.set_xlim(-0.05, 0.05)

                ax4.plot(t, hasil_Vo)
                ax4.set_xlabel('Waktu (s)')
                ax4.set_ylabel('Amplitudo (V)')
                ax4.set_title('Sinyal Vo')
                ax4.grid(True)
                ax4.set_xlim(-0.05, 0.05)

                plt.tight_layout()
                st.pyplot(fig)
        sinusoidal()