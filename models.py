# importar bibliotecas
from sqlalchemy import create_engine, Column, Integer,  String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, declarative_base

# CONFUGURAR BASE DE DADOS / CRIANDO CONEXÃO ENTRE ELES


engine = create_engine('sqlite:///base_vet.sqlite3')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Animal(Base):
    __tablename__ = 'TAB_ANIMAL'
    id_animal = Column (Integer, primary_key=True)
    nome_animal = Column(nullable=False, index=True)
    raca1 = Column(nullable=False, index=True)
    anoNasci = Column(nullable=False, index= True)
    idCliente3 = Column(Integer, ForeignKey('TAB_CLIENTE.id_cliente'))
    cliente = relationship('Cliente')

    def __repr__(self):
        return 'Pessoa: {} {} {}'.format(self.nome_animal, self.raca1, self.anoNasci)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def __delete__(self, instance):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_user = {
            "Nome do animal": self.nome_animal,
            "Raça": self.raca1,
            "Ano de nascimento": self.anoNasci,
        }
        return dados_user

class Cliente(Base):
    __tablename__ = 'TAB_CLIENTE'
    id_cliente = Column(Integer, primary_key=True)
    CPF = Column(String(11), nullable=False, index=True, unique=True)
    Nome1 = Column(String(40), nullable=False, index=True)
    telefone = Column(String(11), nullable=False, index=True)
    Profissão2 = Column(String(40), nullable=False, index= True)
    Area2 = Column(String(40), nullable=False, index=True)

    def __repr__(self):
        return '<Atividade: {}'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self, instance):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_atividade = {
            "id_atividade": self.id,
            "pessoa_id": self.pessoa_id,
            "nome": self.nome,
        }
        return dados_atividade

class Consulta(Base):
    __tablename__ = 'TAB_CONSULTA'
    idConsulta = Column(Integer, primary_key=True)
    motivo_id2 = Column( nullable=False, index=True, unique=True)
    hora = Column(nullable=False, index=True)
    minuto = Column(nullable=False, index=True)
    data1 = Column(nullable=False, index= True)
    valor = Column(nullable=False, index=True)
    idAnimal2 = Column(Integer, ForeignKey('TAB_ANIMAL.id_animal'))
    animal = relationship('Animal')
    idVeterinario = Column(Integer, ForeignKey('TAB_VETERINARIO.id_vet'))
    veterinario = relationship('Veterinario')

    def __repr__(self):
        return '<Consulta: {}'.format(self.idConsulta)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self, instance):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_consulta = {
            "idConsulta": self.idConsulta,
            "motivo_id2": self.motivo_id2,
            "hora": self.hora,
            "minuto": self.minuto,
            "data1'": self.data1,
            "idAnimal2": self.idAnimal2,
            "idVeterinario": self.idVeterinario,
        }
        return dados_consulta
class Motivo(Base):
    __tablename__ = 'TAB_MOTIVO'
    id_motivo = Column(Integer, primary_key=True)
    nome_motivo = Column( nullable=False, index=True)
    motivo_categoria = Column(nullable=False, index=True)
    valor_motivo = Column(nullable=False, index=True)

    def __repr__(self):
        return '<Motivo: {}'.format(self.nome_motivo)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self, instance):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_motivo = {
            "id_motivo": self.id_motivo,
            "nome_motivo": self.nome_motivo,
            "motivo_categoria": self.motivo_categoria,
            "valor_motivo": self.valor_motivo,
        }
        return dados_motivo

class Veterinario(Base):
    __tablename__ = 'TAB_VETERINARIO'
    id_vet = Column(Integer, primary_key=True)
    salario2 = Column( nullable=False, index=True)
    nomeVet = Column(nullable=False, index=True)
    crmv = Column(nullable=False, index=True, unique=True)
    v_consulta1 = Column(nullable=False, index=True)

    def __repr__(self):
        return '<Veterinario: {}'.format(self.crmv)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self, instance):
        db_session.delete(self)
        db_session.commit()

    def serialize_user(self):
        dados_veterinario = {
            "id_vet": self.id_vet,
            "salario2": self.salario2,
            "nomeVet": self.nomeVet,
            "crmv": self.crmv,
            "v_consulta1'": self.v_consulta1,
        }
        return dados_veterinario

def init_db():
    Base.metadata.create_all(bind=engine)

# Executar dentro do arquivo principal(só ele executa)
if __name__ == '__main__':
    init_db()

