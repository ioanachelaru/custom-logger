def read_from_csv(filename):
    file_content = []
    with open(filename, 'r') as f:
        for line in f:
            file_content.extend(line.strip().split(','))
    return file_content