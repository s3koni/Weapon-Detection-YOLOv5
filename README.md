# **Violence Detection in Videos Using YOLOv5**

This project analyzes videos for violent content using a YOLOv5-based object detection system. The system detects weapons like guns and knives, assesses frames for violence, and provides a violence rating for the entire video.

---

## **Features**

1. **Pre-Run Check**:
   - Ensures no overwrite errors occur by verifying if an existing `exp` folder is present in the `yolov5/runs/detect` directory.  
   - If found, the process stops to prevent accidental overwrites.

2. **Video Selection**:
   - Opens a dialog box for the user to select a video file for analysis.
   - The selected video’s path is appended to the `detect.py` command as the `--source` argument.

3. **Video Processing**:
   - YOLOv5 analyzes the video frame by frame, detecting objects like guns and knives.
   - The results are logged and displayed after processing.

4. **Post-Processing**:
   - Invokes `rename_exp.py` to rename the newly generated `exp` folder to `expDUMP` to ensure proper organization of results.
   - The renaming happens when the user presses **Enter** after analysis.

---

## **Workflow**

### **1. Pre-Check**  
`main.py` invokes `check_exp.py` to check for an existing `exp` folder:
   - If no `exp` folder exists, the process continues.
   - If an `exp` folder exists, the user is prompted to resolve the conflict.

### **2. Video Selection**  
A dialog box opens for the user to select a video for processing.  

### **3. Detection**  
The selected video is passed to the `detect.py` script for analysis. The detection results include:
   - Number of frames containing knives.
   - Number of frames containing guns.
   - Total frames classified as violent.
   - Overall violence rating (%).

### **4. Post-Processing**  
The results folder (`exp`) is renamed to `expDUMP` when the user presses Enter.

---

## **How to Run**

1. Clone the repository:
   ```bash
   git clone https://github.com/s3koni/Weapon-Detection-YOLOv5
   cd Weapon-Detection-YOLOv5
   ```

2. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Start the program:
   ```bash
   python main.py
   ```

4. Select a video for processing through the dialog box.

5. View the analysis results, and press **Enter** to rename the `exp` folder to `expDUMP`.

---

## **Example Output**

```plaintext
Pre-check completed successfully.

Starting video processing...
---------------------------------------------------------------------------------------
Processing video: 100%|██████████████████████████████| 218/218 [00:55<00:00,  3.93it/s]

Processing complete!
Analyzing generated labels

Video Analysis Results
This video contains violent content
There are: 0 frames containing knives
           5 frames containing guns
A total number of frames that show violence: 5
This video has a violence rating of: 100.00%

Press Enter to exit...

Successfully renamed exp folder to expDUMP
```

---

## **File Structure**

```plaintext
├── main.py             # Entry point for the program
├── check_exp.py        # Pre-run check for existing 'exp' folder
├── rename_exp.py       # Renames 'exp' to 'expDUMP'
├── yolov5/             # YOLOv5 model folder
│   ├── detect.py           # YOLOv5 detection script
│   ├── runs/
│   │   └── detect/     # Results folders (e.g., exp, expDUMP)
│   └── datasets/       # Datasets used for training
├── requirements.txt    # Python dependencies
└── README.md           # Documentation
```

---

## **Dependencies**

This project requires Python 3.8+ and the following Python packages:
- PyTorch
- YOLOv5 dependencies
- Tkinter (for the dialog box)
- Any other required dependencies are listed in `requirements.txt`.

---


Feel free to reach out with questions or contributions!

