# LeukoFind
## About the Project:
LeukoFind is a deep learning system for _B-ALL detection using blood smear images_ and _transfer learning models_.
This project classify blood smear images into 4 classes - hematogones cells i.e., **Benign** and different forms of B-ALL cells, such as **Early Pre-B, Pre-B, and Pro-B.**

## 📄 Research Paper:

This work was published as an **IEEE conference paper** titled, _LeukoFind: A Deep Learning Approach for Predicting B-Cell Acute Lymphoblastic Leukemia from Blood Smear Images_ 
[DOI: https://doi.org/10.1109/ICISS67859.2026.11454059]

**Team Members Who Worked on this project:**
1. Gokila S - [@Gokila3075](https://github.com/Gokila3075)
2. Kavinaya A - [@kavinaya005](https://github.com/kavinaya005)

## 📂 Dataset

🟢 The **Blood Cells Cancer (ALL)** dataset used in this project [Kaggle Dataset Link: https://www.kaggle.com/datasets/mohammadamireshraghi/blood-cell-cancer-all-4class], where it is provided as part of a published research work on B-Cell Acute Lymphoblastic Leukemia detection. 

🔵 Before model training, the dataset underwent preprocessing and data augmentation. The dataset was split into _training_ and _testing_ sets, with an **80:20 split** applied for model development and evaluation.

## System Architecture:

The system architecture represents the complete pipeline from dataset collection to B-ALL prediction.
<img width="1146" height="483" alt="leukofindarch1" src="https://github.com/user-attachments/assets/39292949-786e-4e07-be51-843e92589cf9" />

## Model Training:

Two transfer learning models, _ResNet50_ and _EfficientNetB3_, were implemented and trained under the same experimental conditions for performance comparison. Among them, **ResNet50** achieved the highest classification accuracy and was selected as the primary model for the web-based B-ALL detection system.

| Model | Accuracy |
|--------|---------:|
| ResNet50 | **98.61%** |
| EfficientNetB3 | **97.07%** |

---

## 📊 Model Evaluation

The performance of the implemented models was evaluated using classification metrics, including _precision, recall, F1-score, accuracy_, and the _confusion matrix_. The confusion matrices of both ResNet50 and EfficientNetB3 are presented below for comparison.
<img width="1278" height="628" alt="image" src="https://github.com/user-attachments/assets/2ebd1183-3db4-4ba4-9f03-6dfd495ff5e1" />

## 💻 System Implementation:

The proposed system is implemented as a **Streamlit** web application, where users can upload blood smear images for B-ALL detection. The application displays the prediction result along with relevant suggestions to support clinical decision-making.

<img width="1920" height="1920" alt="LeukoFind ss collage" src="https://github.com/user-attachments/assets/c0010592-85fd-4683-89d3-77770fe49f8c" />
