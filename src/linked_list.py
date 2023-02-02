# Linked List можно представить как такую структуру:
head = {
    "value": 10,
    "next": {
        "value": 20,
        "next": {
            "value": 30,
            "next": {
                "value": 40,
                "next": None
            }
        }
    }
}


# print(head["next"]["next"]["value"])


########################

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self._length = 1

    def __len__(self):
        return self._length

    def __repr__(self):
        str_ll = "["
        nn = self.head
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
        last_node = self.tail
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
        return last_node.value

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


if __name__ == "__main__":
    ll = LinkedList(5)
    ll.append(35)
    ll.append(135)
    ll.append(235)
    ll.append(335)
    a = ll.pop()
    print(ll)
    print(a)
    print(len(ll))
