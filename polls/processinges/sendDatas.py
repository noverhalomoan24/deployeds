from ..models import Images_all
import io,base64
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



def get_images(name_path):
    check_web = Images_all.objects.filter(web_name=name_path).exists()
    if(check_web):
        #return_image = Images_all.objects.get(web_name=name_path)
        returns = Images_all.objects.filter(web_name=name_path)

        for images_ in returns:
            images_path = str(BASE_DIR) + "\static\img\img_temp\\" + images_.name_images + '.jpg'
            decodedData = base64.b64decode(images_.json_images['img'])
            imgFile = open(images_path, 'wb')
            imgFile.write(decodedData)
            imgFile.close()




