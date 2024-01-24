from ultralytics import YOLO


model = YOLO('yolov8n.pt')

data_path = "data"



results = model.train(data = "", epochs=50, imgsz=900, batch = 12)
