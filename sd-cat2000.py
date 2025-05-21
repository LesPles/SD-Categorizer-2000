#!/usr/bin/env python3
# Version 1.1

import sys
import os
import subprocess
import shutil
import re

FLAG_MAP = {
    '-m': 'Model',
    '-h': 'Model hash',
    '-d': 'Size',
    '-a': 'Sampler',
    '-c': 'CFG scale'
}

def run_exiftool(file_path, tag):
    try:
        result = subprocess.check_output(['exiftool', f'-s3', f'-{tag}', file_path], stderr=subprocess.DEVNULL)
        return result.decode('utf-8').strip()
    except subprocess.CalledProcessError:
        return ''

def safe_name(name):
    return re.sub(r'[\\/:"*?<>|]+', '', name)

def print_progress(current, total):
    percent = int((current / total) * 100)
    sys.stdout.write(f"\rProcessing: {percent}%")
    sys.stdout.flush()

def classify_file(file_path, base_dir, category, verbose):
    filename = os.path.basename(file_path)
    ext = os.path.splitext(filename)[1][1:].upper() or 'UNKNOWN'

    prompt = run_exiftool(file_path, 'Prompt')
    comment = run_exiftool(file_path, 'Comment')
    parameters = run_exiftool(file_path, 'Parameters')
    ucomment = run_exiftool(file_path, 'UserComment')


    # Case A: No metadata at all
    if not prompt and not comment and not parameters and not ucomment:
        target_dir = os.path.join(base_dir, 'No metadata', ext)
        os.makedirs(target_dir, exist_ok=True)
        shutil.move(file_path, os.path.join(target_dir, filename))
        if verbose:
            print(f"Moved '{file_path}' to '{target_dir}' (no metadata).")
        return

    # Case B: ComfyUI
    if '"class_type":' in prompt:
        target_dir = os.path.join(base_dir, 'ComfyUI')
        os.makedirs(target_dir, exist_ok=True)
        shutil.move(file_path, os.path.join(target_dir, filename))
        if verbose:
            print(f"Moved '{file_path}' to '{target_dir}' (ComfyUI detected).")
        return

    # Case C/D: WebUI or Unknown metadata
    metadata_source = parameters or comment or ucomment
    if metadata_source:
        metadata = {}

        # Parse Positive prompt (before Negative prompt: or Steps:)
        pos_match = re.search(r'^(.*?)(Negative prompt:|Steps:|$)', metadata_source, re.DOTALL)
        positive_prompt = pos_match.group(1).strip() if pos_match else metadata_source.strip()
        metadata["Positive prompt"] = positive_prompt

        # Optional Negative prompt
        neg_match = re.search(r'Negative prompt:(.*?)(Steps:|$)', metadata_source, re.DOTALL)
        if neg_match:
            metadata["Negative prompt"] = neg_match.group(1).strip()

        # Key-value parsing from Steps: onward
        steps_start = metadata_source.find("Steps:")
        if steps_start != -1:
            remainder = metadata_source[steps_start:]
            pairs = remainder.split(',')
            for pair in pairs:
                if ':' in pair:
                    key, value = pair.split(':', 1)
                    key = key.strip()
                    value = value.strip().strip('"')
                    if key not in metadata:
                        metadata[key] = value

        # Determine classification value
        value = metadata.get(category)
        if value:
            folder_name = safe_name(value)
            target_dir = os.path.join(base_dir, 'WebUI', folder_name)
        else:
            # CHANGED: Top-level folder for "No <category> found"
            folder_name = f"No {category} found"
            target_dir = os.path.join(base_dir, folder_name)

        os.makedirs(target_dir, exist_ok=True)
        new_path = os.path.join(target_dir, filename)
        shutil.move(file_path, new_path)

        # Write metadata to .txt
        txt_file = new_path + '.txt'
        with open(txt_file, 'w') as f:
            if folder_name.startswith("No "):
                f.write(metadata_source)  # raw, unformatted metadata
            else:
                for k, v in metadata.items():
                    f.write(f"{k}: {v}\n")

        if verbose:
            print(f"Moved '{file_path}' to '{target_dir}' and created metadata file.")
        return

    # Case E: Unknown metadata
    target_dir = os.path.join(base_dir, 'Unknown metadata')
    os.makedirs(target_dir, exist_ok=True)
    shutil.move(file_path, os.path.join(target_dir, filename))
    if verbose:
        print(f"Moved '{file_path}' to '{target_dir}' (unclassified metadata).")

def collect_files(paths):
    files = []
    for path in paths:
        if os.path.isfile(path):
            files.append(path)
        elif os.path.isdir(path):
            for entry in os.listdir(path):
                full_path = os.path.join(path, entry)
                if os.path.isfile(full_path):
                    files.append(full_path)
    return files

def main():
    if len(sys.argv) < 3:
        print("Usage: sd-cat2000.py -<flag> [-v] <file(s) or folder(s)>")
        print("Supported flags:", ' '.join(FLAG_MAP.keys()))
        sys.exit(1)

    flag = sys.argv[1]
    if flag not in FLAG_MAP:
        print(f"Unsupported flag: {flag}")
        sys.exit(1)

    verbose = False
    if sys.argv[2] == '-v':
        verbose = True
        paths = sys.argv[3:]
    else:
        paths = sys.argv[2:]

    category = FLAG_MAP[flag]
    files = collect_files(paths)

    total = len(files)
    for idx, file_path in enumerate(files, 1):
        if not os.path.isfile(file_path):
            if verbose:
                print(f"Skipping: {file_path} (not a regular file)")
            continue
        base_dir = os.path.dirname(os.path.abspath(file_path))
        classify_file(file_path, base_dir, category, verbose)
        if not verbose:
            print_progress(idx, total)

    if not verbose:
        print("\nDone.")

if __name__ == '__main__':
    main()
