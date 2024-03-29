"""Predictions for the app with tfidf and bert models"""
from src.preprocess import dataset_dict_bert, get_reviews, text_cleaning, tokenize_data
from src.config import dic_emotions
from src.utils import detect_en, labels, tfidf_vector
from transformers import Trainer
from typing import Tuple


def classify_tfidf(title, tfidf_model):
    """This function will use tfidf vectors and logistic regression model
    to return the emotions"""
    tfidf_vectorizer = tfidf_vector()
    book, data = get_reviews(title)
    book = book.strip()
    if len(data) == 0:
        percentage_emotions = {}
        return book, percentage_emotions
    else:
        data = data[data["reviews"].apply(detect_en)]
        data["cleaned_review"] = data["reviews"].apply(text_cleaning)
        data = data[data["cleaned_review"].map(len) > 0]
        tfidf_vectorizer = tfidf_vector()
        tfidf_vectors = tfidf_vectorizer.transform(data["cleaned_review"])
        predictions = tfidf_model.predict(tfidf_vectors)
        data["predicted_labels_tfidf"] = predictions
        data["predicted_emotion_tfidf"] = data["predicted_labels_tfidf"].map(
            dic_emotions["emotion"]
        )
        percentage_emotions = (
            data["predicted_emotion_tfidf"].value_counts(normalize=True) * 100
        ).to_dict()
        percentage_emotions = {
            k: str(int(round(v, 0))) + "%" for k, v in percentage_emotions.items()
        }
        return book, percentage_emotions


def classify_bert(title: str, trainer: Trainer) -> Tuple[str, dict]:
    """This function will use bert vectoriztion and bert finetuned model
    to return the emotions"""
    book, data = get_reviews(title)
    book = book.strip()
    if len(data) == 0:
        percentage_emotions = {}
        return book, percentage_emotions
    else:
        data = data[data["reviews"].apply(detect_en)]
        my_dataset_dict = dataset_dict_bert(data)
        my_dataset_dict = my_dataset_dict.map(tokenize_data, batched=True)
        predicted_results = trainer.predict(my_dataset_dict["test"])
        predicted_labels = labels(predicted_results)
        data["predicted_labels_bert"] = predicted_labels
        data["predicted_emotion_bert"] = data["predicted_labels_bert"].map(
            dic_emotions["emotion"]
        )
        percentage_emotions = (
            data["predicted_emotion_bert"].value_counts(normalize=True) * 100
        ).to_dict()
        percentage_emotions = {
            k: str(int(round(v, 0))) + "%" for k, v in percentage_emotions.items()
        }
        return book, percentage_emotions
