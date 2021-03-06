def read_lines_for_python(file_name, file_type):
    if file_type not in ('txt', 'html'):
        raise ValueError('Not correct file format')

    if not file_name:
        raise IOError('File Not Found')

    with open(file_name, 'r') as f:
        for line in f:
            if 'python' in line:
                return 'Found Python'


if not read_lines_for_python('file_without_python_name', 'pdf'):
    print('no correct file format or file name does not exists')
