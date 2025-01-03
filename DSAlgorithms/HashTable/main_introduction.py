'''
INTRODUCTION
Hash Table is a data structure which organizes data using hash functions in order
to support quick insertion and search.

Two different kinds of hash tables: hash set and hash map
  1) Hash Set - is one of the implementations of a set data structure to store no repeated values.
  2) Hash Map - is one of the implementations of a map data structure to store (key, value) pairs.


By choosing a proper hash function, the hash table can achieve wonderful performance in both insertion and search.

In this card, we will answer the following questions
  What is the principle of a hash table?
  How to design a hash table?
  How to use hash set to solve duplicates related problems?
  How to use hash map to aggregate information by key?
  How to design a proper key when using a hash table?
'''

'''
THE PRINCIPLE OF HASH TABLE
The key idea of Hash Table is to use a hash function to map 'keys to buckets'. More, specifically
  1) When we insert a new key, the hash function will decide which bucket the key 
  will be stored in the corresponding bucket.
  2) When we want to search for a key, the hash table will use the 'same' hash function
  to find the corresponding bucket and search only in tthe specific bucket

AN EXAMPLE
We use y = x % 5 as our hash functioon
  Keys        Hash Function       Buckets
  0    ==========================>  0
                                    1
  1987 =================
                       ||========>  2
  24   =========       ||
              ||       || 
  2    ==================           3
              ||
              ===================>  4

In the example, we use y = x % 5 as our hash function. Insertion and Search strategies using this example:
  1) Insertion: We parse the keys through the hash function to map them into the corresponding bucket.
      eg) 1987 is assigned to bucket 2 while 2 is assigned to bucket 4.
  
  2) Search: We parse the keys through the same hash function and search only in the specific bucket
      eg) if we search for 23, will map 23 to 3 and search in bucket 3. And we find out that 23
      is not in bucket 3 which means 23 is not in the hash table.
'''


'''
KEYS TO DESIGN A HASH TABLE
There are two essential factors to pay attention to when designing a hash table.

1. HASH FUNCTION
The hash function is the most important concept of a hash table which is used to make key to a specific bucket.
From the previous example, we use "y = x % 5" as a hash function, where is 'x' is the key value 
and 'y' is the index of the assigned bucket.

The hash function will depend onf the range of key values and the number of buckets.
Ideal hash function will be one-to-one mapping between the key and the bucket.
The idea is to try to assign the key to the bucket as uniformly as you can.
However, in most cases, a hash function is not perfect and it is a tradeoff between the amount of buckets and the capacity of a bucket.

2. COLLISION RESOLUTION
Ideally, if our hash function is a perfect one-one mapping, we will not need to handle collisions.
Unfortunately, in most cases, collisions are almost inevitable. For instance, in our previous hash function (y = x % 5),
both 1987 and 2 are assigned to bucket 2. That is a 'collision',

A collision resolution algorithn should solve ethe following questions:
  1. How to arganize the values in the same bucket?
  2. What if too many values are assigned to the same bucket?
  3. How to search for a target value in a specific bucket?




'''

