import streamlit as st

def register_patient():
    st.subheader('Patient Registration')
    name = st.text_input('Name')
    age = st.number_input('Age', min_value=0, max_value=150, step=1)
    gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
    address = st.text_area('Address')
    contact = st.text_input('Contact Number')

    if st.button('Register'):
        # Here you can perform actions like saving patient data to a database
        st.success(f'Patient {name} registered successfully!')

def schedule_appointment():
    st.subheader('Schedule Appointment')
    patient_id = st.text_input('Patient ID')
    date = st.date_input('Date')
    time = st.time_input('Time')
    doctor = st.text_input('Doctor')

    if st.button('Schedule'):
        # Here you can perform actions like saving appointment data to a database
        st.success('Appointment scheduled successfully!')

def view_patient_info():
    st.subheader('View Patient Information')
    patient_id = st.text_input('Patient ID')

    if st.button('View'):
        # Here you can fetch patient information from a database and display it
        st.write(f'Patient ID: {patient_id}')
        st.write('Name: John Doe')
        st.write('Age: 35')
        st.write('Gender: Male')
        st.write('Address: 123 Main St')
        st.write('Contact: 555-1234')

def main():
    st.title("Accelerometer Data Display")

    # Assuming you have the accelerometer data as a dictionary
    accelerometer_data = {
        "x": 0.0,
        "y": 0.0,
        "z": 0.0
    }

    st.write("### Accelerometer Data:")
    st.write(f"X: {accelerometer_data['x']}")
    st.write(f"Y: {accelerometer_data['y']}")
    st.write(f"Z: {accelerometer_data['z']}")

if __name__ == "__main__":
    main()


def main():
    st.title('Posture detection System')

    task = st.sidebar.selectbox(
        'Task',
        ['Register Patient', 'Schedule Appointment', 'View Patient Info']
    )

    if task == 'Register Patient':
        register_patient()
    elif task == 'Schedule Appointment':
        schedule_appointment()
    elif task == 'View Patient Info':
        view_patient_info()

if __name__ == "__main__":
    main()



