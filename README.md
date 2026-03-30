# Demonstração de Colisão de Hash com Imagens

## Objetivo

Este projeto tem como objetivo demonstrar o conceito de **colisão de funções de hash**, utilizando duas imagens diferentes.

Uma colisão ocorre quando **duas entradas distintas produzem o mesmo valor de hash**.

---

## Abordagem

O experimento foi dividido em duas partes:

### 1. Hashes criptográficos reais
Foram utilizados algoritmos conhecidos:

- MD5
- SHA-256

Esses algoritmos são projetados para evitar colisões.

---

### 2. Hash fraco (didático)
Foi implementado um hash propositalmente simples, baseado apenas nas dimensões da imagem:

Esse tipo de hash não é seguro e permite colisões facilmente.

## Estrutura do Projeto
hash-collision/
├── images/
│ ├── aviao.jpeg
│ └── navio.jpeg
├── src/
│ └── colisao.py
├── README.md
└── requirements.txt


---

## ⚙️ Instalação

Instale a dependência necessária:

```bash
pip install pillow

Na raiz do projeto, execute:

python src/colisao.py

## Saída Esperada

=== HASHES CRIPTOGRÁFICOS ===
Imagem 1 (MD5):    9c8f1c...
Imagem 2 (MD5):    a7d3b2...
Colisão em MD5?    NÃO

Imagem 1 (SHA256): 4f9a2e...
Imagem 2 (SHA256): b81c77...
Colisão em SHA256? NÃO

=== HASH FRACO / DIDÁTICO ===
Imagem 1 (weak hash): 105x70
Imagem 2 (weak hash): 105x70
Colisão no hash fraco? SIM

Conclusão:
As imagens são diferentes, mas geraram o mesmo hash fraco.
Isso demonstra o conceito de colisão de hash.
