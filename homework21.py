# You have source_directory with nested directories (any level of nesting).
# In all those directories could be text files (with extension *.txt) and any other files.
# Create file combined_files.txt.
# For every text file in source_directory that smaller or equal to 120 bytes,
# add filename (without full path) and content to combined_files.txt

import os
source_directory = 'homew21'

with open('combined_files.txt', 'w') as comb_file:
    for dirpath, dirnames, filenames in os.walk(source_directory):
        for file in filenames:
            if file.endswith('.txt'):
                file_path = os.path.join(dirpath, file)
                if os.path.getsize(file_path) <= 120:
                    with open(file_path, 'r') as f:
                        content = f.read()
                    comb_file.write(f"Filename: {file}\n")
                    comb_file.write(f"Content: {content}\n")
                    comb_file.write("-" * 40 + "\n")
