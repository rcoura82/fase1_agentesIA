# Transcrição — Vídeo Executivo da Fase 2

Texto da narração do vídeo, dividido pelos slides para facilitar a gravação. Os títulos entre colchetes são referências visuais e não precisam ser narrados.

## Slide 1 — Da oportunidade à operação

Olá. Este vídeo apresenta a evolução do projeto de agentes de inteligência artificial, da visão estratégica da Fase 1 até os casos de uso operacionais da Fase 2. A proposta não é começar pela tecnologia, mas por problemas concretos da experiência do cliente, da logística e da retenção. O relatório agora detalha três agentes, como eles operam, quais dados precisam, quais decisões exigem pessoas e como medir os resultados. Ao final, apresentamos uma proposta de piloto para validação executiva.

## Slide 2 — Atraso e insatisfação caminham juntos

A base Olist contém quase cem mil pedidos. Cruzamos pedidos entregues com um review por pedido: noventa e cinco mil oitocentos e vinte e quatro registros. No prazo, nove vírgula dois por cento receberam nota um ou dois. Com atraso, cinquenta e quatro vírgula um por cento. A nota média cai de quatro vírgula vinte e nove para dois vírgula cinquenta e sete. É uma associação forte, que justifica priorizar logística e resposta ao cliente, mas não prova causalidade.

## Slide 3 — Agente de Voz do Cliente

O primeiro agente, Voz do Cliente, é acionado por um novo review. Cruza nota e comentário com prazo, produto e vendedor para classificar temas como atraso ou defeito. A ausência de texto não é interpretada como satisfação. Reviews críticos geram resumo e alerta; o atendimento humano valida e contata o cliente. Os resultados alimentam um painel de temas. Indicadores: avaliações negativas, tempo de resposta, nota por categoria e, quando disponíveis, satisfação e NPS.

## Slide 4 — Agente de Exceções Logísticas

O agente de Exceções Logísticas monitora pedidos perto do limite de envio e entregas fora do prazo. Com pedidos, itens, vendedores e localização, prioriza exceções por rota, região, categoria e impacto. Pode sugerir comunicação ao cliente; casos críticos exigem aprovação do analista, que aciona seller ou transportadora. Como a base não possui tracking em tempo real nem identifica a transportadora, causas são hipóteses a validar. A meta é reduzir atrasos e tempo de resolução.

## Slide 5 — Agente de Retenção e Churn

O agente de Retenção apoia CRM e comercial com segmentos de baixa recompra e experiência ruim. Usa o histórico de pedidos, pagamentos e reviews para sugerir ações. Mas a recompra observada é cerca de três vírgula um por cento tanto para clientes com nota baixa na primeira compra quanto para os demais. A base não demonstra relação entre nota e recompra, portanto não permite prever churn individual. Até integrar CRM, engajamento e uma janela adequada, o agente gera hipóteses para avaliação humana e testes controlados.

## Slide 6 — Como os agentes operam

As jornadas mostram gatilhos, entradas, decisões e saídas. Em reviews, a classificação define se há escalonamento. Na logística, risco e impacto definem a prioridade e os casos críticos passam por aprovação. Na retenção, o CRM decide sobre a campanha sugerida. As saídas alimentam painéis e medição de resultados. Os prompts instruem os agentes a separar fatos, hipóteses e recomendações, declarar dados ausentes e não inventar informações. A IA acelera a triagem sem retirar a responsabilidade das equipes.

## Slide 7 — Piloto e decisão

Recomendamos um piloto controlado de Voz do Cliente e Exceções Logísticas, com os dados disponíveis. Antes, as áreas definem a linha de base e metas, como tempo de triagem e resolução de atrasos. A Onda 2 integra retenção ao CRM; a Onda 3 consolida os sinais no Copiloto Executivo. Governança exige trilha de auditoria, responsáveis e aprovação humana nos casos críticos. A decisão solicitada é validar os casos da Onda 1, seus responsáveis e critérios de sucesso. Assim, a oportunidade vira um investimento incremental, mensurável e supervisionado. Obrigado.
