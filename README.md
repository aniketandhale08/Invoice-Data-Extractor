# Invoice Data Extractor

**Invoice Data Extractor** is a Flask-based web application that processes PDF invoices, extracts key information such as customer name, address, order details, and generates an Excel file for easy analysis.  

Live app: [click here](https://my-projects-408316.el.r.appspot.com/upload)

- **Flask**: A lightweight web framework used for building Python applications, allowing for fast and scalable development of web-based applications.
- **Google Cloud Platform (GCP)**: Specifically, we have used **App Engine**, a serverless platform for hosting web applications, providing automatic scaling and simplified deployment.
- **Natural Language Processing (NLP)**: We have used **regular expressions** for pattern matching and word matching in text, enabling efficient text processing and extraction.
- **PyMuPDF**: A Python library used for **text extraction** from PDF documents, making it easier to work with data stored in PDF format.

### Diagram

![Screenshot 2025-01-17 045047 (1)](https://github.com/user-attachments/assets/69f6f4dd-4149-4dac-a141-80bdd89e3625)

## Features  
- Upload multiple PDF invoices at once.  
- Extract critical invoice details such as:  
  - Customer Name  
  - Address  
  - Order ID  
  - Purchase Date  
  - Product Name  
  - Quantity  
  - Total Amount  
- Download extracted data in Excel format.  

---

### Flowchart

![Support process example](https://github.com/user-attachments/assets/48bc2ba4-8ba4-427a-9c88-58012e31f07b)

## Project Structure

```
invoice-data-extractor/
├── flaskapp.py              # Main Python file for the Flask application
├── requirements.txt         
├── templates/               
│   └── index.html           
├── static/                  
│   ├── CSS                  
│   │   └── style.css       
│   ├── js                   
│   │   └── script.js       
```

## How to Run the App Locally  
Follow these steps to run the app on your local machine:  

### Prerequisites  
1. Python 3.9 or above must be installed.  
2. Install `pip`, the Python package manager.  
3. Clone or download this repository to your local machine.  

### Steps 

### 1. Clone the Repository  
 ```bash
 git clone https://github.com/aniketandhale08/Invoice-Data-Extractor.git
```

### 2. Navigate to the Root Directory  
```bash
cd invoice-data-extractor
```

### 3. Install Requirements  
```bash
pip install -r requirements.txt
```

### 4. Run the Application 
```bash
python flaskapp.py
```

### 5. Access the Application
Open your browser and go to:  
```bash
http://127.0.0.1:5000

