import numpy as np
import pandas as pd
import json
json_file_path = "neighbor-districts-modified.json"
with open(json_file_path, 'r') as j:
     contents = json.loads(j.read())
new_string = json.dumps(contents, indent=2, sort_keys=True)
print(new_string)
