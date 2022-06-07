from Assignment1.main import saveToCSV


def new_test_file_write():
    filename = "info_test.csv"
    fieldnames = ["name", "dob", "age", "hobbies"]
    is_new = True

    data = {"name": "yunip", "dob": "1999/01/31", "age": 24, "hobbies": "asdasdasdasd"}

    assert saveToCSV(filename, fieldnames, data, is_new)


def test_file_update():
    filename = "info_test.csv"
    fieldnames = ["name", "dob", "age", "hobbies"]
    is_new = False

    data = {"name": "yunip", "dob": "1999/01/31", "age": 24, "hobbies": "asdasdasdasd"}

    assert saveToCSV(filename, fieldnames, data, is_new)
