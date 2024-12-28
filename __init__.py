import sys
import os

# Добавляем путь к папке с кодом в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from prompt_defender import PromptDefenderClassifier
