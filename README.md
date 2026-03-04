# Egyptian License Plate Detector

This project is a computer vision application designed to detect and recognize Egyptian license plates from video or image files. It utilizes image processing techniques and machine learning to extract and identify characters (numbers and letters) specific to Egyptian plates.

## Features

*   **License Plate Detection:** Automatically locates the license plate within a video frame or image.
*   **Character Segmentation:** Separates individual characters for analysis.
*   **Character Recognition:** Identifies Arabic letters and numbers using a trained dataset.
*   **GUI Interface:** A simple Graphical User Interface (GUI) built with Tkinter to easily input file names.

## Prerequisites

Before running the project, ensure you have the following installed:

*   Python 3.x
*   pip (Python package manager)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Ezatnasef/Egyptian-Licence-Plate-Detector.git
    cd Egyptian-Licence-Plate-Detector
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application:**
    Execute the main script using Python:
    ```bash
    python run.py
    ```

2.  **Input File:**
    *   A window titled "Plate Detector" will appear.
    *   Enter the name of the video or image file you wish to process (e.g., `video.mp4`) in the "File Name" field. *Note: Ensure the file is in the project directory.*
    *   Click **OK**.

3.  **View Results:**
    *   The application will process the input and display the detected plate.
    *   The recognized text (numbers and letters) will be printed in the terminal.

## Technologies Used

*   **OpenCV:** For core image processing tasks.
*   **NumPy:** For efficient numerical array operations.
*   **Scikit-image:** For advanced image processing algorithms.
*   **Numba:** To accelerate Python code performance.
*   **Tkinter:** For the graphical user interface.