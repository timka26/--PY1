import json
INPUT_FILE = "input.csv"
def csv_to_list_dict(filename, delimiter=',', next_str='\n') -> list[dict]:
    with open(filename, 'r') as f:
        first_str = f.readline().strip(next_str).split(delimiter)
        json_array = [dict(zip(first_str, row.strip(next_str).split(delimiter))) for row in f]
    return json.dumps(json_array,indent=4)
print(csv_to_list_dict(INPUT_FILE))
