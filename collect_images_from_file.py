import face_recognition
import cv2
import os
import shutil
from add_to_mongodb import get_student_list

student_list = get_student_list()

def collect_face_encode():
    # Getting names of the person
    image_path = "./Images/"
    all_names = [i for i in os.listdir(image_path) if os.path.isdir(os.path.join(image_path, i)) ]
    # print(names)


    names = [i for i in all_names if i not in student_list]


    person_dict = {}
    for i in names:
        lis = []
        for root,dirs,files in os.walk(f"./Images/{i}/", topdown=False):
            for name in files:
                lis.append(os.path.join(root, name))
        person_dict[i] = lis

    # for i in person_dict.keys():
    #     print(person_dict[i][1])

    # for i in names:
    #     for f in person_dict[i]:
    #         print(f)
    #     print()



    person_dict_encode = {}
    for name in names:
        lisEncode = []
        for f in person_dict[name]:
            

            try:
                print(f)
                img = face_recognition.load_image_file(f)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                # img = cv2.resize(img, (600,400))
                faceLoc = face_recognition.face_locations(img)[0]
                faceEncode = face_recognition.face_encodings(img)[0]

                lisEncode.append(faceEncode)
                print(os.path.basename(f))
                print(faceLoc)
                # cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,255), 2)

                # cv2.imshow(f"{name} {img.shape[:2]}", img)
                # cv2.waitKey(0)
                # cv2.destroyAllWindows()
                
            except:
                print('Fail to detect face. Moving file to junk Folder')
                junk_file = os.path.basename(f)
                print(f"{junk_file}")

                if not os.path.exists(f"./Junk/{name}"):
                    os.makedirs(f"./Junk/{name}")
                shutil.move(f"./Images/{name}/{junk_file}", f"./Junk/{name}/{junk_file}")
                print()
                
                pass

        person_dict_encode[name] = lisEncode
        
    return person_dict_encode

            



