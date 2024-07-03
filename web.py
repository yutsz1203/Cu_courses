import pandas as pd
import os
import json


def main():
    courses_dir = 'course'
    json_list = []
    for entry in os.listdir(courses_dir):
        full_path = os.path.join(courses_dir, entry)
        # print(entry)
        if os.path.isdir(full_path):
            csv_file_1 = os.path.join(full_path, f"{entry}.csv")
            csv_file_2 = os.path.join(full_path, f"{entry}_d.csv")
            # print(csv_file_1, csv_file_2)
            if os.path.isfile(csv_file_1) and os.path.isfile(csv_file_2):
                df1 = pd.read_csv(csv_file_1, header=None, dtype=str)
                df2 = pd.read_csv(csv_file_2, header=None, dtype=str)
                for index, row in df1.iterrows():
                    course_code = entry + row[0]
                    course_name = row[1]
                    course_des = df2.iloc[index, 0]
                    json_list.append({
                        "courseCode": course_code,
                        "courseName": course_name,
                        "courseDescription": course_des
                    })
    json_output = json.dumps(json_list, indent=4)
    with open('cuhk.json', 'w') as json_file:
        json_file.write(json_output)



if __name__=="__main__":
    main()
