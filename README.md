# Sentiment Analysis Website

Local Launch:

1. pull repo down to local machine (git clone https://github.com/jinman36/sentiment_analysis.git)
2. install dependendecies as required, requirements.txt supplied for assistance but may need some adjustments (pip install -r requirements.txt)
3. Move into top level file (cd /sentiment_analysis)
4. Run flask operation (flask run)
5. open browser to indicated location (localhost:5500)

MVP:

- Create a flask APP with a user interface
- Capable of taking user text
- Make a call to custom python function to clean, lemmitize, tokenize the user entered data
- Make a call to a custom python fuction to run the model on each submit
- Return the original text, with the prediction on a seperate page
- Console log - X_train, y_train, X_test, y_test data size and statistics
- Console log - model accuracy score for the model type

Extended goal

- Save new text data to pool
- add fuctionality to use different model types to predict sentiment (currently on TFIDF, but incorporate CV, Vader, etc)
- ability to add csv or larger data files
