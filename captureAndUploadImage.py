from os import access
import time
import cv2
import random
import dropbox

start_time=time.time()

def takeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("Snapshot Taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token=""
    file=img_name
    file_from=file
    file_to="/testfolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name=takeSnapshot()
            upload_file(name)
main()
       
