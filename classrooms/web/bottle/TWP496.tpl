<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Hello Word</title>
</head>
<body>
    <p>
        Bem vindo {{username}}
    </p>
    <ul>
        %for thing in things:
            <li>{{thing}}</li>
        %end
    </ul>
</body>
</html>