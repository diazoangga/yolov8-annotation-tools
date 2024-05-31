# Automated Annotation Tool using Customized YOLOv8

This repository contains an automated annotation tool built using a customized version of YOLOv8. The tool allows you to generate annotated datasets from images with minimal manual intervention.

## Steps to Use the Tool

1. **Install the required packages:**
   ```sh
   pip install -r requirements.txt

2. **Run the annotation script:**
   ```sh
   python gen_annotated_dataset.py

3. **Input Required Information**

You will be prompted to input the following in the terminal:

- **Source Folder:** The path to the folder containing images to be annotated.
- **Output Folder:** The path where the annotated dataset will be generated.
- **Model Path:** The path to the YOLO model, which should be `./yolov8m_310524.pt`.

4. **Compress the output folder:**

Once the dataset generation is complete, compress the output folder into a zip file.

5. **Edit annotations if necessary:**

Upload the zip file to [CVAT](https://cvat.org/) and make any necessary edits to the annotations.

## Example Usage
Here is an example of how to use the tool:

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt

2. **Run the script:**
    ```sh
    python gen_annotated_dataset.py

3. **Follow the prompts in the terminal:**
    ```sh
    Enter the folder path of your source images: /path/to/source/folder
    Enter the path of your output folder: /path/to/output/folder
    Enter the folder path of your model path: ./yolov8m_310524.pt

4. **Compress the output folder:**
    ```sh
    zip -r annotated_dataset.zip /path/to/output/folder

5. Go to CVAT and upload annotated_dataset.zip to review and edit the annotations if needed.