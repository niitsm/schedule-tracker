import pandas as pd
import streamlit as st

# Create a schedule tracker template
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Morning (5:30-9:00 AM)": ["", "", "", "", "", "", ""],
    "Work Hours (9:00 AM - 6:00 PM)": ["", "", "", "", "", "", ""],
    "Evening (6:00 - 10:00 PM)": ["", "", "", "", "", "", ""],
    "Personal Goals Achieved (✔/✘)": ["", "", "", "", "", "", ""]
}

# Create DataFrame
schedule_df = pd.DataFrame(data)

# Streamlit App for Mobile-Friendly Interface
st.title("Weekly Schedule Tracker")
st.write("Update your schedule below:")

# Editable Table
data_editable = st.data_editor(schedule_df, num_rows="dynamic")

# Save Updated Data
if st.button("Save Schedule"):
    st.success("Schedule updated successfully!")
