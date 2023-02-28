"""
Given 16M unique IDs, we want to implement two functions

GetID() -> int which returns an int representating an available IdD and allocates it

ReleaseID(int) -> void which releases an ID and makes it available again

I did two sets: O(1) time, O(N) space

He asked about memory and I struggled a bit. Should review that in CTCI. I tried to imrprove O(N) space but could not think of it - he said cant do that but can make storage more efficient

I asked if we could assume 32 bit int and he said yes.

So I did 

16*4 (bytes) = 64M (at first I said GB and then corrected to MB, phew) - review the table and data types

He pushed me towards a more efficient structure. At first I thought a counter

1
2
3

But then breakz when call release(2)

Then he said 2 states, what is the most efficient way to represent 2 states?

I said bit! And then he mentioned vector

Bit vector / bit array!

ID is the index/key of the array

[0, 1, 1, 1, …]

getID() is now O(N), but storage is more efficient

Now its 16M bits! Or 4M bytes (64MB -> 4MB)

release() is still constant
"""