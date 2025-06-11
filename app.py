# app.py
import streamlit as st
from PIL import Image
from ultralytics import YOLO
import time

st.set_page_config(page_title="YOLOv8 Object Detection", layout="wide")
st.title("📦 YOLOv8 Object Detection with Streamlit")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    model = YOLO("yolov8n.pt")  # Dùng YOLOv8 nhỏ (nhẹ, nhanh)

    st.markdown("### Detecting objects...")
    start_time = time.time()
    results = model.predict(image)
    end_time = time.time()

    result_img = results[0].plot()  # Vẽ bounding boxes
    st.image(result_img, caption="Detected Objects", use_column_width=True)

    st.success(f"Inference Time: {(end_time - start_time):.2f} seconds")
