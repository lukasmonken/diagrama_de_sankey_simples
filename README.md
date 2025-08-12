Gráfico Sankey - Resultado Alpargatas (ALPA4) 2024
Este repositório contém um script em Python que gera um gráfico Sankey para ilustrar o fluxo financeiro simplificado da empresa Alpargatas (ALPA4) referente ao ano de 2024.

Descrição
O gráfico Sankey é uma forma visual de mostrar a distribuição e o fluxo entre diferentes etapas financeiras, neste caso:

Receita Líquida

Lucro Bruto

Lucro Operacional

Lucro Líquido

O script utiliza a biblioteca Plotly para criar um gráfico interativo, com personalização de cores, layout e tooltips para facilitar a compreensão dos dados.

Funcionalidades
Visualização clara do fluxo financeiro entre etapas da demonstração de resultados.

Personalização das cores dos nós e fluxos.

Layout ajustado para evitar sobreposição e melhorar a legibilidade.

Tooltips com informações detalhadas ao passar o mouse sobre os elementos.

Como usar
Certifique-se de ter o Python instalado (recomenda-se Python 3.7+).

Instale a biblioteca Plotly, caso ainda não tenha:

bash
Copiar
Editar
pip install plotly
Execute o script:

bash
Copiar
Editar
python seu_script.py
O gráfico interativo será exibido em seu navegador padrão ou no ambiente Jupyter Notebook.

Código principal
O script define os nós e fluxos do Sankey, as cores dos elementos e configura o layout para melhor visualização, exibindo o resultado final com a função fig.show().

Observações
O índice do nó destino 4 no último fluxo está fora da lista de labels (que vão de 0 a 3), o que pode gerar erro ou comportamento inesperado. Ajuste os índices conforme necessário para seu caso.
