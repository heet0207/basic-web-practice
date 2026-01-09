import streamlit as st 
st.set_page_config(page_title="Faculty Profile", page_icon=" ", layout="wide") 
st.title(" Faculty Profile Demo") 
st.markdown("This example shows how to use **sidebar**, **columns**, and **expanders**.") # Sidebar – Important for filters/settings 
st.sidebar.header("Profile Settings")
faculty_name = st.sidebar.text_input("Faculty Name","Parth Sinroza")
department = st.sidebar.selectbox("Department", ["Computer Engineering", "IT", "AI/ML", "CSE"]) 
experience = st.sidebar.slider("Years of Experience", 0, 40, 10) 
st.sidebar.markdown("---") 
st.sidebar.write("You can put filters, toggles, etc. in the sidebar.") # Main content – using columns 
col1, col2 = st.columns([1, 2]) # 1:2 ratio 
with col1: 
    st.subheader("Basic Info") 
    st.write(f"**Name:** {faculty_name}") 
    st.write(f"**Department:** {department}") 
    st.write(f"**Experience:** {experience} years") 
    
with col2: 
    st.subheader("About") 
    st.markdown(""" Use this area to show detailed information about the faculty member, such as research interests, publications, and courses handled. """) 
    # Expander – for optional/extra info 
with st.expander("Show Courses Handled"): 
    st.write("- Data Structures") 
    st.write("- Machine Learning") 
    st.write("- Database Management Systems") 
with st.expander("Show Publications"): 
    st.write("1. Research Paper A (2021)") 
    st.write("2. Research Paper B (2023)")