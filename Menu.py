#funcionário administrador cadastrado: nome = Teste / senha = 123
from Conexao import *

@db_session
def loginFuncionario(nome, senha):
    funcionario = select(f for f in Funcionario if f.nome == nome and f.senha == senha).first()      
    if funcionario:
        print("Logado com sucesso \n")
        return funcionario.cargo
    else:
        print("Usuário ou senha incorreto \n")
        return False

@db_session
def loginCliente(nome, senha):
    cliente = select(c for c in Cliente if c.nome == nome and c.senha == senha).first()      
    if cliente:
        print("Logado com sucesso \n")
        return cliente
    else:
        print("Usuário ou senha incorreto \n")
        return False
    
def verificador(min, max):
    while True:
        try:
            op = int(input("Opção: "))

            if op <= min or op > max:
                print("Digite um valor válido!")
                continue 
            break

        except ValueError: 
            print("Digite um valor válido!")

    return op

def verificarCliente():
    while True:
        nome = str(input("Nome do cliente: "))

        with db_session:
            cliente = Cliente.get(nome=nome)

            if cliente:
                break                   
            else:
                print("Cliente não cadastrado")
                continue

    return cliente

def verificarPet():
    while True:
        nomePet = str(input("Nome do pet: "))

        with db_session:
            pet = Pet.get(nome=nomePet)

            if pet:
                break           
            else:
                print("Pet não cadastrado")
                continue

    return pet

def verificarFuncionario():
    while True:
        nomeFunc = str(input("Nome do funcionário: "))
        
        with db_session:
            funcionario = Funcionario.get(nome=nomeFunc)

            if funcionario:
                break            
            else:
                print("Funcionario não cadastrado")
                continue

    return funcionario

