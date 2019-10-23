** Notes are directly taken from https://visualgo.net/en/hashtable

A table ADT must support at least the following operations:
  - Search(v) -- to determine if v exists in the ADT or not
  - Insert(v) -- insert v into the ADT
  - Remove(v) -- remove v from the ADT

** Direct Addressing Table (DAT)

When the range of Integer keys is small [0..M-1], we can use initially empty (Boolean) array A of size M and implement the following Table ADT operations directly:

  - Search(v) -- Check if A[v] is truthy or falsey
  - Insert(v) -- Set A[v] to be truthy
  - Remove(v) -- Set A[v] to be falsey

Note: When using small integer key to determine the addresses in the array, hence the name direct addressing, these operations are O(1)

* DAT Limitations

  - The keys must be non-negative integers.
  - The key range must be small, otherwise the memory usage with be large.
  - The keys must be dense and not have very many gaps, otherwise there will be too many empty cells.

We can overcome these limitations using hashing.

** Hashing

Hashing allows us to:

  - Map some non-integer keys to integer keys
  - Map large integers to smaller integers
  - Influence the density, or load factor α = N/M, of the Hash Table where N is the number of keys and M is the size of the Hash Table.


* Example:

We have N = 400 phone numbers, each with 8 digits, meaning we have a total of 10^8 = 100M possible phone numbers.
Instead of using a DAT and use a large array up to size M = 100 million we can use a hash function instead. h(v) = v%997.

This allows us to map these 8 digit integers into 3 digit integers.

  - h(6675 2378) = 66752378 % 997 = 237
  - h(6874 4483) = 68744483 % 997 = 336

This means that instead of prepating for M, array size, of 100 million we can prepare for M of 997 (or 1000).

* Hash Table with Satellite Data

If we have keys that map to satellite data and we want to record the original keys too, we can implement the Hash Table using pair of (Integer, satellite-data-type) array:

  - Search(v) -- Return A[hashfunction(v)], which is a pair of (v, satellite-data), possibly empty
  - Insert(v, sattellite-data) -- Set A[hashfunction(v)] = pair(v, satellite-data)
  - Remove(v) -- Set A[hashfunction(v)] = (empty pair)

* Collisions

In the earlier Hash Function, h(v) = v % 997, there were likely instances of collisions for two different values, v. 

  - h(6675 2378) = 66752378 % 997 = 237
  - h(6675 4372) = 66754372 % 997 = 237

This is a highly likely scenario. 
The Birthday Paradox is a real life example of this scenario which asks: "How many people (number of keys) must be in a room (Hash Table) of size 365 seats (cells) before the probability that some person share a birthday (collision, two keys are hashed to the same cell), ignoring the leap years, becomes greater than 50 percent (more likely than not)?"

Here is the calculation:

  Let Q(n) be the probability of unique birthday for n people in a room.
  Q(n) = 365/365 * 364/365 * 363/365 * . . . * (365 - n+1)/365
  Let P(n) be the probability of same birthday (collision) for n people in a room.
  P(n) = 1-Q(n)

  We compute that P(23) = 0.507 > 0.5 (50%)

We only need 23 people (keys) in the room (Hash Table) of size 365 seats (cells) for a probability of > .5 for two people to share the same birthday.

** Hash Functions

* Traits of a good Hash Function

  - Fast to compute, O(1)
  - Uses as minimum slots/Hash Table size M as possible
  - Scatter the keys into different base addresses as uniformly as possible, ∈ [0 . . M-1]
  - Experience as minimum collisions as possible

A hash value/hash code of key v is computed form then key v with the use of a hash function to get an Integer in the range 0 to M-1. This hash value is used as the base/home index/address of the Hash Table entry for the satellite-data.

* Perfect Hash Functions

A perfect Hash Function has a one-to-one mapping between keys and hash values, no collisions at all. This is easier if all of the keys are known beforehand, but that is very rare.
A minimal perfect hash function is achieved when the table size is the same as the number of keywords supplied. This case is even rarer.

See GNU gperf.

One of the most popular mapping hashing functions is: h(v) = v%M, i.e. map the key v, into Hash Table of size M slots. 

The Hash Table size M is set  to be a reasonable large prime Integer not near the power of 2, about 2+ times larger than the expected number of keys, N, that will ever be used in the Hash Table. 

* Collision Resolution

There are two major ideas for collision resolution: Open Addressing and Closed Addressing

