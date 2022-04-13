class Deque:

    def __init__(self):
        self.queue = []

    def push_front(self, key):
        self.queue.insert(0, key)
        return 'ok'

    def push_back(self, key):
        self.queue.append(key)
        return 'ok'

    def pop_front(self):
        return self.queue.pop(0) if self.size() else 'error'

    def pop_back(self):
        return self.queue.pop() if self.size() else 'error'

    def front(self):
        return self.queue[0] if self.size() else 'error'

    def back(self):
        return self.queue[-1] if self.size() else 'error'

    def clear(self):
        self.queue.clear()
        return 'ok'

    def size(self):
        return len(self.queue)


def process_deque(commands):
    dq = Deque()
    return [
        getattr(dq, command.split()[0])(int(command.split()[1])) if len(command.split()) == 2
        else getattr(dq, command.split()[0])() for command in commands
    ]


if __name__ == "__main__":
    test_cmd = ["push_front 1", "push_front 2", "push_back 6", "front", "back", "clear", "size", "back"]
    # should print ["ok", "ok", "ok", 2, 6, "ok", 0, "error"]
    print(process_deque(test_cmd))

    test_cmd = ["pop_front", "back", "push_back 2", "size"]
    # should print ["error", "error", "ok", 1]
    print(process_deque(test_cmd))

    test_cmd = ["push_back 1", "push_front 10", "push_front 4", "push_front 5", "back", "pop_back", "pop_back", "back"]
    # should print ["ok", "ok", "ok", "ok", 1, 1, 10, 4]
    print(process_deque(test_cmd))
