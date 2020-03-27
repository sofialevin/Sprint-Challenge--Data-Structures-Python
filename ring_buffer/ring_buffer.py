from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.oldest = None

    def append(self, item):
        # if list is under capacity
        if len(self.storage) == 0:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            return

        # set the next node on tail to be the head if we reach capacity
        if (len(self.storage)) == self.capacity and self.storage.tail.next is None:
            self.storage.tail.next = self.storage.head

        # if tail.next is still None we can keep appending to tail
        if self.storage.tail.next is None:
            self.storage.add_to_tail(item)
            self.current = self.current.next
        else:
            # otherwise, set the next nodes value to be the item.
            self.current = self.current.next
            self.current.value = item


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        cursor = self.storage.head

        list_buffer_contents.append(cursor.value)

        cursor = cursor.next

        while cursor is not self.storage.head:
            list_buffer_contents.append(cursor.value)

            if cursor.next is None:
                break
            cursor = cursor.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
