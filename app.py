import streamlit as st
import pandas as pd
import pyodbc

# 1. Konfigurasi Navigasi Halaman
# Menggunakan session_state agar state halaman tidak ter-reset saat tombol ditekan
if 'page' not in st.session_state:
    st.session_state.page = 1

def next_page():
    if st.session_state.page < 3:
        st.session_state.page += 1

def prev_page():
    if st.session_state.page > 1:
        st.session_state.page -= 1

# 2. Fungsi Koneksi ke SQL Server
@st.cache_resource # Memastikan koneksi stabil dan tidak dieksekusi berulang kali
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-JCGQILKU;" # Sesuaikan dengan nama server lokal
        "DATABASE=Company;"
        "Trusted_Connection=yes;"
    )

try:
    conn = init_connection()
except Exception as e:
    st.error(f"Koneksi gagal: {e}")
    st.stop()

st.title("Tugas 07 - Basis Data Interface")

# 3. Logika Pemrosesan Berdasarkan Halaman
if st.session_state.page == 1:
    st.header("1. Karyawan dengan Tanggungan")
    query = """
    SELECT DISTINCT 
        CONCAT(e.first_name, ' ', e.last_name) AS nama_lengkap, 
        'Memiliki Tanggungan' AS status_tanggungan 
    FROM employees e 
    INNER JOIN dependents d ON e.employee_id = d.employee_id
    """
    df = pd.read_sql(query, conn)
    st.dataframe(df, use_container_width=True, hide_index=True)

elif st.session_state.page == 2:
    st.header("2. Analisis Geografis Global")
    query = """
    SELECT 
        r.region_name, 
        ISNULL(c.country_name, 'Belum Terdaftar') AS country_name, 
        COUNT(d.department_id) AS total_departemen
    FROM regions r
    LEFT JOIN countries c ON r.region_id = c.region_id
    LEFT JOIN locations l ON c.country_id = l.country_id
    LEFT JOIN departments d ON l.location_id = d.location_id
    GROUP BY r.region_name, c.country_name
    ORDER BY r.region_name
    """
    df = pd.read_sql(query, conn)
    st.dataframe(df, use_container_width=True, hide_index=True)

elif st.session_state.page == 3:
    st.header("3. Evaluasi Rentang Gaji")
    query = """
    SELECT 
        CONCAT(e.first_name, ' ', e.last_name) AS nama_lengkap, 
        e.salary AS gaji_saat_ini, 
        (j.max_salary - e.salary) AS salary_gap
    FROM employees e
    INNER JOIN jobs j ON e.job_id = j.job_id
    """
    df = pd.read_sql(query, conn)
    st.dataframe(df, use_container_width=True, hide_index=True)

# 4. Tombol Navigasi Halaman Web
st.write("---")
col1, col2, col3 = st.columns([1, 8, 1])

with col1:
    if st.session_state.page > 1:
        st.button("« Before", on_click=prev_page)

with col3:
    if st.session_state.page < 3:
        st.button("Next »", on_click=next_page)
