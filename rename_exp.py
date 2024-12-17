import os
import shutil

def rename_to_expDUMP():
    """
    Renames the exp folder to expDUMP after analysis is complete.
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

if __name__ == "__main__":
    # Run the rename operation
    rename_to_expDUMP()
