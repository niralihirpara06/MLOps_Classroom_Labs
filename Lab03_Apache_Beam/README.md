# Lab 03: Apache Beam - Word Count Pipeline

## Overview
This lab demonstrates the use of **Apache Beam** for building data processing pipelines. We implemented a word count pipeline using the **DirectRunner** to analyze Shakespeare's "King Lear" text and performed additional text analytics.

## Project Structure
```
Lab03_Apache_Beam/
├── data/
│   └── kinglear.txt              # Input: Shakespeare's King Lear
├── outputs/
│   ├── advanced_wordcount.txt    # Top 20 words (case-insensitive)
│   ├── letter_frequency.txt      # Starting letter frequency
│   └── average_word_length.txt   # Average word length analysis
├── Try_Apache_Beam_Python.ipynb  # Main notebook with pipeline code
└── README.md
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/niralihirpara06/MLOps_Classroom_Labs.git
cd MLOps_Classroom_Labs/Lab03_Apache_Beam
```

### 2. Create Virtual Environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install apache-beam ipykernel
```

### 4. Register Jupyter Kernel
```bash
python -m ipykernel install --user --name=venv --display-name "Python (Beam)"
```

### 5. Run the Notebook
Open `Try_Apache_Beam_Python.ipynb` in VS Code or Jupyter and run the cells.

## Pipeline Implementation

### Pipeline Steps Explained
1. **Read lines**: Reads each line from the input text file
2. **Find words**: Uses regex `[a-zA-Z']+` to extract all words
3. **Pair words with 1**: Creates (word, 1) key-value pairs
4. **Group and sum**: Groups by word and sums counts using `CombinePerKey`
5. **Write results**: Outputs to file

## Results Summary

### 1. Basic Word Count
Total unique words identified: **4,785**

**Sample Output:**
| Word | Count |
|------|-------|
| KING | 243 |
| LEAR | 236 |
| the | 786 |
| and | 594 |
| of | 447 |
| to | 438 |

### 2. Advanced Word Count (Top 20 - Case Insensitive)
| Word | Count |
|------|-------|
| king | 311 |
| lear | 253 |
| thou | 219 |
| kent | 175 |
| gloucester | 167 |
| thee | 139 |
| what | 137 |
| edgar | 136 |
| edmund | 131 |
| fool | 120 |

### 3. Letter Frequency (Starting Letter)
| Letter | Count |
|--------|-------|
| T | 1,400 |
| S | 1,340 |
| L | 938 |
| C | 917 |
| F | 917 |
| W | 911 |
| H | 804 |
| M | 806 |

### 4. Average Word Length Analysis
Sample words with their character lengths:
- "gloucester" → 10.00
- "acknowledge" → 11.00
- "king" → 4.00
- "consideration" → 13.00

## Key Concepts Learned

### Apache Beam Transforms Used
- **`beam.io.ReadFromText()`**: Read input from text files
- **`beam.FlatMap()`**: One-to-many element transformation
- **`beam.Map()`**: One-to-one element transformation
- **`beam.CombinePerKey()`**: Aggregate values by key
- **`beam.io.WriteToText()`**: Write output to text files

### DirectRunner
The DirectRunner executes pipelines locally, useful for development and testing before deploying to distributed runners like Dataflow or Spark.

## Technologies Used
- **Python 3.x**
- **Apache Beam 2.52.0**
- **Jupyter Notebook**
- **VS Code**