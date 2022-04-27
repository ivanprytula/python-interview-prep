# Long and un-safe way, 'code smell' detected!
# f = open('test.md', 'r')
# file_contents = f.read()
# f.close()

# Use context manager
with open('test.md', 'r') as f:
    file_contents = f.read()

words = file_contents.split(' ')
word_counts = len(words)
print(f'{word_counts}')


# NB: Custom example
class ManagedWriteFile:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


with ManagedWriteFile('hello.txt') as f:
    f.write('requests==2.24.0')
    f.write('\n')
    f.write('Django>=3.1.3')
