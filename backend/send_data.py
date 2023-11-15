import json
from ufds_backend import UFDS

def process_data(input_data):
    with open('../data/data.json', 'r') as f:
        data = json.load(f)

    id_to_data = {item['id']: item for item in data}

    ufds = UFDS()

    for item in id_to_data.values():
        id = item['id']
        ufds.make_set(id)
        for attr in ['sex', 'city']:
            ufds.make_set(item[attr])
            ufds.union(id, item[attr])
        for interest in item['interests']:
            ufds.make_set(interest)
            ufds.union(id, interest)

    mapped_sets = ufds.map_attributes_to_sets(input_data.values(), id_to_data)
    matching_set = set.intersection(*mapped_sets) if mapped_sets else set()

    result_data = ufds.get_data_by_ids(matching_set, id_to_data)

    with open('../data/response.json', 'w') as f:
        json.dump(result_data, f, indent=2)

    print('Datos escritos en response.json')
