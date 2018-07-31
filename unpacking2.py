# Example:
# 
# string_factory(values)
# ["Hi, I'm Michelangelo and I love to eat PIZZA!", "Hi, I'm Garfield and I love to eat lasagna!"]

template = "Hi, I'm {name} and I love to eat {food}!"

values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]

new_list = []

def string_factory(values):
    for each_dict in values:
        new_list.append(template.format(**each_dict))
    return new_list
