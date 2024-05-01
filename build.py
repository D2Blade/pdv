import os

# Criar diretórios
directories = ['style', 'script']

for directory in directories:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Conteúdo do arquivo HTML
html_content = '''
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro</title>
    <link rel="stylesheet" href="style/index.css">
</head>
<body>
    <header>header</header>
    <nav>
        <button class="bt_cad" onclick="mostrarMain('cod-cliente','nome','cpf')">cadastrar</button>
        <button class="bt_est" onclick="mostrarMain('est_item')">Estoque</button>
    </nav>
    <main>
        <input id="cod-cliente" style="display: none;" maxlength="255" placeholder="cod-cliente"></input>
        <input id="nome" style="display: none;" maxlength="50" placeholder="Nome"></input>
        <input id="cpf" style="display: none;" maxlength="11"></input>
        <input id="est_item" style="display: none;"></input>
    </main>
    <aside>aside</aside>
    <footer>footer</footer>
    <script src="script/script.js"></script>
</body>
</html>
'''

# Escrever o conteúdo no arquivo HTML
with open('index.html', 'w') as file:
    file.write(html_content)

# Conteúdo do arquivo script.js
script_content = '''
//BOTOES
function mostrarMain(...ids) {
  // Oculta todas as labels
  var inputs = document.querySelectorAll('main input');
  inputs.forEach(function(input) {
    input.style.display = 'none';
  });

  ids.forEach(function(id) {
          var input = document.getElementById(id);
          if (input) {
                  input.style.display = 'block';
          }
  });
}

//CPF
var inputCPF = document.getElementById('cpf');

inputCPF.addEventListener('input', function(event) {
  var valor = event.target.value.replace(/\D/g, '');
  
  event.target.value = valor;
});

inputCPF.addEventListener('keypress', function(event) {
  var charCode = event.which ? event.which : event.keyCode;

  if (charCode < 48 || charCode > 57) {
    event.preventDefault();
  }
});
'''

# Escrever o conteúdo no arquivo script.js
with open('script/script.js', 'w') as file:
    file.write(script_content)


style_content = '''
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
	background-color: white;
}

body {
    display: flex;
    margin: 3px;
    flex: 1 1 100vw;
    flex-wrap: wrap;
}

header, nav, main, aside, footer {
    background: blue ;
    display: flex;
    margin: 3px;
}

header {
    flex: 1 1 100vw;
    height: 100px;
}

nav {
    flex: 1 1 200px;
    flex-direction: column;
}

button {
	background-color: yellow;
	height: 5vw;
}

main {
    flex: 20 1 500px;
    height: calc(100vh - 224px);

}

input {
	position: relative;
	top: 50px;
	left: 50px;
	max-width: 50vw;
	height: 30px;
}

#cod-cliente {
	width: 10vw;
	flex-direction: row;
}
#nome {
	flex-direction: row;
	width: 40vw;
}

#cpf {
	flex-direction: column;
	width: 10vw;
}
aside {
    flex: 1 1 200px;
}

footer {
    flex: 1 1 100vw;
    height: 100px
}

@media only screen and (max-width: 923px) {
    main {
        height: calc(100vh - 330px);
        }
    aside {
        flex: 1 1 100vw;
        height: 100px;
        }
    }
@media only screen and (max-width: 717px) {
    nav {
        height: 100px;
        }
    main {
        height: calc(100vh - 436px);
        }
    }
'''

with open('style/index.css', 'w') as file:
    file.write(style_content)

print("Arquivos HTML e script.js gerados com sucesso!")

