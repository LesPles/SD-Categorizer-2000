# SD-Cat2000

A Python script to organize a folder containg all your images into folders and export any **Stable Diffusion** generation metadata.

## 📁 Folder Structure

The script organizes files into the following **top-level folders**:

- **ComfyUI/**  
  Files generated using **ComfyUI**.

- **WebUI/**  
  Files generated using **WebUI**, organized into subfolders based on a **category of your choosing** (e.g., Model, Sampler).  
  A `.txt` file is created for each image with readable generation parameters.

- **No \<category\> found/**  
  Files that include metadata, but **lack the category** you've specified.  
  The text file contains the raw metadata as-is.

- **No metadata/**  
  Files that **do not contain any embedded EXIF metadata**.  
  These are further organized by **file extension** (e.g. PNG, JPG, MP4).

## 🏷 Supported WebUI Categories

The following categories are supported for classifying WebUI images.  

- `Model`
- `Model hash`
- `Size`
- `Sampler`
- `CFG scale`

## 🧰 Usage

```
python3 sd-cat2000.py -<flag> [-v] <file(s) or folder(s)>
```

Where `<flag>` is ONE of the following:
- `-m = Checkpoint Model`
- `-h = Checkpoint Model hash`
- `-d = Image Dimension`
- `-a = Sampler`
- `-c = CFG scale`

Optional:
-v — Verbose mode, prints detailed output for each file processed.
Without -v, a progress percentage is shown instead.


## 💡 Example

```bash
./sd-cat2000.py -m -v ImageDownloads/
```
This processes all files in the ImageDownloads/ folder and classifies WebUI images based on the Model.

Resulting Folder Layout:

```
ImageDownloads/
├── ComfyUI/
│   ├── ComfyUI00001.png
│   └── ComfyUI00002.png
├── No metadata/
│   ├── JPEG/
│   ├── JPG/
│   ├── PNG/
│   └── MP4/
├── No model found/
│   ├── 00005.png
│   └── 00005.png.txt
├── WebUI/
│   ├── cyberillustrious_v38/
│   │   ├── 00001.png
│   │   ├── 00001.png.txt
│   │   └── 00002.png
│   └── waiNSFWIllustrious_v120/
│       ├── 00003.png
│       ├── 00003.png.txt
│       └── 00004.png
```

## 📝 Example Metadata Output

00001.png.txt (from WebUI folder):
```
Positive prompt: High Angle (from the side) view Close shot (focus on head). muscular female, body blush, pale skin, long hair, black hair, sexy, lace trim, teasing, beckoning, wonder woman (cosplay), dreamy, bokeh, depth of field, still life, photo (medium), masterpiece, best quality, newest, sensitive, absurdres, <lora:MuscleUp-Ilustrious Edition:0.75>.
Negative prompt: lowres, bad quality, worst quality, child, loli, bad anatomy, deformity, extra fingers, signature, logo, username, school, bodybuilder.
Steps: 30
Sampler: DPM++ 2M SDE
Schedule type: Karras
CFG scale: 3.5
Seed: 1516059803
Size: 912x1144
Model hash: c34728806b
Model: cyberillustrious_v38
Denoising strength: 0.5
RNG: CPU
ADetailer model: face_yolov8n.pt
ADetailer confidence: 0.3
ADetailer dilate erode: 4
ADetailer mask blur: 4
ADetailer denoising strength: 0.4
ADetailer inpaint only masked: True
ADetailer inpaint padding: 32
ADetailer version: 25.3.0
Template: Freeze Frame shot. muscular female
<lora: MuscleUp-Ilustrious Edition:0.75>
Negative Template: lowres
Hires Module 1: Use same choices
Hires prompt: Freeze Frame shot. muscular female
Hires CFG Scale: 5
Hires upscale: 2
Hires steps: 20
Hires upscaler: 4x-UltraMix_Balanced
Lora hashes: MuscleUp-Ilustrious Edition: 7437f7a09915
Version: f2.0.1v1.10.1-previous-661-g0b261213
```

## ⚠️ Caveats

- Originally developed from a Bash v3.2 prototype.
- Not optimized or tested across all platforms.
- Assumes exiftool is installed and available in your system path.

## 🐞 Known Issues

- Subfolder input handling could be improved
- Hidden files (e.g., .DS_Store) are not ignored by default

## 📜 Version History

- 1.0 – Initial release

## 📦 Requirements

- Python 3.x
- exiftool (for reading image metadata)

