import os 
import cv2
import face_recognition
from add_to_mongodb import does_person_exist
from update_attendance import update_attendance


# image_path = './attendence_images/'
# img_files = [os.path.join(root,file_name) for root,dirs,files in os.walk(image_path, topdown=False) for file_name in files]
def take_attendance():
    camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)


    while(True):
        ret, img = camera.read()
        image = cv2.flip(img,1)
        img = cv2.flip(img,1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        try:
            encodeFace = face_recognition.face_encodings(img)[0]
            faceLoc = face_recognition.face_locations(img)[0]
            cv2.rectangle(image, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,255), 2)
            
            dpe, person_name = does_person_exist(encodeFace)
            print("dpe: ",dpe)
            if dpe == True:
                
                print(person_name)
                attend_true = update_attendance(person_name)

                if attend_true == True:
                    person_name = person_name.replace("_"," ")
                    cv2.putText(image, f'{person_name}: Attendance Taken', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,255), 2)





        except:
            print('Get in the frame')
            print("Or")
            print("Person not in DataBase")
            print()





        cv2.imshow('Frame',image)

        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break 

    camera.release()
    cv2.destroyAllWindows()
