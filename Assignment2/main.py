import pandas as pd

# Function to import dataset files
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


# Function to add line breaks
def lineBreak():
    print("\n\n")


# Main Function
def main():
    # import files
    student_marks, student_status, student_bio = import_files()

    # Merge data from different dataset
    student_data = student_bio.merge(student_marks, how="left", on="id")
    student_data = student_data.merge(student_status, how="left", on="id")

    # Generate height information based on gender
    height_by_gender = student_data.groupby("Gender").aggregate(
        {"Height": ["min", "mean", "max"]}
    )
    print("Height Information based on Gender")
    print(height_by_gender)
    lineBreak()

    # Generate Weight Information based on Gender
    weight_by_gender = student_data.groupby("Gender").aggregate(
        {"Weight": ["min", "mean", "max"]}
    )
    print("Weight Information based on Gender")
    print(weight_by_gender)
    lineBreak()

    # Generate People count based on Gender
    gender_count = student_data.groupby(["Gender"])["Gender"].count()
    print("People count based on Gender")
    print(gender_count)
    lineBreak()

    # Generate Mean Marks Information based on Department
    avg_marks_by_dept = student_data.groupby("Department")[
        ["Mark_10th", "Mark_12th", "Mark_college"]
    ].aggregate("mean")
    print("Mean Marks Information based on Department")
    print(avg_marks_by_dept)
    lineBreak()

    # Generate People count based on Financial Status
    financial_status = student_data.groupby(["FinancialStatus"])[
        "FinancialStatus"
    ].count()
    print("People count based on Financial Status")
    print(financial_status)
    lineBreak()

    # Generate People count based on Stress Level and Study Preference
    stress_level = student_data.groupby(["StressLevel", "StudyPreference"])[
        ["Gender"]
    ].count()
    print("People count based on Stress Level and Study Preference")
    print(stress_level)
    lineBreak()


if __name__ == "__main__":
    main()
