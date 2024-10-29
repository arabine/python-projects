
get_bin = lambda x, n: format(x, 'b').zfill(n)

def decimal_to_signed_binary(decimal_number, int_size, total_size):
    # Vérification de la validité des tailles
    if int_size <= 0 or total_size <= 0 or int_size >= total_size:
        raise ValueError("Les tailles doivent être positives et int_size doit être inférieur à total_size.")

    # Calcul de la taille de la partie fractionnaire
    frac_size = total_size - int_size - 1  # 1 bit pour le signe

    # Vérification des limites du nombre
    min_value = - (2 ** (int_size - 1))
    max_value = (2 ** (int_size - 1)) - 1

    if decimal_number < min_value or decimal_number > max_value:
        raise ValueError(f"Le nombre doit être compris entre {min_value} et {max_value}.")

    # Séparation de la partie entière et de la partie décimale
    integer_part = int(abs(decimal_number))
    fractional_part = abs(decimal_number) - integer_part

    mask = 2**int_size - 1
    integer_part ^= mask  # python n'a pas d'opérateur binaire NON donc on fait un XOR 255
    integer_part += 1  # on ajoute 1
    integer_part %= mask  # on retire l'éventuel dépassement

    # Conversion en chaîne de caractères
    integer_binary = get_bin(integer_part, int_size)

    # Conversion de la partie décimale en binaire
    fractional_binary = []
    while fractional_part > 0 and len(fractional_binary) < frac_size:
        fractional_part *= 2
        bit = int(fractional_part)
        fractional_binary.append(str(bit))
        fractional_part -= bit

    # Remplissage de la partie fractionnaire si nécessaire
    fractional_binary = ''.join(fractional_binary).ljust(frac_size, '0')

    # Concatenation des parties entière et fractionnaire
    binary_representation = integer_binary + '.' + fractional_binary

    return binary_representation

# Exemple d'utilisation
try:
    decimal_number = -3.7  # Nombre décimal à convertir
    int_size = 4            # Taille de la partie entière
    total_size = 8          # Taille totale du registre

    binary_result = decimal_to_signed_binary(decimal_number, int_size, total_size)
    print(f"Le nombre décimal {decimal_number} en binaire signé est : {binary_result}")
except ValueError as e:
    print(e)
