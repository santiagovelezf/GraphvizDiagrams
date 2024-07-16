from graphviz import Digraph
from IPython.display import display, Image

# Crear un nuevo objeto Digraph
dot = Digraph(comment='Diagrama de flujo genérico')

# Configurar la dirección del gráfico de arriba a abajo
dot.attr(rankdir='TB')

# Configurar el estilo general de los nodos
dot.attr('node', shape='rectangle', style='rounded,filled', fillcolor='#E6F3FF', color='#4A90E2', fontname='Arial', fontcolor='#333333', fontsize='12', margin='0.2,0.1')

# Configurar el estilo general de los bordes
dot.attr('edge', fontname='Arial', fontsize='10', color='#4A90E2')

# Definir nodos con letras
dot.node('A', 'Inicio', shape='ellipse', fillcolor='#A6E6A6')
dot.node('B', 'Preparación de datos')
dot.node('C', 'Entrenamiento de modelo')
dot.node('D', 'Evaluación')
dot.node('E', '¿Modelo satisfactorio?', shape='diamond', fillcolor='#FFD700')
dot.node('F', 'Reentrenar modelo')
dot.node('G', 'Despliegue')
dot.node('H', 'Fin', shape='ellipse', fillcolor='#A6E6A6')

# Definir bordes (conexiones entre nodos)
dot.edge('A', 'B', 'Comienza')
dot.edge('B', 'C', 'Prepara datos')
dot.edge('C', 'D', 'Entrena modelo')
dot.edge('D', 'E', 'Evalúa resultados')
dot.edge('E', 'F', 'No', style='dotted')
dot.edge('E', 'G', 'Sí')
dot.edge('F', 'C', 'Mejorar modelo', style='dotted')
dot.edge('G', 'H', 'Despliega modelo')

# Generar el diagrama en formato PNG
dot.render('generic_workflow_diagram', format='png', cleanup=True)

# Generar el diagrama en formato PDF
dot.render('generic_workflow_diagram', format='pdf', cleanup=True)

# Mostrar el diagrama PNG
display(Image('generic_workflow_diagram.png'))

print("Se han generado los archivos 'generic_workflow_diagram.png' y 'generic_workflow_diagram.pdf'")