while True:
    print("=" * 40)
    print("MENU PRINCIPAL".center(40))
    print("=" * 40)
    print("1 - Acessar menu funcionário")
    print("2 - Acessar menu cliente")
    print("3 - Sair")
    print("=" * 40)

    menu = verificador(0,3)

    if menu == 1:
        nomeFuncionario = str(input("Nome: "))
        senhaFuncionario = str(input("Senha: "))
        login = loginFuncionario(nomeFuncionario, senhaFuncionario)

        if login != False:

            if login == "admin":
                while True:
                    print("=" * 40)
                    print("MENU FUNCIONÁRIO - administrador".center(40))
                    print("=" * 40)
                    print("1 - Cadastrar funcionário")
                    print("2 - Excluir Funcionario")
                    print("3 - Sair")
                    print("=" * 40)

                    menuFunc = verificador(0,3)
                    
                    if menuFunc == 1:
                        nomeFunc = str(input("Nome do funcionário: "))
                        emailFunc = str(input("Email do funcionário: "))
                        cargoFunc = str(input("Cargo do funcionário: "))
                        senhaFunc = str(input("Senha de acesso do funcionário: "))

                        with db_session:
                            funcionario = Funcionario(nome=nomeFunc, email=emailFunc, cargo=cargoFunc, senha=senhaFunc)
                            print("Funcionário cadastrado com sucesso!")

                    elif menuFunc == 2:
                        with db_session:
                            funcionario = verificarFuncionario()
                            funcionario.delete()
                            print("Funcionário deletado com sucesso!")

                    elif menuFunc == 3:
                        break

            elif login == "atendente":
                while True:
                    print("=" * 40)
                    print("MENU FUNCIONÁRIO - atendente".center(40))
                    print("=" * 40)
                    print("1 - Cadastrar cliente")
                    print("2 - Editar cadastro de cliente")
                    print("3 - Excluir cliente")
                    print("4 - Buscar cliente \n")
                    print("5 - Cadastrar novo pet")
                    print("6 - Editar pet")
                    print("7 - Excluir pet ")
                    print("8 - Buscar pet \n")
                    print("9 - Marcar atendimento")
                    print("10 - Desmarcar atendimento")
                    print("11 - Ver atendimentos")
                    print("12 - Sair")
                    print("=" * 40)

                    menuFunc = verificador(0, 12)

                    if menuFunc == 1:
                        nomeCliente = str(input("Nome: "))
                        emailCliente = str(input("Email: "))
                        foneCliente = str(input("Telefone: "))
                        senhaCliente = str(input("Senha do cliente:"))

                        with db_session:
                            Cliente(nome=nomeCliente, email=emailCliente, telefone=foneCliente, senha=senhaCliente)
                            print("Cliente cadastrado com sucesso!")
                    
                    elif menuFunc == 2:
                        with db_session:
                            cliente = verificarCliente()
                            
                            print("1 - Editar nome")
                            print("2 - Editar email")
                            print("3 - Editar telefone")
                            print("4 - Editar senha")

                            edicao = verificador(0,4)
                        
                            if edicao == 1:
                                novoNome = str(input("Novo nome: "))
                                cliente.nome = novoNome

                            elif edicao == 2:
                                novoEmail = str(input("Novo email: "))
                                cliente.email = novoEmail

                            elif edicao == 3:
                                novoFone = str(input("Novo telefone: "))
                                cliente.telefone = novoFone

                            elif edicao == 4:
                                novaSenha = str(input("Nova senha: "))
                                cliente.senha = novaSenha

                    elif menuFunc == 3:
                        with db_session:
                            cliente = verificarCliente()
                            cliente.delete()
                            print("Cliente deletado com sucesso!")
                    
                    elif menuFunc == 4:
                        with db_session:
                            cliente = verificarCliente()
                            print(cliente)

                    elif menuFunc == 5:
                        nomePet = str(input("Nome: "))
                        especie = str(input("Espécie: "))
                        raca = str(input("Raça: "))
                        dtNasc = str(input("Data de nascimento: "))

                        with db_session:
                            Pet(nome=nomePet, especie=especie, raca=raca, dtNasc=dtNasc, dono=verificarCliente())
                            print("Pet cadastrado com sucesso!")

                    elif menuFunc == 6:
                        with db_session: 
                            pet = verificarPet()
                            print("1 - Editar nome")
                            print("2 - Editar espécie")
                            print("3 - Editar raça")
                            print("4 - Editar data de nascimento")
                            print("5 - Editar dono")

                            edicao = verificador(0,5)

                            if edicao == 1:
                                novoNome = str(input("Novo nome: "))
                                pet.nome = novoNome

                            elif edicao == 2:
                                novaEspecie = str(input("Novo espécie: "))
                                pet.especie = novaEspecie

                            elif edicao == 3:
                                novaRaca = str(input("Nova raça: "))
                                pet.raca = novaRaca

                            elif edicao == 4:
                                novaData = str(input("Nova data de nascimento: "))
                                pet.dtNasc = novaData

                            elif edicao == 5:
                                pet.dono = verificarCliente()
                    
                    elif menuFunc == 7:
                        nomePet = str(input("Nome do pet: "))

                        with db_session:
                            pet = verificarPet()
                            pet.delete()
                            print("Pet deletado com sucesso!")

                    elif menuFunc == 8:
                        with db_session:
                            print(verificarPet())

                    elif menuFunc == 9:
                        data = str(input("Data: "))
                        servico = str(input("Tipo de atendimento: "))

                        while True:
                            try:
                                valor = float(input("Valor: "))
                                break
                            except ValueError:
                                print("Valor inválido! Use ponto (.) para decimais")

                        with db_session:
                            Atendimento(pet=verificarPet(), funcionario=verificarFuncionario(), data=data, servico=servico, valor=valor)
                            print("Atendimento marcado com sucesso!")
                    
                    elif menuFunc == 10:
                        idAtend = int(input("Id do atendimento: "))

                        with db_session:
                            atendimento = Atendimento.get(id=idAtend)

                            if atendimento:
                                atendimento.delete()
                                print("Atendimento desmarcado!")
                            else:
                                print("Atendimento não cadastrado")

                    elif menuFunc == 11:
                        with db_session:
                            atendimentos = Atendimento.select()
                            for atendimento in atendimentos:
                                print(atendimento)

                    elif menuFunc == 12:
                        break

            else:
                while True:
                    print("=" * 40)
                    print("MENU FUNCIONÁRIO".center(40))
                    print("=" * 40)
                    print("1 - Marcar atendimento")
                    print("2 - Desmarcar atendimento")
                    print("3 - Ver atendimentos")
                    print("4 - Sair")
                    print("=" * 40)

                    menuFunc = verificador(0, 4)

                    if menuFunc == 1:
                        data = str(input("Data: "))
                        servico = str(input("Tipo de atendimento: "))

                        while True:
                            try:
                                valor = float(input("Valor: "))
                                break
                            except ValueError:
                                print("Valor inválido! Use ponto (.) para decimais")

                        with db_session:
                            Atendimento(pet=verificarPet(), funcionario=Funcionario.get(nome=nomeFuncionario), data=data, servico=servico, valor=valor)
                            print("Atendimento marcado com sucesso!")

                    elif menuFunc == 2:
                        idAtend = int(input("Id do atendimento: "))

                        with db_session:
                            atendimento = Atendimento.get(id=idAtend)

                            if atendimento.funcionario.nome == nomeFuncionario:
                                atendimento.delete()
                                print("Atendimento desmarcado!")
                            else:
                                print("Atendimento não encontrado")
                    
                    elif menuFunc == 3:
                        with db_session:
                            atendimentos = Atendimento.select()

                            for atendimento in atendimentos:
                                if atendimento.funcionario.nome == nomeFuncionario:
                                    print(atendimento)

                    elif menuFunc == 4:
                        break

    if menu == 2:
        nomeCliente = str(input("Nome: "))
        senhaCliente = str(input("Senha: "))

        if loginCliente(nomeCliente, senhaCliente) != False:
            while True:
                print("=" * 40)
                print("MENU CLIENTE".center(40))
                print("=" * 40)
                print("1 - Ver atendimentos")
                print("2 - Meus pets")
                print("3 - Sair")
                print("=" * 40)

                menuCliente = verificador(0, 3)

                if menuCliente == 1:
                    with db_session:
                        atendimentos = Atendimento.select()

                        for atendimento in atendimentos:
                            if atendimento.pet.dono.nome == nomeCliente:
                                print(atendimento)

                elif menuCliente == 2:
                    with db_session:
                        cliente = Cliente.get(nome=nomeCliente)
                        for pet in cliente.pets:
                            print(pet)

                elif menuCliente == 3:
                    break
                
    if menu == 3:
        break