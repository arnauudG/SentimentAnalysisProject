import os
import sys
# Get the current directory
current_dir = os.path.abspath('')

# Add the src directory to the system path
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

# Use a pipeline as a high-level helper
from transformers import pipeline
from preprocessing_reviews import preprocessing_review as pr

def predict_sentiment_review(review: str) -> str:

    review = pr.remove_html_tags(review)

    pipeline_deBERTa = pipeline("text-classification",
                            model="Kaludi/Reviews-Sentiment-Analysis")
    
    predictions_deBERTa = pipeline_deBERTa(review,
                                           max_length=512,
                                           truncation=True,
                                           padding=True)
    

    return {'review': review,
            'sentiment_predicted': predictions_deBERTa[0]['label'],
            'score': predictions_deBERTa[0]['score']
    }

