"""
Dict comprehension (same as list comprehension and generator expression)
"""
dial_codes = [
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
]

country_dial = {country: code for code, country in dial_codes}
print(country_dial)

refined_country_dial = {country.upper(): code
                        for country, code in sorted(country_dial.items())
                        if code < 10}
print(refined_country_dial)

"""
Unpacking mapping

We can apply ** to more than one argument in a function call. This works when keys are all strings and unique across all 
arguments (because duplicate keyword arguments are forbidden).
"""

def dump(**kwargs):
    print(kwargs)

dump(**{"a": 1,
        "b": 2},
     c=3,
     **{"d": 4,
        "e": 5},
    )

# /!\ In this case, duplicate keys are allowed. Later occurrences overwrite previous ones.
dump(**{'a': 0, **{'x': 1}, 'y': 2, **{'z': 3, 'x': 4}})

"""
ASK CHATGPT WHAT IS GOING ON ABOVE
why does this syntax exists? Is this really useful are juste here to show the possibilities of the language?
"""