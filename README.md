
# Documentação do Código da Aplicação
## Geral

Essa aplicação procura ser um sistema de gestão de tarefas domésticas que permite ao usuário definir um estado do ambiente (quantidade de pratos sujos, nível de sujeira, umidade das plantas, etc) e executar tarefas com base nas condições desses estados. O sistema usa agentes que são responsáveis por executar tarefas específicas, dependendo das condições definidas, onde os mesmos podem não executar a tarefa, dependendo da sua prioridade.

## Estrutura do Código

### 1. Variáveis Globais

```python
estado_ambiente = {
    'pratos_sujos': 15,
    'nivel_sujeira_chao': 3,
    'umidade_plantas': 2,
    'nivel_lixo': 4,
    'nivel_poeira': 3,
    'roupas_sujas': 12
}
```

- **Descrição**: Dicionário que mantém o estado atual do ambiente, incluindo a quantidade de pratos sujos, o nível de sujeira do chão, a umidade das plantas, e outros. Esses valores são setados manualmente, mas o usuário pode alterar o valor deles na interface.

### 2. Classe `Tarefa`

```python
class Tarefa:
    def __init__(self, nome, prioridade, condicao_func):
        ...
```

- **Descrição**: Representa uma tarefa que pode ser executada. Cada tarefa tem um nome, uma prioridade e uma função de condição que determina se a tarefa pode ser executada.

- **Métodos**:
  - `pode_executar()`: Verifica se a condição para executar a tarefa está satisfeita.
  - `executar()`: Tenta executar a tarefa e retorna uma mensagem de sucesso ou erro.

### 3. Classe `Agente`

```python
class Agente:
    def __init__(self, nome, tarefa):
        ...
```

- **Descrição**: Representa um agente responsável por executar uma tarefa específica.

- **Métodos**:
  - `agir()`: Executa a tarefa atribuída ao agente, chamando o método `executar()` da classe `Tarefa`.

### 4. Condições das Tarefas

As seguintes funções definem as condições sob as quais cada tarefa pode ser executada:

```python
def condicao_lavar_pratos():
    return estado_ambiente['pratos_sujos'] > 10

def condicao_varrer_chao():
    return estado_ambiente['nivel_sujeira_chao'] > 2

def condicao_regar_plantas():
    return estado_ambiente['umidade_plantas'] > 3

def condicao_esvaziar_lixo():
    return estado_ambiente['nivel_lixo'] > 3

def condicao_limpar_poeira():
    return estado_ambiente['nivel_poeira'] > 2

def condicao_lavar_roupas():
    return estado_ambiente['roupas_sujas'] > 10
```

- **Descrição**: Cada função retorna um valor booleano que determina se a tarefa associada pode ser executada com base no estado do ambiente.

### 5. Classe `SistemaGestaoTarefas`

```python
class SistemaGestaoTarefas:
    def __init__(self, agentes):
        ...
```

- **Descrição**: Gerencia a execução das tarefas, armazenando agentes e ajustando as prioridades das tarefas com base no estado do ambiente.

- **Métodos**:
  - `ajustar_prioridades()`: Ajusta as prioridades das tarefas com base nas condições do ambiente.
  - `executar_tarefas()`: Executa as tarefas de acordo com suas prioridades e condições.

### 6. Função Principal

```python
def criar_sistema_tarefas():
    ...
```

- **Descrição**: Cria as tarefas e agentes, associando cada agente a uma tarefa específica e retorna uma instância do sistema de gestão de tarefas.

### 7. Agentes e Tarefas

Abaixo estão os agentes e as tarefas associadas a cada um:

- **Agente 1**: "Agente 1" - Tarefa: "Lavar Pratos"
- **Agente 2**: "Agente 2" - Tarefa: "Varrer Chão"
- **Agente 3**: "Agente 3" - Tarefa: "Regar Plantas"
- **Agente 4**: "Agente 4" - Tarefa: "Esvaziar Lixo"
- **Agente 5**: "Agente 5" - Tarefa: "Limpar Poeira"
- **Agente 6**: "Agente 6" - Tarefa: "Lavar Roupas"
