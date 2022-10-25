import os


def get_files_for_checking(start_path):
    source_files = []
    for root, dirs, files in os.walk(start_path, topdown=True):
        for file in files:
            if file.endswith('.py') and not root.endswith('migrations'):
                source_files.append('%s/%s' % (root, file))
    return source_files
