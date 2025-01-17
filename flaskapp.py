from flask import Flask, render_template, request, send_file, redirect
import io
import pandas as pd
import fitz
import re

app = Flask(__name__)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_document = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text_by_page = []
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text").lower()
        text_by_page.append(text)
    return "\n".join(text_by_page)

# Function to extract data from PDF
def extract_invoice_data(pdf_path):
    text_combined = extract_text_from_pdf(pdf_path)

    # Extract Customer Name
    customer_name_pattern = r"bill to:\s*(.*?)\n"
    customer_name_match = re.search(customer_name_pattern, text_combined)
    customer_name = customer_name_match.group(1).strip() if customer_name_match else "Not found"

    # Extract Address
    address_pattern = r"ship to:\s*([\w\s,]+(?:\n[\w\s,]+)*)(?=\n\w+ \d{1,2} \d{4})"
    address_match = re.search(address_pattern, text_combined)
    address = " ".join(address_match.group(1).split()).strip() if address_match else "Not found"

    # Extract Date
    date_pattern = r"ship to:\s*[\w\s,]+(?:\n[\w\s,]+)*\n(\w+ \d{1,2} \d{4})"
    date_match = re.search(date_pattern, text_combined)
    date = date_match.group(1).strip() if date_match else "Not found"

    # Extract Total Amount
    total_pattern = r"(?:\b\w+\s+class\b)\s*\n\$(\d[\d,.]*)"
    total_match = re.search(total_pattern, text_combined)
    total_amount = f"${total_match.group(1).strip()}" if total_match else "Not found"

    # Extract Order ID
    order_id_pattern = r"order id\s*[:\-]?\s*([a-zA-Z0-9\-]+)"
    order_id_match = re.search(order_id_pattern, text_combined)
    order_id = order_id_match.group(1).strip() if order_id_match else "Not found"

    # Extract Product Name
    product_name_pattern = r"amount\s*([\w\s,'\-]+)\n\d"
    product_name_match = re.search(product_name_pattern, text_combined)
    product_name = product_name_match.group(1).strip() if product_name_match else "Not found"

    # Extract Quantity
    quantity_pattern = r"amount\s*[\w\s,'\-]+\n(\d+)"
    quantity_match = re.search(quantity_pattern, text_combined)
    quantity = quantity_match.group(1).strip() if quantity_match else "Not found"

    return {
        "Order ID": order_id,
        "Customer Name": customer_name,
        "Address": address,
        "Purchase Date": date,
        "Product Name": product_name,
        "Quantity": quantity,
        "Total Amount": total_amount
    }


@app.route('/')
def home():
    return redirect('/upload')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        uploaded_files = request.files.getlist("files[]")
        all_data = []

        for file in uploaded_files:
            if file and file.filename.endswith(".pdf"):
                data = extract_invoice_data(file)
                all_data.append(data)

        # Convert to DataFrame and save as Excel
        df = pd.DataFrame(all_data)
        excel_file = io.BytesIO()
        with pd.ExcelWriter(excel_file, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False, sheet_name="Invoices")

        excel_file.seek(0)

        return send_file(
            excel_file,
            as_attachment=True,
            download_name="invoices_data.xlsx",
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
