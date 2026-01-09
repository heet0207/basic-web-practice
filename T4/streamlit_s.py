# import streamlit as st

# st.set_page_config(
#     page_title="Hello Streamlit",
#     page_icon="👋",
#     layout="centered"
# )

# st.title('Welcome to Streamlit! 👋')
# st.header("This is a header")
# st.subheader("This is a subheader")
# st.text("st.text() is some regular text.")
# st.write("st.write() is a write function that can display various types of content.")
# st.markdown("**st.markdown() is a markdown text with bold and italic formatting.**")

# code_example = '''def add(a, b):
#     return a + b

# result = add(5, 7)
# print(result)
# '''
# st.code(code_example, language='python')
# import streamlit as st
# help(st.code)


# import streamlit as st 
# st.set_page_config(page_title="Faculty Profile", page_icon=" ", layout="wide") 
# st.title(" Faculty Profile Demo") 
# st.markdown("This example shows how to use **sidebar**, **columns**, and **expanders**.") # Sidebar – Important for filters/settings 
# st.sidebar.header("Profile Settings")
# faculty_name = st.sidebar.text_input("Faculty Name","Parth Sinroza")
# department = st.sidebar.selectbox("Department", ["Computer Engineering", "IT", "AI/ML", "CSE","CSD"]) 
# experience = st.sidebar.slider("Years of Experience", 0, 40, 10) 
# st.sidebar.markdown("---") 
# st.sidebar.write("You can put filters, toggles, etc. in the sidebar.") # Main content – using columns 
# col1, col2 = st.columns([1, 2]) # 1:2 ratio 
# with col1: 
#     st.subheader("Basic Info") 
#     st.write(f"**Name:** {faculty_name}") 
#     st.write(f"**Department:** {department}") 
#     st.write(f"**Experience:** {experience} years") 
    
# with col2: 
#     st.subheader("About") 
#     st.markdown(""" Use this area to show detailed information about the faculty member, such as research interests, publications, and courses handled. """) 
#     # Expander – for optional/extra info 
# with st.expander("Show Courses Handled"): 
#     st.write("- Data Structures") 
#     st.write("- Machine Learning") 
#     st.write("- Database Management Systems") 
# with st.expander("Show Publications"): 
#     st.write("1. Research Paper A (2021)") 
#     st.write("2. Research Paper B (2023)")
    
    
    
# import streamlit as st 
# st.title("Number Input & Slider Demo") 
# age = st.number_input("Enter your age:", min_value=0, max_value=100, value=15) 
# rating = st.slider("Rate this session (1–10):", min_value=1, max_value=10, value=7) 
# st.write(f"Your age: {age}") 
# st.write(f"You rated this workshop: {rating}/10")

# import streamlit as st 
# st.title("Selection Widgets Demo") 
# course = st.selectbox( "Select Course:", ["DAA", "CN", "TE-I", "EEF"] ) 
# preferred_days = st.multiselect( "Preferred Days for Extra Lectures", 
#                                 ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] 
#                         )
# delivery_mode = st.radio(
#     "Preferred Delivery Mode:", ["Offline", "Online", "Hybrid"] 
# ) 
# subscribe = st.checkbox("Subscribe to course updates?") 
# st.write("---") 
# st.write(f"**Course:** {course}") 
# st.write(f"**Preferred Days:** {', '.join(preferred_days) if preferred_days else 'None'}") 
# st.write(f"**Delivery Mode:** {delivery_mode}") 
# st.write(f"**Subscribed:** {'Yes' if subscribe else 'No'}")


import streamlit as st 
from datetime import date, time 
st.title("Date, Time & File Uploader Demo") 
exam_date = st.date_input("Select Exam Date:", value=date.today()) 
start_time = st.time_input("Exam Start Time:", value=time(9, 0)) 
uploaded_file = st.file_uploader("Upload CSV file with student marks", type=["csv"]) 
st.write(f"Selected exam date: {exam_date}") 
st.write(f"Exam start time: {start_time}") 
if uploaded_file is not None: 
    st.success("File uploaded successfully!") 
    st.write("File name:", uploaded_file.name) 
    st.write("File type:", uploaded_file.type)
