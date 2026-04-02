# 🌿 Tomato Leaf Disease Detection System

## 📌 Overview

This project is a deep learning-based web application that detects diseases in tomato leaves and also identifies whether an input image is a leaf or not. The model is trained using convolutional neural networks (CNN) and deployed using Gradio for an interactive user interface.

---

## 🚀 Features

* 🌱 Detects multiple tomato leaf diseases
* ❌ Identifies invalid inputs (non-leaf images)
* 📷 Image upload-based prediction
* ⚡ Fast and user-friendly interface using Gradio
* 🧠 Deep learning model trained on PlantVillage dataset

---

## 🧠 Model Details

* Framework: TensorFlow / Keras
* Architecture: CNN
* Input Size: 224 × 224 images
* Output: Disease classification / Invalid image detection

### Classes:

* Bacterial Spot
* Early Blight
* Late Blight
* Leaf Mold
* Septoria Leaf Spot
* Spider Mites
* Target Spot
* Yellow Leaf Curl Virus
* Mosaic Virus
* Healthy Leaf
* Non-Leaf (Invalid)

---

## 📂 Project Structure

```
├── model.keras / model.h5
├── app.py
├── requirements.txt
├── README.md
└── dataset (optional / not uploaded)
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
Upload app.py, model.keras in Hugging Face Transformers
```

Then open the generated local link in your browser.

---

## 🖼️ How It Works

1. Upload an image
2. Model preprocesses the image
3. Predicts:

   * Disease clas
---

## 📊 Dataset

* PlantVillage Dataset (Tomato Leaf Diseases)

---

## 📈 Results

* High accuracy achieved on validation dataset
* Robust performance on real-world images
* Handles invalid inputs effectively

---

## 🌐 Deployment

* Can be deployed on:

  * Hugging Face Spaces
  * Local server
  * Cloud platforms

---

## 💡 Future Improvements

* Add real-time camera detection
* Improve accuracy with larger datasets
* Mobile app integration
* Multi-plant disease detection

---

## 🤝 Contributing

Feel free to fork this repository and contribute!

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* PlantVillage Dataset
* TensorFlow & Keras
* Gradio

---
