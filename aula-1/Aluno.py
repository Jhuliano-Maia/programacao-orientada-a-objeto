'''
    Comentarios em 
    múltiplas
    linhas
'''

class Aluno:
    #Comentario em linha
    #atributo de classe abaixo
    instituicaoEnsino: str

    #Construtor
    #Os atributos de instância estão sempre como parametros do construtor
    def __init__(self, matricula: int, nome: str, idade: int):
        #atribuição instancia
        #valores unico para cada instancia do objeto
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.instituicaoEnsino = "IFAM"
        print("------------------------------------------------------------------")
        print("Objeto Aluno criado com sucesso...")
        print("------------------------------------------------------------------")
        
    #Destruidor
    def __del__(self):
        print("------------------------------------------------------------------")
        print("Objeto Aluno destruido com sucesso...")
        print("------------------------------------------------------------------")

    def __str__(self):
        return (
            f"------------------------------------------------------------------\n"
            f"Objeto Aluno:\n"
            f"Matrícula: {self.matricula}\n"
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Instituição: {self.instituicaoEnsino}\n"
            f"------------------------------------------------------------------"

        )
    