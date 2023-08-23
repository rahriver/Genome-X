import sys
from collections import Counter
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QTabWidget, QTextEdit, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt
from Bio.Seq import Seq
from Bio import Seq, SeqUtils

# <<--------- OPENAI API --------->> #
import openai
openai.api_key = ""

# <<--------- Main --------->> #
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BioApp")
        self.setGeometry(100, 100, 800, 600)
        
        self.create_menu()
        self.create_tabs()
        self.create_sidebar()

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Highlight, QColor(142, 45, 197).lighter())
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)
        
    def create_menu(self):
        menu_bar = self.menuBar()
        menu = menu_bar.addMenu("Tools")
        
        sequence_analysis_action = menu.addAction("Sequence Analysis")
        sequence_analysis_action.triggered.connect(self.show_sequence_analysis_tab)
        
        rna_action = menu.addAction("RNA")
        rna_action.triggered.connect(self.show_rna_tab)
        
        protein_action = menu.addAction("Protein")
        protein_action.triggered.connect(self.show_protein_tab)

        tm_action = menu.addAction("Tm")
        tm_action.triggered.connect(self.show_tm_tab)
        
    def create_tabs(self):
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        
        self.sequence_analysis_tab = SequenceAnalysisTab()
        self.tab_widget.addTab(self.sequence_analysis_tab, "Sequence Analysis")
        
        self.rna_tab = RnaTab()
        self.tab_widget.addTab(self.rna_tab, "RNA")
        
        self.protein_tab = ProteinTab()
        self.tab_widget.addTab(self.protein_tab, "Protein")

        self.tm_tab = TmTab()
        self.tab_widget.addTab(self.tm_tab, "Tm")
        
    def create_sidebar(self):
        self.sidebar = QTextEdit()
        self.sidebar.setReadOnly(True)
        
        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_prompt)
        
        sidebar_layout = QVBoxLayout()
        sidebar_layout.addWidget(self.sidebar)
        sidebar_layout.addWidget(send_button)
        
        sidebar_widget = QWidget()
        sidebar_widget.setLayout(sidebar_layout)
        
        # self.addDockWidget(Qt.RightDockWidgetArea, sidebar_widget)
        
    def send_prompt(self):
        prompt = self.sidebar.toPlainText()
        # Call GPT API and display results in the sidebar
        
    def show_sequence_analysis_tab(self):
        self.tab_widget.setCurrentWidget(self.sequence_analysis_tab)
        
    def show_rna_tab(self):
        self.tab_widget.setCurrentWidget(self.rna_tab)
        
    def show_protein_tab(self):
        self.tab_widget.setCurrentWidget(self.protein_tab)

    def show_tm_tab(self):
        self.tab_widget.setCurrentWidget(self.tm_tab)

class SequenceAnalysisTab(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.sequence_input = QTextEdit()
        layout.addWidget(self.sequence_input)
        
        self.gc_content_output = QTextEdit()
        self.gc_content_output.setReadOnly(True)
        layout.addWidget(self.gc_content_output)
        
        calculate_button = QPushButton("Calculate GC Content")
        calculate_button.clicked.connect(self.calculate_gc_content)
        layout.addWidget(calculate_button)
        
    def calculate_gc_content(self):
        sequence = self.sequence_input.toPlainText()
        gc_content = SeqUtils.gc_fraction(sequence)
        self.gc_content_output.setText(f"GC Content: {round(gc_content * 100, 3)} %")

class RnaTab(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.dna_input = QTextEdit()
        layout.addWidget(self.dna_input)
        
        self.rna_output = QTextEdit()
        self.rna_output.setReadOnly(True)
        layout.addWidget(self.rna_output)
        
        transcribe_button = QPushButton("Transcribe to RNA")
        transcribe_button.clicked.connect(self.transcribe_to_rna)
        layout.addWidget(transcribe_button)
        
    def transcribe_to_rna(self):
        dna_sequence = self.dna_input.toPlainText()
        rna_sequence = Seq(dna_sequence).transcribe()
        self.rna_output.setText(str(rna_sequence))

class ProteinTab(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.dna_input = QTextEdit()
        layout.addWidget(self.dna_input)
        
        self.protein_output = QTextEdit()
        self.protein_output.setReadOnly(True)
        layout.addWidget(self.protein_output)
        
        translate_button = QPushButton("Translate to Protein")
        translate_button.clicked.connect(self.translate_to_protein)
        layout.addWidget(translate_button)
        
    def translate_to_protein(self):
        dna_sequence = self.dna_input.toPlainText()
        protein_sequence = Seq(dna_sequence).translate()
        self.protein_output.setText(str(protein_sequence))


class TmTab(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.dna_input = QTextEdit()
        layout.addWidget(self.dna_input)
        
        self.tm_output = QTextEdit()
        self.tm_output.setReadOnly(True)
        layout.addWidget(self.tm_output)
        
        calculate_tm_button = QPushButton("Calculate Tm")
        calculate_tm_button.clicked.connect(self.calculate_tm)
        layout.addWidget(calculate_tm_button)
        
    def calculate_tm(self):
        dna_sequence = self.dna_input.toPlainText()

        if any(map(str.isdigit, dna_sequence)) == True:
            self.tm_output.setText("Please input a valid sequence!")
        else:
            g,c,a,t = (0,)*4
            nuc = Counter(dna_sequence)
            g,c,a,t = [nuc['G'], nuc['C'], nuc['A'], nuc['T']]
            calculated_tm = 4 * (g + c) + 2 * (a + t)
            self.tm_output.setText(f'{calculated_tm} C{chr(176)}')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
