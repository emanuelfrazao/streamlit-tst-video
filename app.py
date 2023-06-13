import cv2
import streamlit as st
st.write(cv2.CAP_V4L2)
st.write(cv2.CAP_DSHOW)
st.write(cv2.CAP_MSMF)
st.title("Webcam Live Feed")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(1)

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')