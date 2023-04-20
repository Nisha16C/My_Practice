
import streamlit as st
#title
st.title("Python Station")

#header
st.header("I am Nisha")

#Sub-header
st.header("Python subheader")

#test
st.text('''Hello Everyone!
         I hope both are Good and healthy.
         If you have any problem then you can contact me and msg me.........''')

#Write
st.write("All are doing practice about streamlit.......")

#Image
from PIL import Image
img = Image.open('fixed.png')
st.image(img, caption='Vinu Chaurasiya')


#..............#Colorfull text.................
#Success(Green clr hota..)
st.success("Success")

#Error
st.error("Error")


#Warning
st.warning("Warning")

#information
st.info("Note: You have to know about this....")

#Exception
st.exception("Name is not defined")


#Help
st.help(help)

#Video
vid = open('doraemon-twixtor-clips-for-amv-edit-steptodown.com.mp4', 'rb').read()
# rb = read binary mode
st.video(vid)


#sidebar
st.sidebar.header('About as')
st.sidebar.text('''Hello , how are you ..
I am fine and you ....
I also workinh on python.................''')


##Widgets

#checkbox
if st.checkbox('Show/hide'):
    st.write("If you like this , then you can try it ...")

#radio
status = st.radio('What is your Status?',('Active','Inactive'))
if status is 'Active':
    st.success('You are Active')
else:
    st.warning('You are Inactive')


#selectbox
# st.selectbox('What is your hobby?',['Dancing','Singing','Programmer','Reading'])

Hobby = st.selectbox('What is your hobby?',['','Dancing','Singing','Programmer','Reading'])
st.write('Your hobby is', Hobby)


#Multiselect
# st.multiselect('Whare are you from?', ('Satna','Indore','Rewa','Mumbai'))
Location = st.multiselect('Whare are you from?', ('Satna','Indore','Rewa','Mumbai'))
st.write('You selected', len(Location))



#Slider
st.slider('What is your age?',21,30)

#Button
# st.button('About Me')

if st.button('About Me'):
    st.write('Hey ........Myself Nisha ')


#Text_input
#  User se input lena

gmail = st.text_input('Enter your Gmail Id:')
if '@gmail.com' in gmail:
    st.write("Confirm your gmail id {gmail}")

#text_area
Message = st.text_area("Give your experience about streamlit .......")

#Date /Time

#date
import datetime
st.date_input("Today is ", datetime.datetime.now())

#time
import time
st.time_input("Time is ", datetime.time())

#Display row code
#code
st.text('How to install streamlit')
st.code('pip install streamlit')

#echo
#  Comment dikhane ke liye ya row code
with st.echo():
     #how to import streamlit in your python script
     import streamlit


#Display JSON

st.json({"name":"Nisha","Age":21, "Batch":"CSE"})



#Spinner
with st.spinner("Wait a second............"):
    time.sleep(5)
    st.success("success")


#Balloons
st.balloons()