In Open Addressing, all hashed keys are located in a single array. The hash code of a key gives its base address. Collision is resolved by cehcking/probing multiple alternative addresses (hense the name open) in the table based on a certain rule.

In Closed Addressing, the Hash Table looks like an Adjacentcy List (a graph data structure). The hash code of the key gives its fixed/closed base address. Collision is resolved by appending the collided keys in a Doubly Linked List identified by the base address.

** Open Addressing

Three Open Addressing collision resolution techniques:

Linear Probing (LP), Quadratic Probing (QP), Double Hashing (DH)

M = HashTable.length = The current Hash Table size
base = (key % HashTable.length)
step = The current probing step
secondary = smaller_prime - key % smaller_prime (to avoid zero)

Probing sequences:

  - Linear Probing -- i = (base+base * 1) % M
  - Quadratic Probing -- i = (base + step * step) % M
  - Double Hashing -- i = (base + step * secondary) % M

** Linear Probing

In Linear Probing collision resolution technique, we scan forwards one index at a time for the next empty/deleted slot (wrapping around when we have reached the last slot) whenever there is a collision.

As an example, let's assume we start with an empty Hash Table HT with table size M = HT.length = 7 (prime). The (primary) Hash Function is simple, h(v) = v % M

If we have a Hash Table M = 7:

i:0() i:1() i:2() i:3() i:4() i:5() i:6()

* Insert

For an Insert([18, 14, 21]) the calculation will look something like this:

First:
h(18) = 18 % 7 = 4  

so we insert 18 at i:4()

i:0() i:1() i:2() i:3() i:4(18) i:5() i:6()

Second:
h(14) = 14 % 7 = 0

so we insert 14 at i:0()

i:0(14) i:1() i:2() i:3() i:4(18) i:5() i:6()

Third:
h(21) = 21 % 7 = 0  

i:0(14) is occupied by 14 so we cannot put 21 there. 
Since we are using Linear Probing as our collision resolution technique, we look for the next empty slot. 
i:1() is empty so we put 21 there.

i:0(14) i:1(21) i:2() i:3() i:4(18) i:5() i:6()

Now  if we wanted to Insert([1, 35]):

First:
h(1) = 1 % 7 = 1

i:0(14) i:1(21) i:2(1) i:3() i:4(18) i:5() i:6()

Second:

h(35) = 35 % 7 = 0

i:0(14) i:1(21) i:2(1) i:3(35) i:4(18) i:5() i:6()


* Search

Psuedo code for search:

```
step = 0
i = base = key % HT.length
while True:
   if (HT[i] == EMPTY) return "Not Found"
   else if (HT[i] == key) return "found at index {i}"
   else step++; i = (base+step*1) % HT.length
```

Assuming we are using the Hash Table from above:

i:0(14) i:1(21) i:2(1) i:3(35) i:4(18) i:5() i:6()

If we wanted to Search(35):

step = 0
i = base = 35 % 7 # this is 0
here we check iteratively from i:0 until we either: 

  - Hit an empty node
  - Run out of nodes to check
  - Find the value

We start where we would normally insert, 35 % 7 = 0 so we check i:0 first:

i:0(14) != 35
so now we increment:

step ++; i = (base+step * 1) % HT.length = (0 + 1 * 1) % 7 # this is 1

i:1(21) != 35


step ++; i = (base+step * 1) % HT.length = (0 + 2 * 1) % 7 # this is 2

i:2(1) != 35


step ++; i = (base+step * 1) % HT.length = (0 + 3 * 1) % 7 # this is 3

i:2(35) == 35

return step # found at index 3

* Remove

Psuedo code for remove:

```
step = 0l i = base = key % HT.length;
while (true)
    if (HT[i] == EMPTY) break
    else if  (HT[i] == key)
        HT[i] = DELETED # where DELETED is some symbol that does not mean that the index is empty
    else step++; i = (base+step*1) % HT.length
```

We need to set the value to be deleted to some symbol that does not mean the same as the node is empty. This is because of the way Search(v) is implemented.

Later on, if we need to Insert(v) where v % HT.length we should replace the DELETE symbol with the value, v, we want to insert. This allows us to resue this space without affecting the correctness of the future search.

* Clustering

Although we can resolve collisions with Linear Probing, it is not the most effective way.

A cluster is a collection of consecutive occupied slots. A cluster that covers the base address of a key is called the primary cluster of a key.

Linear Probing can create large primary clusters that will increase the running time of Search(v)/Insert(v)/Remove(v) operations beyond O(1)

