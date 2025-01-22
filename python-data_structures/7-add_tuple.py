def add_tuple(tuple_a=(), tuple_b=()):
  # Si tuple_a ou tuple_b ont moins de 2 éléments, on les complète avec 0
    a1 = tuple_a[0] if len(tuple_a) > 0 else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 else 0

    # Retourner le tuple avec la somme des premiers et deuxièmes éléments
    return (a1 + b1, a2 + b2)
