# Your code here
import os, glob


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    # entries = os.listdir("/users")
    for path in files:
        print(os.listdir("hashtables/ex5" + path))
    # return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
