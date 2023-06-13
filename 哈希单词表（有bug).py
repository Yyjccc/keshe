class Ht_item:
  def __init__(self, key, value):
    self.key = key
    self.value = value

class HashTable:
    def __init__(self, size):
        self.size = size
        self.count = 0
        self.items = [None] * size

    def insert(self, key, value):
        # Compute the index from the key
        index = self.hash(key)

        # Create a new item
        item = Ht_item(key, value)

        # Check if the index is empty
        if self.items[index] is None:
            # Create a new linked list at the index
            self.items[index] =[]

        # Append the item to the linked list at the index
        self.items[index].append(item)

        # Increment the count of elements
        self.count += 1

        # Check if the load factor is too high
        if self.count / self.size > 0.75:
            # Resize the table
            self.resize()


    def delete(self, key):
        # Compute the index from the key
        index = self.hash(key)

        # Check if the index is not empty
        if self.items[index] is not None:
            # Traverse the linked list at the index
            current = self.items[index].head
            previous = None
            while current is not None:
                # Check if the key matches
                if current.data.key == key:
                    # Delete the node from the linked list
                    if previous is None:
                        # The node is the head of the list
                        self.items[index].head = current.next
                    else:
                        # The node is in the middle or end of the list
                        previous.next = current.next

                    # Decrement the count of elements
                    self.count -= 1

                    # Check if the load factor is too low
                    if self.count / self.size < 0.25:
                        # Resize the table
                        self.resize()

                    # Return the deleted value
                    return current.data.value

                # Move to the next node in the list
                previous = current
                current = current.next

        # The key was not found in the table
        return None


    def find(self, key):
        # Compute the index from the key
        index = self.hash(key)

        # Check if the index is not empty
        if self.items[index] is not None:
            # Traverse the linked list at the index
            current = self.items[index].head
            while current is not None:
                # Check if the key matches
                if current.data.key == key:
                    # Return the value
                    return current.data.value

                # Move to the next node in the list
                current = current.next

        # The key was not found in the table
        return None


    def resize(self):
        # Save the old list of items
        old_items = self.items

        # Double the size if the load factor is too high
        if self.count / self.size > 0.75:
            self.size *= 2

        # Halve the size if the load factor is too low
        elif self.count / self.size < 0.25:
            self.size //= 2

        # Create a new list of items with the new size
        self.items = [None] * self.size

        # Reset the count of elements
        self.count = 0

        # Rehash all the old items into the new list
        for old_item in old_items:
            if old_item is not None:
                # Traverse the linked list at each index
                current = old_item.head
                while current is not None:
                    # Insert the key-value pair into the new list
                    self.insert(current.data.key, current.data.value)
                    # Move to the next node in the list
                    current = current.next


    def spell_check(self, word):
        # Print the word itself
        print(word, end=" ")

        # Find the suggested words in the hash table
        suggestions = self.find(word)

        # Check if the word is correct or incorrect
        if suggestions is not None:
            # The word is correct
            print("is correct")

        else:
            # The word is incorrect
            print(":", end="")

            # Generate possible suggestions by inserting, deleting, or replacing a letter
            for i in range(len(word)):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    # Insert a letter at position i
                    new_word = word[:i] + letter + word[i:]
                    suggestions = self.find(new_word)
                    if suggestions is not None:
                        # Print a space and then the suggestion
                        print(" ", new_word, end="")

                    # Replace a letter at position i
                    new_word = word[:i] + letter + word[i + 1:]
                    suggestions = self.find(new_word)
                    if suggestions is not None:
                        # Print a space and then the suggestion
                        print(" ", new_word, end="")

                # Delete a letter at position i
                new_word = word[:i] + word[i + 1:]
                suggestions = self.find(new_word)
                if suggestions is not None:
                    # Print a space and then the suggestion
                    print(" ", new_word, end="")

            # Print a newline at the end of each word
            print()

# Create a hash table with size 10
ht = HashTable(10)

# Insert some words and their suggested words into the hash table
ht.insert("i", ["i"])
ht.insert("is", ["is"])
ht.insert("has", ["has"])
ht.insert("have", ["have"])
ht.insert("be", ["be"])
ht.insert("my", ["my"])
ht.insert("more", ["more"])
ht.insert("contest", ["contest"])
ht.insert("me", ["me"])
ht.insert("too", ["too"])
ht.insert("if", ["if"])
ht.insert("award", ["award"])

# Spell check some words using the hash table
ht.spell_check("me")
ht.spell_check("aware")
ht.spell_check("m")
ht.spell_check("contest")
ht.spell_check("hav")
ht.spell_check("oo")
ht.spell_check("or")
ht.spell_check("i")
ht.spell_check("fi")
ht.spell_check("mre")
