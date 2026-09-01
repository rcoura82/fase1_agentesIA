# Mapa Inicial de Agentes de IA

## Visão Geral

Os agentes abaixo foram desenhados para resolver dores centrais do enunciado e atuar como apoio operacional e analítico, sempre com supervisão humana.

## Agente 1 — Analista de Voz do Cliente

**Objetivo**  
Transformar notas e comentários de reviews em temas priorizados, causas prováveis e alertas analíticos.

**Problema que resolve**  
A empresa recebe sinais dispersos de insatisfação, mas não converte esse volume em diagnóstico estruturado e priorização rápida.

**Usuários principais**  
CX, atendimento, produto, operações e liderança.

**Benefício esperado**  

- identificação rápida de temas críticos;
- redução de leitura manual;
- melhora na resposta ao cliente;
- apoio à priorização interáreas.

**Dependências de dados**  
reviews e notas por pedido. Tickets, NPS, pesquisas e histórico de interações precisam ser integrados para ampliar a cobertura.

## Agente 2 — Orquestrador de Exceções Logísticas

**Objetivo**  
Analisar o ciclo histórico dos pedidos, identificar desvios de prazo e recomendar prioridades de investigação.

**Problema que resolve**  
Falhas logísticas costumam ser detectadas tarde, com reação manual e baixa visibilidade de causa-raiz.

**Usuários principais**  
operações, logística, atendimento e gestores de SLA.

**Benefício esperado**  

- resposta mais rápida a atrasos;
- menor retrabalho;
- priorização de exceções críticas;
- aumento de previsibilidade.

**Dependências de dados**  
pedidos, datas de entrega estimada e realizada, itens, vendedores e localização. Tracking, transportadoras, devoluções e contatos de suporte não estão disponíveis na base atual.

## Agente 3 — Guardião de Retenção e Churn

**Objetivo**  
Identificar perfis com baixa recompra observada e experiências negativas, gerando hipóteses para retenção.

**Problema que resolve**  
Perdas de clientes são percebidas tarde, quando o custo de recuperação já é maior ou a reversão se torna improvável.

**Usuários principais**  
CRM, comercial, sucesso do cliente e liderança de receita.

**Benefício esperado**  

- atuação proativa em contas de risco;
- melhor alocação de incentivos;
- aumento de retenção e lifetime value.

**Dependências de dados**  
histórico transacional, frequência de compra e reviews. Engajamento, atendimento e campanhas exigem fontes externas; `customer_unique_id` é a chave para a frequência de compra.

## Agente 4 — Copiloto Executivo de Eficiência

**Objetivo**  
Consolidar sinais dos demais agentes em uma visão executiva com prioridades, impacto potencial, riscos e recomendações.

**Problema que resolve**  
A liderança precisa decidir rápido, mas normalmente recebe análises fragmentadas por área.

**Usuários principais**  
diretoria, gerência e PMO de transformação.

**Benefício esperado**  

- visão integrada para decisão;
- alinhamento entre áreas;
- melhor governança;
- clareza sobre impacto e trade-offs.

**Dependências de dados**  
saídas dos demais agentes, KPIs executivos e metas operacionais.

## Priorização Recomendada

### Onda 1 — dados já disponíveis

- Analista de Voz do Cliente
- Orquestrador de Exceções Logísticas

### Onda 2 — após validação do proxy histórico

- Guardião de Retenção e Churn

### Onda 3 — após integração das saídas e metas

- Copiloto Executivo de Eficiência

## Critérios de Sucesso

- uso recorrente pelas áreas;
- redução de tempo entre sinal e ação;
- melhoria dos indicadores-alvo;
- confiança nas recomendações;
- qualidade de governança e rastreabilidade.
- cobertura e qualidade das fontes necessárias para cada recomendação.
