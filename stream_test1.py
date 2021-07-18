"""
To deploy streamlit apps, please refer to the documentation below
https://docs.streamlit.io/en/stable/getting_started.html

To run a python script as an app, use the below command : 
streamlit run stream_test1.py
"""

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = [1,2,3,4,5]
b = [10,24,54,67,89]
dummy_df=pd.DataFrame({"col1":a, "col2":b})

def dummy_function(name):
    """
    This function prints the name of the app you give it : 
    Input : name
    Output : print statement telling the app's name
    sadasdsa
    """
    print(f"Hello, I am a dummy function with name ${name}")

# Add title

st.title('My first app with streamlit')
st.header("My first application-- HEADER")
st.subheader("My Subheader")
st.write("This dataframe is ",dummy_df)
st.write(dummy_function)

code = """
def dummy_function(name):
    \"""
    This function prints the name of the app you give it : 
    Input : name
    Output : print statement telling the app's name
    sadasdsa
    \"""
    print(f"Hello, I am a dummy function with name ${name}")

"""
st.code(code)
######################### MAGIC COMMANDS ##############
"Magic command starts"
st.text("This is a dummy text")
# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''

df = pd.DataFrame({'col1': [1,2,3]})
df  # <-- Draw the dataframe

x = 10
'x', x  # <-- Draw the string 'x' and then the value of x
############### STREAMLIT MARKDOWN ###########################
st.markdown("""Streamlit is **_really_ cool**.
### I am a big fan of markdown and I just love it
""")

#plt.plot(a,b)
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

"This is a JSON"

st.json({
     'foo': 'bar',
     'baz': 'boz',
     'stuff': [
         'stuff 1',
         'stuff 2',
         'stuff 3',
         'stuff 5',
     ],
 })

## Linechart - will just plot all column on the same axis

a = [1,2,3,4,5]
b = [10,24,54,67,89]

st.line_chart(dummy_df)
fig, ax = plt.subplots()
ax.plot(a,b)
plt.title('Draw dummy data')
st.pyplot(fig)

#from PIL import Image
#image = Image.open('https://www.imagescanada.ca/wp-content/uploads/2019/03/Spectacular-Photos-of-Niagara-Falls-Casinos.jpg')

st.markdown("# My Image")
st.image("https://www.imagescanada.ca/wp-content/uploads/2019/03/Spectacular-Photos-of-Niagara-Falls-Casinos.jpg", caption='Building')

st.markdown("# My video")
st.video("https://youtu.be/rJ5jron0z7Y")

### Display interactive widgets
st.markdown("# Display interactive widgets")

if st.button('Hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')


genre = st.radio(
    "What's your favorite movie genre",
    ('Comedy', 'Drama', 'Documentary'))
if genre == 'Comedy':
    st.write('You selected comedy.')
elif genre == 'Drama':
    st.write('You selected Drama.')
else:
    st.write("You selected Documentary")

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))
st.write('You selected:', option)

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    default = ['Yellow', 'Red'])

st.write('You selected:', options)

age = st.slider("Age", min_value=1, max_value=120, value=1, step=1, format=None, key='Age Slider', help="Slide to indicate your age", on_change=None, args=None)
st.write("I'm ", age, 'years old')


add_selectbox = st.sidebar.selectbox(
    "How would you lik",
    ("Email", "Home phone", "Mobile phone")
)

with st.form("my_form"):
   st.write("Inside the form")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)
st.write("Outside the form")