# Overlay Textures on Image

This function is a basic script that takes textures from the resource file and overlays them on the `output.png` file.

## Getting Started

Install python 3.6.5 or higher and pip3.6.5 or higher. Then run the following command to install the required packages.

```
pip3 install -r requirements.txt
```

`If you are using a different python version, you will need to install the required packages manually.`

## Running the file.

    Ensure that python is installed. Python 3.7.3 or higher is recommended.
    run the following command in the terminal:
        python3 textures_overlay.py` or python textures_overlay.py
        or bash -c "python3 textures_overlay.py"

The output will be saved in the same directory as the script as `output_overlay.png`
The script will take a few seconds to run. Please be patient, and do not close the terminal.
Recommend to put all the files in the same directory so that the script can find them easily.

When prompted, enter the following:

```

`textures.json` - (or path where this is located) This is json file where we have textures and their positions.

`output.png`    - This is original image that we want to overlay the textures on.

`./preprocessed_textures/ or /resources/assets/minecraft/textures/block`

```

## Resources

The resources are located in the `resources` folder. and some images may need to be pre-processed. For now the following images are used:
`preprocessed_textures/` which contains images without edge cases.

If the `preprocessed_textures` folder is not found, set the directory to the `resources/assets/minecraft/textures/block/` folder.
This can be takes by another script that is located in the `resources` folder.

## Textures JSON

This is a JSON file that contains the information about the textures. ensure that it located and all the names of the images to be used are correct and spelled correctly with the correct capitalization and positioning in the grid of the image.
