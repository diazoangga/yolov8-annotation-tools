from ultralytics import YOLO
import os
import shutil

def detect_and_annotate(img_input, model_path='./yolov8m_custom.pt'):
    model = YOLO(model_path)
    predictions = model(img_input, save_txt=None)
    txt_save_path = f'{obj_train_data_dir}/{os.path.basename(img_input).split(".")[0]}.txt'
    img_save_path = os.path.join(obj_train_data_dir, os.path.basename(img_input))
    shutil.copy(img_input, img_save_path)
    with open(txt_save_path, '+w') as file:
        for idx, prediction in enumerate(predictions[0].boxes.xywhn): # change final attribute to desired box format
            cls = int(predictions[0].boxes.cls[idx].item())
            file.write(f"{cls} {prediction[0].item()} {prediction[1].item()} {prediction[2].item()} {prediction[3].item()}\n")
    
    print(f'exporting annotation file.... Successfully stored in {txt_save_path}')

def create_txt_train(images, save_dir):
    with open(f'{save_dir}/train.txt', '+w') as file:
        for img in images:
            img_name = os.path.basename(img)
            file.write(f'data/obj_train_data/{img_name}\n')

def create_obj_data(out_folder):
    content = """classes = 11
train = data/train.txt
names = data/obj.names
backup = backup/
"""
    with open(os.path.join(out_folder, "obj.data"), "w") as file:
        file.write(content)

def create_obj_names(out_folder):
    obj_names_content = """person
head
face
upper body
lower body
arm
sit down
motorcycle
fire
smoke
weapon/tool
"""

    with open(os.path.join(out_folder, "obj.names"), "w") as obj_names_file:
        obj_names_file.write(obj_names_content)


def get_all_images(src_path):
    imgs_path = [os.path.join(src_path, img) for img in os.listdir(src_path) if img.endswith('.png')]
    print(imgs_path)
    return imgs_path





# print(os.listdir(os.path.join(source_folder, 'img')))


if __name__ == "__main__":
    source_folder = input("Enter the folder path of your source images: ")
    out_folder = input("Enter the path of your output folder: ")
    model_path = input("Enter the path of your custom YOLOv8 model: ")
    obj_train_data_dir = os.path.join(out_folder, 'obj_train_data')

    print(f"This program is to annotate dataset automatically.\nModel :{model_path} \nSource path: {source_folder}\nOutput path: {out_folder} \nStarting...")
    print("=================================")
    print("Creating the output folder...")

    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
        print(f"path {out_folder} is created")
    if not os.path.exists(obj_train_data_dir):
        os.makedirs(obj_train_data_dir)
        print(f"path {obj_train_data_dir} is created")
    
    print(f"All the output from Yolov8 will be stored in {out_folder}")

    print(f"Getting all the images from the input path: {source_folder}")
    imgs_path = get_all_images(source_folder)

    print("=================================")
    print("YOLO....")
    for img_input in imgs_path:
        print(f"Detecting object for {os.path.basename(img_input)}")
        detect_and_annotate(img_input, model_path=model_path)

    print("=================================")
    print("Generating complement files...")
    create_txt_train(imgs_path, out_folder)
    create_obj_data(out_folder)
    create_obj_names(out_folder)

    print("DONE")
    print("To edit the annotation, you can zip the output path, and import the dataset to the CVAT with the YOLO 1.1 format")