#!/user/lib/python
import requests
import os
import mdl


mdl.banner()

try:
   cep_val = input('                \033[7;32mDigite Um cep: \033[m') 
#VERIFICANDO SE NÃO TEM OITO DIGITOS
   if len(cep_val) != 8:
       
       print ('CEP INVALIDO')
       exit()

#VERIFICANDO SE TEM OITO DIGITOS

   elif len(cep_val) == 8:
        
    #SE NAO DER ERRO VAI RODA ESSES COMANDOS
        try:
           validar = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_val))
           dados = validar.json()
        
           print ("                  \033[1;33mBUSCANDO CEP!\033[m")
           os.system('sleep 2.0')
           print ("                  \033[4;32mlocalidade:\033[1;33m {}\033[m".format(dados['localidade']))
    
           print ("                  \033[4;32mEstado:\033[1;33m {}\033[m".format(dados['uf']))
           print ("                  \033[4;32mbairro:\033[1;33m {}\033[m".format(dados['bairro']))
           cont = input("\033[1;31m           DESEJA CONTINUA FAZENDO BUSCAS? S /PARA SIM, N /PARA NÃO: \033[m")
           if cont == 's':
               os.system('python cep.py')
           else:
                mdl.banner()
                print("\033[1;32m                     SAINDO....")
                os.system('sleep 2.0')
        except:
        #SE DER ERRO VAI RODA ESSE COMANDO
              mdl.banner()
              print ("Cep {} Não Emcontrado".format(cep_val))
              exit()
except:
       print ('ERRO!!!')
