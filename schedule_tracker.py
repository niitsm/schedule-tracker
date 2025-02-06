{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import pandas as pd\
import streamlit as st\
\
# Create a schedule tracker template\
data = \{\
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],\
    "Morning (5:30-9:00 AM)": ["", "", "", "", "", "", ""],\
    "Work Hours (9:00 AM - 6:00 PM)": ["", "", "", "", "", "", ""],\
    "Evening (6:00 - 10:00 PM)": ["", "", "", "", "", "", ""],\
    "Personal Goals Achieved (\uc0\u10004 /\u10008 )": ["", "", "", "", "", "", ""]\
\}\
\
# Create DataFrame\
schedule_df = pd.DataFrame(data)\
\
# Streamlit App for Mobile-Friendly Interface\
st.title("Weekly Schedule Tracker")\
st.write("Update your schedule below:")\
\
# Editable Table\
data_editable = st.experimental_data_editor(schedule_df, num_rows="dynamic")\
\
# Save Updated Data\
if st.button("Save Schedule"):\
    st.success("Schedule updated successfully!")\
}