# import core package
import streamlit as st
from PIL import Image
from transformers import pipeline

@st.cache
def load_img(path):
	return Image.open(path)

img = load_img("images/univ.jpeg")

st.image(img, width=200)

# initialize qa pipepile
@st.cache(allow_output_mutation=True)
def load_qa():
	qa = pipeline("question-answering")
	return qa

qa = load_qa()

context = """
The pre-class quizes are not graded. They are just to check your understaning of the reading.
The deadline for the submission of the session quiz/exercises is at 5pm-on-the-day-of-the-following-lecture.
Only for exceptional cases extension would be allowed for the quizs and exercises submission.
You need about 15 hours per week to complete this module.
The exercises are auto-graded once you click the submit button.
If you have different approach to the exercise, the auto-grader will not accept alternative solutions. Please follow the prescribed instructions.
The exercises has to be done individually but you can work with your peers in the break out room.
Labs are not compulsory, and will mostly review previously covered materials.
All sessions  will be recorded but office hours will not be recorded.
All enrolled students have access to live-streaming and to all the video captured materials.
You can find the recordings on edStem once it's posted.
If you have any questions regarding the reading materials you can post your quesiton on edStem.
Reading for the next session will be posted after every lab.
You can find all course lectures and materials on edStem.
You can find all the assignments on edStem in the lession tab.
You and your partner are required to submit the homework in the edStem lessons tab.
The homework release is subject to change and hence will be announced during the session.
TAs will take the office hours.
Please check the course information slide for zoom links.
A significant part of this course is a group project. You will work in teams of four on a project about a topic of your choosing from those proposed in the class. You will acquire the data, design, and implement your application using the tools and techniques learned during the course.
Project deadline can be extended only when there are exceptional cases.
You have to do only one presentation for the final project at the end of the module.
You have to submit a 5 minutes video presentation along with the slides an a jupyter notebook with the code.
Both project and presentations will be done in a group of 4.
Sharing solutions outside your team members is a violation of our code conduct.
A small component of grading is allocated to class attendance. Please check the grading policy for more information.
All official communication by Prof. Protopapas will be made on edStem forums not on slack.
For other queries please post a private message on edstem.
"""

# Text Area
ques = st.text_area("Question", height=100)

# add a button
button1 = st.button("Submit")

# add button clicked functionality
if button1:
	# get the answer
	answer = qa(question=ques, context=context)

	# show ans
	# st.write(answer['answer'])
	st.info(answer['answer'])

