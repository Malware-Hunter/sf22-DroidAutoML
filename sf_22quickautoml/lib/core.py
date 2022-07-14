import os
import pandas as pd
from androguard.core.bytecodes.apk import APK
import re
from termcolor import colored

class core:


    def diretorios(self):
        
        if(self.classe==1):
            diretorio="Malwares"
        else:
            diretorio="Benignos"
        directory = "output/"+str(diretorio)
        parent_dir = os.getcwd()
        path = os.path.join(parent_dir, directory)

        try:
            os.makedirs(path, exist_ok = True)
            os.makedirs("input", exist_ok = True)
            
        except OSError as error:
            print("Sem Permissão sudo")
        return directory


    @classmethod
    def extrair_permissoes(self):
        # Listas
        sha256 = []
        nome_APP = []
        API_ver = []
        API_MIN = []
        permissoes = []
        dire = self.d
        class_ref = core()
        print(colored('Gerando dados de Permissões...', 'blue'))
        print(colored('Salvando em '+str(class_ref.diretorios()),'yellow'))
        colunas = ['sha256', 'NOME', 'API_VER', 'API_MINI', 'PERMISSOES']
        for entry in os.scandir(self.d):
            # verifica se o arquivo termina com .apk e se é um arquivo regular
            if entry.path.endswith(".apk") and entry.is_file():
                # pega o sha256 do apk
                sha256=os.path.basename(entry.path.replace(".apk", ""))
                #print("\n Arquivo",sha256)
                # atribui o caminho e o arquivo a variavel app
                app = APK(entry.path)
                # extrai Nome do app e versão de API
                try:
                    nome = app.get_app_name()
                except:
                    nome = "Nao encontrado"
                pacote= app.get_package()
                API = app.get_effective_target_sdk_version()
                minSdkVersion = app.get_min_sdk_version()
                perm = app.get_permissions()
                data=[sha256,nome,pacote,API, minSdkVersion,perm]
                # cria um dataframe
                df = pd.DataFrame([data], columns=['SHA256','NOME','PACOTE','API','API_MIN','PERMISSOES'])
                 
                # salva em csv
                df.to_csv(str(class_ref.diretorios())+'/'+str(sha256)+'_permissao.csv', index = False, encoding="utf-8-sig")
                print(colored(str(sha256)+'_permissao.csv','yellow'))
        
                
        

    @classmethod
    def set_dataset(self):
        class_ref = core() 
        
        print(colored('Gerando Dataset...', 'blue'))
       
        try:
            caracteristicas = open("input/"+str(self.dataset),'r').readlines()
            dados_caracteristicas = [s.rstrip('\n') for s in caracteristicas]
            dataset_df = pd.DataFrame(columns=dados_caracteristicas)
        except:
            print(colored('Você deve informar um arquivo de características valido EX.: Permissões.txt', 'red'))
        #dataset_df = dataset_df[~dataset_df.index.duplicated()]
        # dataset de benignos
        dataset_b = {}
        dir_apks=class_ref.diretorios()
        # percorre o diretorio de benignos
        for entry in os.scandir(dir_apks):
            # verifica se possui arquivos e no formato apk
            if entry.path.endswith(".csv") and entry.is_file():
                # atribui o caminho e o arquivo a variavel app
                app = entry.path
                
                df = pd.read_csv(app)
                dataset_b['SHA256'] = df.SHA256.values
                dataset_b['Nome'] = df.NOME.values
                dataset_b['Pacote'] = df.PACOTE.values
                dataset_b['API_MIN'] = df.API.values
                dataset_b['API'] = df.API_MIN.values
                perm=df.PERMISSOES.values
                #perm = re.sub('^.*\.', '', str(perm))
                #perm1 = perm.replace("']\"]","")
                for i in dados_caracteristicas:
                    for j in perm:
                        if i in j:
                            dataset_b[i]=1
                        else:
                            dataset_b[i]=0
                            break
                # atribui a classificação benigno ao dataset
                dataset_b['Class'] =self.classe
                dataset_df=dataset_df.append(dataset_b, ignore_index=True)
        # Converte o dataframe em CSV
        dataset_df.to_csv(str(class_ref.diretorios())+'_Malware_Hunter_Dataset.csv', index=False)
        print(colored('Salvando em '+str(class_ref.diretorios())+'_Malware_Hunter_Dataset.csv','yellow'))
    
    

    @classmethod
    def main(self, d, caracteristica=2, dataset="Permissoes.txt",classe=0):
        self.d = d
        self.dataset = dataset
        self.classe =classe
        if caracteristica >= 2:
            self.extrair_permissoes()
            self.set_dataset()
