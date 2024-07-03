import pandas as pd
import os


def main():
    courses_dir = 'courses'
    for entry in os.listdir(courses_dir):
        full_path = os.path.join(courses_dir, entry)
        print(entry)
        if os.path.isdir(full_path):
            print(f"Subdirectory: {entry}")
            csv_file_1 = os.path.join(full_path, f"{entry}.csv")
            csv_file_2 = os.path.join(full_path, f"{entry}_d.csv")
            print(csv_file_1, csv_file_2)


if __name__=="__main__":
    main()
