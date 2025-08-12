import plotly.graph_objects as go
# Importa a biblioteca Plotly para gráficos, especificamente o módulo 'graph_objects' que permite criar gráficos detalhados.

# Rótulos dos nós
labels = [
    'Receita Líquida',     # 0  -> nome do nó 0
    'Lucro Bruto',         # 1  -> nome do nó 1
    'Lucro Operacional',   # 2  -> nome do nó 2
    'Lucro Líquido'        # 3  -> nome do nó 3
]

# Fluxos entre os nós
sources = [0, 1, 2, 3]  # de onde vem cada fluxo, índice do nó de origem
targets = [1, 2, 3, 4]  # para onde vai cada fluxo, índice do nó de destino
values  = [1000, 100, 50, 20]  # valor (quantidade) do fluxo entre os nós

# Cores personalizadas para os nós
node_colors = ['#40531A','#40531A', '#40531A','#40531A', '#40531A']
# Define a cor de cada nó no gráfico (no caso, todas com mesma cor verde escuro)

# Cores personalizadas para os links (com transparência)
link_colors = [
    '#C7D59F',   # Receita → Bruto
    '#C7D59F',   # Bruto → Operacional
    '#C7D59F',   # Operacional → Líquido
    '#C7D59F'    # Lucro Líquido (nota: aqui o target é 4 que não existe na lista de labels)
]

# Criação do Sankey
fig = go.Figure(data=[go.Sankey(
    arrangement="snap",  # Mantém os nós alinhados automaticamente, evita sobreposição
    node=dict(
        pad=10,             # Espaçamento interno entre nós
        thickness=20,       # Espessura dos nós
        line=dict(color="gray", width=1), # Contorno dos nós: cor cinza e largura 1px
        label=labels,       # Usa a lista de labels para nomear os nós
        color=node_colors,  # Aplica as cores definidas para os nós
        hoverlabel=dict(    # Configuração do estilo da label ao passar o mouse sobre os nós
            bgcolor="white",   # Fundo branco da tooltip
            font_size=14,      # Tamanho da fonte na tooltip
            font_family="Helvetica"  # Fonte Helvetica na tooltip
        )
    ),
    link=dict(
        source=sources,     # Define o nó origem de cada link
        target=targets,     # Define o nó destino de cada link
        value=values,       # Define o valor (largura) do link
        color=link_colors,  # Aplica cores personalizadas para cada link
        hoverlabel=dict(    # Estilo da tooltip ao passar o mouse nos links
            bgcolor="lightgray", # Fundo cinza claro na tooltip
            font_size=13,        # Tamanho da fonte da tooltip
            font_family="Helvetica"  # Fonte Helvetica para tooltip
        )
    )
)])

# Layout geral
fig.update_layout(
    title_text=" 🩴 Resultado Alpargatas (ALPA4) 2024", # Título do gráfico que aparecerá acima do Sankey
    font=dict(
        family="Helvetica",   # Fonte usada no título e textos do gráfico
        size=20,              # Tamanho da fonte principal do gráfico
        color='rgba(189,224,81,255)' # Cor da fonte em formato RGBA (verde claro)
    ),
    margin=dict(l=50, r=50, t=80, b=50),  # Espaço das margens (left, right, top, bottom)
    paper_bgcolor='rgba(31,31,31,255)',   # Cor de fundo da área total do gráfico (fundo da página do gráfico)
    plot_bgcolor='rgba(31,31,31,255)'     # Cor de fundo da área interna do gráfico (área onde os nós e links ficam)
)

fig.show()
# Exibe o gráfico gerado interativo em uma janela/jupyter notebook/ambiente suportado.