* Probing Sequence

The probe sequence of Linear Probing can be described as follows:

```
h(v)  # base address
(h(v) + 1*1)  # First probing step if there is a collision
(h(v) + 2*1)  # Second probing step if there is a collision
(h(v) + 3*1)  # Third probing step if there is a collision
. . .
(h(v) + k*1)  # K-th probing step if there is a collision
```

** Quadratic Probing

To reduce primary clustering, we can modify the probe sequence to:

```
h(v)  # base address
(h(v) + 1 * 1)  # first step if there is a collision
(h(v) + 2 * 2)  # second step if there is a collision
(h(v) + 3 * 3)  # third step if there is a collision
. . .
(h(v) + k * k)  # kth step if there is a collision
```

* Insert(v)

Insert(v) = v % M + (n * n)

As an example, if we wanted to insert into an empty Hash Table of size M = 7:

i:0() i:1() i:2() i:3() i:4() i:5() i:6()

Insert(10) = 10 % 7 + (0 * 0) = 3

i:0() i:1() i:2() i:3(10) i:4() i:5() i:6()

Insert(18) = 18 % 7 + (0 * 0) = 4

i:0() i:1() i:2() i:3(10) i:4(18) i:5() i:6()

Insert(38) = 38 % 7 + (0 * 0) = 3

Three is taken so now we take a step

Insert(38) = 38 % 7 + (1 * 1)  = 4

Four is takenm so now we take a step

Insert(38) = 38 % 7 + (2 * 2) = 7

Seven is out of bounds in our Hash Table, so we use the modulo operator to find it's index:

7 % M = 7 % 7 = 0

Zero is not taken so we put 38 in that index

i:0(38) i:1() i:2() i:3(10) i:4(18) i:5() i:6()


* Remove(v)

Remove(v) = h(v) = v % M + (n * n) if h(v) if h(v).value == v

This is very similar to insert due to the hashing algorithm.

Given:

i:0(38) i:1() i:2() i:3(10) i:4(18) i:5() i:6()

We can try to do a remove: 

Remove(38) = h(38) = 38 % 7 + (0 * 0) = 3

i:3 contains 10

10 != 38 so now we step

Remove(38)  h(38) = h(38) = 38 % 7 + (1 *  1) = 4

i:4 contains 18

18 != 38 so we step

Remove(38) = h(38) = 38 % 7 + (2 * 2) = 7

7 > M - 1 ==  7 > 6  

So we need to use modulo to find it's index 

7 % M == 7 % 7 == 0

i:0 contains 38

38 == 38 so we replace it with our DEL symbol

* Search(v)

Search uses the same logic as Remove

Given:

i:0(38) i:1() i:2() i:3(10) i:4(18) i:5() i:6()

We can do a search:

Search(10) = h(10) = 10 % 7 = 3

i:3 contains 10

10 == 10 so we return index 3

* Notes about Quadratic Probing

One major issue is that we could end up in a situation where we will cycle through the same modulo forever.

Given the Hash Table:

i:0(38) i:1() i:2() i:3(10) i:4(18) i:5() i:6()

If we try to Insert(12)

Insert(12) = h(12) = 12 % 7 + (0 * 0) = 5

i:5 is not taken so we put 12 there.

i:0(38) i:1() i:2() i:3(10) i:4(18) i:5(12) i:6()

Our new Hash Table looks like this:

i:0(38) i:1() i:2() i:3(10) i:4(18) i:5(12) i:6()

Now if we try to Insert(17)

Insert(17) = h(17) = 17 % 7 + (0 * 0) = 3
Then
Insert(17) = h(17) = 17 % 7 + (1 * 1) = 4
Then
Insert(17) = h(17) = 17 % 7 + (2 * 2) = 0
Then
Insert(17) = h(17) = 17 % 7 + (3 * 3) = 5
Then
Insert(17) = h(17) = 17 % 7 + (4 * 4) = 5
Then
Insert(17) = h(17) = 17 % 7 + (5 * 5) = 0
Then
Insert(17) = h(17) = 17 % 7 + (6 * 6) = 4
Then
Insert(17) = h(17) = 17 % 7 + (7 * 7) = 3
This will continue forever even though we have three empty cells left

How do we overcome this?

If α < 0.5 and M is a prime > 3, where α is the load factor and M is the Hash Table size (HT.length)

