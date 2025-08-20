'''
    Comentarios em 
    múltiplas
    linhas
'''

class Aluno:
    #Comentario em linha
    instituicaoEnsino: str

    #Construtor
    def __init__(self, matricula: str, nome: str, idade: str):
        #atribuição instancia
        #valores unico para cada instancia do objeto
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.instituicaoEnsino = "IFAM"
        print("_____________________________________________________________")
        print("Objeto Aluno criado com sucessp...")
        print("_____________________________________________________________")
        