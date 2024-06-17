# Train YOLOv10 on Custom Dataset (Ubuntu)

### 1. Download and configure YOLOv10 environment (if not done yet)
```bash
git clone https://github.com/THU-MIG/yolov10.git
conda activate yolov10
cd /home/hammond/yolov10
pip install -r requirements.txt
pip install -e .
```
### 2. Train YOLOv10 on your own dataset (from Roboflow in this case)
Something to be chanegd in data.yaml (paths to things)
```yaml
path: /home/hammond/useYOLO

train: /home/hammond/useYOLO/train
val: /home/hammond/useYOLO/valid
test: /home/hammond/useYOLO/test

names: 
  0: Kapadokya
  1: Nurlu
  2: Sira
```
Then,
```bash
yolo train data=/home/hammond/useYOLO/data.yaml model=/home/hammond/useYOLO/yolov10n.pt epochs=100 batch=32 plots=True
yolo val data=/home/hammond/useYOLO/data.yaml model=/home/hammond/useYOLO/yolov10n.pt batch=32 imgsz=640
yolo predict model=/home/hammond/useYOLO/yolov10n.pt source=/path/to/your/test/images
```
