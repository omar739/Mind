import streamlit as st
st.image("Mind_cloud.jpg")
st.header("Mind Cloud Basic Training Roadmap - 2025")

tab1 , tab2 , tab3 , tab4 = st.tabs(["Phase 1 :  Software","Phase 2 :  Hardware and Electronics","Phase 3 :  Microcontroller","Phase 4 :  AI and Computer vision"])

with tab1 :
    st.subheader("[ 1 ] Git and GitHub")
    st.subheader("[ 2 ] Introduction to C++")
    st.subheader("[ 3 ] Introduction to python")
    st.subheader("[ 4 ] Object oriented programming ( oop )")
    
with tab2  :
    st.subheader("[ 1 ] Introduction to Electronics - 1 ")
    st.write("Resistor - Capacitor - Inductor - Diode - Transistor - optocoupler")
    st.subheader("[ 2 ] Introduction to Electronics - 2 ")
    st.write("Voltage Regulator - Mosfet - opamp ")
    st.subheader("[ 3 ] PCB Design basics ")
with tab3 :
    st.subheader("[ 1 ] Microcontroller Hardware")
    st.subheader("[ 2 ] Microcontroller Software")
    st.subheader("[ 3 ] Connections protocols")
with tab4 :
    st.subheader("[ 1 ] Introduction to Machine Learning")
    st.write("Logistic Regression - RandomForest ")
    st.subheader("[ 2 ] Introduction to Computer vision using OpenCV")
    st.subheader("[ 3 ] Image processing principles")