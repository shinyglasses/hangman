import json

with open('../resources/user_data.json', 'r') as file:
  data = json.load(file)
# the above code will screw stuff up if the file is empty

class Save_Files:
  pass

class Load_Files:
  pass
