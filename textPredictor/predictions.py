from tensorflow.keras.models import load_model
import numpy as np
import pickle

model = load_model('nextword.h5')

tokenizer = pickle.load(open('tokenizer1.pkl', 'rb'))

def predict(model, tokenizer, text):
    for i in range(3):
        sequence = tokenizer.texts_to_sequences([text])[0]
        sequence = np.array(sequence)
        preds = model.predict_classes(sequence)
        predicted_word = ""

        for key, value in tokenizer.word_index.items():
            if value == preds:
                predicted_word = key
                break

        print(predicted_word)
        return predicted_word

while(True):
    text = input("enter line: ")
    if text == "stop":
        break
    else:
        try:
            text = text.split(" ")
            text = text[-1]
            text = ''.join(text)
            predict(model, tokenizer, text)
        except:
            continue


