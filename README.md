![logo](https://github.com/rahriver/Genome-X/assets/89016694/8141288c-f551-47a3-bacb-9ed585a5d88b)

# GUI for Biopython

## Introduction

This repository contains a graphical user interface (GUI) application that interacts with various bioinformatics-related Python packages, including Biopython. The application provides an easy-to-use interface for performing sequence analysis, transcribing DNA to RNA, translating DNA to protein, and calculating melting temperature (Tm) for DNA sequences.

## ⚙ Features

- **Sequence Analysis:** Calculate the GC content of a given DNA sequence.
- **Transcribe to RNA:** Transcribe a DNA sequence into its corresponding RNA sequence.
- **Translate to Protein:** Translate a DNA sequence into its corresponding protein sequence.
- **Calculate Tm:** Estimate the melting temperature (Tm) of a DNA sequence.

## ⚡ Getting Started

To use the GUI tool, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies (Biopython, Openai, PyQT5)
3. Obtain an OpenAI API key and replace the empty string in the `openai.api_key` assignment with your API key. **Not working currently**
4. Run the `main.py` script using Python.

### 🖇 Menu Bar

- **Tools:** Access different sequence analysis tools through the menu bar.
  - **Sequence Analysis:** Calculate the GC content of a DNA sequence.
  - **RNA:** Transcribe a DNA sequence to its RNA counterpart.
  - **Protein:** Translate a DNA sequence to its protein counterpart.
  - **Tm:** Calculate the melting temperature (Tm) of a DNA sequence.

### 📑 Tabs

The application includes the following tabs:

- **Sequence Analysis Tab:** Calculate GC content.
- **RNA Tab:** Transcribe DNA to RNA.
- **Protein Tab:** Translate DNA to protein.
- **Tm Tab:** Calculate melting temperature.

## 🎯 Goals
- Integrate GPT as a copilot
- Include more analysis
- Integrate other terminal-based applications (e.g., Primer 3, Clustalw)
- More attractive design

## Contributing
I want you to know that contributions to this repository are welcome. If you find any issues or have suggestions for improvements, feel free to create an issue or submit a pull request.
