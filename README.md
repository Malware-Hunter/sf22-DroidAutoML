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

**Etapa 3**: na **seleção de modelos**, a ferramenta recebe um subconjunto reduzido de características da etapa anterior e aplica sobre 3 algoritmos de aprendizado de máquina :
- K-Nearest Neighbor(KNN)
- Random forest
- AdaBoost

**Etapa 4**: por fim ocorre o **ajuste do modelo** onde os algoritmos da etapa anterior são otimizados com hiper-parâmetros e avaliado selecionando melhor modelo, ou seja, aquele que atingir a melhor acurácia.
Como saída a ferramenta retorna **( a )** modelo treinado serializado no formato ".pkl"; **( b )** subconjunto reduzido de características; **( c )** relatório de desempenho do modelo contendo (melhor modelo e seus Hiper-parâmetros, Acurácia, Precisão, Recall, Medida-F e tempo de execução do pipeline completo).

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
  --output-results      saída para o arquivo de métricas da ferramenta (e.g. acuracy, recall,time) padrão "droidautoml_results.csv"
  --output-model        saída para o modelo treinado e serializado formato .pkl padrão "model_serializable.pkl"

```

## Exemplos de utilização

```python
Run in SigPID:
python3 droidautoml.py --dataset datasets/drebin_215_permissions.csv --use-select-features permissions
Run in RFG:
python3 droidautoml.py --dataset datasets/drebin_215_api_calls.csv --use-select-features api-calls
Run in Jowmdroid:
python3 droidautoml.py --dataset datasets/drebin_all.csv --use-select-features mult-features
```

## Ambiente de testes

A DroidAutoML foi instalada e testada nos seguintes ambientes:
- Notebook Intel(R) Core(TM) i7-1185G7 3.00GHz da
geração 11.
- Memória RAM de 32GB
- Sistema operacional Microsoft Windows 10 64 bit. 

Para a execução da ferramenta foi utilizada uma máquina
virtual [VirtualBox](https://www.virtualbox.org/) Versão (6.1.26 r145957 - Qt5.6.2)  executando um Linux Ubuntu 20.04.3 LTS 64 bit.
- kernel = 5.15.0-43-generic
- GNOME = 42.0
-  4 CPUs 
- 16GB de RAM


