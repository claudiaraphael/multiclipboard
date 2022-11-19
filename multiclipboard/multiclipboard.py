import sys
import clipboard
import json


SAVED_DATA = "clipboard.json"
# variable that stores the json file^

# function that creates a json file:
# filepath is how you will save the data


def save_data(filepath, data):
    with open(filepath, "w") as f:  # this means your creating a new file as the variable f (or overriding an existing one with the same name)
        # you dump the data in the variable f, which means you dump the data in the file
        json.dump(data, f)

# function that loads the json file:


def load_data(filepath):
    try:
        # opens the file in "r" mode which stands for read mode. opens the file in the variable f
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}  # como da primeira vez q vc roda o programa a json file n existe, vc cria o except e ele cria um dicionario vazio pra lidar com o erro de "file does not exist".


if len(sys.argv) == 2:  # condição para q haja somente 1 argumento na linha de comando
    command = sys.argv[1]
    data = load_data(SAVED_DATA)  # here you load the json file

    if command == 'save':
        key = input("Enter a key:")
        # a json file recebe a key como se fosse um dicionario python:
        data[key] = clipboard.paste()
        # rewrites the file with the key, saving the data.
        save_data(SAVED_DATA, data)
        print("Data saved.")

    elif command == 'load':
        key = input("Enter key:")
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard.')
        else:
            print("Key does not exist")
    elif command == 'list':
        print(data)
    else:
        print("Unknown command")
else:
    print('Please pass exactly one command.')
