# Lógica das Barras de Interface

## Como funciona

Isso pode ser utilizado para criar múltiplas barras em uma interface de console. Você pode criar uma barra de vida, uma barra de MP, uma barra de armadura e praticamente qualquer outra coisa que quiser!

Eu estava pensando em como poderia implementar algo assim, porque acredito que meu próximo passo nessa jornada de aprendizado de programação, criar um RPG de console, pode ser divertido e uma ótima experiência de aprendizado.

## Sobre o código

Para testar isso, criei uma classe para armazenar os valores de vida e MP do jogador. Isso me deu uma boa ideia de como eu poderia construir a classe do jogador futuramente (provavelmente não será exatamente assim, mas já é um começo!). Então, vamos para a parte principal.

Temos a função `display_bars`, que recebe uma lista de barras criadas anteriormente. Começamos com uma variável importante chamada `bar_width`:

```python
bar_width = 20
```

Para manter tudo devidamente centralizado, esse valor precisa ser par.

Depois disso, criamos algumas listas:

```python
top = []
titles = []
values = []
bottom = []
```

Essas listas nos permitem criar quantas barras lado a lado quisermos. Então, chegou a hora de falar sobre como preenchê-las sem quebrar a interface. Vamos dar uma olhada no código:

```python
def calc_filled_empty(max_value, actual_value, bar_width):
    # Recebemos os valores máximo e atual, junto com a largura da barra.
    filled = round(actual_value / max_value * bar_width)
    # Aqui, dividimos o valor atual pelo valor máximo e multiplicamos pela largura da barra.
    empty = bar_width - filled
    # Depois de descobrir quanto da barra está preenchido, é fácil saber quanto ficará vazio.

    return filled, empty # Retorna ambos os valores
```

Então, quando dividimos o valor atual pelo valor máximo, obtemos sua porcentagem. Depois, usamos essa porcentagem para determinar quanto da barra deve ser preenchido. Vamos ver um exemplo:

```python
max_value = 50
actual_value = 25
bar_width = 20

round(actual_value / max_value * bar_width)
```

Basicamente, isso é `25 / 50 * 20`. Como `25 / 50` é igual a `0.5`, sabemos que 25 representa 50% de 50. Então, `0.5 * 20` resulta em 10, porque metade (50%) de 20 é 10.

Assim, teremos 10 caracteres preenchidos e 10 espaços vazios!
