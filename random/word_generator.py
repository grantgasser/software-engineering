import random

# Define the discrete distribution of sounds
sound_dist = {'ba': 0.2, 'opa': 0.3, 'baba': 0.5}

# Function to generate a random word based on the distribution

''.join(random.choices(list(sound_dist.keys()), weights=sound_dist.values()))

# Generate a random word

print(random_word)
print('hey')
