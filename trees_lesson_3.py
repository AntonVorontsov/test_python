from hexlet.fs import mkdir, mkfile


def generate():
    return mkdir(
        'python-package',
        [
            mkfile('Makefile'),
            mkfile('README.md'),
            mkdir('dist'),
            mkdir('tests', [
                mkfile('test_solution.py'),
            ]),
            mkfile('pyproject.toml'),
            mkdir(
                '.venv',
                [
                    mkdir('lib', [
                        mkdir('python3.6', [
                            mkdir('site-packages', [
                                mkfile('hexlet-python-package.egg-link'),
                            ]),
                        ]),
                    ]),
                ],
                {'owner': 'root', 'hidden': False},
            ),
        ],
        {'hidden': True},
    )


def test_downcase_file_names():
    expected = {
        'name': 'python-package',
        'meta': {'hidden': True},
        'type': 'directory',
        'children': [
            {'name': 'Makefile', 'meta': {}, 'type': 'file'},
            {'name': 'README.md', 'meta': {}, 'type': 'file'},
            {'name': 'dist', 'meta': {}, 'type': 'directory', 'children': []},
            {
                'name': 'tests',
                'meta': {},
                'type': 'directory',
                'children':
                    [{'name': 'test_solution.py', 'meta': {}, 'type': 'file'}],
            },
            {'name': 'pyproject.toml', 'meta': {}, 'type': 'file'},
            {
                'name': '.venv',
                'meta': {'owner': 'root', 'hidden': False},
                'type': 'directory',
                'children': [{
                    'name': 'lib',
                    'meta': {},
                    'type': 'directory',
                    'children': [{
                        'name': 'python3.6',
                        'meta': {},
                        'type': 'directory',
                        'children': [{
                            'name': 'site-packages',
                            'meta': {},
                            'type': 'directory',
                            'children': [{
                                'name': 'hexlet-python-package.egg-link',
                                'meta': {},
                                'type': 'file',
                            }],
                        }],
                    }],
                }],
            },
        ],
    }
    assert generate() == expected