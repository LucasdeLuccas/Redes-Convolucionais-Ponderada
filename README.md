# Redes-Convolucionais-Ponderada

## Estrutura do Projeto

```plaintext
Redes-Convolucionais-Ponderada/
├── app.py
├── train_model.py
├── pesos.h5
├── templates/
│   ├── upload.html
│   └── predict.html
├── static/
│   ├── css/
│   │   └── styles.css
│   └── images/
│       ├── estevao.png
│       └── success.gif
└── README.md
```

## Requisitos

- Python 3
- pip (Python package installer)

## Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/LucasdeLuccas/Redes-Convolucionais-Ponderada
cd Redes-Convolucionais-Ponderada
```

2. **Crie e ative um ambiente virtual:**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

## Treinamento do Modelo

1. **Execute o script de treinamento:**

```bash
python train_model.py
```

Isso irá treinar a CNN usando o dataset MNIST e salvar os pesos treinados em um arquivo chamado `pesos.h5`.

## Executando a Aplicação

1. **Inicie o servidor Flask:**

```bash
python app.py
```

2. **Acesse a aplicação no navegador:**

Abra o navegador e vá para `http://127.0.0.1:5000/`.

## Estrutura dos Arquivos

- `app.py`: Contém o backend Flask para servir a aplicação web.
- `train_model.py`: Contém o código para treinar a CNN no dataset MNIST.
- `templates/`: Contém os templates HTML para a aplicação.
  - `upload.html`: Página de upload para enviar imagens.
  - `predict.html`: Página de resultado da predição.
- `static/`: Contém arquivos estáticos como CSS e imagens.
  - `css/`: Contém o arquivo de estilos `styles.css`.
  - `images/`: Contém imagens usadas na aplicação (`estevao.png` e `success.gif`).


## Demonstração

https://youtu.be/Yn5QehQAzJQ

Clique no link acima para assistir à demonstração do projeto.
