from time import sleep  
            
def primeira_ativade():
    print("Minha primeira ativadade")
    sleep(2)
def segunda_ativade():
    print("Minha segunda ativadade")
    sleep(2)
def terceira_ativade():
    print("Minha terceira ativadade")
    sleep(2)
def pipeline():
    primeira_ativade()
    segunda_ativade()
    terceira_ativade()
    print("Pipeline Finalizou")

pipeline()