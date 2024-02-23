def to_indexed(source_file, output_file):
    with open(source_file, 'r') as file_read:
        lines = file_read.readlines()

    with open(output_file, 'w') as file_write:
        for i, line in enumerate(lines):
            file_write.write(f"{i}: {line}")

# Використання функції
# to_indexed('source.txt', 'output.txt')
