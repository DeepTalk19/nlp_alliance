#import libraries
from transformers import LayoutLMv2Processor, LayoutLMv2ForQuestionAnswering, set_seed
import torch
from PIL import Image
from transformers import LayoutLMv2Config

from flask import Flask

app = Flask(__name__)

#inference on the image
@app.route('/nlphome/', methods=['GET', 'POST'])
def predict():

	set_seed(88)
	processor = LayoutLMv2Processor.from_pretrained("./layoutlmv2-base-uncased")
	model = LayoutLMv2ForQuestionAnswering.from_pretrained("./2023-01-19 06:06 model Epoch 10 Total-epoch51/")

	image_path = "./sample_data/Cheque309069.jpg"
	image = Image.open(image_path).convert("RGB")
	#specify the question to be answered by the model
	question = "accountno?"
	encoding = processor(image, question, return_tensors="pt")

	outputs = model(**encoding)
	predicted_start_idx = outputs.start_logits.argmax(-1).item()
	predicted_end_idx = outputs.end_logits.argmax(-1).item()
	predicted_start_idx, predicted_end_idx

	predicted_answer_tokens = encoding.input_ids.squeeze()[predicted_start_idx : predicted_end_idx + 1]
	predicted_answer = processor.tokenizer.decode(predicted_answer_tokens)
	return predicted_answer

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8888)
