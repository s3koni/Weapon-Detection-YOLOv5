import os
import glob

def analyze_labels():
    print("Analyzing generated labels")
    
    # Define the labels directory path
    labels_dir = os.path.join('yolov5', 'runs', 'detect', 'exp', 'labels')
    
    # Check if directory exists and contains .txt files
    if not os.path.exists(labels_dir):
        return "No files or folders detected"
    
    txt_files = glob.glob(os.path.join(labels_dir, '*.txt'))
    if not txt_files:
        return "No files or folders detected"
    
    # Initialize counters
    knife_frames = 0  # class 0
    gun_frames = 0    # class 1
    violent_frames_set = set()  # To track unique violent frames
    
    # Process each label file
    for label_file in txt_files:
        with open(label_file, 'r') as f:
            content = f.read().strip()
            if content:  # Check if file is not empty
                lines = content.split('\n')
                has_knife = any(line.startswith('80 ') for line in lines)
                has_gun = any(line.startswith('81 ') for line in lines)
                
                if has_knife:
                    knife_frames += 1
                if has_gun:
                    gun_frames += 1
                if has_knife or has_gun:
                    violent_frames_set.add(label_file)
    
    # Calculate totals and rating
    total_violent_frames = len(violent_frames_set)  # Count unique violent frames
    total_frames = len(txt_files)
    violence_rating = (total_violent_frames / total_frames * 100) if total_frames > 0 else 0
    
    # Prepare output message
    result = f"""
Video Analysis Results
---------------------------------------------------------------------------------------
There are: {knife_frames} frame(s) containing knives
          {gun_frames} frame(s) containing guns
A total number of frames that depict violence: {total_violent_frames}
Based on the frames, the Violence Probability Rating is: {violence_rating:.2f}%

(NOTE! If the model is able to detect other objects in the video, this can help 
generate a more accurate Violence Probability Rating.)

Press Enter to exit..."""
    
    return result


'''
 Main function to run the analysis.
'''
def main():
    result = analyze_labels()
    print(result)
    if result != "No files or folders detected":
        input()  # Wait for Enter only if analysis was successful

if __name__ == "__main__":
    main()


def rename_exp_folder():
    """
    Renames the 'exp' folder to 'expDUMP' after analysis is complete.
    Returns True if successful, False if there was an error.
    """
    try:
        base_path = os.path.join('yolov5', 'runs', 'detect')
        exp_path = os.path.join(base_path, 'exp')
        dump_path = os.path.join(base_path, 'expDUMP')
        
        # Check if exp folder exists
        if not os.path.exists(exp_path):
            print("No exp folder found to rename")
            return False
            
        # If expDUMP already exists, remove it
        if os.path.exists(dump_path):
            try:
                import shutil
                shutil.rmtree(dump_path)
            except Exception as e:
                print(f"Error removing existing expDUMP folder: {e}")
                return False
        
        # Rename exp to expDUMP
        os.rename(exp_path, dump_path)
        print("Successfully renamed exp folder to expDUMP")
        return True
        
    except Exception as e:
        print(f"Error renaming exp folder: {e}")
        return False