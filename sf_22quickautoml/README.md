# Getting Started
QuickAutoML é uma ferramenta para treinamento automatizado de modelos de machine learning. Com ela, é possível:
- Selecionar automaticamente as melhores features para determinado conjunto de dados;
- Encontrar automaticamente o melhor modelo para determinado conjunto de dados;
- Gerar relatórios de métricas para cada algoritmo treinado;

## Como instalar
* Clonar o repositório
```bash
git clone https://github.com/Malware-Hunter/sf22_quickautoml.git
```
* Instalar a biblioteca
```bash
cd sf22_quickautoml
sh distribute.sh
```

## Como utilizar?
```bash
sh run_quick.sh datasets/DrebinDatasetPermissoes.csv
option 10 default
option 11 permissions
option 12 apicalls

```
```python
python3 quick.py datasets/DrebinDatasetPermissoes.csv --default
python3 quick.py datasets/DrebinDatasetPermissoes.csv --permissions
python3 quick.py datasets/DrebinDatasetPermissoes.csv --apicalls
```