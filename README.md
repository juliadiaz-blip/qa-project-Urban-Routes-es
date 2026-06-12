# Urban Routes Automation Project

Automated UI tests for Urban Routes using Selenium and Pytest.

## Author

Elisa Diaz

## Technologies used

* Python 3.12
* Selenium
* Pytest
* WebDriver Manager

## Installation

Clone the repository:
git clone <repository_url>

Create virtual environment:
python -m venv .venv

Activate virtual environment:

### Windows
.venv\Scripts\activate

### macOS/Linux
source .venv/bin/activate

Install dependencies:
pip install -r requirements.txt

## Configuration

Before running the tests, make sure the test server is running.
The URL is configured in `data.py`:
DATA_URL = 'https://cnt-ec91c2eb-...'

## Run tests

Run all tests:
pytest main.py -v

Run a specific test:
pytest main.py::TestUrbanRoutes::test_agregar_tarjeta -v

## Test cases

* test_set_route - Verifies route is set correctly
* test_verificar_tarifa_confort - Verifies Comfort tariff selection
* test_agregar_telefono - Verifies phone number is added
* test_agregar_tarjeta - Verifies payment card is added
* test_mensaje_para_conductor - Verifies driver message is set
* test_manta_y_panuelos - Verifies blanket and tissues toggle
* test_pedir_dos_helados - Verifies two ice creams are ordered