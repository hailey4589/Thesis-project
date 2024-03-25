from ultralytics import YOLO


model = YOLO('yolov8n.pt')


results = model.train(data = "/home/avl/Thesis-project/data/data.yaml", epochs=12, imgsz=608, batch = 64)
