# Weather Information App

This project is a desktop application built with Tkinter that fetches and displays the current weather information for various cities in Azerbaijan using the Weatherstack API. The weather data is presented in a table format, and the application also saves the data to a CSV file.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [License](#license)

## Features

- Fetches current weather data for multiple cities.
- Displays the weather information in a Tkinter table.
- Saves the weather data to a CSV file.

## Technologies Used

- Python
- Tkinter
- Requests
- Pandas

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/hasan0v/weather-information-app.git
    ```

2. Navigate to the project directory:
    ```sh
    cd weather-information-app
    ```

3. Set up a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

5. Replace the placeholder `'your_access_key'` in the script with your actual Weatherstack API access key:
    ```python
    params = {
        'access_key': 'your_access_key',
        'query': c,
    }
    ```

6. Run the application:
    ```sh
    python app.py
    ```

## Usage

1. **Run the Application**: When you run the script, a window will open displaying the weather information for various cities in Azerbaijan.

2. **View Weather Data**: The weather data for each city, including the temperature, description, and cloud cover, will be displayed in a table.

3. **Save to CSV**: The weather data is automatically saved to a file named `hava_melumati.csv` in the project directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please open an issue first to discuss what you would like to change.

If you find this project useful, please consider giving it a star on GitHub. Your feedback and support are greatly appreciated!
