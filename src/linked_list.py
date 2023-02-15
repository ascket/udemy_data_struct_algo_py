class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        self._length = 0
        if not value:
            self.head = None
            self.tail = None
        else:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self._length += 1

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
        new_node = Node(value)
        if self._length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._length += 1
        return True

    def pop(self):
        if self._length == 0:
            return None
        pre = self.head
        post = self.head
        while (post.next):
            pre = post
            post = post.next
        self.tail = pre
        self.tail.next = None
        self._length -= 1
        if self._length == 0:
            self.head = None
            self.tail = None
        return post

    def prepend(self, value):
        new_node = Node(value)
        if self._length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self._length += 1
        return True

    def pop_first(self):
        if self._length == 0:
            return None
        pre = self.head
        self.head = self.head.next
        pre.next = None
        self._length -= 1
        if self._length == 0:
            self.tail = None
        return pre

    def __getitem__(self, index):
        if index < 0 or index >= self._length:
            return None
        pre = self.head
        for _ in range(index):
            pre = pre.next
        return pre

    def __setitem__(self, index, value):
        node = self[index]
        if node:
            node.value = value
            return True
        return False

    def insert_value(self, index, value):
        if index == 0:
            return self.prepend(value)
        if index == self._length:
            return self.append(value)
        if index < 0 or index > self._length:
            return False
        pre = self[index - 1]
        node = Node(value)
        node.next = pre.next
        pre.next = node
        self._length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self._length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self._length - 1:
            return self.pop()
        pre = self[index - 1]
        post = pre.next
        pre.next = post.next
        post.next = None
        self._length -= 1
        return post

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self._length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def reverse_head_tail(self):
        """Reverse only head and tail"""
        pre = self.head
        pre_post = self.get_item(self._length - 2)
        self.head = self.tail
        self.head.next = pre.next
        self.tail = pre
        self.tail.next = None
        pre_post.next = self.tail


if __name__ == "__main__":
    ll = LinkedList(5)
    ll.append(20)
    ll.append(30)
    print(ll)
    a = ll.remove(2)
    print(a.value)
    print(ll)
