# app.py
import streamlit as st
from PIL import Image
from ultralytics import YOLO
import time
import numpy as np
import cv2

# Page configuration
st.set_page_config(
    page_title="YOLOv8 Object Detection",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    
    .metric-container {
        background: linear-gradient(45deg, #f093fb 0%, #f5576c 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin: 1rem 0;
    }
    
    .info-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
    }
    
    .upload-section {
        border: 2px dashed #667eea;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        background: linear-gradient(45deg, #f8f9ff 0%, #e8edff 100%);
        margin: 1rem 0;
    }
    
    .stProgress .st-bo {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    .result-section {
        background: white;
        padding: 1rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Main header
st.markdown('<h1 class="main-header">🔍 YOLOv8 Object Detection Studio</h1>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Settings")
    
    # Model selection
    model_choice = st.selectbox(
        "🤖 Select YOLOv8 Model",
        ["yolov8n.pt", "yolov8s.pt", "yolov8m.pt"],
        help="Choose model size: n=nano(fastest), s=small, m=medium(most accurate)"
    )
    
    # Confidence threshold
    confidence = st.slider(
        "🎯 Confidence Threshold", 
        min_value=0.1, 
        max_value=1.0, 
        value=0.5, 
        step=0.1,
        help="Minimum confidence for object detection"
    )
    
    # Show advanced options
    show_labels = st.checkbox("🏷️ Show Labels", value=True)
    show_conf = st.checkbox("📊 Show Confidence", value=True)
    
    st.markdown("---")
    st.markdown("### 📈 Model Information")
    
    model_info = {
        "yolov8n.pt": {"Size": "6.2MB", "Speed": "⚡ Fastest", "Accuracy": "⭐⭐⭐"},
        "yolov8s.pt": {"Size": "21.5MB", "Speed": "⚡⚡ Fast", "Accuracy": "⭐⭐⭐⭐"},
        "yolov8m.pt": {"Size": "49.7MB", "Speed": "⚡⚡⚡ Medium", "Accuracy": "⭐⭐⭐⭐⭐"}
    }
    
    info = model_info[model_choice]
    st.info(f"""
    **Model**: {model_choice}
    
    **Size**: {info['Size']}
    
    **Speed**: {info['Speed']}
    
    **Accuracy**: {info['Accuracy']}
    """)

# Main content area
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📤 Upload Image")
    
    # Custom upload section
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=["jpg", "png", "jpeg"],
        help="Supported formats: JPG, PNG, JPEG"
    )
    
    if not uploaded_file:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h4>📁 Drop your image here</h4>
            <p>or click to browse files</p>
            <p style="color: #666; font-size: 0.9em;">Supported: JPG, PNG, JPEG</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Example images
    st.markdown("### 🖼️ Try Example Images")
    col_ex1, col_ex2, col_ex3 = st.columns(3)
    
    with col_ex1:
        if st.button("🚗 Cars", use_container_width=True):
            st.info("Upload your own image to detect cars!")
    
    with col_ex2:
        if st.button("👥 People", use_container_width=True):
            st.info("Upload your own image to detect people!")
    
    with col_ex3:
        if st.button("🐕 Animals", use_container_width=True):
            st.info("Upload your own image to detect animals!")

with col2:
    st.markdown("### 📊 Detection Results")
    
    if uploaded_file is None:
        st.markdown("""
        <div class="info-box">
            <h4>🎯 Ready for Object Detection!</h4>
            <p>Upload an image to start detecting objects using YOLOv8</p>
            <br>
            <p><strong>Detectable Objects:</strong></p>
            <p>🚗 Vehicles • 👥 People • 🐕 Animals • 🏠 Furniture • 🍎 Food • ⚽ Sports Equipment • And 70+ more!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Show original image
        image = Image.open(uploaded_file)
        st.markdown("#### 📷 Original Image")
        st.image(image, caption=f"Uploaded: {uploaded_file.name}", use_container_width=True)
        
        # Detection process
        st.markdown("#### 🔍 Detection Process")
        
        # Progress bar
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        try:
            # Load model
            status_text.text("🤖 Loading YOLOv8 model...")
            progress_bar.progress(25)
            model = YOLO(model_choice)
            
            # Perform detection
            status_text.text("🔍 Detecting objects...")
            progress_bar.progress(50)
            start_time = time.time()
            
            results = model.predict(
                image, 
                conf=confidence,
                show_labels=show_labels,
                show_conf=show_conf
            )
            
            end_time = time.time()
            progress_bar.progress(75)
            
            # Process results
            status_text.text("📊 Processing results...")
            result_img = results[0].plot()
            
            # Convert from BGR to RGB for display
            result_img = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
            
            progress_bar.progress(100)
            status_text.text("✅ Detection completed!")
            
            # Show results
            st.markdown("#### 🎯 Detection Results")
            st.image(result_img, caption="Objects Detected", use_container_width=True)
            
            # Metrics
            inference_time = end_time - start_time
            detections = results[0].boxes
            num_objects = len(detections) if detections is not None else 0
            
            # Display metrics in columns
            metric_col1, metric_col2, metric_col3 = st.columns(3)
            
            with metric_col1:
                st.metric(
                    label="⏱️ Inference Time",
                    value=f"{inference_time:.2f}s",
                    delta=f"Model: {model_choice}"
                )
            
            with metric_col2:
                st.metric(
                    label="🎯 Objects Detected", 
                    value=num_objects,
                    delta="Objects found"
                )
            
            with metric_col3:
                st.metric(
                    label="📊 Confidence",
                    value=f"{confidence*100:.0f}%",
                    delta="Threshold"
                )
            
            # Detected objects details
            if num_objects > 0:
                st.markdown("#### 📋 Detected Objects Details")
                
                detected_objects = []
                for box in detections:
                    class_id = int(box.cls[0])
                    confidence_score = float(box.conf[0])
                    class_name = model.names[class_id]
                    detected_objects.append({
                        "Object": class_name.title(),
                        "Confidence": f"{confidence_score:.2f}",
                        "Confidence %": f"{confidence_score*100:.1f}%"
                    })
                
                # Create a nice table
                st.dataframe(
                    detected_objects, 
                    use_container_width=True,
                    hide_index=True
                )
                
                # Download option
                st.markdown("#### 💾 Download Results")
                
                # Convert PIL image to bytes for download
                import io
                result_pil = Image.fromarray(result_img)
                buf = io.BytesIO()
                result_pil.save(buf, format='PNG')
                
                st.download_button(
                    label="📥 Download Detection Result",
                    data=buf.getvalue(),
                    file_name=f"detected_{uploaded_file.name}",
                    mime="image/png",
                    use_container_width=True
                )
            
            else:
                st.warning("No objects detected. Try lowering the confidence threshold or uploading a different image.")
                
        except Exception as e:
            st.error(f"❌ Error during detection: {str(e)}")
            st.info("💡 Make sure you have a stable internet connection for model download.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 2rem; color: #666;">
    <h4>🚀 YOLOv8 Object Detection Studio</h4>
    <p>Powered by Ultralytics YOLOv8 • Built with Streamlit</p>
    <p>Detect 80+ object classes with state-of-the-art accuracy</p>
</div>
""", unsafe_allow_html=True)

# Performance tips in expander
with st.expander("💡 Performance Tips & Tricks"):
    st.markdown("""
    ### 🎯 Getting the Best Results:
    
    **🖼️ Image Quality:**
    - Use high-resolution images (but not too large > 5MB)
    - Ensure good lighting and contrast
    - Avoid blurry or heavily compressed images
    
    **⚙️ Model Selection:**
    - **YOLOv8n**: Fastest inference, good for real-time applications
    - **YOLOv8s**: Balanced speed and accuracy
    - **YOLOv8m**: Best accuracy, slower inference
    
    **🎚️ Confidence Threshold:**
    - Lower values (0.1-0.3): Detect more objects (may include false positives)
    - Higher values (0.6-0.9): Only high-confidence detections
    - Sweet spot: 0.4-0.6 for most use cases
    
    **📱 Supported Objects:**
    Person, Car, Truck, Bus, Motorcycle, Bicycle, Dog, Cat, Horse, Cow, Elephant, Bear, Zebra, Giraffe, and 65+ more!
    """)