If these two conditions are met, we can prove that the first M/2 Quadratic Probing indices. including the base address h(v) are all distinct and unique

If we do not enforce this, we should break the loop after n number of steps to prevent an infinate loop.

In Quadratic Probing, clusters are formed along the path of probing, instead of around the base address like in linear Probing. These clusters are called Secondary Clusters.

Secondary clusters are caused by probing using the same patterns for all keys. If two distinct keys have the same base address, their Quadratic Probing sequences are going to be the same.

Secondary clustering in Quadratic Probing is not as bad as primary clustering in Linear Probing as a good hash function should disperse the keys into different base addresses, ∈ [0..M-1].

** Double Hashing

In double hashing we modify the probe sequence, in order to reduce the primary and secondary clustering, to be:

```
h(v)  # base address
(h(v) + (1 * h2(v))) % M # First probing step if there is a collision
(h(v) + (2 * h2(v))) % M # Second probing step if there is a collision
(h(v) + (3 * h2(v))) % M # Third probing step if there is a collision
. . .
(h(v) + (k * h2(v))) % M # K-th probing step if there is a collision
```

So the probe jumps according to the value of the second hash function, h2(v), that wraps around the Hash Table as necessary.

Note: h2(v) cannot be 0 or else we will keep getting the same index, if h2(v) = 1 it's bacially linear probing.

h(v) = v % M
h2(v) = (M' - (v % M')) where M' is a prime < M 

As an example:

If we had a table of size, M,  7
M' would be 5, a smaller prime
and we wanted to hash 35:

h(35) = 35 % 7 = 0
h2(35) = 5 - (35 % 5) = 5 (cannot be 0 so we return M' which is 5) = 5

(h(35) + h2(35)) % M = (0 + 5) % 7 = 5

If we wanted to hash 42 (which has the same base address as 35) we will see a different address:

h(42) = 42 % 7 = 0
h2(42) = 5 - (42 % 5) = 3

(h(42) + h2(42)) % M = (0 + 3) % 7 = 3 

In order for this to work, h2(v) needs to yeild some Integer, n, where 0 < n < M

This normally makes the return value diverse enough to avoid primary or secondary clustering.

* Insert

Given a Hash Table:

i:0(14) i:1() i:2() i:3() i:4() i:5() i:6()

Insert(35) = h(35) = v % M = 35 % 7 = 0  # i:0 is taken so we step
             h(35) = (v % M) + (step * (M' - (v % M'))) = (35 % 7) + (1 * (5 - (35 % 5))) = 5 # i:5 is empty so we place 35 there

i:0(14) i:1() i:2() i:3() i:4() i:5(35) i:6() 

Insert(17) = h(17) = v % M = 17 % 7 = 3  # i:3 is empty so we place 17 there

i:0(14) i:1() i:2() i:3(17) i:4() i:5(35) i:6()

* Search

Searching uses the same algorithm to find values in the Hash Table

Given a Hash Table:

i:0(14) i:1() i:2() i:3(17) i:4() i:5(35) i:6()

Search(35) = h(35) = v % M = 35 % 7 = 0  # i:0 == 14 != 35 so we step
             h(35) = (v % M) + (step + (M' - (v % M'))) = (35 % 7) + (1 * (5 - (35 % 5))) = 5  # i:5 == 35 == 35 so we return the index 5

* Remove

Searching is similar to Search, but when we find the value we set it to our delete symbol

Given a Hash Table:

i:0(14) i:1() i:2() i:3(17) i:4() i:5(35) i:6()

Remove(35) = h(35) = v % M = 35 % 7 = 0  # i:0 == 14 != 35 so we step
             h(35) = (v % M) + (step + (M' - (v % M'))) = (35 % 7) + (1 * (5 - (35 % 5))) = 5  # i:5 == 35 == 35 so we set i:5 to our delete symbol and return the index 5


** Closed Addressing

Separate Chaining (SC) collision resolution uses M copies of auxiliary data structures, usually Doubly Linked Lists. If two keys, a and b, both have the same hash value, i, both will be appended to the (front or back) of Doubly Linked List. 

If we use Separate Chaining, the load factor α = N/M describes the average length of the M lists and it will determine the performance of Search(v) as we have to explore α elements on average. 
Remove(v) requires Search(v), so it's performance will be similar.
Insert(v) is O(1).

If we can bound α to a small constant, all operations, Search(v) Insert(v) Remove(v), using Separate Chaining will be O(1).

** Separate Chaining





