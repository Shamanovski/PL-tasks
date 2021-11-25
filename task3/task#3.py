import sys
import json


def main():
    path1, path2 = sys.argv[1], sys.argv[2]

    with open(path1, "r") as file1, \
         open(path2, "r") as file2:
        tests = json.load(file1)["tests"]
        values = json.load(file2)["values"]
    # map id to value
    values = {value["id"]: value["value"] for value in values}
    iterate_recursivly(tests, values)
    with open("report.json", "w") as f:
        json.dump(tests, f)


def iterate_recursivly(parent, values):
    for child in parent:
        if child.get("value", None) is not None:
            child_id = child["id"]
            child["value"] = values[child_id]
        nested_values = child.get("values", None)
        if nested_values is not None:
            iterate_recursivly(nested_values, values)


main()
