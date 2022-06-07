from datetime import datetime
from fileinput import close
from os.path import exists
from user_exceptions import NullValueError, NumValueError, AlphaValueError
import csv


def input_name():
    while True:
        name = input("Name: ")
        try:
            if not name:
                raise NullValueError
            else:
                return name
        except NullValueError:
            print("Name can't be empty.")
        except:
            print("Please enter name.")


def input_age():
    while True:
        age = input("Age: ")
        try:
            if not age:
                raise NullValueError
            if age.isalpha():
                raise ValueError
            age = int(age)
            return age

        except NullValueError:
            print("Age can't be empty.")
        except ValueError:
            print("Age can contain only numbers.")
        except:
            print("Age can contain only numbers.")


def input_date():
    while True:
        date = input("Date: ")
        try:
            if not date:
                raise NullValueError
            if date.isalpha():
                raise AlphaValueError
            date = datetime.strptime(date, "%Y/%m/%d")
            return datetime.strftime(date, "%Y/%m/%d")

        except NullValueError:
            print("Date can't be empty.")
        except AlphaValueError:
            print("Date must not contain alphabets.")
        except:
            print("Date must be in format YYYY/MM/DD.")


def input_hobbies():
    while True:
        hobbies = input("Hobbies: ")
        try:
            if not hobbies:
                raise NullValueError
            else:
                return hobbies
        except NullValueError:
            print("Hobbies can't be empty.")
        except:
            print("Please enter hobbies.")


def input_form_data():
    data = {}
    data["name"] = input_name()
    data["dob"] = input_date()
    data["age"] = input_age()
    data["hobbies"] = input_hobbies()
    return data


def saveToCSV(filename, fieldnames, data, is_new):
    if is_new:
        filemode = "w"
    else:
        filemode = "a+"
    with open(filename, mode=filemode) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if is_new:
            writer.writeheader()
        writer.writerow(data)
        print("Record added to ", filename)
        csv_file.close()

        return True


def main():
    data = input_form_data()
    fieldnames = ["name", "dob", "age", "hobbies"]
    filename = "info.csv"
    is_new = not exists(filename)
    saveToCSV(filename, fieldnames, data, is_new)


if __name__ == "__main__":
    main()
