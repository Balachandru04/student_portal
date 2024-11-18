import backend as be
import streamlit as st
from PIL import Image
data = {"BALA": '101', "CHANDRU": '102', "MOHAN": '103', "ASHARAJA": '104'}
design="------------------------------------------------------------------------------------"
if 'student' not in st.session_state:
    st.session_state.student = None
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

st.header("Welcome to Students Login Portal")
name= st.text_input("Username:",type="password").upper()
reg_no=st.text_input("Password",type="password")

if st.button("Login"):
    if name in data.keys() and reg_no in data[name]:
        class_name = name   
        student_class = getattr(be, class_name) 
        student = student_class()

        st.session_state.student = student
        st.session_state.submitted = True  
        st.success(f"Welcome {name.title()}, Login successfully!")
        
    else:
        st.error("Invalid UserName or Password")

if st.session_state.submitted:
    st.sidebar.header(f"{name}")
    st.sidebar.title("Select what details you needed")
    student_info = st.sidebar.button("Student Information")
    student_attendance = st.sidebar.button("Attendance")
    mark_details = st.sidebar.button("Mark Details")
    grade_button = st.sidebar.button("Grade")
    contact_info=st.sidebar.button("Contact Details")
    exit_button=st.sidebar.button("Logout")

    if student_info:
        if st.session_state.student:
            student = st.session_state.student
            st.title("Student Information:")
            st.text(design)
            st.markdown(f"Name: {name.title()}")
            st.markdown(f"course: {student.course}")
            st.markdown(f"Batch: {student.batch}")
            st.markdown(f"Instution name: {student.instution_name}")
            st.image(student.img ,width=200)
            st.header(f"{name.lower()}")

    elif student_attendance:
        if st.session_state.student:
            student = st.session_state.student
            leave=90-student.attendance
            st.title("Attendance Details:")
            st.text(design)
            st.markdown("<h4>Total number of days class conducted : 90</h4>",unsafe_allow_html=True)
            st.markdown(f"<h5>Number of days you attend : {student.attendance}</h5> ",unsafe_allow_html=True)
            st.markdown(f"<h5>Attendance Percentage is {round(student.attendance /90 *100 , 2)}% </h5>",unsafe_allow_html=True)

    elif mark_details:
        if st.session_state.student:
            student = st.session_state.student
            st.title("Mark Details:")
            st.text(design)
            st.markdown(f"name:          {name}")
            st.markdown(f"mini_project:  {student.mini_project}")
            st.markdown(f"assignment:    {student.assignment}")
            st.markdown(f"finall_project:{student.finall_project}")
            st.markdown(f"total_marks:   {student.total}/30")
    elif grade_button:
        if st.session_state.student:
            student = st.session_state.student
            st.title("Grade:")
            st.text(design)
            st.markdown(f"<h5>Total marks : 30</h5> \n<h5>your total marks is {student.total} </h5> ",unsafe_allow_html=True)
            if 10 <= student.total <=15:
                grade="C"
            elif 16 <= student.total <=25:
                grade="B"
            elif 25<student.total<=30:
                grade="A"
            else :
                grade="D"

            if grade !="D":
                st.success(f"you got {grade} Grade")
            else:
                st.warning(f"You got {grade} grade.")
                st.markdown(f"Meet HOD")

    elif contact_info:
        if st.session_state.student:
            student = st.session_state.student
            st.title("Contact info:")
            st.text(design)
            st.markdown(f"<h5>Mobile Number : {student.phone}</h5>",unsafe_allow_html=True)
            st.markdown(f"<h5>Mail_ID : {student.mail_id}</h5>",unsafe_allow_html=True)

    elif exit_button:
        st.session_state.clear()

# streamlit run student_portal.py  