import hashlib
import os
import random
from questionary import prompt
import time
import sys
from termcolor import colored
from colorama import Fore, Back, Style, init
from pathlib import Path

# Initialiser Colorama pour les couleurs dans la console
init(autoreset=True)

# Fonction pour calculer le hash MD5 d'une chaîne
def calculate_md5_hash(password):
    md5_hash = hashlib.md5(password.encode()).hexdigest()
    return md5_hash

# Fonction pour vérifier le hash
def check_password_hash(indicated_hash):
    # Lecture du fichier de mots de passe
    with open("passwords.txt", "r") as file:
        for line in file:
            # Supprimer les caractères de nouvelle ligne
            password = line.strip()

            # Calculer le hash MD5 du mot de passe
            hashed_password = calculate_md5_hash(password)

            # Comparer les hashes
            if hashed_password == indicated_hash:
                return password
    return None

# Fonction pour vérifier les hashs avec une liste de hashs
def check_password_hashes(indicated_hashes):
    found_passwords = []
    for indicated_hash in indicated_hashes:
        password = check_password_hash(indicated_hash)
        if password:
            found_passwords.append(password)
    return found_passwords

# Fonction pour vérifier les hashs avec un fichier .txt de hashs
def check_password_hashes_from_file(file_path):
    with open(file_path, "r") as file:
        indicated_hashes = [line.strip() for line in file.readlines()]
    return check_password_hashes(indicated_hashes)

# Fonction pour afficher l'araignée multicolore
def print_mixed_colors_spider(twinkling_duration=8):
    spider = [
        '    / _ \\ ',
        '  \\_\\(_)/_/',
        '   _//""\\_',
        '    /   \\  '
    ]

    # Liste de couleurs
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.LIGHTMAGENTA_EX, Fore.WHITE, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX, Fore.MAGENTA, Fore.LIGHTWHITE_EX, Fore.LIGHTBLACK_EX]

    start_time = time.time()

    while time.time() - start_time < twinkling_duration:
        for line in spider:
            colored_line = ''
            for char in line:
                colored_line += random.choice(colors) + char + Style.RESET_ALL + Back.RESET
            print(colored_line)
        sys.stdout.flush()
        time.sleep(0.1)
        print("\033c")  # Effacer l'écran pour créer un effet de clignotement

# Fonction pour afficher du texte clignotant avec des couleurs aléatoires
def twinkling_text(text, twinkling_duration=2):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.LIGHTMAGENTA_EX, Back.LIGHTGREEN_EX, Fore.WHITE, Back.LIGHTBLUE_EX, Fore.LIGHTRED_EX, Back.LIGHTYELLOW_EX,  Fore.LIGHTYELLOW_EX, Back.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, Back.LIGHTRED_EX, Fore.LIGHTBLACK_EX,  Back.LIGHTWHITE_EX, Back.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX, Fore.MAGENTA, Fore.LIGHTWHITE_EX, Fore.LIGHTBLACK_EX, Back.WHITE]

    start_time = time.time()

    while time.time() - start_time < twinkling_duration:
        colored_text = [random.choice(colors) + char + Style.RESET_ALL + Back.RESET for char in text]
        sys.stdout.write(''.join(colored_text) + "\r")
        sys.stdout.flush()
        time.sleep(0.1)

    print('')


def fun_prompt():
            print(colored("Bienvenue sur l'outil de crack md5 par TRHACKNON ", 'cyan'))

            twinkling_text("Md5 Crack by TRHACKNON", twinkling_duration=4)
            print_mixed_colors_spider(twinkling_duration=6)


# Fonction pour obtenir le hash à comparer
def get_hash_input():
    fun_prompt()
    default_choice = "Utiliser par défaut: hash.txt"  # Valeur par défaut
    questions = [
        {
            "type": "select",
            "name": "input_type",
            "message": "Choisissez le type d'entrée pour le hash :",
            "choices": ["hash", "fichier de hash", default_choice],
            "default": default_choice,
        }
    ]

    answers = prompt(questions)
    input_type = answers["input_type"]

    if input_type == "hash":
        hash_input = input("Entrez le hash à comparer : ")
        return hash_input
    elif input_type == "fichier de hash":
        file_path = input("Entrez le chemin vers le fichier de hash : ")
        return file_path
    else:
        # Utiliser par défaut : hash.txt
        default_file = Path("hash.txt")
        if default_file.is_file():
            return "hash.txt"
        else:
            print(Fore.RED + "Aucun fichier de hash par défaut trouvé.")
            return None

hash_input = get_hash_input()

if hash_input:
    if "," in hash_input:
        indicated_hashes = hash_input.split(",")
        found_passwords = check_password_hashes(indicated_hashes)
    elif os.path.isfile(hash_input):
        found_passwords = check_password_hashes_from_file(hash_input)
    else:
        found_passwords = [check_password_hash(hash_input)]

    print_mixed_colors_spider()

    if found_passwords:
        print(Fore.GREEN + "Mots de passe trouvés :")
        for password in found_passwords:
            color = random.choice([Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.LIGHTMAGENTA_EX, Fore.WHITE, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX, Fore.MAGENTA, Fore.LIGHTWHITE_EX, Fore.LIGHTBLACK_EX])
            print(color + f"{password}")
    else:
        print(Fore.RED + "Aucun mot de passe trouvé dans la liste.")