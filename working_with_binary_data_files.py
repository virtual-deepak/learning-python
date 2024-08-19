import pickle

class Person:
    age = 45
    name = 'John Doe'
    kids = ['Pete', 'Lilly', 'Kate']
    employers = {'AWS': 2022, 'Microsoft': 2018, 'Yahoo': 2005}
    shoe_sizes = (11, 12)

def serialize_obj_inmem(obj):
    binary_data = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"Serialized: {binary_data}")
    return binary_data

def deserialize_obj_inmem(binary_data):
    obj = pickle.loads(binary_data)
    print(f"Deserialized: {obj}") 
    # You can also directly print attribute like: print(f"Deserialized: {obj.employers}") 

def read_binary(file_name):
    with open(file_name, 'rb') as file:
        binary_data = pickle.load(file)
        print(binary_data)

def write_binary(file_name, obj):
    with open(file_name, 'wb') as file:
        pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)

obj = Person()
#write_binary('./samples/files/my_binary_data.xyz', obj)
#read_binary('./samples/files/my_binary_data.xyz')
binary_data = serialize_obj_inmem(Person())
deserialize_obj_inmem(binary_data)