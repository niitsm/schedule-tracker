import pandas as pd
import streamlit as st

# Create a schedule tracker template with predefined tasks
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Morning (5:30-9:00 AM)": [
        "Meditation, Job Search, Gym", 
        "Meditation, Networking, Consulting", 
        "Meditation, Job Applications", 
        "Meditation, Gym, Podcast Planning", 
        "Meditation, Job Search, Outreach", 
        "Meditation, Gym, Strategy Planning", 
        "Meditation, Rest"
    ],
    "Work Hours (9:00 AM - 6:00 PM)": [
        "Current Job Tasks",
        "Current Job Tasks",
        "Current Job Tasks",
        "Current Job Tasks",
        "Current Job Tasks",
        "Consulting Work, Website Updates",
        "Consulting Work, Strategy Review"
    ],
    "Evening (6:00 - 10:00 PM)": [
        "Networking Calls, Podcast Work, TV",
        "Job Applications, Podcast Editing, TV",
        "Consulting Outreach, Gym, TV",
        "Networking, Gym, TV",
        "Job Search Review, TV",
        "Social Time, TV",
        "Relax & TV"
    ],
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
