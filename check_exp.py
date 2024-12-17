import os
import shutil
import time

def check_existing_exp():
    """
    Checks for existing exp folder before analysis begins.
    Returns True if it's safe to proceed, False if user cancels or error occurs.
    """
    base_path = os.path.join('yolov5', 'runs', 'detect')
    exp_path = os.path.join(base_path, 'exp')
    
    if os.path.exists(exp_path):
        print("Found existing 'exp' folder. This needs to be handled before proceeding.")
        while True:
            response = input("Would you like to (D)elete it, (R)ename it to expOLD, or (Q)uit? ").lower()
            if response == 'd':
                try:
                    print("Deleting exp folder...")
                    # Make sure all files are closeable
                    for root, dirs, files in os.walk(exp_path):
                        for file in files:
                            filepath = os.path.join(root, file)
                            try:
                                os.chmod(filepath, 0o777)
                            except:
                                pass
                    
                    # Try to delete
                    shutil.rmtree(exp_path, ignore_errors=True)
                    
                    # Wait and verify deletion
                    time.sleep(1)
                    if not os.path.exists(exp_path):
                        print("Successfully deleted exp folder")
                        return True
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
                        return True
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

if __name__ == "__main__":
    # Run the check
    if not check_existing_exp():
        print("Operation cancelled or failed. Please resolve the exp folder issue before proceeding.")
        exit(1)  # Exit with error code 1 if check fails
    print("Pre-check completed successfully.")
    exit(0)  # Exit with success code 0 if check passes