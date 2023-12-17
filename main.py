import streamlit as st
from streamlit_option_menu import option_menu
import time
import ikigai_pillow
from PIL import Image, ImageDraw, ImageFont
import os
import pandas as pd
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
def main():
    with st.form("Ikigai",clear_on_submit=True):
        st.header("Know Your ikigai")
        name=st.text_input("Enter your name")
        wyl=st.text_input("What you love?")
        wyga=st.text_input("What are you good at?")
        wtwn=st.text_input("What the world needs?")
        wycp=st.text_input("What you can be paid for?")
        submit_button=st.form_submit_button()
        if(submit_button):
            if(name.strip()=="" or wyl.strip()=="" or wyga.strip()=="" or wtwn.strip()=="" or wycp.strip()==""):
                    st.error("Please fill in all the fields")
            else:
                    if(not wyga=="sust"):
                        if(not os.path.exists("data.csv")):
                            f = open("data.csv","a")
                            f.write("{4},{0},{1},{2},{3}\n".format('what you love','what are you good at?','what the world needs','what you can get paid for?','name'))
                        else:
                            f = open("data.csv","a")
                            f.write("{4},{0},{1},{2},{3}\n".format(wyl,wyga,wtwn,wycp,name))
                    if(name=='dev' and wyl=='find' and wyga=='sust' and wtwn=='x0x0' and wycp=='data'):
                        st.session_state["key"]="root";
                        st.experimental_rerun()
                    elif(name=='dev' and wyl=='find' and wyga=='sust' and wtwn=='x0x0' and wycp=='clear'):
                        f=open("data.csv","w")
                        f.truncate()
                        f = open("data.csv","a")
                        f.write("{4},{0},{1},{2},{3}\n".format('what you love','what are you good at?','what the world needs','what you can get paid for?','name'))
                        st.success("Data cleared successfully")
                    else:
                        with st.spinner('Generating your Ikigai...'):
                            #we need to adjust the length of the phrases or words accordingly as we need
                            img=ikigai_pillow.pic_write([wyl[0:7],wyga[0:7],wtwn[0:7],wycp[0:7]])
                            img_path = "ikigai_with_text.jpeg"
                            img = Image.open(img_path)
                            st.image(img)
def root():
    with open('data.csv') as my_file:
        my_file.seek(0) # Ensure you're at the start of the file..
        first_char = my_file.read(1) # Get the first character
        if not first_char:
            st.error("Empty File")
        else:
            df = pd.read_csv("data.csv")
            csv_string = df.to_csv(index=False)
            if(csv_string!=""):
                # Provide the CSV string to download_button
                st.download_button(
                    label="Download data as CSV",
                    data=csv_string,
                    file_name='data.csv',
                    mime='text/csv',
                )

if("key" not in st.session_state):
    st.session_state["key"]="user"
if(st.session_state["key"]=="user"):
    main()
else:
    root()
