This is a basic Python 3 script generated in ChatGPT to organise your image dump folders and export the WebUI generation parameters if found.

The script will organise into these four top level folders:

- ComfyUI: Containing any files generated using ComfyUI
- WebUI: Containing any files generated using WebUI, broken down by a category of your choosing, e.g. by Model.  A text file containing the generation parameters is included for ease of reading.
- No <category found>: Containing any files that have metadata that is unknown, incomplete or just doesn't contain the category of your choosing.  A text file containing whatever metadata can be found.
- No metadata: Containing any other files that do not contain any metadata, broken down by file extension

For the WebUI categories, it supports 'Model', 'Model hash', 'Size', 'Sampler' & 'CFG scale'.


----

Usage: sd-cat2000.py -<flag> [-v] <file(s) or folder(s)>

Where <flag> is ONE of the following"
-m Model
-h Model hash
-d Size
-a Sampler
-c CFG scale

Optionally add -v for verbose output to show details of each file being processed.

Without the -v, you will see a simple percentage progress only.

----

Example usage:

./sd-cat2000.py -m -v ImageDownloads/


This will execute the script, process all files in your ImageDownloads folder and break down the WebUI images based on the SD Model, e.g.:

ImageDownloads/ComfyUI/ComfyUI00001.png
ImageDownloads/ComfyUI/ComfyUI00002.png
ImageDownloads/No metadata/JPEG/00006.jpeg
ImageDownloads/No metadata/JPG/00007.jpg
ImageDownloads/No metadata/MP4/00008.mp4
ImageDownloads/No metadata/PNG/00009.png
ImageDownloads/No metadata/UNKNOWN/
ImageDownloads/No model found/00005.png
ImageDownloads/No model found/00005.png.txt
ImageDownloads/WebUI/cyberillustrious_v38/00001.png
ImageDownloads/WebUI/cyberillustrious_v38/00001.png.txt
ImageDownloads/WebUI/cyberillustrious_v38/00002.png
ImageDownloads/WebUI/cyberillustrious_v38/00002.png.txt
ImageDownloads/WebUI/waiNSFWIllustrious_v120/00003.png
ImageDownloads/WebUI/waiNSFWIllustrious_v120/00003.png.txt
ImageDownloads/WebUI/waiNSFWIllustrious_v120/00004.png
ImageDownloads/WebUI/waiNSFWIllustrious_v120/00004.png.txt


The content of "ImageDownloads/WebUI/cyberillustrious_v38/00001.png.txt" example:

Positive prompt: High Angle (from the side) view Close shot (focus on head).  muscular female,  body blush, pale skin, long hair, black hair,  sexy,  lace trim,  teasing, beckoning,  wonder woman \(cosplay\),  dreamy,  bokeh,  depth of field,  still life,  photo \(medium\),   masterpiece, best quality, newest, sensitive, absurdres, <lora:MuscleUp-Ilustrious Edition:0.75>.
Negative prompt: lowres, bad quality, worst quality, child, loli,  bad anatomy, deformity, extra fingers, signature, logo, username,  school,  bodybuilder,.
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
Template: Freeze Frame shot.  muscular female
<lora: MuscleUp-Ilustrious Edition:0.75>
Negative Template: lowres
Hires Module 1: Use same choices
Hires prompt: Freeze Frame shot.  muscular female
Hires CFG Scale: 5
Hires upscale: 2
Hires steps: 20
Hires upscaler: 4x-UltraMix_Balanced
Lora hashes: MuscleUp-Ilustrious Edition: 7437f7a09915
Version: f2.0.1v1.10.1-previous-661-g0b261213

-----

Caveats:

- This was "developed" from a Bash v3.2 script.  It has not been tested on other environments or optimised in any way


-----

Known Issues:

- Better handle sub-folders as input
- Ignore hidden files

-----


History:

1.0: Intial release
