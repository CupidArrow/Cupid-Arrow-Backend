class UFDS:
    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.sets = {}

    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 0
        self.sets[x] = {x}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
            self.sets[y_root].update(self.sets[x_root])
            del self.sets[x_root]
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
            self.sets[x_root].update(self.sets[y_root])
            del self.sets[y_root]
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
            self.sets[x_root].update(self.sets[y_root])
            del self.sets[y_root]

    def get_set(self, attributes, id_to_data):
        sets = []
        for attr in attributes:
            for item in self.sets:
                if attr in id_to_data[item].get('sex', '') or \
                        attr in id_to_data[item].get('city', '') or \
                        attr in id_to_data[item].get('interests', []):
                    sets.append(self.sets[self.find(item)])
        return set.intersection(*sets) if sets else set()

    def map_attributes_to_sets(self, attributes, id_to_data):
        mapped_sets = []
        for attr in attributes:
            attr_set = set()
            for item in self.sets:
                item_data = id_to_data[item]
                if (
                    attr == item_data.get('sex') or
                    attr == item_data.get('city') or
                    attr in item_data.get('interests', [])
                ):
                    attr_set.update(self.sets[self.find(item)])
            mapped_sets.append(attr_set)
        return mapped_sets

    def get_data_by_ids(self, ids, id_to_data):
        result = []
        for item_id in ids:
            item_data = id_to_data.get(item_id)
            if item_data:
                result.append(item_data)
        return result
