from django.shortcuts import render
from .forms import PredictionForm
from .models import AI_Detection
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from django.conf import settings
import os
import pickle

def load_pretrained_model():
    model_path = "C:/Users/puja2/Downloads/ai_detection_model.h5"
    return load_model(model_path)

model = load_pretrained_model()
with open('C:/Users/puja2/Downloads/tokenizer_file.pkl', 'rb') as tokenizer_file:
    tokenizer = pickle.load(tokenizer_file)

def make_prediction(model, text):
    predictions = {}
    for i in text:
        input_sequence = tokenizer.texts_to_sequences([i])
        padded_sequence = pad_sequences(input_sequence, padding='post', maxlen=1000)
        prediction = model.predict(padded_sequence)
        predictions[i] = float(prediction[0][0]*100)
    return predictions

def predict_view(request):
    form = PredictionForm(request.POST or None)
    prediction_result = None

    if request.method == 'POST' and form.is_valid():
        text_input = form.cleaned_data['text_input']
        text_input = text_input.split('. ')[:-1]
        #print(text_input)

        prediction_result = make_prediction(model, text_input)

    return render(request, 'predict.html', {'form': form, 'prediction_result': prediction_result})