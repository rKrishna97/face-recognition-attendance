import pymongo
import face_recognition

default_connection_url = "mongodb://localhost:27017/"
client = pymongo.MongoClient(default_connection_url)
db = client["Student"]
collection = db["face_encode"]


def insert_face_encode(face_encode_dict):
    for key in face_encode_dict.keys():
        encodings = []
        for i in range(0, len(face_encode_dict[key])):
            print(key)
            encode = face_encode_dict[key][i].tolist()
            encodings.append(encode)
            print()

        _ = collection.insert_one({"name": key, "encode": encodings})
        print("insert complete")
        print(db.list_collection_names())
    client.close()
    print("Client Closed")


def get_student_list():
    cursor = collection.find({})
    name_list = []
    for document in cursor:
        name_list.append(document["name"])
    cursor.close()
    return name_list


def does_person_exist(encodeFace):
    cursor = collection.find({}, {"_id": 0})
    face_encode_list = []
    for document in cursor:
        face_encode_list.append(document)
    cursor.close()
    face_exist = []
    for i in face_encode_list:
        name, encode = i.items()
        name = name[1]
        face_encode = encode[1]
        result = []
        face_match_check = face_recognition.compare_faces(face_encode, encodeFace)
        face_exist.append(max(face_match_check))
        if max(face_match_check):
            person_name = name

    return max(face_exist), person_name


def check_if_student_is_present(student_name):
    cursor = collection.find({})
    name_list = []
    for document in cursor:
        name_list.append(document["name"])
    cursor.close()
    return student_name in name_list
