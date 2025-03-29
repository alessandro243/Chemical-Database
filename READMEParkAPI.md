<h1 align="center">🧪 Chemical Database 💊 </h1>

<h3 align="center">Um software para controle de estoque de remédios</h3>

Um Software para gerenciar estoques de medicamentos veterinários, facilita a dinâmica de medicar animais de estimação, registrando o medicamentos para cada pet. Você pode registra-los e os remédios que cada pet estará consumindo. Ele lista os remédios que foram armazenados em seu banco de dados de acordo com sua data de validade, indicando os que estão próximos de estrapolar a data, em vermelho. Ele exibe informações importantes acerca de cada medicamento, como nome famacêutico, peso líquido, validade, nome do pet que o consome e mais.

O programa possui quatro principais funções que resumem seu funcionamento. Ao iniciar o executável ele executa a primeira, a função "Listar", que é resposável pelo execução do processo de exibição descrito a cima. Então ela praticamente é a função responsável pela saída de dados para o usuário.

O segundo encargo é chamado "Adicionar" e esse é o elemento responsável por registrar medicamentos no banco de dados. Ele exige que o usuário transcreva informações sobre o remédio, entre elas a identificação do pet para o qual o remédio será destinado, pois esse campo é obrigatório para que o programa faça a relação entre o banco de remédios e o de animais de estimação.

Então Antes de registrar quaisquer remédios, o usuário precisará registrar ao menos um pet. Isso é feito através do método "Adicionar Pet", regsitrando cor, peso do animal e o nome, que é o identificador usado na relação entre os dois bancos de dados. Logo se for o caso de regsitrar um remédio sem pet, é necessário definir previamente um pet como "Indefinido" ou "Indeterminado".

A Quarta função, "Buscar", usa outros quatro métodos como sub-funções para realizar buscas no banco, duas para realizar as buscas de fato, usando o nome como identificador para remédios e para pets, sendo elas as funções "Consultar pets" e "Buscar medicamentos". Os outros dois submétodos usados pela função "Buscar" são programados para atualizar o elemento antes retornado da base de dados. Então através do nome você acessa novamente a tela de registro para captar os dados novamente e atualiza-los no banco.

### ⚙️ Tecnologias Utilizadas 

Linguagens, ferramentas e bibliotecas utilizadas para elaborar o projeto.

* [Python](https://www.python.org/)
* [SQL]
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [PySide6](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Signal.html)
* [Dbeaver](https://dbeaver.io/)

##  🪄 Como rodar o projeto

Faça download do projeto através do github, na pasta dist, crie um atalho do exectável na área de trabalho. Será criado um arquivo "SGM.sqlite3" na pasta dist, aonde serão registrados os dados nas tabelas de pet e remédios.

## 🔧 Construindo a base do projeto

Quando executado o programa, se pela primeira vez o script cria e monta a base de dados utilizada no projeto. 

Você pode encontrar o arquivo do banco de dados na diretório do projeto na pasta "dist", após a primeira execução.

## ⚠️ Problemas enfrentados

### Erro de abertura de conexões com o banco:
No iníco o programa funcionava abrindo uma conexão em torno de toda a execução do software, porém dentro de cada função tentavasse abrir uma nova conexão. Em um aplicação que usasse outro SGBD, com suporte à multiplas conexões, isso não resultaria em erro, mas como o SGBD aqui implementado, SQLite, não tem esse suporte, esse entrelaçamento gerou exceções.

* **Como solucionar:** Foi removida a conexão da execução do código principal, deixando somente as conexões dos métodos.

### Erro de diretório de criação para o banco de dados:
O caminho referenciado para criar o banco de dados não se aplicava bem ao exportar o programa para outra máquina. Então ao executa-lo, ele não encontrava as tabelas necessárias e por isso não abria.
* **Como solucionar:** Foi usado um caminho absoluto no código de criação do banco de dados.

## ⏭️ Próximos passos

Futuramente, a inclusão do pet também contará com o registro do peso.