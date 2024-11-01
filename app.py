from flask import Flask
# __name__ = "__main__"
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello_world"

@app.route("/about")
def about():
    return "Página sobre"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
from models.task import Task
# __name__ = "__main__"
app = Flask(__name__)

# CRUD 
# Create, Read, Update and Delete

tasks = []                              # Minhas tarefas vão ser armazenadas aqui dentro.
task_id_control = 1                     # Identificador
@app.route('/tasks', methods=['POST'])
def create_task():                      # Função para criar a atividade
    global task_id_control              # Global parar pegar a referência que está fora do método
    data = request.get_json()           # Receber informações que o cliente inserir.
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message":"Nova tarefa criada com sucesso"})            #Aqui vai me retornar a mensagem em json

@app.route('/tasks', methods=['GET'])
def get_tasks():                            # Função para retornar todas as minhas atividades.
    task_list = [task.to_dict() for task in tasks]      # Nessa parte o comando for vai me retornar tudo no comando to_dict para trazer em dicionário
        
    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET']) # Função para retornar uma tarefa. # Parâmetro de rotas, convertendo "id" para int.
def get_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
        
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=['PUT'])              # Método Update
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)        
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>', methods=['DELETE'])       # Método DELETE
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t                # Caso a lista de tarefas fosse grande, após achar o id que queriamos podemos
            break                   # usar o comando break para interromper a busca para não forçar o servidor
    
    if not task:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)

