<h1 align="center">🧪 Chemical Database 💊 </h1>

<h3 align="center">Um programa para controle de estoque de remédios</h3>

O software para gerenciar estoques de medicamentos veterinários. Ele facilita a dinâmica de medicar animais de estimação, registrando os medicamentos para cada pet. Você pode registrá-los, bem como os remédios que cada pet estará consumindo. O programa lista os remédios armazenados em seu banco de dados de acordo com a data de validade, destacando em vermelho aqueles que estão próximos de expirar. Além disso, exibe informações importantes sobre cada medicamento, como nome farmacêutico, peso líquido, validade, nome do pet que o consome e mais.

O programa possui quatro funções principais que resumem seu funcionamento. Ao iniciar o executável, ele executa a primeira função, chamada "Listar", responsável pela exibição dos dados descritos acima. Essa função é essencialmente responsável pela saída de dados para o usuário.

O segundo encargo é chamado "Adicionar", sendo o elemento responsável por registrar medicamentos no banco de dados. Ele exige que o usuário insira informações sobre o remédio, incluindo a identificação do pet para o qual o medicamento será destinado, pois esse campo é obrigatório para que o programa relacione o banco de remédios com o de animais de estimação.

Antes de registrar qualquer remédio, o usuário precisa registrar ao menos um pet. Isso é feito através do método "Adicionar Pet", onde são inseridos a cor, o peso do animal e o nome, que servirá como identificador na relação entre os bancos de dados. Caso seja necessário registrar um remédio sem um pet específico, recomenda-se criar previamente um pet com nome "Indefinido" ou "Indeterminado".

A quarta função, "Buscar", utiliza outros quatro métodos como subfunções para realizar pesquisas no banco de dados. Duas dessas funções realizam buscas diretas, utilizando o nome como identificador para remédios e pets: "Consultar Pets" e "Buscar Medicamentos". Os outros dois submétodos da função "Buscar" permitem a atualização dos elementos já cadastrados no banco de dados. Dessa forma, ao pesquisar pelo nome, o usuário pode acessar novamente a tela de registro para atualizar os dados.

### ⚙️ Tecnologias Utilizadas 

Linguagens, ferramentas e bibliotecas utilizadas no desenvolvimento do projeto:

* [Python](https://www.python.org/)
* [SQL]
* [sqlite3](https://docs.python.org/3/library/sqlite3.html)
* [PySide6](https://doc.qt.io/qtforpython-6/PySide6/QtCore/Signal.html)
* [DBeaver](https://dbeaver.io/)

##  🪄 Como rodar o projeto

Faça o download do projeto através do GitHub. Na pasta dist, crie um atalho do executável na área de trabalho. Será criado um arquivo "SGM.sqlite3" na pasta dist, onde os dados serão registrados nas tabelas de pets e remédios.

## 🔧 Construindo a base do projeto

Ao executar o programa pela primeira vez, o script criará e montará automaticamente a base de dados utilizada no projeto.

Você pode encontrar o arquivo do banco de dados no diretório do projeto, dentro da pasta "dist", após a primeira execução.

## ⚠️ Problemas enfrentados

### Erro de abertura de conexões com o banco:
No início, o programa funcionava abrindo uma conexão única durante toda a execução do software, mas dentro de cada função tentava-se abrir uma nova conexão. Em uma aplicação que utilizasse outro SGBD, com suporte a múltiplas conexões, isso não geraria erro. No entanto, como o SQLite não possui esse suporte, esse entrelaçamento gerava exceções.
* **Como solucionar:** A conexão foi removida do código principal, deixando apenas as conexões específicas dentro de cada método.

### Erro de diretório de criação para o banco de dados:
O caminho referenciado para criar o banco de dados não era adequado ao exportar o programa para outra máquina. Assim, ao executá-lo, o programa não encontrava as tabelas necessárias e, consequentemente, não funcionava corretamente.
* **Como solucionar:** Foi utilizado um caminho absoluto no código de criação do banco de dados para garantir compatibilidade ao exportar o programa.

## ⏭️ Próximos passos

Futuramente, a inclusão do pet também contará com o registro do peso.