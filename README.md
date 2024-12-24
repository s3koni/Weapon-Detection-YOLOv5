# **Weapon Detection in Videos Using YOLOv5**

This project analyzes videos for violent content using a YOLOv5-based object detection system. The system detects weapons like guns and knives, assesses frames for violence, and provides a violence probability rating for the entire video.

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
`main.py` invokes `check_existing_exp()` to check for an existing `exp` folder:
   - If no `exp` folder exists, the process continues.
   - If an `exp` folder exists, the user is prompted to resolve the conflict.

### **2. Video Selection**  
A dialog box opens for the user to select a video for processing.  

### **3. Detection**  
The selected video is passed to the `detect.py` script for analysis. The detection results include:
   - Number of frames containing knives.
   - Number of frames containing guns.
   - Total frames classified as violent.
   - Overall violence probability rating (%).

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
---------------------------------------------------------------------------------------
There are: 0 frame(s) containing knives
           5 frame(s) containing guns
A total number of frames that depict violence: 5
Based on the frames, the Violence Probability Rating is: 40.00%

(NOTE! If the model is able to detect other objects in the video, this can help 
generate a more accurate Violence Probability Rating.)

Press Enter to exit...

Successfully renamed exp folder to expDUMP
```

---

## **File Structure**

```plaintext
├── main.py             # Entry point for the program
├── analyze_labels.py   # Runs the logic to analyze the contents of the exp folder.
├── rename_exp.py       # Renames 'exp' to 'expDUMP'
├── yolov5/             # YOLOv5 model folder
│   ├── detect.py       # YOLOv5 detection script
│   ├── skViolence.pt   # Custom Trained weight for detection
│   └── runs/
│       └── detect/     # Results folders (e.g., exp, expDUMP)
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