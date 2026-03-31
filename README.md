# 🚗 Bird’s Eye View (BEV) Occupancy Mapping

## 📌 Project Overview
This project implements a Bird’s Eye View (BEV) occupancy mapping system using classical computer vision techniques.

The system converts front-view camera images into a top-down (BEV) representation using Inverse Perspective Mapping (IPM) and generates a 2D occupancy grid indicating free and occupied space.

---

## 🎯 Objectives
- Transform perspective camera images into BEV (top-down view)
- Map road and obstacles onto a 2D ground plane
- Generate an occupancy grid (free vs occupied space)
- Maintain spatial consistency for autonomous driving applications

---

## ⚙️ Pipeline
Input Image → BEV Transformation (IPM) → Occupancy Detection → Grid Mapping
## 🧠 Methodology

### 1. Input Data
- Front-view camera images from the nuScenes dataset

### 2. BEV Transformation
- Applied Inverse Perspective Mapping (IPM)
- Used homography to map image plane to ground plane

### 3. Occupancy Grid Generation
- Converted BEV image to grayscale
- Applied adaptive thresholding
- Classified pixels into:
  - Occupied space (obstacles)
  - Free space (drivable area)

### 4. Grid Representation
- Divided BEV into fixed-size cells
- Visualized structured spatial layout

---

## 🛠️ Technologies Used
- Python
- OpenCV
- NumPy
- Matplotlib

---

## 📊 Results

The system produces:

- Original camera image  
- Bird’s Eye View (BEV) image  
- Occupancy grid (binary map)  
- Grid-based spatial representation  

---

## ⚡ Performance
- Lightweight implementation (no deep learning models)
- Runs efficiently on CPU (Google Colab)
- Fast execution using geometric transformations

---

## 📦 Dataset
We use the nuScenes dataset for input images.  
Dataset is not included in this repository due to size and licensing restrictions.

---

## 🚀 Future Scope
- Multi-camera BEV fusion  
- Integration with LiDAR data  
- Deep learning-based BEV models  
- Real-time deployment on edge devices  

---

## ▶️ How to Run
1. Upload an input image (from nuScenes dataset)
2. Run the notebook step-by-step
3. View outputs:
   - BEV image
   - Occupancy grid
   - Grid visualization

---

## 📌 Note
This is a simplified prototype developed for hackathon purposes, focusing on clarity, efficiency, and core BEV transformation concepts.

---

## 👩‍💻 Team
- Sunidhi P
- Aashka Srivasatava
- Anjana Krishnan
- Harshitha D
