import requests
from datetime import date

# URL of the file to be downloaded
url = 'https://www.ceasacampinas.com.br/sites/ceasacampinas.com.br/files/cotacoes/{year}/{month}/{day}%2004%202024.pdf'

# Local path where the file will be saved
local_filename = 'img/ceasa_campinas/{YYYYmm}/ceasa_campinas_{YYYYmmdd}.pdf'

def download_file(url, local_filename):
    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Write the content of the response to a local file
        with open(local_filename, 'wb') as f:
            f.write(response.content)
        print(f"File downloaded successfully and saved as {local_filename}")
    else:
        print(f"Failed to download file. HTTP Status code: {response.status_code}")

# Call the function to download the file
def main():
    # current_time
    current_time = date(2024, 4, 17)

    url_formatted = url.format(year=current_time.year,
                           month=current_time.month if current_time.month >= 10 else f"0{current_time.month}", 
                           day=current_time.day if current_time.day >= 10 else f"0{current_time.day}")

    local_filename_formatted = local_filename.format(YYYYmm=current_time.strftime("%Y%m"), 
                                                  YYYYmmdd=current_time.strftime("%Y%m%d"))

    download_file(url_formatted, local_filename_formatted)
