from sklearn.cluster import KMeans
import cv2
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

model = tf.keras.models.load_model("KmeansHistogramYellow.keras")

def extract_yellow_histogram_features(image, bins=10, visualize=False):
    lab_image = cv2.cvtColor(image.astype(np.uint8), cv2.COLOR_RGB2LAB)
    L, A, B = lab_image[:, :, 0], lab_image[:, :, 1], lab_image[:, :, 2]
    L_valid, A_valid, B_valid = L.flatten(), A.flatten(), B.flatten()

    if L_valid.size == 0:
        return np.zeros(bins * 3)

    L_hist = np.histogram(L_valid / 255.0, bins=bins, range=(0, 1), density=True)[0]
    A_hist = np.histogram((A_valid + 128) / 255.0, bins=bins, range=(0, 1), density=True)[0]
    B_hist = np.histogram((B_valid + 128) / 255.0, bins=bins, range=(0, 1), density=True)[0]

    feature_vector = np.concatenate([L_hist, A_hist, B_hist])

    return feature_vector

def visualize_masking(image, valid_mask):
    masked_image = image.copy()
    masked_image[~valid_mask] = [0, 0, 0]

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(masked_image)
    plt.title("Masked Sclera")
    plt.axis("off")

    plt.show()

def predict_jaundice(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    features = extract_yellow_histogram_features(image)
    features = features.reshape(1, -1)

    prediction = model.predict(features)
    print(prediction)
    return "Jaundiced" if prediction >= 0.50 else "Normal"

image_path = "healthy.jpg"
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

result = predict_jaundice(image_path)
print("Prediction:", result)

extract_yellow_histogram_features(image, visualize=True)