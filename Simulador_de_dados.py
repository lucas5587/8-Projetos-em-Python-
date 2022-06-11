# simulador de dado
# Simular o uso de um dado, gerando um valor de 1 ate 6 
import random # essa e a biblioteca para gerar os numeros aleatorios 
import PySimpleGUI 


class SimuladorDeDado: # aqui foi criada a base. no caso chamada de classe 
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Voce gostaria de gerar um novo valor para o dado?'
        #oque tem que fazer com o pysimplegui e 
        #criar um Layout
        layout = [
            [sg.Text('Vamos JOgar o dado?')]
            [sg.button('sim'),sg.botton('nao')]
            
        #Criar uma janela 
        #ler os valores na tela 
        # vamos fazer alguma coisa com esses valores 
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        try: # se for digitado algo que nao esteja programado ou seja nao e o correto ele vai dar essa exceção  
            if resposta == 'sim' or resposta == 's':  # ele vai responder esses dois tipos de respostas  
                self.GerarValordoDado()        
            elif resposta == 'nao' or reposta == 'n': # ele vai responder esses dois tipos de respostas 
                print('Agradecemos a sua aprticipaçao')               
            else:
                print('Favor digitar sim ou não')
        except: #esse comando faz parte do try, no caso ele diz se ocorrer alguma exceção ele pode ate escrever algo
            print('Ocorreu um erro ao receber sua resposta') # essa vai ser a resposta se tiver alguma exceçao
                       

    def GerarValordoDado(self):
        
        print(random.randint(self.valor_minimo,self.valor_maximo))
        
    
simulador = SimuladorDeDado()
simulador.Iniciar()              