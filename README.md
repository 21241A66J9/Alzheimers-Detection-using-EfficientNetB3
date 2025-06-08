# 🧠 Alzheimer’s Detection using EfficientNetB3

This project presents a **deep learning-based system** for the early detection and classification of **Alzheimer’s disease stages** using structural brain **MRI scans**. The model leverages **EfficientNetB3** with **transfer learning** and **advanced preprocessing** techniques—such as resizing, normalization, and data augmentation—to accurately classify images into four categories:

- Non-Demented  
- Very Mild Dementia  
- Mild Dementia  
- Moderate Dementia  

The system is designed to be **lightweight, accurate, and scalable**, making it suitable for real-world clinical applications.

---

## 📦 Dataset
The dataset used in this project is curated and preprocessed via **Roboflow**, based on MRI scans from the **OASIS** dataset.

🔗 **[Download Dataset via Roboflow](https://app.roboflow.com/traffic-violation-2hmbm/alzheimers-dataset-oasis/models)**

---

## 🚀 How to Run the Code

### 🧪 Option 1: Using Google Colab
1. Open [Google Colab](https://colab.research.google.com/)
2. Paste the training/inference code provided in the project.
3. Download the dataset from Roboflow.
4. Train the model or directly load `best.keras` to run predictions.

### 💻 Option 2: Run Locally with GUI
1. Use the provided `alzheimers.py` (Tkinter-based interface).
2. Ensure `best.keras` is available in your project directory.
3. Create a virtual environment and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run `alzheimers.py` to use the interactive prediction tool.

---

## 📊 Results
- **Training Accuracy:** 93.5%
- **Validation Accuracy:** 92.4%
- **Test Accuracy:** 100%
- **Test Loss:** 0.0045

The model provides high-confidence predictions and generalizes well across all Alzheimer’s stages.

---

## 📥 Downloads
You can access the trained model and full project documentation using the link below:

🔗 **[Download best.keras and Project Report (PDF)](https://drive.google.com/drive/folders/1MCqUzqOZIpTnTMEyu0sNJcKWUzfMiGkB?usp=sharing)**

**Contents:**
- ✅ `best.keras`: Pretrained model file  
- 📄 `Major Project - Alzheimer's.pdf`: Detailed documentation

> Please download these files and place `best.keras` in your project root directory before running inference.

---

## 📁 Requirements
To install all required dependencies, use:

```txt
tensorflow
numpy
pillow
matplotlib
sklearn
opencv-python
```

---

## 📬 Contact
For questions or contributions, please reach out via GitHub or email:  
📧 **manjunath.varala@gmail.com**
