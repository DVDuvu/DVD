import pygame
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import random
from transformers import pipeline
import pyttsx3

pygame.init()

WIDTH = 400
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Proto")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (150, 150, 150)
DARK_GRAY = (100, 100, 100)
RED = (255, 0, 0)
PINK = (255, 105, 180)
YELLOW = (255, 255, 0)

proto_head_normal = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,6,6,6,3,3,0,0,0,0,0,0,0,0,0,0],
    [0,9,9,6,6,3,3,3,3,9,0,0,0,0,0,0],
    [0,0,1,9,6,6,3,3,9,1,1,1,1,1,1,0],
    [0,0,9,9,1,6,6,9,1,1,6,6,1,1,1,1],
    [0,0,0,1,9,6,6,9,1,1,6,6,1,1,1,1],
    [0,0,0,9,1,9,6,9,1,1,1,1,1,1,1,1],
    [0,0,9,1,9,6,6,9,1,1,6,1,6,6,1,1],
    [0,0,3,9,6,9,9,9,1,1,1,6,1,1,6,1],
    [0,0,3,3,9,6,6,9,9,1,1,1,1,1,1,0],
    [0,0,0,3,9,6,6,9,3,9,0,0,0,0,0,0],
    [0,0,0,0,3,9,9,9,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0]
]

proto_head_blink = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,6,6,6,3,3,0,0,0,0,0,0,0,0,0,0],
    [0,9,9,6,6,3,3,3,3,9,0,0,0,0,0,0],
    [0,0,1,9,6,6,3,3,9,1,1,1,1,1,1,0],
    [0,0,9,9,1,6,6,9,1,1,1,1,1,1,1,1],
    [0,0,0,1,9,6,6,9,1,1,1,1,1,1,1,1],
    [0,0,0,9,1,9,6,9,1,1,1,1,1,1,1,1],
    [0,0,9,1,9,6,6,9,1,1,6,1,6,6,1,1],
    [0,0,3,9,6,9,9,9,1,1,1,6,1,1,6,1],
    [0,0,3,3,9,6,6,9,9,1,1,1,1,1,1,0],
    [0,0,0,3,9,6,6,9,3,9,0,0,0,0,0,0],
    [0,0,0,0,3,9,9,9,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0]
]

proto_head_talk = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,6,6,6,3,3,0,0,0,0,0,0,0,0,0,0],
    [0,9,9,6,6,3,3,3,3,9,0,0,0,0,0,0],
    [0,0,1,9,6,6,3,3,9,1,1,1,1,1,1,0],
    [0,0,9,9,1,6,6,9,1,1,6,6,1,1,1,1],
    [0,0,0,1,9,6,6,9,1,1,6,6,1,1,1,1],
    [0,0,0,9,1,9,6,9,1,1,1,1,1,1,1,1],
    [0,0,9,1,9,6,6,9,1,1,1,1,6,6,1,1],
    [0,0,3,9,6,9,9,9,1,1,1,6,1,1,6,1],
    [0,0,3,3,9,6,6,9,9,1,1,1,6,6,1,0],
    [0,0,0,3,9,6,6,9,3,9,0,0,0,0,0,0],
    [0,0,0,0,3,9,9,9,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0]
]

proto_head_afk = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,6,6,6,3,3,0,0,0,0,0,0,0,0,0,0],
    [0,9,9,6,6,3,3,3,3,9,0,0,0,0,0,0],
    [0,0,1,9,6,6,3,3,9,1,1,1,1,1,1,0],
    [0,0,9,9,1,6,6,9,1,1,6,1,6,1,1,1],
    [0,0,0,1,9,6,6,9,1,1,1,6,1,1,1,1],
    [0,0,0,9,1,9,6,9,1,1,6,1,6,1,1,1],
    [0,0,9,1,9,6,6,9,1,1,1,1,1,1,1,1],
    [0,0,3,9,6,9,9,9,1,1,1,1,1,1,1,1],
    [0,0,3,3,9,6,6,9,9,1,1,1,1,1,1,0],
    [0,0,0,3,9,6,6,9,3,9,0,0,0,0,0,0],
    [0,0,0,0,3,9,9,9,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0]
]

