def dot_product(vec1, vec2):
    if len(vec1) != len(vec2):
        raise ValueError("Dot product can't be calculated for vectors of different dimentions.")

    result = 0
    for i in range(len(vec1)):
        result += vec1[i] * vec2[i]
    return result

vector_a = [1, 2, 3]
vector_b = [4, 5, 6]
dp = dot_product(vector_a, vector_b)
print(f"Dot product : {dp}")

# Incomplete feature
