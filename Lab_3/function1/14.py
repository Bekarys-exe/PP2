from Functions import filter_prime, print_permutations, reverse_words, sphere_volume, guess_the_number

numbers = [10, 15, 3, 7, 2, 8, 5]
prime_numbers = filter_prime(numbers)
print(f"Prime numbers: {prime_numbers}")

input_string = "abc"
print(f"Permutations of '{input_string}':")
print_permutations(input_string)

sentence = "We are ready"
reversed_sentence = reverse_words(sentence)
print(f"Reversed sentence: {reversed_sentence}")

radius = 5
volume = sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is {volume:.2f}")

guess_the_number()