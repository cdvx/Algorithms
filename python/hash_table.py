"""Python implementation of the HashTable data structure"""


class Item:

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTable:

    def __init__(self, size):
        self.hash_table = [[] for _ in range(size)]
        self.size = size
        self.hash_func = lambda key: hash(key) % len(self.hash_table)

    def __str__(self):
        return self.hash_table.__str__()


    def key_exists(self, bucket, key):
        k , v =0,0
        if bucket:
            for index, k_v in enumerate(bucket):
                k, v = k_v
                if k == key: break
            return (v, index) if k==key else False
        return False


    # hash table insert: Chaining -> Collision Resolution
    def insert(self, item):
        key, value = item.key, item.value
        hash_key = self.hash_func(key)

        # get bucket matching the hash key
        bucket = self.hash_table[hash_key]
        exists = self.key_exists(bucket, key)
        if exists:
            bucket[exists[1]] = ((key, value))
        else:
            bucket.extend([(key, value)])

    def search(self, item, del_=None):
        key = item.key
        hash_key = self.hash_func(key)
        # get bucket from hash key
        bucket = self.hash_table[hash_key]
        value = self.key_exists(bucket, key)
        if del_:
            add_key = lambda val, hash_key: list(value)+[hash_key] if val else None
            return add_key(value, hash_key)
        return value[0] if value else None

    def delete(self, item):
        key = item.key
        check = self.search(item, del_=True)
        if check:
            val, index, hash_k = check
            self.hash_table[hash_k].remove((key, val))
            print(f'Key {key} deleted! \nTable: {self.hash_table} \nHash_key:{hash_k}')
        else:
            print(f'Key {key} Not found! \nTable: {self.hash_table}')
        

if __name__ == '__main__':
    table = HashTable(10)
    nepal = Item(10, 'Nepal')
    usa = Item(25, 'USA')
    india = Item(20, 'India')
    table.insert(nepal)
    table.insert(usa)
    table.insert(india)
    print(table.search(usa))
    print(table.search(nepal))
    print(table.search(india))
    print('\n Before delete: del india',table, end='\n\n')
    table.delete(india)
    print('\n After delete:',table, end='\n\n')
