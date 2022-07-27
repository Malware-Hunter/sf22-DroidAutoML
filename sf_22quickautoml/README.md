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
python3 quick.py -d datasets/drebin_215_api_calls_limpo.csv --use-select-features api-calls
Run in Jowmdroid:
python3 quick.py --dataset datasets/DrebinDatasetPermissoes.csv --use-select-features mult-features
```
## Outras opções de uso
```bash
Opções:
  --about               retorna informações do desenvolvedor
  --help                exibe as opções de parametros de entrada
  --dataset             dataset (e.g. datasets/DrebinDatasetPermissoes.csv)
  --use-select-features seleção de caracteristicas (e.g., permissions, api-calls, mult-features )
                        
  --sep                 separador usado no dataset por padrão ","
  --class-column        nome da coluna que determina a clasificação do aplicativo por padrão "class"
  --output-results      saida para o arquivo de metricas da ferramenta (e.g. acuracy, recall,time)padrão "quick_results.csv"
  --output-model        saida para o modelo treinado e serializado formato .pkl parão "model_serializable.pkl"
```