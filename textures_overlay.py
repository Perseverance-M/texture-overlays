import os
from matplotlib.pyplot import imread;
from matplotlib.pyplot import imsave;
import json
import sys



""" 
    if __name__ == '__main__': run the file as a script python3 textures_overlay.py 
    Python3 is recommended to run the file as a script.
    # run the script on the command line.
"""


def overlay_textures_to_output_image(json_file_path, output_image_file_path, textures_path,patch_size = 64):
    """ 
      Takes the parameters: below and returns: an image with the textures overlaid on the output image.
      
      :param json_file json file that includes the positions of the textures in the output image
      :param outputImagePath: path of the output image
      :param path_images_to_overlay: path of the folder that contains the textures to overlay
      :param patch_size: size of the patches - must in either 16 | 32 | 64 | 128
      :return: an image with the textures overlaid on the output image. 
    """
   
    if patch_size % 16 != 0:
        # raise an error if the patch size is not a multiple of 16 
        raise FileExistsError('patch must comply with the multiple of 16, 32, 64, 128, 256, 512')
       
  
    if not os.path.exists(json_file_path):
        # check if the user has provided a valid json file
        raise FileExistsError('json file does not exist', json_file_path, 'please check the path')
  

    if not os.path.exists(output_image_file_path):
        # check if the user has provided a valid output image path
        raise FileExistsError('output image does not exist', output_image_file_path, 'please check the path')

   
    # open the texture json file.
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    # convert the texture json file to a dictionary
    out_read = imread(output_image_file_path)
    

    # check if the directory exists
    if not os.path.exists(textures_path):
       raise FileExistsError(textures_path + ' directory does not exist', 'please create the directory')
    for filename in os.listdir(textures_path):
        #check if the file is a png file
        if filename.endswith('.png'):
            # iterate over the textures in the json file and overlay them on the output image
            for i in range(0,len(data)):
                # for each texture in the json file
                fileData = data[i]
                # check the file if fileData['name'] == filename
                if filename in fileData['fileName']:
                    texture = imread(textures_path + '/' + filename)
                    # print in a new line the filename and the position of the texture
                    print(filename + ' ' + str(fileData['position']))
                   
                     # extract the postion of the texture in the output image
                    GRID_SIZE = 63
                    y = GRID_SIZE-fileData['position'][1]
                    x = fileData['position'][0]
                    # check the x,y if is not between 0 and 63
                    if x < 0 or x > patch_size-1 or y < 0 or y > patch_size-1:
                        # throw an error
                        raise ValueError('position of the texture is not in the output image', x, y)
                    else:
                        
                        x = x * patch_size 
                        y = y * patch_size
                        # replace the positions on the data with the new positions
                        fileData['position'][0] = x
                        fileData['position'][1] = y
                        
                        out_read[y:y + texture.shape[0], x:x + texture.shape[1]] = texture
                        imsave('output_overlay.png', out_read)
                        print('image',filename,'overlaid')

                else :
                    print('\n')
                    continue
        else:
            # throw an error
            # file is not a png file so we do not want to overlay it. 
            raise FileExistsError('file is not a png file', filename)
            
    return 'Overlaying textures on the output image complete!.' + ' textures overlayed : ' + str(len(data))
    


def main( ):
    # accept the paramters as sys.argv and run the function
    print('\n')
    # prompt the user to enter the path of the json file
    json_file_path = input('Enter the path of the json file: ')
    # prompt the user to enter the path of the output image
    output_image_file_path = input('Enter the path of the output image: ')
    # prompt the user to enter the path of the textures
    textures_path = input('Enter the path of the textures:(preprocesses_textures) ')   
    print(overlay_textures_to_output_image(json_file_path, output_image_file_path, textures_path))
      

if __name__ == '__main__':
    print('\n'), 'Overlay Textures on the output image'
    main()
