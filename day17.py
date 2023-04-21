import streamlit as st

st.title('st.secrets')

st.write("My_username:", st.secrets["Username"])
st.write("MY_password:", st.secrets["Password"])

# import os
#
# st.write(
#     os.
# )