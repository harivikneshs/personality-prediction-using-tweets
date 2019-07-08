# Personality prediction using user's tweets.
This project aims in identifying one's personality (like introvert,extrovert,judgemental etc.) using his latest tweets

Check 'Building the model.ipynb' jupyter notebook to learn how i built the model. I have used countvectoriser and multilayer perceptron to train the model, feel free to use any other model/vectoriser to improve accuracy and let me know.

The trained model has been saved in 'model.h5' file and vocabulary in 'vocab.pkl', you can use these directly in your model for predicting without training. Check out 'trained_model.py' which uses saved model and vocabulary.

If you like to see how it works download all files to same directory and execute trained_model.py and enter twitter username viola !. Make sure you have installed all required libraries like nltk,keras,sklearn,tweepy. It is preferable to execute the jupyter notebook on cloud.

The Jupyter notebook is also available at
https://www.kaggle.com/harivikneshs/personality-identification-using-twitter-api
