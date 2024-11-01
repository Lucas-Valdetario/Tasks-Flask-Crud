class Task:
    def __init__(self, id, title, description, completed=False) -> None: 
# completed recebe o atributo False para ficar em aberto e depois completar.
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
        
    def to_dict(self): # Método de retorno, que vai retornar o objeto em dicionário.
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }