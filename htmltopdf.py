import requests

def htmltopdf(html_path):
    print('html to pdf conversion started')
    # Read HTML content from the file
    with open(html_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # API endpoint for PDF conversion
    url = "https://api.pdfendpoint.com/v1/convert"

    # Payload data for the conversion request
    payload = {
        "html": text,
        "sandbox": False,
        "orientation": "vertical",
        "page_size": "A4",
        "margin_top": "1cm",
        "margin_bottom": "1cm",
        "margin_left": "1cm",
        "margin_right": "1cm"
    }
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer pdfe_live_321ec8da5ad0441ded66277d3ed9ac472b1c"
    }

    # Make the POST request to convert HTML to PDF
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        # Convert response JSON to dictionary
        response_data = response.json()
        
        if response_data.get('success'):
            # Download the PDF file if conversion was successful
            pdf_url = response_data['data']['url']
            pdf_response = requests.get(pdf_url)
            
            pdf_path = html_path.replace('.html', '.pdf')
            # Save the PDF file
            with open(pdf_path, 'wb') as pdf_file:
                pdf_file.write(pdf_response.content)
                
            print("PDF successfully downloaded and saved as 'converted_document.pdf'.")
            return pdf_path
        else:
            print(f"Conversion failed: {response_data.get('message', 'No error message provided')}.")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)

    
