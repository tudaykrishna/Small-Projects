import streamlit as st
from Langchain import generate

st.title("Restaurant Name Generator")

cuisine= st.sidebar.selectbox("Pick a Cuisine",("","Indian","Italian","Mexican","American","Japanese","Thai"))





if cuisine:
    response=generate(cuisine)
    st.header(response['restaurant_name'].strip())

    menu=response['menu_items'].strip().split(",")


    st.write("**Menu Items**")

    for item in menu:
        st.write("*",item)

