# Importando as bibliotecas necessárias do SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

# Conectar ao SQLite em memória
# Criando uma instância do SQLAlchemy Engine para se conectar ao banco de dados SQLite em memória
engine = create_engine('sqlite:///meudb.db', echo=True)

# Criando uma classe base para todas as classes de mapeamento ORM
Base = declarative_base()

# Criando uma classe de mapeamento ORM para a tabela de usuários
class Usuario(Base):
    # Definindo o nome da tabela no banco de dados
    __tablename__ = 'usuarios'

    # Definindo as colunas da tabela
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    senha = Column(String)

# Criando todas as tabelas definidas nas classes de mapeamento no banco de dados
Base.metadata.create_all(engine)

# Abrindo uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()
# Criando um novo usuário
novo_usuario = Usuario(nome='Alice', idade=25, senha='123456')
# Adicionando o novo usuário à sessão
session.add(novo_usuario)
# Commitando a sessão para salvar as alterações no banco de dados
session.commit()

print("usuario criado com sucesso!")

# consultando os dados
# consultando apenas a primeira linha da tabela de usuários
usuario = session.query(Usuario).first()
print(usuario.nome, usuario.idade, usuario.senha)

# consultando todos os usuários
usuarios = session.query(Usuario).all()
print(usuario.nome, usuario.idade, usuario.senha)

# consultando com filtro
usuarios = session.query(Usuario).filter(Usuario.idade > 20).all()
print(usuario.nome, usuario.idade, usuario.senha)
