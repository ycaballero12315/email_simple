from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Email(Base):

    __tablename__ = "emails"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    to = Column(String(500), nullable=False, comment="Destinatarios separados por coma")
    cc = Column(String(500), nullable=True, comment="Copia separados por coma")
    subject = Column(String(500), nullable=False, comment="Asunto del correo")
    body = Column(Text, nullable=False, comment="Contenido HTML del correo")
    
    def __repr__(self):
        return f"<Email(id={self.id}, subject='{self.subject}')>"