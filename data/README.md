# Inventário de Dados — Olist

## Arquivos canônicos

| Arquivo | Linhas | Uso principal |
|---|---:|---|
| `olist_customers_dataset.csv` | 99.441 | localização do cliente e chave longitudinal |
| `olist_orders_dataset.csv` | 99.441 | ciclo e status do pedido |
| `olist_order_items_dataset.csv` | 112.650 | itens, preços, frete e vendedor |
| `olist_order_payments_dataset.csv` | 103.886 | forma, parcelas e valor do pagamento |
| `olist_order_reviews_dataset.csv` | 99.224 | nota e texto de avaliação |
| `olist_products_dataset.csv` | 32.951 | categoria e atributos físicos do produto |
| `olist_sellers_dataset.csv` | 3.095 | localização do vendedor |
| `olist_geolocation_dataset.csv` | 1.000.163 | coordenadas por CEP |
| `product_category_name_translation.csv` | 71 | tradução de categorias |

## Relacionamentos e grão

- Use `order_id` para relacionar pedidos, itens, pagamentos e reviews.
- Use `customer_id` para relacionar pedidos ao cadastro; use `customer_unique_id` para análises longitudinais de recompra.
- Relacione itens a produtos por `product_id` e a vendedores por `seller_id`.
- A geolocalização deve ser agregada por `geolocation_zip_code_prefix` antes do uso, pois há múltiplas coordenadas para o mesmo CEP.

## Qualidade e limitações

- O recorte de compras vai de 04/09/2016 a 17/10/2018; não representa operação em tempo real.
- `review_id` e `order_id` podem se repetir nos reviews; a granularidade deve ser definida antes de agregações.
- Apenas 41,3% dos reviews possuem mensagem textual; análises semânticas devem declarar essa cobertura.
- Há 610 produtos sem categoria e alguns atributos ausentes; a tradução de categorias contém um marcador BOM no cabeçalho.
- Arquivos auxiliares como `olist_geolocation_dataset.csv.zip`, `__MACOSX/` e a cópia de vendedores na raiz não são fontes canônicas de análise.
- Não há tracking de transportadora, tickets, NPS, campanhas nem dados de CRM.
