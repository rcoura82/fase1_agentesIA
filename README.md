# fase1_agentesIA

Entregáveis da Fase 1 para análise estratégica, planejamento executivo e desenho inicial de uma solução com agentes de IA aplicada ao Brazilian Ecommerce Dataset by Olist.

## Estrutura

- `/home/runner/work/fase1_agentesIA/fase1_agentesIA/data/` — arquivos canônicos do dataset Brazilian Ecommerce (Olist)
- `/home/runner/work/fase1_agentesIA/fase1_agentesIA/data/README.md` — inventário, relacionamentos e limitações dos dados
- `/home/runner/work/fase1_agentesIA/fase1_agentesIA/docs/relatorio_executivo_fase1.md`
- `/home/runner/work/fase1_agentesIA/fase1_agentesIA/docs/mapa_agentes_ia.md`
- `/home/runner/work/fase1_agentesIA/fase1_agentesIA/docs/arquitetura_conceitual_inicial.md`
- `/home/runner/work/fase1_agentesIA/fase1_agentesIA/docs/prompts_iniciais_agentes.md`
- `/home/runner/work/fase1_agentesIA/fase1_agentesIA/docs/roteiro_video_executivo.md`

## Dataset disponível

O projeto já contém os nove arquivos CSV do dataset, referentes a compras realizadas de setembro de 2016 a outubro de 2018. A base cobre pedidos, clientes, itens, pagamentos, reviews, produtos, vendedores, geolocalização e tradução de categorias.

Os arquivos usados nas análises devem ser lidos da pasta `data/`. A documentação executiva foi atualizada com o baseline observado: 99.441 pedidos, 96.478 entregas, 7.826 entregas após a data estimada e 99.224 registros de review.

## Limites de uso

O dataset é histórico e não contém eventos de tracking, tickets de atendimento, NPS, campanhas ou interações de CRM. Portanto, ele sustenta diagnóstico, priorização e protótipos analíticos; agentes operacionais em tempo real exigirão integração com essas fontes adicionais.