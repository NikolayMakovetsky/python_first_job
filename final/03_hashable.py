print("\n---Python Hashable")

# What Is Hashable?
# Hashing is a process of converting some large amount of data to small amount
# in a repeatable way, so that it can be looked up in constant-time(O(1))

# An object is hashable if all of these requirements are met:
# ==========================================================
# 1. It supports the hash() function via a hash() method that always return
# the same value over the lifetime of the object.
# 2. It supports equality via an eq() method.
# 3. If a == b is True then hash(a) == hash(b) must also be True.

print("\n---Why Is List Not Hashable?")
# Lists are mutable and two lists can be equal if they have same items.

a = [1, 2]
b = [1, 2]
print(a == b)   # True


tt = (1, 2, (30, 40))
print(hash(tt))             # -3907003130834322577
tl = (1, 2, [30, 40])
# print(hash(tl))           # TypeError: unhashable type: 'list'

print("\n---dict")

# Python use a hash table to implement a dict.
# A hash table is a sparse array. In standard data structure texts,
# the cells in a hash table are often called “buckets.” In a dict hash table,
# the bucket for each item containing two fields: a reference to the key and
# a reference to the value of the item.
# The fetch the value at my_dict[search_key].
# Python calls hash(serach_key) to obtain the hash value of search_key and
# uses the least significant bits of that number as an offset to look up a bucket
# in the hash table.
# If the bucket is empty, KeyError is raised.
# Otherwise, the found buckets has an item – a found_key:found_value pair – and
# then Python check whether search_key == found_key.
# If they match, that was the item sought: found_value is returned.
# However, if serach_key and found_key do not match, this is a hash collision.
