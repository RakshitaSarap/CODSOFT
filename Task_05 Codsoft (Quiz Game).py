import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QRadioButton, QMessageBox
from PyQt5.QtGui import QFont, QPalette, QColor
from PyQt5.QtCore import Qt

quiz_data = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Berlin", "Paris", "Madrid"],
        "correct_choice": "Paris",
    },
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_choice": "Jupiter",
    },
    {
        "question": "Which gas do humans breathe out?",
        "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "correct_choice": "Carbon Dioxide",
    },
    {
        "question": "How many continents are there on Earth?",
        "choices": ["5", "6", "7", "8"],
        "correct_choice": "7",
    },
    {
        "question": "What is the largest mammal on Earth?",
        "choices": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "correct_choice": "Blue Whale",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Mars", "Venus", "Earth", "Jupiter"],
        "correct_choice": "Mars",
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Ag", "Au", "Fe", "Hg"],
        "correct_choice": "Au",
    },
]

color_scheme = {
    "background": QColor(0, 125, 255),  
    "text": QColor(255, 255, 255),  
    "button": QColor(51, 153, 102),  
    "button_text": QColor(0, 0, 0) 
}

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Quiz Game')
        self.setGeometry(100, 100, 600, 400)

        self.current_question = 0
        self.score = 0

        self.palette = QPalette()
        self.palette.setColor(QPalette.Window, color_scheme["background"])
        self.palette.setColor(QPalette.WindowText, color_scheme["text"])
        self.palette.setColor(QPalette.Button, color_scheme["button"])
        self.palette.setColor(QPalette.ButtonText, color_scheme["button_text"])
        self.setPalette(self.palette)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.welcome_label = QLabel("Welcome to the Quiz Game!")
        self.welcome_label.setFont(QFont('Poppins', 20, QFont.Bold))
        self.layout.addWidget(self.welcome_label)

        self.start_button = QPushButton('Start Quiz')
        self.start_button.setFont(QFont('Arial', 12))
        self.start_button.clicked.connect(self.start_quiz)
        self.layout.addWidget(self.start_button)

        self.question_label = QLabel()
        self.question_label.setFont(QFont('Poppins', 14, QFont.Bold))

        self.choice_buttons = []

        self.submit_button = QPushButton('Submit')
        self.submit_button.setFont(QFont('Arial', 12))
        self.submit_button.clicked.connect(self.check_answer)

    def start_quiz(self):
        self.layout.removeWidget(self.welcome_label)
        self.layout.removeWidget(self.start_button)
        self.welcome_label.deleteLater()
        self.start_button.deleteLater()
        random.shuffle(quiz_data)
        self.current_question = 0
        self.score = 0
        self.layout.addWidget(self.question_label)
        for i in range(4):
            choice_button = QRadioButton()
            choice_button.setFont(QFont('Arial', 12))
            self.layout.addWidget(choice_button)
            self.choice_buttons.append(choice_button)
        self.layout.addWidget(self.submit_button)
        self.display_question()

    def display_question(self):
        if self.current_question < len(quiz_data):
            question_data = quiz_data[self.current_question]
            self.question_label.setText(question_data["question"])
            for i, choice_button in enumerate(self.choice_buttons):
                choice_button.setText(question_data["choices"][i])
                choice_button.setChecked(False)
        else:
            self.display_final_result()

    def check_answer(self):
        user_answer = None

        for i, choice_button in enumerate(self.choice_buttons):
            if choice_button.isChecked():
                user_answer = quiz_data[self.current_question]["choices"][i]
                break

        correct_answer = quiz_data[self.current_question]["correct_choice"]

        if user_answer == correct_answer:
            self.score += 1

        self.current_question += 1

        if self.current_question < len(quiz_data):
            self.display_question()
        else:
            self.display_final_result()

    def display_final_result(self):
        result_message = f"Your Score: {self.score}/{len(quiz_data)}\n"
        if self.score == len(quiz_data):
            result_message += "Congratulations! You got all the answers correct!"
        else:
            result_message += "Good effort. Keep learning!"
        QMessageBox.information(self, 'Quiz Completed', result_message)
        play_again = QMessageBox.question(self, 'Play Again', 'Do you want to play again?', QMessageBox.Yes | QMessageBox.No)
        if play_again == QMessageBox.Yes:
            self.start_quiz()
        else:
            sys.exit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    ex = QuizApp()
    ex.show()
    sys.exit(app.exec_())
