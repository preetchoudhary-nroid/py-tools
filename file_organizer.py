#FILE ORGANIZER
import os
import shutil #HAS POWER TO CUT PASTE COPY FILE----
print("----- SYSTEM AUTOMATED FILE ORGANIZER -----")
target_dir = "./TargetFolder" #TARGET FILE WHERE TO THINGS WILL BE ORGANIZED----
EXTENSION_MAP = {
    '.pdf': 'PDFs',
    '.docx': 'Documents',
    '.txt':'Documents',
    '.jpg':'Images',
    '.png':'Images',
    '.mp4':'Videos',
    '.zip':'Archives'
}
if not os.path.exists(target_dir):              #IF THERE IS NO TARGET FOLDER PYTHON AUTOMATICALLY MAKES IT.
    os.makedirs(target_dir)
    print(f"[!] Created '{target_dir}. Please drop some test files inside it!!!.")
else:
    print(f"[!] Scanning directory: {target_dir}")
files_moved_count = 0
folders_created = set()
moved_files_history = []
print(f"[+] Scanning directory: {target_dir}\n")

for filename in os.listdir(target_dir):
    source_path = os.path.join(target_dir, filename)

    if os.path.isdir(source_path):
        continue
    name, ext = os.path.splitext(filename)
    ext = ext.lower()

    if ext in EXTENSION_MAP:
        subfolder_name = EXTENSION_MAP[ext]
        subfolder_path = os.path.join(target_dir, subfolder_name)

        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
            folders_created.add(subfolder_name)
        destination_path = os.path.join(subfolder_path, filename)
        shutil.move(source_path, destination_path)            #MOVES THE FILE FROM OLD TO NEW

        moved_files_history.append((source_path, destination_path))
        files_moved_count += 1
        print(f"[->] Moved: {filename} to {subfolder_name}")

print("\n" + "="*40)
print("         SCAN SUMMARY            ")
print("="*40)
print(f"total files Moved : {files_moved_count}")
print(f"Subfolders created : {len(folders_created)} ({','.join(folders_created) if folders_created else 'None' })")
print("="*40 + "\n")

if files_moved_count > 0:
        undo_choice = input("would you like to undo this file? (y/n")
        if undo_choice == "yes" or undo_choice == "y":
            print("\n[!] Reversing the operations---Restoring original states")

            for original_path, new_path in moved_files_history:
                if os.path.exists(new_path):
                    shutil.move(new_path, original_path)
                    print(f"[->] Restored: {os.path.basename(original_path)}")
            print("\n[+] UNDO OPERATION IS COMPLETE. ALL FILES ARE RETURNED SAFELY")
        else:
             print("\n[+] Changes saved permanently. CLEANING SESSION FINALIZED")
else:
    print("[*] No target files found to organize")































