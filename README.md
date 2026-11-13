# Game Bar Logic

## How It Works

This can be used to create multiple bars in a console interface. You can create a health bar, MP bar, armor bar, and pretty much anything else you want!

I was just thinking about how I could implement something like this, because I think my next step in this programming journey, creating a console RPG game, could be fun and a great learning experience.

## About the Code

To test this, I created a class to store the player's health and MP values. It gave me a good idea of how I might build the player class in the future (it probably won't look exactly like this, but it's a start!). So, let's get to the main part.

We have the `display_bars` function, which receives a list of bars created beforehand. We start with an important variable called `bar_width`:

```python
bar_width = 20
```

To keep everything properly centered, this value needs to be even.

After that, we create some lists:

```python
top = []
titles = []
values = []
bottom = []
```

These lists allow us to create as many bars side by side as we want. So, it's time to talk about how we fill the bars without breaking the interface. Let's take a look at the code:

```python
def calc_filled_empty(max_value, actual_value, bar_width):
    # We receive the maximum and actual values, along with the bar width.
    filled = round(actual_value / max_value * bar_width)
    # Here, we divide the actual value by the maximum value and multiply it by the bar width.
    empty = bar_width - filled
    # After figuring out how much of the bar is filled, it's easy to know how much is left empty.

    return filled, empty # Return both values
```

So, when we divide the actual value by the maximum value, we get its percentage. We then use that percentage to determine how much of the bar should be filled. Let's see an example:

```python
max_value = 50
actual_value = 25
bar_width = 20

round(actual_value / max_value * bar_width)
```

This is basically `25 / 50 * 20`. Since `25 / 50` equals `0.5`, we know that 25 is 50% of 50. Then, `0.5 * 20` equals 10, because half (50%) of 20 is 10.

So, we're going to have 10 filled characters and 10 empty spaces!
