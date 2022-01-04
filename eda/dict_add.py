# Given three arguments ⁠— a dictionary obj, a key name and a value ⁠— 
# return a dictionary with that name and value in it (as key-value pairs).

def add_name(obj, key, val):
    obj[key] = val
    return obj

if __name__ == "__main__":
    new_dict = {"name": "Craig"}
    print(add_name(new_dict, "number", 22))