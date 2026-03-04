# 🖥️ Automação de Cadastro de Produtos

Este projeto foi desenvolvido em **Python** para automatizar o processo de login em um sistema e o cadastro de produtos a partir de uma base de dados CSV.  
A automação é feita com **PyAutoGUI** (para interação com a interface gráfica) e **Pandas** (para manipulação da base de dados).

---

## 📌 Objetivo
O objetivo é **automatizar tarefas repetitivas** de cadastro de produtos em um sistema interno da empresa, reduzindo erros humanos e aumentando a produtividade.

---

## 🚀 Funcionalidades
- Abre automaticamente o navegador e acessa o sistema.
- Realiza login com usuário e senha.
- Lê a base de dados `produtos.csv`.
- Remove duplicidades de produtos pelo campo `codigo`.
- Preenche os campos do sistema (código, marca, tipo, categoria, preço, custo e observação).
- Cadastra cada produto de forma automatizada.
- Permite interromper a automação manualmente (movendo o mouse para o canto superior esquerdo da tela).

---

## 🛠️ Tecnologias utilizadas
- **Python 3.x**
- [PyAutoGUI](https://pyautogui.readthedocs.io/) → automação da interface gráfica.
- [Pandas](https://pandas.pydata.org/) → manipulação da base de dados.
- **Time** → controle de pausas e intervalos.

---

## 📂 Estrutura do projeto
automacao_cadastro_produtos/
│
├── main.py            # Script principal da automação
├── produtos.csv       # Base de dados dos produtos
├── requirements.txt   # Lista de dependências
└── README.md          # Documentação do projeto

Detalhes do funcionamento

Configuração inicial

Define pausas (pyautogui.PAUSE) e fail-safe (pyautogui.FAILSAFE).

Configura o link do sistema.

Login automático

Abre o navegador Edge.

Digita o link do sistema.

Preenche usuário e senha.

Importação da base de dados

Lê o arquivo produtos.csv.

Remove duplicados pelo campo codigo.

Cadastro dos produtos

Itera sobre cada linha da tabela.

Preenche os campos do sistema com os dados do CSV.

Cadastra o produto.

Retorna ao início da tela para o próximo cadastro.

Interrupção manual

Caso o mouse seja movido para o canto superior esquerdo, a automação é interrompida com segurança.
