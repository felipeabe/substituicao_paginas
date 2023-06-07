from random import randint
import time
numero_quadros=int(input("Número de quadros: "))
paginas=int(input('Paginas distintas: '))

class AlgoritimoSubstitucao():
    def __init__(self):
        self.__ordem = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
        self.__linhas = numero_quadros

    @property
    def ordem(self):
        return self.__ordem

    @property
    def linhas(self):
        return self.__linhas

    def print_menu(self):
        print("Escolha o algoritimo de substituição:")
        print("1 - LRU")
        print("2 - CLOCK")
        print("3 - LFU")
        print("4 - FIFO ")
        print("0 - Encerrar")
        opcao = int(input("Opcao: "))
        return opcao

    def main_menu(self):
        switcher = {0: self.encerrar,
                    1: self.lru,
                    2: self.clock,
                    3: self.lfu,
                    4: self.fifo}

        while True:
            opcao = self.print_menu()
            funcao_selecionada = switcher[opcao]
            funcao_selecionada()

    def encerrar(self):
        exit(0)

    def lru(self):
        print("Ordem de acesso: ", end="")
        print(", ".join([str(int) for int in self.ordem]))

        miss_compulsoria = 0
        miss_capacidade = 0
        hit = 0
        indicador = 0
        substituidos = []
        cache = [None] * self.linhas
        temporizador = []

        for mem in self.ordem:
            if mem in cache:
                hit += 1
                indicador = cache.index(mem)
                temporizador[indicador] = 0

            else:
                if mem in substituidos:
                    indicador = temporizador.index(max(temporizador))
                    substituidos.append(cache[indicador])
                    cache[indicador] = mem
                    temporizador[indicador] = 0
                    miss_capacidade += 1
                else:
                    if None in cache:
                        cache[indicador] = mem
                        temporizador.append(0)
                        indicador += 1
                        miss_compulsoria += 1
                    else:
                        indicador = temporizador.index(max(temporizador))
                        substituidos.append(cache[indicador])
                        cache[indicador] = mem
                        temporizador[indicador] = 0
                        miss_compulsoria += 1

            for tempo in range(len(temporizador)):
                temporizador[tempo] += 1

        print(f"Cache {', '.join([str(int) for int in cache])}")
        print(f"HIT {hit}")
        print(f"MISS compulsoria {miss_compulsoria}")
        print(f"MISS capacidade {miss_capacidade}")
        print(f"{len(substituidos)} Substituições")

    def lfu(self):
        print("Ordem de ordem: ", end="")
        print(", ".join([str(int) for int in self.ordem]))

        miss_compulsoria = 0
        miss_capacidade = 0
        hit = 0
        indicador = 0
        substituidos = []
        cache = [None] * self.linhas
        contadores = []

        for mem in self.ordem:
            if mem in cache:
                hit += 1
                indicador = cache.index(mem)
                contadores[indicador] += 1
            else:
                if mem in substituidos:
                    substituidos.append(cache[indicador])
                    cache[indicador] = mem
                    indicador += 1
                    miss_capacidade += 1
                else:
                    if None in cache:
                        cache[indicador] = mem
                        contadores.append(1)
                        indicador += 1
                        miss_compulsoria += 1
                    else:
                        indicador = contadores.index(min(contadores))
                        substituidos.append(cache[indicador])
                        cache[indicador] = mem
                        indicador += 1
                        miss_compulsoria += 1
            if indicador > self.linhas - 1:
                indicador = 0

        print(f"Cache {', '.join([str(int) for int in cache])}")
        print(f"HIT {hit}")
        print(f"MISS compulsoria {miss_compulsoria}")
        print(f"MISS capacidade {miss_capacidade}")
        print(f"{len(substituidos)} Substituições")

    def fifo(self):
        start_time = time.time()
        #print("Ordem de ordem: ", end="")
        #print(", ".join([str(int) for int in self.ordem]))

        miss_compulsoria = 0
        miss_capacidade = 0
        hit = 0
        indicador = 0
        substituidos = []
        cache = [None] * self.linhas

        for mem in self.ordem:
            if mem in cache:
                hit += 1
            else:
                if mem in substituidos:
                    substituidos.append(cache[indicador])
                    cache[indicador] = mem
                    indicador += 1
                    miss_capacidade += 1
                else:
                    if None in cache:
                        cache[indicador] = mem
                        indicador += 1
                        miss_compulsoria += 1
                    else:
                        substituidos.append(cache[indicador])
                        cache[indicador] = mem
                        indicador += 1
                        miss_compulsoria += 1
            if indicador > self.linhas - 1:
                indicador = 0

        print(f"Cache {', '.join([str(int) for int in cache])}")
        print(f"HIT {hit}")
        print(f"MISS compulsoria {miss_compulsoria}")
        print(f"MISS capacidade {miss_capacidade}")
        print(f"{len(substituidos)} Substituições")
        end_time = time.time()  # Mede o tempo de final da função
        execution_time = end_time - start_time  # Calcula o tempo de execução

        print(f"Tempo de execução: {execution_time} segundos")
    
    def clock(self):
        miss_compulsoria = 0
        miss_capacidade = 0
        hit = 0
        indicador = 0
        substituidos = []
        indices_cache = [0] * 4
        cache = [None] * 4

        for mem in [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]:
            print('indicador: ', indicador, 'Add: ', mem)
            print(cache)
            print('-------')
            print(indices_cache)
            print('==============')
            if mem in cache:
                hit += 1
                indices_cache[cache.index(mem)] = 1
            else:
                if None in cache:
                    indicador_cache = cache.index(None)
                    cache[indicador_cache] = mem
                    indices_cache[indicador_cache] = 1
                    miss_compulsoria += 1
                    indicador = (indicador + 1) % len(cache)
                else:
                    while True:
                        if indices_cache[indicador] == 0:
                            substituidos.append(cache[indicador])
                            cache[indicador] = mem
                            indices_cache[indicador] = 1
                            miss_capacidade += 1
                            indicador = (indicador + 1) % len(cache)
                            break
                        else:
                            indices_cache[indicador] = 0
                            indicador = (indicador + 1) % len(cache)

        print(f"Cache {', '.join([str(int) for int in cache])}")
        print(f"HIT {hit}")
        print(f"MISS compulsoria {miss_compulsoria}")
        print(f"MISS capacidade {miss_capacidade}")
        print(f"{len(substituidos)} Substituições")






if __name__ == "__main__":
    AlgoritimoSubstitucao().main_menu()
