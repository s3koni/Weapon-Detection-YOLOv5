import tkinter as tk
from tkinter import filedialog
import subprocess
import sys
from tqdm import tqdm
import re
import os
import shutil
import time

def check_existing_exp():
    base_path = os.path.join('yolov5', 'runs', 'detect')
    exp_path = os.path.join(base_path, 'exp')
    
    if os.path.exists(exp_path):
        print("Found existing 'exp' folder. This needs to be handled before proceeding.")
        while True:
            response = input("Would you like to (D)elete it, (R)ename it to expOLD, or (Q)uit? ").lower()
            if response == 'd':
                try:
                    print("Deleting exp folder...")
                    for root, dirs, files in os.walk(exp_path):
                        for file in files:
                            filepath = os.path.join(root, file)
                            try:
                                os.chmod(filepath, 0o777)
                            except:
                                pass
                    
                    shutil.rmtree(exp_path, ignore_errors=True)
                    time.sleep(1)
                    if not os.path.exists(exp_path):
                        print("Successfully deleted exp folder")
                        break
                    else:
                        print("Failed to delete exp folder completely")
                        return False
                        
                except Exception as e:
                    print(f"Error deleting exp folder: {str(e)}")
                    return False
                    
            elif response == 'r':
                try:
                    old_path = os.path.join(base_path, 'expOLD')
                    if os.path.exists(old_path):
                        print("Removing existing expOLD folder...")
                        shutil.rmtree(old_path, ignore_errors=True)
                        time.sleep(1)
                    
                    print("Renaming exp to expOLD...")
                    os.rename(exp_path, old_path)
                    
                    if os.path.exists(old_path) and not os.path.exists(exp_path):
                        print("Successfully renamed to expOLD")
                        break
                    else:
                        print("Failed to rename folder")
                        return False
                        
                except Exception as e:
                    print(f"Error renaming exp folder: {str(e)}")
                    return False
                    
            elif response == 'q':
                print("Operation cancelled by user")
                return False
            else:
                print("Please enter 'D' to delete, 'R' to rename, or 'Q' to quit.")    
    
    return True

def select_video():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)  # Make sure the dialog appears on top
    root.focus_force()  # Force focus to the window
    video_path = filedialog.askopenfilename(
        parent=root,  # Set the parent window
        title="Select a Video File",
        filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.mkv")]
    )
    root.destroy()  # Destroy the root window after selection
    return video_path

def run_detection(video_path):
    command = f'python yolov5/detect.py --weights yolov5/skViolence.pt --source "{video_path}" --conf-thres 0.25 --save-txt --save-conf'
    
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )

    pbar = None
    total_frames = None

    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            match = re.search(r'\((\d+)/(\d+)\)', output.strip())
            if match:
                current_frame, total_frames = map(int, match.groups())
                
                if pbar is None:
                    pbar = tqdm(total=total_frames, desc="Processing video", 
                              bar_format='{l_bar}{bar:30}{r_bar}')
                    
                pbar.update(1)
    
    if pbar:
        pbar.close()
    
    return process.poll()

def main():
    # First check for existing exp folder
    if not check_existing_exp():
        print("Pre-check failed, exiting...")
        return
        
    # Continue with video selection and processing
    print("\nPlease select a video file...")
    video_file_path = select_video()
    
    if not video_file_path:  # If no file was selected
        print("\nNo video selected. Exiting...")
        return
        
    print(f"\nSelected video: {video_file_path}")
    print("\nStarting video processing...")
    print("---------------------------------------------------------------------------------------")
    run_detection(video_file_path)
    print("\nProcessing complete!")

    # Run analysis
    from analyze_labels import analyze_labels
    result = analyze_labels()
    print(result)
    if result != "No files or folders detected":
        input()
        # After analysis and pressing Enter:
        subprocess.run(['python', 'rename_exp.py'])

if __name__ == "__main__":
    main()