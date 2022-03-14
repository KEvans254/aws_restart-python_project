import json
def dict_to_json():
    initial_clients = {
        0: {
            "username": "trial",
            "pin": 0000,
            "balance": {"KSh": 140, "USD": 0}
        },
        1: {
            "username": "evans",
            "pin": 1111,
            "balance": {"KSh": 1500, "USD": 10}
        }
    }

    f = open("clients.json", "w")
    json.dump(initial_clients, f)
    f.close()

def json_to_dict():
    with open('clients.json') as json_file:
        clients = json.load(json_file)
    print(clients["1"])
json_to_dict()