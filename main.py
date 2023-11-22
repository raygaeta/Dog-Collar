import random
import time
from gtts import gTTS
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# List of quotes for the pet
quotes = [
    "Every day with you is a tail-wagging adventure.",
    "You make my world brighter with your love.",
    "Your presence is my favorite treat.",
    "Thank you for every belly rub and ear scratch.",
    "In your arms, I've found my forever home.",
    "I fetch your love, and I treasure it always.",
    "Your love is the best thing that's ever happened to me.",
    "You are the sunshine of my doggy days.",
    "Your smile makes my tail wag with joy.",
    "With you, life is one big, happy walk.",
    "I woof you more than words can express.",
    "Home is where your scent is.",
    "Your love is like a comforting paw on my heart.",
    "My heart beats to the rhythm of your love.",
    "You are my favorite hooman ever.",
    "Your love makes me feel like top dog.",
    "Every day, I'm pawsitively grateful for you.",
    "Thank you for always being there to cuddle.",
    "With you, life is filled with endless belly rubs.",
    "Your love is the treat I'll never get enough of.",
    "Your presence is my greatest gift.",
    "My love for you is fur-real.",
    "You complete my pack.",
    "You're the paw-fect companion.",
    "Your love is the leash to my happiness.",
    "In your eyes, I see a world of love.",
    "Every day with you is a new tail-wagging chapter.",
    "You make every moment a walk in the park.",
    "Our bond is stronger than any chew toy.",
    "I'm your loyal companion for life.",
    "You're the bone-afide love of my life.",
    "With you, every day is a treat.",
    "Your love is like a warm and cozy bed.",
    "I'm pawsitively thrilled to call you my own.",
    "You're my howl-mate for life.",
    "Thank you for teaching me the meaning of love.",
    "In your arms, I've found my forever lap.",
    "You make my tail wag with your kindness.",
    "With you, every day is a pawsome adventure.",
    "I love you more than all the tennis balls in the world.",
    "I fetch your love and return it with kisses.",
    "Your love is my favorite treat.",
    "You're the best part of my day.",
    "Thank you for the walks, cuddles, and love.",
    "Your love is the best kind of fetch.",
    "I'll follow you anywhere because I love you.",
    "Your love is my daily dose of happiness.",
    "Your smile makes my tail wag with joy.",
    "With you, every day is a doggone good time.",
    "Your love fills my heart with woofs of joy.",
    "You're my paw-some reason to wag my tail.",
    "Your love is the wind beneath my floppy ears.",
    "I'm doggone lucky to have you in my life.",
    "Your love is like the coziest blanket on a cold day.",
    "With you, I've found the paw-fect friend.",
    "Your love is like a delicious bone that I can't resist.",
    "You're the sunshine on my fur.",
    "Every day with you is a grand adventure.",
    "You make my tail wag with your kindness.",
    "I fetch your love, and it's the best game ever.",
    "Thank you for being my loyal pack leader.",
    "Your love is my greatest treasure.",
    "I love you more than all the squirrels in the world.",
    "With you, every day is full of belly rubs and treats.",
    "Your love is the leash to my heart.",
    "You're my woof-tastic source of joy.",
    "Thank you for every delicious meal and cuddle.",
    "Your love is like a warm, cozy blanket on a rainy day.",
    "You complete my pack in the most paw-some way.",
    "Your love is the best kind of fetch.",
    "I'm tail-over-paws in love with you.",
    "With you, every moment is a grand adventure.",
    "Your love is the key to my happy tail.",
    "You're my paw-some partner for life.",
    "Every day with you is like a walk in the park.",
    "Thank you for always being there with a smile.",
    "Your love is my most treasured possession.",
    "I love you more than all the sticks in the world.",
    "With you, life is filled with endless cuddles and play.",
    "Your love is the treat that fills my heart.",
    "You're the tail-wagging joy in my life.",
    "Every day with you is a journey of love.",
    "You make my tail wag with your love and care.",
    "I fetch your love, and it's my favorite game.",
    "Your love is my happy place.",
    "With you, every day is a woof-tastic celebration.",
    "Your love is the bone-afide best.",
    "You're the paw-fect reason for my happiness.",
    "Thank you for every adventure and cuddle.",
    
]

# Function to play a random quote using text-to-speech
def play_random_quote():
    # Select a random quote from the list
    random_quote = random.choice(quotes)

    # Generate audio for the quote using gTTS
    tts = gTTS(random_quote)

    # Save the audio to a temporary file
    audio_file = "quote.mp3"
    tts.save(audio_file)

    # Load and play the audio using pygame mixer
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)

# Main loop to play quotes at intervals
while True:
    try:
        play_random_quote()
        print("Quote played successfully.")
    except Exception as e:
        print(f"Error: {e}")

    # Wait for an hour before playing the next quote
    time.sleep(3600)
