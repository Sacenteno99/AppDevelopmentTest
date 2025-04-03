import streamlit as st

st.title('My streamlit app')
st.write('Hello World!')

if st.button('Load Data'):
    file = st.file_uploader("Upload a CSV file", type="csv")
    if file is not None:
        df = pd.read_csv(file)
        st.write(df)