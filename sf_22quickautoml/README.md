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

```python
Run in SigPID:
python3 quick.py -d datasets/DrebinDatasetPermissoes.csv --use-select-features permissions
Run in RFG:
python3 quick.py -d datasets/DrebinDatasetPermissoes.csv --use-select-features api-calls
```