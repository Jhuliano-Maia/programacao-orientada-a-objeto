from Aluno import Aluno

class Main:
    aluno: Aluno

    def __init__(self):
        pass

    def executar(self):
        print("Programa sendo executado...")
        self.aluno = self.entradaDados()
        self.exibirDados()
        print("Programa finalizado...")

    def entradaDados(self):
        print("Cadastro de Aluno")
        #Entrada de dados
        matricula = input("Digite a matricula: ")
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        return Aluno(matricula, nome, idade)
    
    def exibirDados(self):
        print(self.aluno)

app = Main()
app.executar()

