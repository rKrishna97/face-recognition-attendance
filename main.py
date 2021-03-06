import cv2
import face_recognition 
from collect_images_from_file import collect_face_encode
from add_to_mongodb import insert_face_encode, check_if_student_is_present
from attendence import take_attendance
from add_to_mongodb import get_student_list
print("How you want to collect images:")
print("1. Collect faces from files")
print("2. Collect faces from webcam")
print('3. Take Attendance')
print(('4. Get students names'))
ch = int(input("Select option: "))

if ch == 1:
    print("Place the image files in ./Images/<Person Name>/<Image File>.jpg")
    face_encode_dict = collect_face_encode()

    _ = insert_face_encode(face_encode_dict=face_encode_dict)
    # user_presence = check_if_student_is_present(student_name='Elon_Musk') 
    
elif ch == 2:
    print("Opening Webcam") # IN PROGRESS

elif ch == 3:
    _ = take_attendance()

elif ch == 4:
    student_names = get_student_list()
    for i,name in enumerate(student_names):
        print(f"{i}. {name}")


