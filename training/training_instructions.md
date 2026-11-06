# Model Training Instructions

## 1. Overview

This project uses the YOLOv5 object detection model to identify two types of road hazards:

- Speed Breakers
- Potholes

The model is trained using the **Indian Roads Dataset**, obtained from Kaggle.

## 2. Dataset Source

**Dataset Name:** Indian Roads Dataset

**Author:** mitangshu11

**Platform:** Kaggle

**Dataset Link:** https://www.kaggle.com/datasets/mitangshu11/indian-roads-dataset

The dataset contains images of Indian roads, including potholes, marked and unmarked speed-breakers, and poorly maintained unpaved roads.

The images are annotated for object detection and use the YOLO annotation format.

## 3. Dataset Preparation

1. Visit the Kaggle dataset link.
2. Download the dataset to your computer.
3. Extract the downloaded ZIP file.
4. Arrange the images and corresponding annotation files into training and validation folders.
5. Ensure that the dataset structure matches the paths specified in `dataset.yaml`.

Expected directory structure:

```text
dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

## 4. Dataset Configuration

The project uses the following `dataset.yaml` configuration:

```yaml
train: ./dataset/images/train
val: ./dataset/images/val

nc: 2
names: ['speed-breakers', 'potholes']
```

The model is configured to detect two classes:

- Class 0: speed-breakers
- Class 1: potholes

## 5. Environment Setup

Install the required Python dependencies from the YOLOv5 project directory:

```bash
pip install -r requirements.txt
```

Make sure Python and the required libraries are installed before starting training.

## 6. Model Training

Run the following command from the YOLOv5 project directory:

```bash
python train.py --img 640 --batch 16 --epochs 50 --data dataset.yaml --weights yolov5s.pt
```

Command parameters:

| Parameter | Description |
|---|---|
| `--img 640` | Input image size |
| `--batch 16` | Batch size |
| `--epochs 50` | Number of training epochs |
| `--data dataset.yaml` | Dataset configuration |
| `--weights yolov5s.pt` | Pretrained YOLOv5s weights |

These are example training settings. Use the actual values from your training run if they differ.

## 7. Training Results

YOLOv5 generally saves training results in:

```text
runs/train/exp/
```

The trained model weights are stored in:

```text
runs/train/exp/weights/
├── best.pt
└── last.pt
```

- `best.pt`: Best-performing checkpoint during training.
- `last.pt`: Checkpoint from the final training epoch.

## 8. Model Evaluation

Evaluate the trained model using validation images.

Important performance metrics include:

- Precision
- Recall
- Mean Average Precision (mAP)
- Training and validation loss

## 9. Model Testing

Use the trained model to detect road hazards in test images:

```bash
python detect.py --weights runs/train/exp/weights/best.pt --source path/to/test/image
```

Replace the image path with the location of your test image or supported video source.

## 10. Important Notes

- The dataset is not included in this GitHub repository because of its size.
- Users must download the dataset separately from Kaggle.
- Make sure the dataset folder paths match `dataset.yaml`.
- Keep the YOLO-format image annotations alongside their corresponding images.
- Test the trained model before deploying it on the Raspberry Pi.