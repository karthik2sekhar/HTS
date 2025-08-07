# HTS Special Rate Eligibility Predictor

This project predicts special rate eligibility for Harmonized Tariff Schedule (HTS) codes using a machine learning model built with PyCaret. It features a FastAPI backend for serving predictions and a Streamlit frontend for user-friendly interaction.

## Features

- **Machine Learning Model:** Trained with PyCaret to predict special rate eligibility.
- **FastAPI Backend:** Exposes a `/predict/` endpoint secured with an API key.
- **Streamlit Frontend:** Simple web interface for entering product and tariff details and viewing predictions.
- **API Key Security:** Only authorized requests can access the prediction endpoint.

## How It Works

1. **User enters HTS and product details** in the Streamlit app.
2. **Streamlit sends the data** to the FastAPI backend.
3. **FastAPI returns the eligibility prediction**.
4. **The result is displayed** in the Streamlit app.

## Getting Started

### Prerequisites

- Python 3.8–3.12
- (Recommended) [Anaconda](https://www.anaconda.com/products/distribution) or `venv` for environment management

### Installation

1. Clone the repo:
    ```sh
    git clone https://github.com/karthik2sekhar/HTS.git
    cd HTS
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Project

1. **Start the FastAPI backend:**
    ```sh
    uvicorn hts_api:app --reload
    ```

2. **Start the Streamlit frontend (in a new terminal):**
    ```sh
    streamlit run frontend.py
    ```

3. Open your browser to [http://localhost:8501](http://localhost:8501) for the frontend.

### API Usage

- **Endpoint:** `POST /predict/`
- **Header:** `x-api-key: htfb-lijm-sdfer-aov`
- **Body Example:**
    ```json
    {
      "Indent": 1,
      "Description": "Sample",
      "Unit_of_Quantity": "kg",
      "Chapter": "01",
      "Country_of_Origin": "USA",
      "heading_code": "0101",
      "subheading_code": "010121",
      "hts_length": 6
    }
    ```

## Project Structure

```
HTS/
├── models/           # Saved PyCaret model
├── hts_api.py        # FastAPI backend
├── frontend.py       # Streamlit frontend
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## License

This project is for educational and portfolio