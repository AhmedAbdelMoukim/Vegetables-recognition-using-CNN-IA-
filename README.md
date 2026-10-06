# Fruit and Vegetable Recognition System

A deep learning image classification pipeline built in Python using TensorFlow, Keras, Pillow, and Scikit-Learn. This project provides scripts to preprocess images, split datasets into structured directories, and train a Convolutional Neural Network (CNN) to recognize different types of fruits and vegetables.

---

## 🛠️ Features

- **Automated Image Resizing (`resize.py`):** Recursively resizes images across subfolders to a standard resolution (`224x224`).
- **Dataset Partitioning (`organisation.py`):** Organizes raw class folders into structured `train`, `validation`, and `test` subsets.
- **Model Training & Evaluation (`fruit_recognition.ipynb`):** Configures data generators, builds/compiles a Keras model, trains it on image batches, evaluates test accuracy, and exports the model (`fruit_model.h5`).

---

## 📂 Repository Structure

```text
.
├── resize.py               # Preprocessing script to resize raw dataset images
├── organisation.py         # Script to split and organize dataset into train/val/test folders
├── fruit_recognition.ipynb # Jupyter notebook to compile, train, evaluate, and save the model
└── README.md               # Project documentation
```

---

## 📋 Requirements & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/fruit-recognition.git](https://github.com/your-username/fruit-recognition.git)
   cd fruit-recognition
   ```

2. **Install dependencies:**
   ```bash
   pip install tensorflow pillow scikit-learn matplotlib numpy
   ```

---

## 🚀 Step-by-Step Usage

### 1. Preprocess Images
Run `resize.py` to recursively scale all images to `224x224` pixels:
```bash
python resize.py
```

### 2. Organize Dataset
Run `organisation.py` to create `train`, `validation`, and `test` directory splits:
```bash
python organisation.py
```

### 3. Train & Evaluate the Model
Open `fruit_recognition.ipynb` in Jupyter Notebook or Google Colab:
1. Define your CNN architecture (e.g., Sequential model with Conv2D, MaxPooling2D, Dense layers).
2. Compile the model with an optimizer (e.g., `adam`) and loss function (`categorical_crossentropy`).
3. Train the model using `model.fit()` with your data generators:
   ```python
   # Example training step in fruit_recognition.ipynb
   history = fruit_model.fit(
       train_generator,
       epochs=10,
       validation_data=validation_generator
   )
   ```
4. Evaluate performance on the test generator and save the model to disk:
   ```python
   score = fruit_model.evaluate(test_generator, verbose=0)
   print("Test loss:", score[0])
   print("Test accuracy:", score[1])

   fruit_model.save('fruit_model.h5')
   ```

---

## 📊 Results & Predictions

Run the final cells in `fruit_recognition.ipynb` to plot test sample images alongside their predicted class labels using Matplotlib.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
