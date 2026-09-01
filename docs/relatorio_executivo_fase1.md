# Relatório Executivo — Fase 1

## 1. Objetivo da Fase 1

Estruturar uma visão executiva para adoção de agentes de IA orientados a resultado de negócio, com foco em melhorar experiência do cliente, eficiência operacional, qualidade logística e capacidade de resposta sobre sinais vindos de reviews e retenção.

Esta fase prioriza análise estratégica, definição de oportunidades, desenho conceitual da solução e alinhamento com diretoria antes de qualquer implantação técnica.

## 2. Contexto de Negócio

O problema proposto indica um ambiente com pressão simultânea sobre:

- satisfação e experiência do cliente;
- desempenho logístico;
- volume de feedback em reviews;
- retenção de clientes;
- eficiência operacional.

Esse cenário normalmente aponta para empresas que já possuem dados relevantes, porém ainda não transformam esses dados em decisões rápidas, priorização confiável e ações coordenadas entre áreas.

## 3. Baseline Observado no Dataset Olist

O recorte disponível cobre compras entre setembro de 2016 e outubro de 2018 e permite validar parte relevante das hipóteses da Fase 1:

- 99.441 pedidos de 96.096 clientes únicos; 96.478 pedidos foram entregues (97,0%);
- 7.826 pedidos entregues chegaram após a data estimada (8,1% das entregas), com prazo médio de entrega de 12,6 dias;
- 14,7% dos reviews receberam nota 1 ou 2, enquanto 57,8% receberam nota 5;
- somente 41,3% dos reviews contêm comentário textual, o que limita a cobertura da análise semântica;
- 3,1% dos clientes únicos têm mais de um pedido observado, logo recompra é um proxy histórico e não uma medida de churn em tempo real.

O dataset não contém tracking de transportadoras, tickets, NPS, campanhas ou CRM. As conclusões devem, portanto, diferenciar o diagnóstico histórico suportado pela base de automações operacionais que dependerão de novas integrações.

## 4. Problema Central

O negócio provavelmente enfrenta uma combinação de cinco dores:

1. dificuldade de identificar rapidamente os fatores que mais impactam clientes;
2. baixa visibilidade sobre gargalos operacionais e logísticos;
3. uso reativo de reviews e reclamações, sem geração sistemática de causa-raiz;
4. dificuldade de antecipar risco de churn ou queda de recompra;
5. excesso de esforço manual para consolidar dados e apoiar decisões.

Em termos executivos, o problema não é apenas “falta de IA”, mas sim falta de uma camada inteligente de priorização, diagnóstico e apoio à ação.

## 5. Hipóteses de Oportunidade

Com o dataset do Brazilian Ecommerce disponível como base analítica do projeto, é possível formular hipóteses de alto valor a partir dos dados reais de clientes, pedidos, logística e reviews:

- clientes insatisfeitos podem estar concentrados em jornadas específicas;
- atrasos logísticos podem estar associados a regiões, transportadoras, categorias ou períodos;
- reviews podem conter sinais recorrentes que não aparecem em indicadores agregados;
- queda de retenção pode decorrer de experiências ruins logo nas primeiras interações;
- equipes operacionais e gerenciais podem gastar tempo excessivo consolidando informação antes de agir.

## 6. Análise Estratégica por Frente

### 6.1 Clientes

Questões-chave:

- quais perfis concentram maior valor e maior risco;
- quais jornadas geram maior fricção;
- quais segmentos apresentam maior reclamação, atraso ou cancelamento;
- quais grupos respondem melhor a ações corretivas.

Valor esperado:

- melhor priorização comercial e de atendimento;
- redução de perdas em contas relevantes;
- foco em segmentos com maior retorno.

### 6.2 Logística

Questões-chave:

- onde estão os principais atrasos;
- quais rotas, parceiros ou categorias mais falham;
- qual o impacto operacional e reputacional dessas falhas;
- quais desvios podem ser tratados de forma preditiva.

Valor esperado:

- redução de exceções;
- melhoria do SLA;
- menor custo de retrabalho e atendimento;
- ganho de previsibilidade operacional.

### 6.3 Reviews e Voz do Cliente

Questões-chave:

- quais temas aparecem com maior recorrência;
- quais problemas são mais críticos para percepção de valor;
- quais temas estão crescendo;
- quais problemas podem ser resolvidos com ação rápida entre áreas.

Valor esperado:

- leitura contínua de voz do cliente;
- redução do tempo entre problema percebido e resposta da empresa;
- melhoria de reputação e NPS.

### 6.4 Retenção

Questões-chave:

- quais sinais antecedem churn, queda de recompra ou abandono;
- quais jornadas geram erosão de confiança;
- quais intervenções têm maior probabilidade de retenção.

Valor esperado:

