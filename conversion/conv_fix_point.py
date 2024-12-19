
get_bin = lambda x, n: format(x, 'b').zfill(n)


def complement_a_deux(binary_str, num_bits=None):
    """
    Calcule le complément à deux d'un nombre binaire.

    :param binary_str: Nombre binaire en chaîne de caractères (ex: "0110").
    :param num_bits: Nombre de bits (optionnel). Par défaut, la longueur de binary_str est utilisée.
    :return: Une chaîne binaire représentant le complément à deux.
    """
    # Déterminer le nombre de bits
    num_bits = num_bits or len(binary_str)

    # Convertir en entier, inverser les bits avec XOR, puis ajouter 1
    original_value = int(binary_str, 2)
    max_value = (1 << num_bits) - 1  # Valeur maximale pour `num_bits`
    complement = (~original_value & max_value) + 1

    # Retourner la valeur en chaîne binaire, tronquée au nombre de bits
    return format(complement & max_value, f'0{num_bits}b')

def decimal_to_signed_binary(decimal_number, int_size, total_size):
    # Vérification de la validité des tailles
    if int_size <= 0 or total_size <= 0 or int_size >= total_size:
        raise ValueError("Les tailles doivent être positives et int_size doit être inférieur à total_size.")

    # Calcul de la taille de la partie fractionnaire
    frac_size = total_size - int_size

    # Vérification des limites du nombre
    min_value = - (2 ** (int_size - 1))
    max_value = (2 ** (int_size - 1)) - 1

    if decimal_number < min_value or decimal_number > max_value:
        raise ValueError(f"Le nombre doit être compris entre {min_value} et {max_value}.")

    # Séparation de la partie entière et de la partie décimale
    integer_part = int(abs(decimal_number))
    fractional_part = abs(decimal_number) - integer_part

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

    # On concatène les deux parties puis reconversion en décimal pour éventuellement conversion en complément à deux
    if decimal_number < 0:
        # decimal_number = int(integer_binary + fractional_binary, 2)
#
        print(f"Le nombre est négatif, interger binary: {integer_binary}, fractional binary : {fractional_binary}")
        #
        # mask = 2**int_size - 1
        # decimal_number ^= mask  # python n'a pas d'opérateur binaire inverseur donc on fait un XOR 255
        # decimal_number += 1  # on ajoute 1
        # decimal_number %= mask  # on retire l'éventuel dépassement

        # On revient en binaire, en séparant l'entier du décimal
        # value_in_bin = get_bin(decimal_number, total_size)


        value_in_bin = complement_a_deux(integer_binary + fractional_binary, total_size)

        # On sépare la partie entière et fractionelle
        integer_binary = value_in_bin[0:int_size]
        fractional_binary = value_in_bin[int_size:total_size]


    # Concatenation des parties entière et fractionnaire
    binary_representation = integer_binary + '.' + fractional_binary

    return binary_representation

# Exemple d'utilisation
try:
    decimal_number = 4.75  # Nombre décimal à convertir
    int_size = 4            # Taille de la partie entière
    total_size = 8          # Taille totale du registre

    binary_result = decimal_to_signed_binary(decimal_number, int_size, total_size)
    print(f"Le nombre décimal {decimal_number} en binaire signé est : {binary_result}")
except ValueError as e:
    print(e)
