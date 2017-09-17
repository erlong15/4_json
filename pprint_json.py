import sys
import json


def load_data(filepath):
    with open(filepath, 'r') as json_file:
        json_obj = json.load(json_file)
        return json_obj


def pretty_print_json(json_for_print):
    print(json.dumps(json_for_print, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    json_object = load_data(sys.argv[1])
    pretty_print_json(json_object)
