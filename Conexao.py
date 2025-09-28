from pony.orm import *

db = Database()
db.bind(provider='sqlite', filename='PetShop.db', create_db=True)

class Cliente(db.Entity):
    nome = Required(str)
    email = Required(str)
    telefone = Required(str)
    senha = Required(str)
    pets = Set("Pet")

    def __str__(self):
        return f"""Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Senha: {self.senha} 
Pets: {[pet.nome for pet in self.pets]}"""

class Pet(db.Entity):
    nome = Required(str)
    especie = Required(str)
    raca = Optional(str, nullable=True)
    dtNasc = Required(str)
    dono = Required(Cliente)
    atendimento = Set("Atendimento")
    
    def __str__(self):
        return f"Nome: {self.nome}, Raça: {self.raca}, Nascimento: {self.dtNasc}, Dono: {self.dono.nome}"

class Funcionario(db.Entity):
    nome = Required(str)
    email = Required(str)
    cargo = Required(str)
    senha = Required(str)
    atendimentos = Set("Atendimento")

class Atendimento(db.Entity):
    pet = Required(Pet)
    funcionario = Required(Funcionario)
    data = Required(str)
    servico = Required(str)
    valor = Required(float)

    def __str__(self):
        return f"ID: {self.id}, Pet: {self.pet.nome}, Funcionário: {self.funcionario.nome}, Data: {self.data}, Serviço: {self.servico}, Valor: R${self.valor}\n"

db.generate_mapping(create_tables=True)