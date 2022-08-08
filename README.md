# DroidAutoML

DroidAutoML é uma ferramenta de AutoML de domínio específico que abstrai a execução das etapas de limpeza de dados, engenharia de características, escolha de algoritmos e ajuste de hiper-parâmetros, identificando o  modelo que melhor se ajusta ao problema de classificação de malwares Android. 

A DroidAutoML também implementa níveis de personalização, transparência, interpretabilidade e depuração que não são comuns nas ferramentas de AutoML de proposito geral, que funcionam essencialmente como "caixas pretas" (e.g., apenas apresentação das métricas finais aos usuários).

## O pipeline de AutoML

![O pipeline da DroidAutoML](https://gcdnb.pbrd.co/images/ZLQfWKF12ZN5.png?o=1)

**Etapa 1**: o **pré-processamento dos dados** trata valores ruidosos com:
- valores faltantes NaN (ou preenchê-los dependendo do caso);
- valores nulos (ou preenchê-los dependendo do caso);
- características/colunas que contenham apenas valor "0" zero para todas as amostras.

**Etapa 2**: na **engenharia de características**, a principal tarefa é identificar aquelas características mais relevantes para o domínio do problema, utilizando métodos sofistidados de seleção de características; 

Métodos atualmente disponíveis:
- SigPID: especializado em permissões
- RFG: especializado em chamadas de API
- JOWMDroid: diversos tipos de características

**Etapa 3**: 

**Etapa 4**: 

## Instalação 
* Clonar o repositório
```bash
git clone https://github.com/Malware-Hunter/sf22_quickautoml.git
```
* Instalar dependências
```bash
cd sf22_quickautoml
sh distribute.sh
```

## Parâmetros de entrada (opções de utilização)

```bash
Opções:
  --about               retorna informações do desenvolvedor
  --help                exibe as opções de parâmetros de entrada
  --dataset             dataset (e.g. datasets/DrebinDatasetPermissoes.csv)
  --use-select-features seleção de características (e.g., permissions, api-calls, mult-features )                       
  --sep                 separador usado no dataset por padrão ","
  --class-column        nome da coluna que determina a classificação do aplicativo por padrão "class"
  --output-results      saída para o arquivo de métricas da ferramenta (e.g. acuracy, recall,time) padrão "quick_results.csv"
  --output-model        saída para o modelo treinado e serializado formato .pkl padrão "model_serializable.pkl"

```

## Exemplos de utilização

```python
Run in SigPID:
python3 quick.py -d datasets/DrebinDatasetPermissoes.csv --use-select-features permissions
Run in RFG:
python3 quick.py -d datasets/drebin_215_api_calls_limpo.csv --use-select-features api-calls
Run in Jowmdroid:
python3 quick.py --dataset datasets/DrebinDatasetPermissoes.csv --use-select-features mult-features
```

## Ambiente de testes

A DroidAutoML foi instalar e testada nos seguintes ambientes:


