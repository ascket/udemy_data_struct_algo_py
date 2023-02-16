class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        node = Node(value)
        self.top = node
        self._length = 1

    def __len__(self):
        return self._length

    def __repr__(self):
        if self._length == 0:
            return "[]"
        nn = self.top
        str_stack = "["
        str_stack += str(nn.value)
        while (nn.next):
            str_stack += f", {str(nn.next.value)}"
            nn = nn.next
        str_stack += f"]"
        return str_stack

    def push(self, value):
        node = Node(value)
        if self._length == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self._length += 1
        return True

    def pop_first(self):
        if self._length == 0:
            return None
        pre = self.top
        self.top = pre.next
        pre.next = None
        self._length -= 1
        return pre
