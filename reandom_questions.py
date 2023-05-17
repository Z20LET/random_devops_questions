import random
from colorama import init, Fore

init()

def get_question(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    sections = content.split('---\n')
    questions = []

    for section in sections:
        lines = section.strip().split('\n')
        if len(lines) > 1:
            section_title = lines[0].strip('# ')
            section_questions = [line.strip('# ') for line in lines[1:] if line.startswith('###')]
            if len(section_questions) > 0:
                question = random.choice(section_questions)
                questions.append((section_title, question))

    return questions


file_path = 'module_advanced_devops.md'
questions = get_question(file_path)
title = "\n\n--- DevOps Technical Trial Inteview Questions: ---"

print(f"{Fore.CYAN}{title}{Fore.RESET}")
for i, (section_title, question) in enumerate(questions, 1):
    section_title = f"{Fore.MAGENTA}{section_title}{Fore.RESET}"
    print(f"\n\n{i}. {section_title}: {question}")

