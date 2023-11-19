import json

def readJsonFile(fileName):
    data=""
    try:
        with open('/home/ec2-user/environment/pythonAWS/week3/calc_json.py') as json_file:
            data = json.load(json_file)
    except IOError:
        print("Could not read file")
    return 

