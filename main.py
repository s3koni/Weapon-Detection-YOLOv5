import tkinter as tk
from tkinter import filedialog
import subprocess
import sys
from tqdm import tqdm
import re

# First, check for existing exp folder
import subprocess
result = subprocess.run(['python', 'check_exp.py'])
if result.returncode != 0:
    print("Pre-check failed, exiting...")
    exit(1)

# Then run selection function
def select_video():
    root = tk.Tk()
    root.withdraw()
    video_path = filedialog.askopenfilename(
        title="Select a Video File",
        filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.mkv")]
    )
    return video_path

def run_detection(video_path):
    command = f'python yolov5/detect.py --weights yolov5/runs/train/exp/weights/best.pt --source "{video_path}" --conf-thres 0.25 --save-txt --save-conf'
    
    # Start the process with pipe for output
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )

    # Initialize progress bar
    pbar = None
    total_frames = None

    # Process output in real-time
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            # Parse the frame count from the output
            match = re.search(r'\((\d+)/(\d+)\)', output.strip())
            if match:
                current_frame, total_frames = map(int, match.groups())
                
                # Initialize progress bar if not already done
                if pbar is None:
                    pbar = tqdm(total=total_frames, desc="Processing video", 
                              bar_format='{l_bar}{bar:30}{r_bar}')
                    
                # Update progress
                pbar.update(1)
    
    if pbar:
        pbar.close()
    
    return process.poll()

if __name__ == "__main__":
    video_file_path = select_video()
    if video_file_path:
        print("\nStarting video processing...")
        print("---------------------------------------------------------------------------------------")
        run_detection(video_file_path)
        print("\nProcessing complete!")
    else:
        print("\nNo video selected.")

# Initializing the analyze_labels script
from analyze_labels import analyze_labels

# After your first script's operations complete successfully
result = analyze_labels()
print(result)
if result != "No files or folders detected":
    input()

    # After analysis and pressing Enter:
subprocess.run(['python', 'rename_exp.py'])