class AgendaTelefonica:
    def __init__(self):
        self.contatos={}
        
    def adicionar_contato(self, nome, telefone):
        if nome in self.contatos:
            print(f"Contato '{nome}' já existe na sua agenda.")
        else:
            self.contatos [nome] = telefone
            print(f"Contato '{nome}' foi adicionado com sucesso a sua agenda.")
            
    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato '{nome}' foi removido com sucesso da sua agenda.")
        else:
            print(f"Contato '{nome}' não foi encontrado na sua agenda.")
            
    def pesquisar_contato(self,nome):
        if nome in self.contatos:
            print(f"{nome}: {self.contatos[nome]}")
        else:
            print(f"Contato '{nome}' não foi encontrado na sua agenda.")
    
    def linta_cntatos(self):
        if not self.contatos:
            print("Sua agenda ainda não tem contatos adicionados")
        else:
            for nome, telefone in self.contatos.items():
                print(f"{nome}: {telefone}")
def menu():
    agenda = AgendaTelefonica()
    
    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar Contato")
        print("2. Romover Contato")
        print("3. Pesquisar Contato")
        print("4. listar Contatos")
        print("5. Sair")
        escolha = input("digite o numero da opção desejada: ")
        
        if escolha == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            agenda.adicionar_contato(nome, telefone)
        elif escolha == '2':
            nome = input("Nome: ")
            agenda.remover_contato(nome)
        elif escolha == '3':
            nome = input("Nome: ")
            agenda.pesquisar_contato(nome)
        elif escolha == '4':
            agenda.linta_cntatos()
        elif escolha == '5':
            print("Saindo da agenda telefônica")
        else:
            print("Opção invalida, insira o numero correspondete a opção desejada. Tente novamente.")

if __name__ == "__main__":
    menu()