# Car Price Prediction 

This is a Flask web application that predicts the price of a car based on its specifications using a linear regression model.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/JK1Real/car_price_prediction.git
    ```

2. Navigate to the project directory:

    ```bash
    cd carpriceprediction
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python application.py
    ```

2. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Enter the car details (company, model, year, fuel type, kilometers driven) in the form and click "Predict" to see the estimated price.

## Files

- `app.py`: Contains the Flask application code.
- `Linear regression model.pk1`: Pickle file containing the trained linear regression model.
- `Cleaned Car.csv`: CSV file containing cleaned car data used for prediction.
- `index.html`: HTML template for the web interface.

## Dependencies

- Flask
- pandas
- numpy
- scikit-learn


