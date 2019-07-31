"""Python implementation of the HashTable data structure"""

hash_table = lambda length: [[] for _ in range(length)]

hash_func = lambda key, table: hash(key) % len(table)

def key_exists(bucket, key):
    k , v =0,0
    if bucket:
        for index, k_v in enumerate(bucket):
            k, v = k_v
            if k == key: break
        return (v, index) if k==key else False
    return False


# hash table insert: Chaining -> Collision Resolution
def insert(hash_table, key, value):
    hash_key = hash_func(key, hash_table)

    # get bucket maching the hash key
    bucket = hash_table[hash_key]
    exists = key_exists(bucket, key)
    if exists:
        bucket[exists[1]] = ((key, value))
    else:
        bucket.extend([(key, value)])

def search(hash_table,key, del_=None):
    hash_key = hash_func(key, hash_table)
     # get bucket from hash key
    bucket = hash_table[hash_key]
    value = key_exists(bucket, key)
    if del_:
        add_key = lambda val, hash_key: list(value)+[hash_key] if val else None
        return add_key(value, hash_key)
    return value[0] if value else None

def delete(hash_table, key):
    check = search(hash_table, key, del_=True)
    if check:
        val, index, hash_k = check
        hash_table[hash_k].remove((key, val))
        print(f'Key {key} deleted! \nTable: {hash_table} \nHash_key:{hash_k}')
    print(f'Key {key} Not found! \nTable: {hash_table}')
        




 

table = hash_table(10)
insert(table, 10, 'Nepal')
insert(table, 25, 'USA')
insert(table, 20, 'India')
print(search(table, 25))
print(search(table, 10))
print(search(table, 20))
print('\n Before delete:',table, end='\n\n')
delete(table, 20)
print('\n After delete:',table, end='\n\n')
