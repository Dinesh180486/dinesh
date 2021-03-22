import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as s


st.title("User interface")
st.write("user name : DINESH")
a =st.file_uploader("upload files",type=['csv'])
Button = st.button("output")
if Button==True:
    df=pd.read_csv(a)
    st.write(df.head())

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.scatter(
        df["petal.length"],
        df["sepal.length"],)

    ax.set_xlabel("petal.length")
    ax.set_ylabel("sepal.length")

    st.write(fig)
