# Listar algoritmos de caja herramientas
alg_list = QgsApplication.processingRegistry().algorithms()

word = 'buffer'

for alg in alg_list:
    if word in alg.name() or word in alg.displayName():
        alg_info = f"{alg.provider().name()}: {alg.name()}--> {alg.displayName()}"
        print(alg_info)