- priorização de ações de recuperação;
- melhor uso de orçamento de retenção;
- aumento de lifetime value.

### 6.5 Eficiência Operacional

Questões-chave:

- quanto esforço humano hoje é gasto para consolidar análises;
- quantas decisões ficam lentas por falta de diagnóstico;
- quais equipes dependem de relatórios manuais;
- quais processos podem ser apoiados por agentes especializados.

Valor esperado:

- redução de tempo analítico;
- aumento da velocidade de resposta;
- padronização de análises;
- maior capacidade de escala.

## 7. Benefícios Esperados

### Benefícios para o negócio

- melhor qualidade de decisão;
- priorização orientada a impacto;
- maior capacidade de resposta interáreas;
- redução de perdas por churn, atraso e experiência ruim.

### Benefícios para operação

- triagem automática de sinais;
- menor dependência de consolidação manual;
- alertas mais rápidos;
- padronização de diagnóstico.

### Benefícios para liderança

- visão executiva unificada;
- clareza sobre onde atuar primeiro;
- rastreabilidade de hipóteses, riscos e ganhos;
- base para investimento em Fase 2.

## 8. Usuários Impactados

### Diretoria e liderança

- usam a solução para priorização, governança e alocação de recursos.

### Operações e logística

- usam diagnósticos e alertas para atacar causas de atraso, erro ou exceção.

### CX, atendimento e sucesso do cliente

- usam leitura de reviews e sinais de insatisfação para resposta coordenada.

### Comercial, CRM e retenção

- usam insights para campanhas de retenção, reativação e foco em clientes de maior valor.

### Analytics e produto de dados

- usam a arquitetura proposta para evoluir métricas, monitoramento e automações futuras.

## 9. Riscos e Limitações

### Riscos de negócio

- priorizar casos de uso sem impacto mensurável;
- gerar confiança excessiva em recomendações ainda não validadas;
- baixa adesão se a solução não se integrar ao fluxo real das áreas.

### Riscos de dados

- ausência de padronização entre fontes;
- reviews sem qualidade suficiente para análise semântica robusta;
- histórico incompleto para retenção;
- granularidade insuficiente em eventos logísticos.
- ausência de fontes operacionais necessárias para alertas em tempo real;
- duplicidade potencial de `review_id` e `order_id` nos reviews;
- necessidade de usar `customer_unique_id`, e não `customer_id`, em análises de recompra.

### Riscos operacionais

- excesso de agentes sem clareza de dono e processo;
- falta de SLA para resposta humana;
- baixa governança de exceções.

### Riscos éticos e de governança

- enviesamento em priorização de clientes;
- decisões automatizadas sem supervisão adequada;
- uso inadequado de dados sensíveis;
- falta de trilha de auditoria.

## 10. Recomendações Executivas

1. começar por casos de uso com impacto claro e disponibilidade de dados;
2. definir indicadores de sucesso antes da implementação;
3. usar agentes como apoio à decisão, não substituição integral da governança humana;
4. garantir dono de negócio para cada agente;
5. evoluir por ondas: diagnóstico, piloto controlado e expansão.

## 11. Critérios de Priorização para a Fase 2

Os casos de uso devem ser priorizados segundo:

- impacto econômico potencial;
- urgência operacional;
- disponibilidade e qualidade de dados;
- simplicidade de integração ao processo atual;
- capacidade de medir resultado rapidamente.

## 12. Indicadores Executivos Recomendados

- taxa de atraso logístico;
- tempo médio de resolução de exceções;
- volume e severidade de reviews negativos;
- taxa de pedidos entregues após a data estimada;
- taxa de reviews com nota 1 ou 2;
- taxa de recompra por `customer_unique_id`;
- churn por segmento, quando houver base CRM longitudinal;
- tempo gasto em consolidação analítica;
- taxa de adoção das recomendações dos agentes.

## 13. Próximos Passos Imediatos

1. formalizar as métricas e chaves descritas no inventário de dados;
2. priorizar o diagnóstico de atraso e reviews negativos, já mensuráveis na base;
3. validar com as áreas as dores prioritárias e as ações possíveis;
4. selecionar um piloto de maior valor;
5. integrar tracking, atendimento e CRM antes de propor alertas operacionais ou retenção em tempo real.

## 14. Conclusão

A oportunidade da Fase 1 é criar base decisória para usar IA com foco real em negócio. O maior ganho esperado não é apenas automação, mas capacidade de transformar dados dispersos em priorização prática, resposta mais rápida e melhoria contínua da experiência do cliente e da operação.

Com o dataset completo disponível, este relatório passa a ter um baseline quantitativo para orientar o piloto. A validação do contexto operacional atual e a integração de fontes ausentes continuam necessárias antes de escalar recomendações para execução.
