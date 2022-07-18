from hexlet import fs

# mkdir вторым параметром принимает список детей,
# которые могут быть либо директориями, созданными mkdir,
# либо файлами, созданными mkfile
tree = fs.mkdir('etc', [
    fs.mkfile('bashrc'),
    fs.mkdir('consul', [
        fs.mkfile('config.json'),
    ]),
])