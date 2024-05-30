# Table-From-Image-DL (Work-In-Progress)

## Motivation
Imagine you're trying to scrape data from a website and all their tables are in images. What do you do then? A quick search online you can pay $2 per 50 images to turn your images into tables. Well, some of us are trying to scrape a lot of data and aren't willing to spend that much. Also, that seems like the easiest ML problem ever. First there's no need to adjust colors since the tables are in B&W, the words are nicely spaced and there's no glare or anything to adjust. 

You might have heard of the PyPDF2 package (https://pypdf2.readthedocs.io/en/3.x/user/extract-text.html). This package is incredible, but it wouldn't work for the table structure I was looking for. 


## Basic structure
Turning an image into a table using a Convolutional Neural Network (CNN) involves extracting structured information from the image. This task is generally referred to as "image-to-table conversion" or "table recognition." The nature of this project often includes multiple steps, combining different types of machine learning models and techniques. The components can be broadly categorized as follows:

### 1. **Image Preprocessing:**
   - **Segmentation:** Detect and segment the table region from the rest of the image. This can be done using techniques like image thresholding, edge detection, or more sophisticated deep learning models like Mask R-CNN.
   - **Line Detection:** Identify lines to understand the boundaries of rows and columns. This might involve techniques like Hough Transform or deep learning models specifically trained for line detection.

### 2. **Cell Detection and Recognition:**
   - **Cell Detection:** Identify individual cells within the table. This can be approached using object detection models like Faster R-CNN, YOLO, or SSD, which are trained to detect the bounding boxes of cells.
   - **Cell Recognition:** Once cells are detected, extract the content from each cell. This typically involves Optical Character Recognition (OCR) to convert the text within each cell from an image format to a string format.

### 3. **Structured Data Extraction:**
   - **Table Structure Recognition:** Understand the spatial arrangement and logical structure of the table, including the relationships between rows and columns.
   - **Post-Processing:** Clean and organize the recognized text data into a structured table format (e.g., CSV, Excel).

### Type of Machine Learning Models Involved:
1. **CNN for Feature Extraction:** CNNs are primarily used for their strength in feature extraction from images, especially in the segmentation and detection stages.
2. **Object Detection Models:** These models (often based on CNNs) are used for detecting table boundaries and individual cells.
3. **OCR Models:** OCR is crucial for recognizing and extracting text from the detected cells. Models like Tesseract or specialized deep learning-based OCR models (e.g., CRNN, Attention-OCR) are commonly used.

### Example Workflow:
1. **Table Detection:** Use a CNN-based object detection model to identify and segment the table from the image.
2. **Cell Detection:** Apply another object detection model to locate individual cells within the detected table.
3. **OCR:** Use an OCR model to extract text from each detected cell.
4. **Post-Processing:** Organize the extracted text into a structured table format.

### Summary:
This project is a combination of classification, detection, and recognition tasks. While CNNs are crucial for feature extraction and initial segmentation/detection tasks, the overall system integrates various specialized models and techniques to achieve the final goal of converting an image into a table. Therefore, it's not just a classifier but a composite system involving several machine learning components.



## Workflows

1. Update config.yaml with the path to the image you want to convert to a table
2. Update secrets.yaml 
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. Add app.py

## How to run?

### STEPS:

1. Clone the repository

```bash
git clone https://github.com/luizamfsantos/Table-From-Image-DL-MLflow-DVC
```

2. Create a virtual environment

```bash
python3 -m venv tbldtc
```
or 
```bash
conda create -n tbldtc python=3.12 -y
```

3. Activate the virtual environment

```bash
source tbldtc/bin/activate
```
or 
```bash
conda activate tbldtc
```

4. Install the requirements

```bash
pip install -r requirements.txt
```