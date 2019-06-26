import locale
from datetime import datetime
import json


def read_file(path):
    try:
        with open(path, "r") as file_r:
            return json.load(file_r)
    except FileNotFoundError:
        print("Файл не найден")
        exit(1)


def add_test(name, error, dt):
    temp_test = {
        "name": name,
        "status": "successfully" if error == 0 else "fail",
    }
    for i, check_test in enumerate(check_tests["captures"]):
        if (dt == datetime.strptime(
                check_test["time"][:-6], "%Y-%m-%dT%H:%M:%S")):
            temp_test["expected"] = check_test["expected"]
            temp_test["actual"] = check_test["actual"]
            del check_tests["captures"][i]
            break
    else:
        temp_test["expected"] = "unknown"
        temp_test["actual"] = "unknown"

    tests["tests"].append(temp_test)


locale.setlocale(locale.LC_TIME, "en")

tests = {"tests": []}
logs1 = read_file("logs1.json")
logs2 = read_file("logs2.json")
check_tests = read_file("check_tests.json")

for log in logs1["logs"]:
    log_error = 0 if log["output"] == "fail" else 1
    log_dt = datetime.utcfromtimestamp(int(log["time"]))
    add_test(log["test"], log_error, log_dt)

for suite in logs2["suites"]:
    for log in suite["cases"]:
        log_error = log["errors"]
        log_dt = datetime.strptime(log["time"][:log["time"].find(" UTC")],
                                   "%A, %d-%b-%y %H:%M:%S")
        add_test(log["name"], log_error, log_dt)

with open("result.json", "w") as file_w:
    json.dump(tests, file_w, indent=4)
    print("Данные успешно записанны в файл.")
