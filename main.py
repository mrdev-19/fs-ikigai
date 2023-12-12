import streamlit as st
from streamlit_option_menu import option_menu
import time
import ikigai_pillow
from PIL import Image, ImageDraw, ImageFont
#---------------------------------------------------
# page config settings:

page_title="Know Your Ikigai"
page_icon="💭"
layout="centered"

st.set_page_config(page_title=page_title,page_icon=page_icon,layout=layout)
st.title(page_title+" "+page_icon)

#--------------------------------------------------
#hide the header and footer     

hide_ele="""
        <style>
        #Mainmenu {visibility:hidden;}
        footer {visibility:hidden;}
        header {visibility:hidden;}
        </style>
        """
st.markdown(hide_ele,unsafe_allow_html=True)
#---------------------------------------------------

with st.form("Ikigai",clear_on_submit=True):
    st.header("Know Your ikigai")
    wyl=st.text_input("What you love?")
    wyga=st.text_input("What are you good at?")
    wtwn=st.text_input("What the world needs?")
    wycp=st.text_input("What you can be paid for?")
    submit_button=st.form_submit_button()
    if(submit_button):
        with st.spinner('Generating your Ikigai...'):
            #we need to adjust the length of the phrases or words accordingly as we need
            img=ikigai_pillow.pic_write([wyl[0:6],wyga[0:6],wtwn[0:6],wycp[0:6]])
            img_path = "ikigai_with_text.jpeg"
            img = Image.open(img_path)
            st.image(img)


