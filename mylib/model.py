from PIL import Image

def predict(image):
    class_labels = ["cat", "dog", "bird"]
    return class_labels[hash(image) % len(class_labels)]

def resize_image(image, size):
    return image.resize(size)

def convert_to_grayscale(image):
    return image.convert("L")   