proto_head_happy = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,6,6,6,3,3,0,0,0,0,0,0,0,0,0,0],
    [0,9,9,6,6,3,3,3,3,9,0,0,0,0,0,0],
    [0,0,1,9,6,6,3,3,9,1,1,1,1,1,1,0],
    [0,0,9,9,1,6,6,9,1,1,6,1,1,1,1,1],
    [0,0,0,1,9,6,6,9,1,6,1,6,1,1,1,1],
    [0,0,0,9,1,9,6,9,1,1,1,1,1,1,1,1],
    [0,0,9,1,9,6,6,9,1,1,6,1,6,6,1,1],
    [0,0,3,9,6,9,9,9,1,1,1,6,1,1,6,1],
    [0,0,3,3,9,6,6,9,9,1,1,1,1,1,1,0],
    [0,0,0,3,9,6,6,9,3,9,0,0,0,0,0,0],
    [0,0,0,0,3,9,9,9,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0]
]

proto_head_enamored = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,6,6,6,3,3,0,0,0,0,0,0,0,0,0,0],
    [0,9,9,6,6,3,3,3,3,9,0,0,0,0,0,0],
    [0,0,1,9,6,6,3,3,9,1,1,1,1,1,1,0],
    [0,0,9,9,1,6,6,9,1,1,6,1,6,1,1,1],
    [0,0,0,1,9,6,6,9,1,1,6,6,6,1,1,1],
    [0,0,0,9,1,9,6,9,1,1,1,6,1,1,1,1],
    [0,0,9,1,9,6,6,9,1,1,1,1,1,1,1,1],
    [0,0,3,9,6,9,9,9,1,1,1,1,1,1,1,1],
    [0,0,3,3,9,6,6,9,9,1,1,1,1,1,1,0],
    [0,0,0,3,9,6,6,9,3,9,0,0,0,0,0,0],
    [0,0,0,0,3,9,9,9,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0]
]

proto_head_nervous = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [6,6,6,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,6,6,6,3,3,0,0,0,0,0,0,0,0,0,0],
    [0,9,9,6,6,3,3,3,3,9,0,0,0,0,0,0],
    [0,0,1,9,6,6,3,3,9,1,1,1,1,1,1,0],
    [0,0,9,9,1,6,6,9,1,1,1,6,1,1,1,1],
    [0,0,0,1,9,6,6,9,1,1,6,6,1,1,1,1],
    [0,0,0,9,1,9,6,9,1,1,1,1,1,1,1,1],
    [0,0,9,1,9,6,6,9,1,1,1,1,6,6,1,1],
    [0,0,3,9,6,9,9,9,1,1,1,6,1,1,6,1],
    [0,0,3,3,9,6,6,9,9,1,6,1,1,1,1,0],
    [0,0,0,3,9,6,6,9,3,9,0,0,0,0,0,0],
    [0,0,0,0,3,9,9,9,3,0,0,0,0,0,0,0],
    [0,0,0,0,0,3,3,3,0,0,0,0,0,0,0,0]
]

PIXEL_SIZE = 12

is_talking = False
talk_timer = 0
is_afk = False
last_interaction_time = time.time()
afk_message_shown = False
is_happy = False
happy_timer = 0
is_enamored = False
enamored_timer = 0
is_nervous = False
nervous_timer = 0
talk_repeats = 0
is_speaking = False  

generator = pipeline("text-generation", model="distilgpt2")


engine = pyttsx3.init()
engine.setProperty('rate', 150)  


def on_start(name):
    global is_speaking
    is_speaking = True

def on_end(name, completed):
    global is_speaking
    is_speaking = False

engine.connect('started-utterance', on_start)
engine.connect('finished-utterance', on_end)

