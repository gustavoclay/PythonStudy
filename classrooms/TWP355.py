arquivo = open('hello.html', 'w', encoding = 'utf-8')
arquivo.write('''<!DOCTYPE html>
<head>
<meta charset = "utf-8">
<title>Title</title>
</head>
<body>
Hello Word
</body>
</hmtl>''')
arquivo.close()