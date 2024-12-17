import sys

class Node:
    def __init__(self):
        self.children = {}
        self.permissions = {}

class FileSystem:
    def __init__(self):
        self.root = Node()

    def _get_node(self, path):
        current = self.root
        parts = path.strip('/').split('/')
        for part in parts:
            if part not in current.children:
                current.children[part] = Node()
            current = current.children[part]
        return current

    def grant(self, user, mode, path):
        node = self._get_node(path)
        node.permissions[user] = mode
        return "done"

    def block(self, user, mode, path):
        node = self._get_node(path)
        if user in node.permissions:
            del node.permissions[user]
        return "done"

    def check(self, user, mode, path):
        current = self._get_node(path)
        while current:
            if user in current.permissions:
                if current.permissions[user] == mode:
                    return "allowed"
                else:
                    return "forbidden"
            break
        return "forbidden"



results = []
for command in sys.stdin.readline():
    parts = command.split()
    cmd_type = parts[0]
    user = parts[1]
    mode = parts[2]
    path = ' '.join(parts[3:])

    if cmd_type == "grant":
        results.append(fs.grant(user, mode, path))
    elif cmd_type == "block":
        results.append(fs.block(user, mode, path))
    elif cmd_type == "check":
        results.append(fs.check(user, mode, path))

print(results)
for result in results:
    print(result)