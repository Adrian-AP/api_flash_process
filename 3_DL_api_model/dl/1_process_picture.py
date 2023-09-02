import pickle
from tensorflow.keras.models import load_model
import gdown
import logging
from PIL import Image
import matplotlib.pyplot as plt


def calling_drive_files(file_id = str, file_name = str):
    
    """ Fucntion to read files from a drive url link

    Args:
        file_id (_type_, optional): Drive id for specific file.
        file_name (_type_, optional): Name of file to be read.
    """
    
    full_url = "https://drive.google.com/uc?id=" + file_id
    
    try:
        
        logging.warning("Process initialization...")
        outputx = gdown.download(full_url, file_name, quiet=False)
        logging.info
        
        return outputx
    
    except:
        logging.error("It could not be executed.")


def save_picture(drive_file = str, route_to_save = str ,pltx =False):
    
    """ Function to save a picture.
    
     Args:
        drive_file (_type_, optional): object from drive.
        route_to_save (_type_, optional): Route where it is going to be saved.
        pltx = It is a flag in case of True image will be ploted.
    """
    

    foto = Image.open(drive_file)
    
    where_it = route_to_save + "picp.png"
    foto.save(where_it)
    logging.warning(f'Picture saved in {route_to_save}')
    
    if pltx == True:
        plt.imshow(foto)
        plt.axis('off')  # Desactivar ejes
        plt.show()

if __name__ == "__main__":
    
    print("Hello")
    
    id_model = "1aw9tlW1RwLyczca11-ebxERJk8Jnp8NQ"
    name_file = "model.pkl"
    
    id_pict = "1k9eHI-1qAVh08IWrrQ78zMDB73b-V8oi"
    name_pic = "late-blight.jpg"
    
    #model = calling_drive_files(file_id= id_model, file_name= name_file)
    pic = calling_drive_files(file_id= id_pict, file_name= name_pic)

    save_picture(drive_file = pic, route_to_save = 'api_flash_process/3_DL_api_model/dl/static/', pltx = True)


