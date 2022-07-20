import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import QTimer
from random import randint

text_font = QFont("Times", 14)
button_font = QFont( "Arial", 12)
computer_score = 0
player_score = 0

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors")
        self.setGeometry(350, 150, 550, 550)
        self.UI()

    def UI(self):
        self.score_computer = QLabel("Computer Score : ", self)
        self.score_computer.move(30, 20)
        self.score_computer.setFont(text_font)
        self.score_player = QLabel("Your Score : ", self)
        self.score_player.move(330, 20)
        self.score_player.setFont(text_font)

        self.image_computer = QLabel(self)
        self.image_computer.setPixmap(QPixmap("image/rock.png"))
        self.image_computer.move(50, 100)

        self.image_vs = QLabel(self)
        self.image_vs.setPixmap(QPixmap("image/game.png"))
        self.image_vs.move(240,150)

        self.image_player = QLabel(self)
        self.image_player.setPixmap(QPixmap("image/rock.png"))
        self.image_player.move(330, 100)

        self.btn_start = QPushButton("Start", self)
        self.btn_start.setFont(button_font)
        self.btn_start.setStyleSheet("background-color:green")
        self.btn_start.move(180, 250)
        self.btn_start.clicked.connect(self.start_game)

        self.btn_stop = QPushButton("Stop", self)
        self.btn_stop.setStyleSheet("background-color:red")
        self.btn_stop.setFont(button_font)
        self.btn_stop.move(270, 250)
        self.btn_stop.clicked.connect(self.stop_game)

        self.timer = QTimer(self)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.play_game)

        self.show()

    def start_game(self):
        self.timer.start()

    def stop_game(self):
        global computer_score
        global player_score
        self.timer.stop()


        if self.rnd_val_comp == 1 and self.rnd_val_player == 1:
            mbox = QMessageBox.information(self, "Information", "Game Draw!")

        elif (self.rnd_val_comp == 1) and (self.rnd_val_player == 2): 
            mbox = QMessageBox.information(self, "Information", "You Win!")
            player_score +=1
            self.score_player.setText("Your Score:{}".format(player_score))


        elif self.rnd_val_comp == 1 and self.rnd_val_player == 3:
            mbox = QMessageBox.information(self, "Information", "Computer Wins!")
            computer_score +=1
            self.score_computer.setText("Computer Score:{}".format(computer_score))

        elif self.rnd_val_comp == 2 and self.rnd_val_player == 1:
            mbox = QMessageBox.information(self, "Information", "Computer Wins!")
            computer_score +=1
            self.score_computer.setText("Computer Score:{}".format(computer_score))

        elif self.rnd_val_comp == 2 and self.rnd_val_player == 2:
            mbox = QMessageBox.information(self, "Information", "Game Draw!")

        elif self.rnd_val_comp == 2 and self.rnd_val_player == 3:
            mbox = QMessageBox.information(self, "Information", "You Wins!")
            player_score +=1
            self.score_player.setText("Your Score:{}".format(player_score))

        elif self.rnd_val_comp == 3 and self.rnd_val_player == 1:
            mbox = QMessageBox.information(self, "Information", "You Win!")
            player_score +=1
            self.score_player.setText("Your Score:{}".format(player_score))

        elif self.rnd_val_comp == 3 and self.rnd_val_player == 2:
            mbox = QMessageBox.information(self, "Information", "Computer Wins!")
            computer_score +=1
            self.score_computer.setText("Computer Score:{}".format(computer_score))
        
        elif self.rnd_val_comp == 3 and self.rnd_val_player == 3:
            mbox = QMessageBox.information(self, "Information", "Game Draw!")

        if computer_score == 3 or player_score == 3:
            mbox = QMessageBox.information(self, "Information", "Game Over")
            sys.exit()



    def play_game(self):
        self.rnd_val_comp = randint(1, 3)
        if self.rnd_val_comp == 1:
            self.image_computer.setPixmap(QPixmap("image/rock.png"))
        elif self.rnd_val_comp == 2:
            self.image_computer.setPixmap(QPixmap("image/paper.png"))
        else:
            self.image_computer.setPixmap(QPixmap("image/scissors.png"))

        self.rnd_val_player = randint(1, 3)
        if self.rnd_val_player == 1:
            self.image_player.setPixmap(QPixmap("image/rock.png"))
        elif self.rnd_val_player == 2:
            self.image_player.setPixmap(QPixmap("image/paper.png"))
        else:
            self.image_player.setPixmap(QPixmap("image/scissors.png"))

        

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == "__main__":
    main()
