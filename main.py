balance_dict = {
    '(': ')',
    '[': ']',
    '{': '}'
}

balanced_list = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]

unbalanced_list = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


def check_balance(sequence):
    stack = Stack()
    for item in sequence:
        if item in balance_dict:
            stack.push(item)
        elif item == balance_dict.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.is_empty()


if __name__ == '__main__':
    for seq in balanced_list + unbalanced_list:
        print(check_balance(seq))

