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
        self.length = 1

    def __repr__(self):
        list_ = "["
        start_node = self.head
        list_ += str(start_node.value)
        while (start_node.next):
            list_ += f", {str(start_node.next.value)}"
            start_node = start_node.next
        list_ += "]"
        return list_

    def empty_list(self):
        self.head = None
        self.next = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        last_node = self.tail
        if self.length == 0:
            return None
        pre = self.head
        post = self.head
        while (post.next):
            pre = post
            post = post.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return last_node.value


if __name__ == "__main__":
    ll = LinkedList(5)
    ll.append(35)
    ll.append(135)
    ll.append(235)
    ll.append(335)
    a = ll.pop()
    print(ll)
    print(a)
