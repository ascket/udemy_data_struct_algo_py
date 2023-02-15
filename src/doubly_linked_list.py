class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self._length = 1

    def __len__(self):
        return self._length

    def __repr__(self):
        if self._length == 0:
            return "[]"
        nn = self.head
        str_ll = "["
        str_ll += str(nn.value)
        while (nn.next):
            str_ll += f", {str(nn.next.value)}"
            nn = nn.next
        str_ll += "]"
        return str_ll

    def append(self, value):
        node = Node(value)
        if self._length == 0:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._length += 1
        return True

    def pop(self):
        if self._length == 0:
            return None
        pre = self.tail
        if self._length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            pre.prev = None
        self._length -= 1
        return pre

    def prepend(self, value):
        node = Node(value)
        if self._length == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self._length += 1
        return True

    def pop_first(self):
        if self._length == 0:
            return None
        pre = self.head
        if self._length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            pre.next = None
        self._length -= 1
        return pre

    def get_item(self, index):
        if index < 0 or index >= self._length:
            return None
        temp = self.head
        if index < self._length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self._length - 1, index, -1):
                temp = temp.prev
        return temp

    def set_item(self, index, value):
        pre = self.get_item(index)
        if pre:
            pre.value = value
            return True
        return False

    def insert_item(self, index, value):
        if index < 0 or index > self._length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self._length:
            return self.append(value)
        node = Node(value)
        pre = self.get_item(index - 1)
        post = pre.next
        pre.next = node
        node.prev = pre
        node.next = post
        post.prev = node
        self._length += 1
        return True

    def remove_item(self, index):
        if index < 0 or index >= self._length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self._length - 1:
            return self.pop()
        temp = self.get_item(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self._length -= 1
        return temp

    def reverse(self):
        if len(self) in [0, 1]:
            return self
        pre = self.head
        self.head = self.tail
        self.tail = pre
        pre_prev = pre.prev
        pre_after = pre.next
        before = None
        for _ in range(self._length):
            pre_prev = pre.prev
            pre_after = pre.next
            pre.next = before
            pre.prev = pre_after
            before = pre
            pre = pre_after


if __name__ == "__main__":
    ld = DoubleLinkedList(5)
    ld.append(10)
    ld.prepend(0)
    a = ld.get_item(0)
    print(ld)
    print(a.value)
