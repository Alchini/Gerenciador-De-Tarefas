import random

estado_ambiente = {
    'pratos_sujos': 15,       # Quantidade de pratos sujos
    'nivel_sujeira_chao': 3,  # Nível de sujeira do chão (0 - Limpo, 5 - Muito sujo)
    'umidade_plantas': 2,     # Nível de umidade das plantas (0 - Molhadas, 5 - Secas)
    'nivel_lixo': 4,          # Quantidade de lixo (0 - Vazio, 5 - Cheio)
    'nivel_poeira': 3,        # Nível de poeira na casa (0 - Sem poeira, 5 - Muito empoeirado)
    'roupas_sujas': 12        # Quantidade de roupas sujas
}

# Definição de uma Tarefa
class Tarefa:
    def __init__(self, nome, prioridade, condicao_func):
        self.nome = nome
        self.prioridade = prioridade
        self.condicao_func = condicao_func
        self.concluida = False

#Verifica se a condição para executar a tarefa bate com as regras definidas.
    def pode_executar(self):
        return self.condicao_func()

    def executar(self):
        if self.pode_executar():
            self.concluida = True
            return f"Tarefa {self.nome} concluída."
        else:
            return f"Não é possível executar {self.nome} agora."

# Definição de um Agente
class Agente:
    def __init__(self, nome, tarefa):
        self.nome = nome
        self.tarefa = tarefa

    def agir(self):
        return self.tarefa.executar()

# Regras baseadas no estado do ambiente, caso os valores inseridos pelo usuário sejam menores, a tarefa não será executada.
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

# Criando o Sistema de Regras para Gerenciar Tarefas
class SistemaGestaoTarefas:
    def __init__(self, agentes):
        self.agentes = agentes

    def ajustar_prioridades(self):
        """Ajusta as prioridades das tarefas com base no estado do ambiente."""
        for agente in self.agentes:
            if agente.tarefa.nome == "Lavar Pratos":
                agente.tarefa.prioridade = 5 if estado_ambiente['pratos_sujos'] > 10 else 3

            elif agente.tarefa.nome == "Varrer Chão":
                agente.tarefa.prioridade = 4 if estado_ambiente['nivel_sujeira_chao'] > 2 else 2

            elif agente.tarefa.nome == "Regar Plantas":
                agente.tarefa.prioridade = 3 if estado_ambiente['umidade_plantas'] > 3 else 1

            elif agente.tarefa.nome == "Esvaziar Lixo":
                agente.tarefa.prioridade = 4 if estado_ambiente['nivel_lixo'] > 3 else 2

            elif agente.tarefa.nome == "Limpar Poeira":
                agente.tarefa.prioridade = 3 if estado_ambiente['nivel_poeira'] > 2 else 1

            elif agente.tarefa.nome == "Lavar Roupas":
                agente.tarefa.prioridade = 5 if estado_ambiente['roupas_sujas'] > 10 else 2

    def executar_tarefas(self):
        """Executa as tarefas de acordo com suas prioridades e condições."""
        # Ajusta as prioridades antes de ordenar
        self.ajustar_prioridades()

        # Ordena os agentes pela prioridade de suas tarefas
        self.agentes.sort(key=lambda agente: agente.tarefa.prioridade, reverse=True)

        # Percorre os agentes e tenta executar as tarefas
        resultados = []
        for agente in self.agentes:
            resultado = agente.agir()
            resultados.append(resultado)
        return resultados

# Função principal
def criar_sistema_tarefas():
    # Criando as tarefas com suas respectivas condições e prioridades
    lavar_pratos = Tarefa("Lavar Pratos", prioridade=3, condicao_func=condicao_lavar_pratos)
    varrer_chao = Tarefa("Varrer Chão", prioridade=2, condicao_func=condicao_varrer_chao)
    regar_plantas = Tarefa("Regar Plantas", prioridade=1, condicao_func=condicao_regar_plantas)
    esvaziar_lixo = Tarefa("Esvaziar Lixo", prioridade=2, condicao_func=condicao_esvaziar_lixo)
    limpar_poeira = Tarefa("Limpar Poeira", prioridade=1, condicao_func=condicao_limpar_poeira)
    lavar_roupas = Tarefa("Lavar Roupas", prioridade=2, condicao_func=condicao_lavar_roupas)

    # Criando agentes para cada tarefa
    agente1 = Agente("Agente 1", lavar_pratos)
    agente2 = Agente("Agente 2", varrer_chao)
    agente3 = Agente("Agente 3", regar_plantas)
    agente4 = Agente("Agente 4", esvaziar_lixo)
    agente5 = Agente("Agente 5", limpar_poeira)
    agente6 = Agente("Agente 6", lavar_roupas)

    # Retornando o sistema de gestão de tarefas
    return SistemaGestaoTarefas([agente1, agente2, agente3, agente4, agente5, agente6])

if __name__ == "__main__":
    sistema = criar_sistema_tarefas()
    resultados = sistema.executar_tarefas()
    for resultado in resultados:
        print(resultado)
