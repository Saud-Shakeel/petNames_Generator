import langchain_helper as lch
import streamlit as st


st.title('Pets Names Generator ')

user_pet_type = st.sidebar.selectbox('What is your pet ?',('Cat', 'Dog', 'Rat', 'Parrot'))
user_pet_color = st.sidebar.text_area(label=f'What color is your {user_pet_type} ?', max_chars=15)

if user_pet_type == 'Cat':
    user_pet_color
elif user_pet_type == 'Dog':
    user_pet_color
elif user_pet_type == 'Rat':
    user_pet_color
else:
    user_pet_color

if user_pet_color:
    response = lch.generate_petNames(petType=user_pet_type, petColor=user_pet_color)
    st.text(response['pet_name'])




