from pathlib import Path
import requests



def get_url():
    return input("Enter image URL: ")
def get_file_name():
    image_name=input("Image name: ")
    if not image_name.endswith(".jpg"):
        image_name=image_name +".jpg"
    return image_name
def download_image(url,file_name,downloads_folder):
    image=requests.get(url)
    if image.status_code == 200:
        image_path=downloads_folder / file_name
        if image_path.exists():
            print("A file with that name already exists.")
        else:
            with open( downloads_folder / file_name, "wb") as file:
                file.write(image.content)  #conatains image bytes
            print("Image downloaded successfully")
    else:
            print(f"Download failed. Status code: {image.status_code}")


def main():

    downloads_folder=Path("downloads")
    downloads_folder.mkdir(exist_ok=True)# if folder is missing creates it 
    url=get_url()
    image_name=get_file_name()
    download_image(url,image_name,downloads_folder)

main()
