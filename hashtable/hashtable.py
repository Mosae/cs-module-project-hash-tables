class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8
#Linked List
class LinkedList:
    def __init__(self):
        self.head = None
                                 

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.data = [LinkedList()] * capacity
        self.count = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        l = self.capacity
        #print('length',l)
        return l

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        #return the number of items in hash table divided by the total number of slots
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        pass

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash 

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the data capacity of the hash table.
        """
        
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        #find index in the hash table for the key
        index = self.hash_index(key)
        #if Linked List is empty
        if self.data[index].head == None:
            #insert value at head
            self.data[index].head = HashTableEntry(key, value)
            #increase count
            self.count += 1
            return
        else:
            #if its not empty - current is head
            curr = self.data[index].head
            while curr.next:
                if curr.key == key:
                    curr.value = value
                curr = curr.next
            #insert at the next available slot    
            curr.next = HashTableEntry(key,value)
            self.count += 1  
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity*2)


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        curr = self.data[index].head
        # prev = None
        if curr.key == key:
            self.data[index].head = self.data[index].head.next
            self.count -= 1
            return 
        while curr.key != None:
            if curr.key == key:
                prev.next = curr.next
                self.count -= 1
                return None
            prev = curr
            curr = curr.next
        return None  
 
            

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        curr = self.data[index].head
        if curr == None:
            return None
        if curr.key == key:
            return curr.value
        while curr.next:
            curr = curr.next
            if curr.key == key:
                return curr.value
        return None            
        # if curr is not None:
        #     while curr:
        #         if curr.key == key:
        #             return curr.value
        #         curr = curr.next
        # return            

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        #make a new array with double the capacity of the old one
        #refere the hash table to the new array
        #itarate through the old array and put them in the new one
        # if len(self.data) > self.capacity:
        #     self.capacity = new_capacity
        self.capacity = new_capacity
        new_arr = [LinkedList()] * new_capacity

        for i in self.data:
            curr = i.head

            while curr is not None:
                index = self.hash_index(curr.key)

                if new_arr[index].head == None:
                    new_arr[index].head = HashTableEntry(curr.key, curr.value)
                else:
                    new_node = HashTableEntry(curr.key, curr.value)
                    new_node.next = new_arr[index].head

                    new_arr[index].head = new_node
                curr = curr.next
        self.data = new_arr                


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
