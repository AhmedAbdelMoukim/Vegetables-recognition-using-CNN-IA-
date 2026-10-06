import os
import random
from sklearn.model_selection import train_test_split
import shutil

dataset_folder = ''

classes = os.listdir(dataset_folder)

test_ratio = 0.1
validation_ratio = 0.2

for class_name in classes:
    class_folder = os.path.join(dataset_folder, class_name)
    image_files = os.listdir(class_folder)

    train_files, test_validation_files = train_test_split(image_files, test_size=test_ratio + validation_ratio, random_state=42)

    test_files, validation_files = train_test_split(test_validation_files, test_size=validation_ratio/(test_ratio + validation_ratio), random_state=42)

    train_folder = os.path.join('', class_name)
    test_folder = os.path.join('', class_name)
    validation_folder = os.path.join('', class_name)

    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    os.makedirs(validation_folder, exist_ok=True)

    for file in train_files:
        shutil.copy(os.path.join(class_folder, file), os.path.join(train_folder, file))

    for file in test_files:
        shutil.copy(os.path.join(class_folder, file), os.path.join(test_folder, file))

    for file in validation_files:
        shutil.copy(os.path.join(class_folder, file), os.path.join(validation_folder, file))

print("Dataset split completed successfully!")