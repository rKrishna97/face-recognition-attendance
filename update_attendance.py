from datetime import datetime
from add_to_mongodb import get_student_list
import pandas as pd
import os


def update_attendance(person_name):
    today = datetime.today().strftime("%d-%m-%Y")

    students = sorted(get_student_list())

    filename = "Attendance.csv"
    # header = ["Name", today]

    entry_dict = {}
    for i in students:
        if i == person_name:
            entry_dict[i] = 1
        else:
            entry_dict[i] = 0

    print(entry_dict)

    if not os.path.exists(filename):
        entry = []
        name = []
        for key, value in entry_dict.items():
            name.append(key)
            entry.append(value)
        csv_file = pd.DataFrame({"Name": name, today: entry})
        csv_file.to_csv(filename, sep=",", index=False)
    else:
        entry = []
        name = []
        for key, value in entry_dict.items():
            name.append(key)
            entry.append(value)
        df = pd.read_csv("Attendance.csv")

        new_names = []
        for i in students:
            if i not in list(df["Name"]):
                new_names.append(i)

        if len(new_names) != 0:
            for i in new_names:
                df.loc[len(df)] = 0
                df["Name"].iloc[-1] = i

        print(df)

        if today not in df.columns:
            df[today] = 0
            df.loc[df["Name"] == person_name, today] = 1
            print()
            print(df)
        elif today in df.columns:
            df.loc[df["Name"] == person_name, today] = 1

        df.to_csv(filename, index=False)

    return True
