import pandas as pd


def import_files():
    student_marks = pd.read_csv("Assignment2/dataset/student_marks.csv")
    # print(student_marks.to_string())

    student_status = pd.read_json("Assignment2/dataset/student_status.json")
    # print(student_status.to_string())

    student_bio = pd.read_excel(
        "Assignment2/dataset/student_bio.xlsx", sheet_name="Sheet1"
    )
    student_bio = student_bio.astype({"id": "int"})
    # print(student_bio.to_string())

    return student_marks, student_status, student_bio


def lineBreak():
    print("\n\n")


def main():
    student_marks, student_status, student_bio = import_files()

    student_data = student_bio.merge(student_marks, how="left", on="id")
    student_data = student_data.merge(student_status, how="left", on="id")

    # print(student_data.to_string())

    height_by_gender = student_data.groupby("Gender").aggregate(
        {"Height": ["min", "mean", "max"]}
    )
    print("Height Information based on Gender")
    print(height_by_gender)
    lineBreak()

    weight_by_gender = student_data.groupby("Gender").aggregate(
        {"Weight": ["min", "mean", "max"]}
    )
    print("Weight Information based on Gender")
    print(weight_by_gender)
    lineBreak()

    gender_count = student_data.groupby(["Gender"])["Gender"].count()
    print("People count based on Gender")
    print(gender_count)
    lineBreak()

    avg_marks_by_dept = student_data.groupby("Department")[
        ["Mark_10th", "Mark_12th", "Mark_college"]
    ].aggregate("mean")
    print("Mean Marks Information based on Department")
    print(avg_marks_by_dept)
    lineBreak()

    financial_status = student_data.groupby(["FinancialStatus"])[
        "FinancialStatus"
    ].count()
    print("People count based on Financial Status")
    print(financial_status)
    lineBreak()

    stress_level = student_data.groupby(["StressLevel", "StudyPreference"])[
        ["Gender"]
    ].count()
    print("People count based on Stress Level and Study Preference")
    print(stress_level)
    lineBreak()


if __name__ == "__main__":
    main()
