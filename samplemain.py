# -*- coding: utf-8 -*-
"""MTSI_BERT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1y4DqpEgscfATFaAbCPGEaeP2PtBSsoyh
"""

import torch
from pytorch_transformers import BertTokenizer, BertModel
# OPTIONAL: if you want to have more information on what's happening, activate the logger as follows
import logging
# Debugging
import pdb

#logging.basicConfig(filename='MTSI_log.txt', level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

#check GPU
if(torch.cuda.is_available()):
  dev = 'cuda'
  device_id = torch.cuda.current_device()
  torch.cuda.device(device_id)
  device_count = torch.cuda.device_count()
  device_name = torch.cuda.get_device_name(device_id)
  print('Currently active: ' + device_name + '(id='+ str(device_id) + ')\n' +\
        '# of devices: ' + str(device_count))
else:
  dev = 'cpu'
  print('CUDA not active')


# Load pre-trained model tokenizer (vocabulary)
# from URL: https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-vocab.txt
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokenized_text = tokenizer.tokenize("[CLS] It's me, [SEP] Mario![PAD]")
#tokenized_text[5] = '[MASK]'
print(tokenized_text)

# Convert tokens to vocabulary indices
indexed_tokens = tokenizer.convert_tokens_to_ids(tokenized_text)
print(indexed_tokens)

# Create tensor for indeces
tokens_tensor = torch.tensor([indexed_tokens])

# Define sentence indeces A and B (must be a LongTensor)
segments_tensor = torch.zeros(len(tokenized_text), dtype=torch.long)
print(tokens_tensor)
print(segments_tensor)

#pdb.set_trace()
#get BertModel hidden states

model = BertModel.from_pretrained('bert_base_uncased')
model.eval()

#put everything on GPU if active
model.to(dev)
tokens_tensor = tokens_tensor.to(dev)
segments_tensor = segments_tensor.to(dev)

#deactivate the gradient graph in eval script
with torch.no_grad():
  #encoded_layers, pooled_output = model(tokens_tensor, segments_tensor)
  model(tokens_tensor, segments_tensor)
#print(encoded_layers)

print(len(encoded_layers))
print(encoded_layers[0].shape)
print(pooled_output.type())
print(pooled_output.shape)