import re


def detect_data_leaks(filepath, regexs):
    with open(filepath, "r", encoding="utf-8") as inputfile:
        input = "\n".join(inputfile.readlines())

    for regex in regexs:
        if re.match(regex, input) is not None:
            return regex

    return None
