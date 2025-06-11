# 📦 YOLOv8 Object Detection with Streamlit

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**🚀 Real-time Object Detection Made Simple**

[Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Features](#-features) • [Contributing](#-contributing)

</div>

---

## 🌟 Overview

<div align="center">
  <img src="https://github.com/ultralytics/assets/raw/main/yolov8/yolo-comparison-plots.png" alt="YOLOv8 Performance" width="600">
</div>

**YOLOv8 Object Detection with Streamlit** là một ứng dụng web đơn giản và mạnh mẽ cho việc phát hiện đối tượng trong thời gian thực. Được xây dựng với công nghệ tiên tiến nhất:

- 🔥 **YOLOv8** - State-of-the-art object detection
- ⚡ **Streamlit** - Interactive web interface  
- 🎯 **Real-time Processing** - Instant results
- 📱 **User-friendly** - No coding required

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎯 Core Features
- [x] **Real-time Object Detection**
- [x] **Multiple Image Formats** (JPG, PNG, JPEG)
- [x] **Interactive Web Interface**
- [x] **Bounding Box Visualization**
- [x] **Performance Metrics**
- [x] **Responsive Design**

</td>
<td width="50%">

### 🚀 Performance
- ⚡ **Lightning Fast** - YOLOv8n model
- 📊 **Accurate Detection** - 80+ object classes
- 💻 **Low Resource Usage**
- 🔄 **Batch Processing Ready**
- 📈 **Scalable Architecture**

</td>
</tr>
</table>

## 🎬 Demo

<div align="center">

### 📸 Before & After

| Original Image | Detected Objects |
|:--------------:|:----------------:|
| ![Original](https://via.placeholder.com/300x200?text=Upload+Your+Image) | ![Detected](https://via.placeholder.com/300x200?text=Objects+Detected!) |

> 🎉 **Try it yourself!** Upload any image and watch the magic happen

</div>

## 🛠️ Installation

### Prerequisites

```bash
# Check Python version (3.8+ required)
python --version
```

### Quick Start

```bash
# 1️⃣ Clone the repository
git clone https://github.com/vanhai1231/yolov8_streamlit_app.git
cd yolov8-streamlit-detection

# 2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the app
streamlit run app.py
```

### 📦 Requirements

Create a `requirements.txt` file:

```txt
streamlit>=1.28.0
ultralytics>=8.0.0
Pillow>=9.0.0
opencv-python>=4.8.0
torch>=2.0.0
torchvision>=0.15.0
```

## 🚀 Usage

### 1. **Launch the Application**
```bash
streamlit run app.py
```

### 2. **Open Your Browser**
Navigate to `http://localhost:8501`

### 3. **Upload & Detect**
- 📤 Click "Upload an image"
- 🖼️ Select your image (JPG, PNG, JPEG)
- ⏱️ Wait for detection results
- 🎯 View detected objects with bounding boxes

## 🏗️ Project Structure

```
📁 yolov8-streamlit-detection/
├── 📄 app.py                 # Main Streamlit application
├── 📄 requirements.txt       # Python dependencies
├── 📄 README.md             # This file
├── 📁 models/               # YOLOv8 model files
│   └── 📄 yolov8n.pt
├── 📁 samples/              # Sample images for testing
│   ├── 🖼️ sample1.jpg
│   └── 🖼️ sample2.png
└── 📁 docs/                 # Documentation
    └── 📄 API.md
```

## 🔧 Configuration

### Model Selection

You can switch between different YOLOv8 models:

```python
# Available models (trade-off between speed and accuracy)
model = YOLO("yolov8n.pt")  # Nano - fastest
model = YOLO("yolov8s.pt")  # Small
model = YOLO("yolov8m.pt")  # Medium  
model = YOLO("yolov8l.pt")  # Large
model = YOLO("yolov8x.pt")  # Extra Large - most accurate
```

### Confidence Threshold

```python
# Adjust detection confidence
results = model.predict(image, conf=0.5)  # 50% confidence
```

## 📊 Supported Objects

YOLOv8 can detect **80 different object classes**:

<details>
<summary>Click to see all supported objects</summary>

```
🚗 Vehicles: car, truck, bus, motorcycle, bicycle
👥 People: person
🐕 Animals: dog, cat, horse, cow, elephant, bear, zebra, giraffe
🏠 Indoor: chair, sofa, bed, dining table, toilet, tv, laptop, mouse, keyboard
🍎 Food: banana, apple, sandwich, orange, broccoli, carrot, pizza, donut, cake
⚽ Sports: sports ball, kite, baseball bat, baseball glove, skateboard, surfboard
... and many more!
```

</details>

## 🤝 Contributing

We welcome contributions! Here's how you can help:

<div align="center">

| Type | How to Contribute |
|:----:|:------------------|
| 🐛 **Bug Reports** | Open an issue with detailed description |
| 💡 **Feature Requests** | Suggest new features via issues |
| 🔧 **Code Contributions** | Fork → Branch → PR |
| 📖 **Documentation** | Improve README or add tutorials |
| ⭐ **Support** | Star the repo and share with others |

</div>

### Development Setup

```bash
# Fork the repo and clone your fork
git clone https://github.com/vanhai1231/yolov8_streamlit_app.git

# Create a feature branch
git checkout -b feature/amazing-feature

# Make your changes and commit
git commit -m "Add amazing feature"

# Push and create a Pull Request
git push origin feature/amazing-feature
```

## 📈 Performance Benchmarks

<div align="center">

| Model | Size | mAP | Speed (CPU) | Speed (GPU) |
|:-----:|:----:|:---:|:-----------:|:-----------:|
| YOLOv8n | 6.2MB | 37.3 | 80ms | 8ms |
| YOLOv8s | 21.5MB | 44.9 | 128ms | 10ms |
| YOLOv8m | 49.7MB | 50.2 | 234ms | 15ms |

*Benchmarks on COCO dataset*

</div>

## 🛡️ License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- 🏆 [Ultralytics](https://github.com/ultralytics/ultralytics) - For the amazing YOLOv8 implementation
- 🎨 [Streamlit](https://streamlit.io/) - For the beautiful web framework
- 🤗 [Hugging Face](https://huggingface.co/) - For model hosting and community

## 📞 Support & Contact

<div align="center">

Got questions? We're here to help!

[![GitHub Issues](https://img.shields.io/badge/GitHub-Issues-red?style=for-the-badge&logo=github)](https://github.com/vanhai1231/yolov8_streamlit_app.git/issues)
[![Email](https://img.shields.io/badge/Email-Contact-blue?style=for-the-badge&logo=gmail)](mailto:vanhai11203@gmail.com)

**⭐ If you found this project helpful, please give it a star!**

</div>

---

<div align="center">

**Made with ❤️ by [Your Name](https://github.com/vanhai1231)**

*Don't forget to ⭐ star this repo if you found it useful!*

</div>