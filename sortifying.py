import os
import shutil

# Mapping file extensions to destination folder names
EXT_MAP = {
    'Documents': ['.pdf', '.docx', '.doc', '.txt', '.pptx', '.xlsx', '.csv'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp'],
    'Audio': ['.mp3', '.wav', '.flac', '.m4a'],
    'Video': ['.mp4', '.mkv', '.mov', '.avi'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Executables': ['.exe', '.msi', '.bat'],
    'Code': ['.py', '.js', '.html', '.css', '.cpp', '.c', '.java', '.json']
}

def organize_directory(target_path):
    if not os.path.exists(target_path):
        print(f"Error: Path '{target_path}' does not exist.")
        return

    print(f"Organizing: {target_path}...\n")
    
    for filename in os.listdir(target_path):
        filepath = os.path.join(target_path, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder_name, extensions in EXT_MAP.items():
            if file_ext in extensions:
                destination_dir = os.path.join(target_path, folder_name)
                os.makedirs(destination_dir, exist_ok=True)
                
                shutil.move(filepath, os.path.join(destination_dir, filename))
                print(f"[MOVED] {filename} -> {folder_name}/")
                moved = True
                break

        # Move unknown file types to 'Others'
        if not moved and file_ext:
            destination_dir = os.path.join(target_path, 'Others')
            os.makedirs(destination_dir, exist_ok=True)
            shutil.move(filepath, os.path.join(destination_dir, filename))
            print(f"[MOVED] {filename} -> Others/")

    print("\nSortifying run complete! Target directory clean.")

if __name__ == "__main__":
    target = input("Enter path to organize (or press Enter for current directory): ").strip()
    if not target:
        target = os.getcwd()
    organize_directory(target)