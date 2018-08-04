#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


def main():

    # import the sys
    import sys

    # check if the stdin comes from a pipe
    if sys.stdin.isatty():
        print("The JSON must be inputted through stdin")
        sys.exit()

    # create the string that will store the full stdin
    data_inserted = str()

    # append the stdin to the variable
    for line in sys.stdin:
        data_inserted += line

    # try to parse the json
    try:
        parsed_json = json.loads(data_inserted)
    except Exception:
        raise ValueError("Could not parse the JSON from stdin")

    # reprint the json formatted
    print(json.dumps(parsed_json, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
