dictionary = {
    "User": "Sigma",
    "Age": 12,
    "Affilation": "Sigiemeczka"
}

swapped = dict((v,k) for k,v in dictionary.items())

print(swapped)