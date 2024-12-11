# New Article Summarizer
The **News Article Summarizer** is an application that leverages Transformer models to generate concise and accurate summaries of large news articles. The model has been trained on over 20,000 news articles to ensure high-quality outputs. The application is deployed on an AWS EC2 instance, providing a user-friendly web interface for article summarization. 
The text summariser is hosted at [http://18.217.224.109/](http://18.217.224.109/)

## Features

- High-Quality Summaries: Uses state-of-the-art Transformer models to create accurate and concise summaries.

- User-Friendly Interface: Intuitive web interface built with Flask for easy usage.

- AWS Hosting: Deployed on an AWS EC2 instance for reliable and scalable access.

- Real-Time Processing: Summarizes articles in real-time with low latency.

## Tech Stack

- Frontend: HTML, CSS

- Backend: Flask (Python)

- Model: Transformer-based model

- Hosting: AWS EC2 instance

- Additional Libraries: Pandas (data processing)

## Prerequisites

To set up the project locally, ensure you have the following installed:

- Python 3.8 or later

- Pip (Python package installer)

## Installation

- ### Clone the Repository
```
git clone https://github.com/kishalay2002/Text-Summarizer.git
cd Text-Summarizer
```
- ### Install Dependencies
```
pip install -r requirements.txt
```
- ### Run the Application Locally
```
python app.py
```
The application will be accessible at `http://localhost:5000`

## Usage

- Navigate to the application URL.

- Paste the news article text into the input box.

- Click "Summarize" to generate a summary.

- The summarized text will be displayed below the input box.

## Example Input and Output

### Input:

"Artificial intelligence (AI) is transforming industries around the globe. Companies are investing heavily in AI technologies to enhance efficiency and drive innovation."

### Output:

"AI is transforming industries, with companies investing to enhance efficiency and innovation."

## Future Enhancements

- Add support for summarizing URLs directly.

- Improve the UI for better user experience.

- Implement multilingual summarization capabilities.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
