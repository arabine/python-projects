def fixed_point_to_decimal_with_dot(binary_str, signed=False):
    """
    Convertit un nombre binaire avec un point en décimal.

    :param binary_str: Chaîne représentant le nombre binaire avec un point (ex. '11.011010').
    :param signed: Indique si le nombre est signé (True) ou non (False).
    :return: La valeur décimale.
    """
    # Séparer la partie entière et fractionnaire
    if '.' in binary_str:
        integer_part, fractional_part = binary_str.split('.')
    else:
        integer_part, fractional_part = binary_str, ''

    # Nombre de bits pour la partie fractionnaire
    fractional_bits = len(fractional_part)

    # Convertir la partie entière
    if signed and integer_part.startswith('1'):
        # Ajouter des zéros à gauche si nécessaire pour gérer les nombres signés
        total_bits = len(integer_part) + fractional_bits
        padded_binary = integer_part + fractional_part
        integer_value = int(padded_binary, 2)
        if padded_binary[0] == '1':  # Bit de signe à 1
            integer_value -= 1 << total_bits
    else:
        integer_value = int(integer_part + fractional_part, 2)

    # Diviser par 2^fractional_bits pour obtenir la valeur finale
    decimal_value = integer_value / (2 ** fractional_bits)

    return decimal_value


# Exemple d'utilisation
if __name__ == "__main__":
    binary_number = "1.1100110"  # Nombre binaire avec un point
    signed = False               # Indiquer si le nombre est signé

    result = fixed_point_to_decimal_with_dot(binary_number, signed)
    print(f"Le nombre décimal correspondant est : {result}")




