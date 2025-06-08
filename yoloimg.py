from ultralytics import YOLO

# Load a pre-trained YOLO model (adjust model type as needed)
model = YOLO("yolo11n.pt")  # n, s, m, l, x versions available --> n being the fastest

# Perform object detection on an image
results = model.predict(source="D:\PROJECTS\Pycharm\TestFiles\cars1.png")  # Can also use video, directory, URL, etc.

# Display the results
results[0].show()  # Show the first image results