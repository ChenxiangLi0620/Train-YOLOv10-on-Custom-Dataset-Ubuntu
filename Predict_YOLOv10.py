from ultralytics import YOLOv10  # Ensure you import YOLOv10 from the correct module

# Path to the trained model weights
model_path = '/home/hammond/yolov10/runs/detect/train/weights/best.pt'

# Initialize the YOLOv10 model with the trained weights
model = YOLOv10(model_path)

# Define the source directory containing test images
test_images_dir = '/home/hammond/useYOLO/test/images'

# Run inference on the test dataset
results = model(source=test_images_dir, conf=0.25, save=True)

# If save=True, results will be saved in the specified directory