def get_grok_response(message):
    try:
        prompt = f"furry, name Dipi, a cute pixel Proto head. Respond to this: {message}"
        response = generator(prompt, max_length=50, num_return_sequences=1)[0]["generated_text"]
        return response[len(prompt):].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def draw_fox_head(surface, fox_array, x, y):
    for i in range(16):
        for j in range(16):
            if fox_array[i][j] == 1:
                pygame.draw.rect(surface, BLACK, (x + j * PIXEL_SIZE, y + i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
            elif fox_array[i][j] == 3:
                pygame.draw.rect(surface, GRAY, (x + j * PIXEL_SIZE, y + i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
            elif fox_array[i][j] == 6:
                pygame.draw.rect(surface, BLUE, (x + j * PIXEL_SIZE, y + i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
            elif fox_array[i][j] == 9:
                pygame.draw.rect(surface, DARK_GRAY, (x + j * PIXEL_SIZE, y + i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))


def speak_text(text):
    def speak_thread():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=speak_thread, daemon=True).start()

def create_chat_window():
    global is_talking, last_interaction_time, is_afk, afk_message_shown, talk_repeats, is_happy, is_enamored, is_nervous
    root = tk.Tk()
    root.title("Chat with Mini Proto")
    root.geometry("300x400")

    chat_display = tk.Text(root, height=20, width=30)
    chat_display.pack(pady=5)

    entry = tk.Entry(root, width=25)
    entry.pack(pady=5)

    def send_message():
        global is_talking, last_interaction_time, is_afk, afk_message_shown, talk_repeats, is_happy, is_enamored, is_nervous
        if is_speaking: 
            return
        message = entry.get()
        if message:
            chat_display.insert(tk.END, "You: " + message + "\n")
            entry.delete(0, tk.END)
            
            response = get_grok_response(message)
            talk_repeats = len(response.split())

            message_lower = message.lower()
            response_lower = response.lower()

            enamored_keywords = ["love", "sweet", "darling", "beautiful", "adorable", "charming", "excited", "passionate", "romantic", "dear", "❤️", "kiss", "kissing"]
            if any(keyword in message_lower for keyword in enamored_keywords) or any(keyword in response_lower for keyword in enamored_keywords):
                is_enamored = True

            nervous_keywords = ["sorry", "nervous", "scared", "afraid", "oops", "awkward", "embarrassed", "shame", "uncomfortable", "bad", "fear", "terrified", "bad boy", "sad"]
            if any(keyword in message_lower for keyword in nervous_keywords) or any(keyword in response_lower for keyword in nervous_keywords):
                is_nervous = True

            happy_keywords = ["nice", "thank", "cute", "happy", "good", "great", "awesome", "like", "enjoy", "pleased", "comfortable", "glad", "good boy"]
            if any(keyword in message_lower for keyword in happy_keywords) or any(keyword in response_lower for keyword in happy_keywords):
                is_happy = True

            chat_display.insert(tk.END, "Proto: " + response + "\n")
            chat_display.see(tk.END)
            is_talking = True  
            send_button.config(state="disabled")  
            entry.config(state="disabled")  
            speak_text(response)  
            last_interaction_time = time.time()
            is_afk = False
            afk_message_shown = False

    send_button = ttk.Button(root, text="Send", command=send_message)
    send_button.pack(pady=5)

    def check_speech_status():
        if not is_speaking:
            send_button.config(state="normal")  
            entry.config(state="normal")  
        root.after(100, check_speech_status)  

    root.after(100, check_speech_status)  
    root.mainloop()

chat_thread = threading.Thread(target=create_chat_window)
chat_thread.daemon = True
chat_thread.start()

clock = pygame.time.Clock()
running = True
blink_timer = 0
is_blinking = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    current_time = time.time()
    if current_time - last_interaction_time > 300:  
        is_afk = True
        if not afk_message_shown:
            def show_afk_warning():
                messagebox.showwarning("AFK", "where are you? you don't want to communicate anymore")
                speak_text("where are you? you don't want to communicate anymore")
            threading.Thread(target=show_afk_warning, daemon=True).start()
            afk_message_shown = True
    else:
        is_afk = False

    blink_timer += 1
    if blink_timer > 100 and not is_blinking and not is_afk and not is_talking and not is_happy and not is_enamored and not is_nervous:
        is_blinking = True
        blink_timer = 0
    elif blink_timer > 10 and is_blinking:
        is_blinking = False
        blink_timer = 0

    if is_talking:
        talk_timer += 1
        if talk_timer >= 30:  
            talk_repeats -= 1
            talk_timer = 0
            if talk_repeats <= 0:
                is_talking = False
                if is_happy:
                    happy_timer = 300  
                if is_enamored:
                    enamored_timer = 300  
                if is_nervous:
                    nervous_timer = 300  

    if is_happy and not is_talking:
        happy_timer -= 1
        if happy_timer <= 0:
            is_happy = False

    if is_enamored and not is_talking:
        enamored_timer -= 1
        if enamored_timer <= 0:
            is_enamored = False

    if is_nervous and not is_talking:
        nervous_timer -= 1
        if nervous_timer <= 0:
            is_nervous = False

    screen.fill(YELLOW)
    
    if is_afk:
        draw_fox_head(screen, proto_head_afk, 100, 50)
    elif is_enamored and not is_talking:
        draw_fox_head(screen, proto_head_enamored, 100, 50)
    elif is_nervous and not is_talking:
        draw_fox_head(screen, proto_head_nervous, 100, 50)
    elif is_happy and not is_talking:
        draw_fox_head(screen, proto_head_happy, 100, 50)
    elif is_talking:
        draw_fox_head(screen, proto_head_talk, 100, 50)
    elif is_blinking:
        draw_fox_head(screen, proto_head_blink, 100, 50)
    else:
        draw_fox_head(screen, proto_head_normal, 100, 50)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()