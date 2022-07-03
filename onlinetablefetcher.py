import streamlit as st
import pandas as pd
import requests
import html5lib

def convert_df_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

st.title("Online Table Fetcher")
st.subheader("Developed with 💖 by Svarnarup")
url = st.text_input("Enter link of website:").replace(" ","")
if url == '':
    st.error("Please enter a valid url to proceed.")
elif url != '':
    html = requests.get(url).content
    try:
        df_list = pd.read_html(html)
    except:
        st.error("Oops could not fetch any table.")
    else:
        st.balloons()
        df = df_list[0]
        st.write(df)
        csv = convert_df_csv(df)
        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='example.csv',
            mime='text/csv',
        )
       
