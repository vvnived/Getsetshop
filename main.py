import streamlit as st
import pandas as pd
import base64
import requests
main_bg = "images/Background.jpg"
main_bg_ext = "jpg"
side_bg = "images/website background.jpg"
side_bg_ext = "jpg"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
        background-size: cover
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
)
template = """
   <div style = "background-color : #33F5E6; padding : 1px;">
   <h2 style = "color:white;text-align:center;"> Get.Set.Shop </h2>
   </div>
   """
st.markdown(template, unsafe_allow_html=True)
st.sidebar.title("Get.Set.Shop")
st.sidebar.image("images/logo.png",width = 300)
add_selectbox = st.sidebar.selectbox('Select laptop brand',('dropdown to select','Lenovo','Acer','hp'))
st.image("images/template.png", width=700)
st.write("Scroll down after you select product")
if add_selectbox == "Lenovo":
    radio1 = st.sidebar.radio("Select the Product",("None","Ideapad 3","Ideapad 5"))
    if radio1 == "None":
        st.success("Please select a product for Comparison")
    if radio1 == "Ideapad 3":
        st.success("Here is your comparison chart for Lenovo Ideapad 3")
        df = pd.read_csv("Lenovo ideapad3.csv")
        def make_clickable(link):
            # target _blank to open new window
            # extract clickable text to display for your link
            text = "BUY NOW"
            return f'<a target="_blank" href="{link}">{text}</a>'
        # link is the column with hyperlinks
        df['link'] = df['link'].apply(make_clickable)
        df = df.to_html(escape=False)
        st.write(df, unsafe_allow_html=True)
    if radio1 == "Ideapad 5":
        st.success("Here is your comparison chart for Lenovo Ideapad 5")
        df = pd.read_csv("Lenovo Ideapad5.csv")
        def make_clickable(link):
            # target _blank to open new window
            # extract clickable text to display for your link
            text = "BUY NOW"
            return f'<a target="_blank" href="{link}">{text}</a>'
        # link is the column with hyperlinks
        df['link'] = df['link'].apply(make_clickable)
        df = df.to_html(escape=False)
        st.write(df, unsafe_allow_html=True)
if add_selectbox == "Acer":
    radio2 = st.sidebar.radio("Select the product",("None","Aspire 3","Aspire 5"))
    if radio2 == "None":
        st.success("Please select a product for comparison")
    if radio2 == "Aspire 3":
        st.success("Here is your comparison chart for Acer Aspire 3")
        df = pd.read_csv("Acer Aspire 3.csv")
        def make_clickable(link):
            # target _blank to open new window
            # extract clickable text to display for your link
            text = "BUY NOW"
            return f'<a target="_blank" href="{link}">{text}</a>'
        # link is the column with hyperlinks
        df['link'] = df['link'].apply(make_clickable)
        df = df.to_html(escape=False)
        st.write(df, unsafe_allow_html=True)
    if radio2 == "Aspire 5":
        st.success("Here is your comparison chart for Acer Aspire 5")
        df = pd.read_csv("Acer Aspire 5.csv")
        def make_clickable(link):
            # target _blank to open new window
            # extract clickable text to display for your link
            text = "BUY NOW"
            return f'<a target="_blank" href="{link}">{text}</a>'
        # link is the column with hyperlinks
        df['link'] = df['link'].apply(make_clickable)
        df = df.to_html(escape=False)
        st.write(df, unsafe_allow_html=True)
if add_selectbox == "hp":
    radio3 = st.sidebar.radio("Select the product",("None","Pavillion","Omen 15"))
    if radio3 == "None":
        st.success("Please select a product for comparison")
    if radio3 == "Pavillion":
        st.success("Here is your comparison chart for Hp Pavillion")
        df = pd.read_csv("Hp pavillion.csv")
        def make_clickable(link):
            # target _blank to open new window
            # extract clickable text to display for your link
            text = "BUY NOW"
            return f'<a target="_blank" href="{link}">{text}</a>'
        # link is the column with hyperlinks
        df['link'] = df['link'].apply(make_clickable)
        df = df.to_html(escape=False)
        st.write(df, unsafe_allow_html=True)
    if radio3 == "Omen 15":
        st.success("Here is your comparison chart for Hp Omen 15")
        df = pd.read_csv("Hp Omen.csv")
        def make_clickable(link):
            # target _blank to open new window
            # extract clickable text to display for your link
            text = "BUY NOW"
            return f'<a target="_blank" href="{link}">{text}</a>'
        # link is the column with hyperlinks
        df['link'] = df['link'].apply(make_clickable)
        df = df.to_html(escape=False)
        st.write(df, unsafe_allow_html=True)


