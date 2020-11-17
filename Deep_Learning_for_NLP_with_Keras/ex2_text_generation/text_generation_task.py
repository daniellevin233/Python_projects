'''

#!/usr/bin/env python
# coding: utf-8

# # Deep Learning with Python - Assignment 2 - Daniel Levin

# # 1 Text Generation

# ###### Verify GPU

# In[1]:


import tensorflow as tf
# device_name = tf.test.gpu_device_name()
# if device_name != '/device:GPU:0':
#   raise SystemError('GPU device not found')
# print('Found GPU at: {}'.format(device_name))


gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    try:
        # Restrict TensorFlow to only use the fourth GPU
        tf.config.experimental.set_visible_devices(gpus[0], 'GPU')

        # Currently, memory growth needs to be the same across GPUs
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        logical_gpus = tf.config.experimental.list_logical_devices('GPU')
        print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
    except RuntimeError as e:
        # Memory growth must be set before GPUs have been initialized
        print(e)


# ## Goal of the assignment
# 

# We are configuring a deep learning network that will learn a language model based on the input texts. The network can be used for text generation by character. 'frankenstein.txt' will be the default input text for this network. Since some of the texts uploaded on Ilias are in German I tried to feed the network by some of them too. I couldn't see any difference in perfomance between German and English, which makes sense knowing that all what the network learns is statistics of the input data. So the result depends significantly on the data the network was fed on. I considered using several texts for training as well but decided not to do it for clearness of evaluation, i.e. the model will imitate the style of the text it's trained on. This means that if different texts will constitute a training input for the network it might get confused which style/lexicon it's imitating. In general this approach might be useful for certain goals. In our case I've chosen to limit the model to one specific text to make the assessment of the model more comprehensible.
# 
# As a side note I'd notice that for this type of learning problem it's quite challenging to come up with a meaningful evaluation method, especially when comparing between two languages.

# The text, on which the network will be trained, should be chosen here:

# In[2]:


# TEXT_FILE = 'texts/frankenstein.txt'
TEXT_FILE = 'texts/Biene Maja.txt'


# ###### Import libraries

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

import keras
from keras import models, layers, metrics, optimizers
from sklearn.model_selection import train_test_split


# # Data preprocessing
# ###### Importing the text for training
# We're reading the text from the previously configured file in variable TEXT_FILE into one string. Upper case is ignored since it doesn't constitute anything meaningful for learning a language model. Moreover it doubles the size of the alphabet which significantly decreases the depth of the language model that's being learned. Newline characters aren't removed because we do want to keep the sequential properties of the text. In other words we want our network to generate a text that has the same layout as the text that was used for training.

# In[4]:


with open(TEXT_FILE, 'r') as f:
    text = f.read().lower()

print('Corpus length:', len(text))


# The corpus length is more than 400000 which should be enough for training a network.

# Now we extract snippets by length 80 (`maxlen`) characters each with every sequence starting after `step` 3 tokens after the previous one. This code fragment is identical to what is shown in chapter 8.1. 

# In[5]:


# the maximal length of characters of each sequence
maxlen = 80

# a new sequence will be sampled every `step` characters
step = 3

# extracted sequences
sentences = []

# the list of 'follow-up' characters - target labels
next_chars = []

for i in range(0, len(text) - maxlen, step):
    sentences.append(text[i: i + maxlen])
    next_chars.append(text[i + maxlen])
    
print('Number of sequences: ', len(sentences))


# Now we're building a list of unique characters in the text in order to index characters.

# In[6]:


# list of unique characters in the text
chars = sorted(list(set(text)))
print('Unique characters: ', len(chars))

# Dictionary mapping characters to their indices according to their order in `chars` list
char_indices = dict((char, i) for i, char in enumerate(chars))


# Next let's one-hot encode the characters into binary matrices.

# In[7]:


x = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for j, char in enumerate(sentence):
        x[i, j, char_indices[char]] = 1
    y[i, char_indices[next_chars[i]]] = 1


# # Building the network
# As a baseline let's take a very straightforward architecture that was proposed by Chollet in chapter 8.1 - one `LSTM` layer followed by a `Dense` classifier and softmax over all possible characters.

# In[8]:


model = keras.models.Sequential()
model.add(layers.LSTM(128, input_shape=(maxlen, len(chars))))
model.add(layers.Dense(len(chars), activation='softmax'))


# Our targets are one-hot encoded, therefore we will use the `categorical_crossentropy` loss during compilation.

# In[9]:


model.compile(loss='categorical_crossentropy', optimizer=optimizers.RMSprop(lr=0.01))


# # Training the language model and sampling from it
# Here we implement the `sample` function identical to what we've seen in Chollet's chapter, namely the imlementation of reweighting of the probability distribution given a certain temperature.

# In[10]:


def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)


# Now we are ready to implement the main loop where we generate text by appending the most recent prediction sampled according to the reweighted distribution to the current text and sampling again and again.
# 
# First let's fit the model.

# In[ ]:


epochs = 1
batch_size = 4096

history = model.fit(x, y,
                    batch_size=batch_size,
                    epochs=epochs)


# Second let's implement a function `generate_text` that will generate and append the next `length` predicted characters given a `text` and `start_index`. The sampling is done according to the distribution defined by the `model` with given `temperature` used for reweighting.

# In[ ]:


import random
import sys

def generate_text(text, start_index, temperature=1.0, length=300):
    
    # the window in the text we're currently looking at
    generated_text = text[start_index: start_index + maxlen]
    
    print('--- Generating with seed: "' + generated_text + '"')
    
    sys.stdout.write(generated_text)

    # we generate `length` characters
    for i in range(length):
        sampled = np.zeros((1, maxlen, len(chars)))
        for t, char in enumerate(text):
            sampled[0, t, char_indices[char]] = 1.

        # predict the next character
        preds = model.predict(sampled, verbose=0)[0]
        next_index = sample(preds, temperature)
        next_char = chars[next_index]

        # update the current generated text by appending the sampled char and moving it one char right
        generated_text = generated_text[1:] + next_char

        sys.stdout.write(next_char)
        sys.stdout.flush()
    print()


# Now let's tune the model by using different temperatures and observing the outcome

# In[ ]:


temperatures = np.arange(0.0, 1.5, 0.2)
for temperature in temperatures:
    # Select a text seed at random
    start_index = random.randint(0, len(text) - maxlen - 1)
    generate_text(text, start_index, temperature=temperature)
    


# As we can see from the generated texts high temperature value result in a quite creative text with not existing words that still comply with the phonotactical limits of the language. In contrary low temperature values produce a very predictable and repetitive structures and words, very similar to the training text.

# # 2 Extra Credit: Literature and Computation

# I will relate to the most relevant fragment (in my opinion):
# 
# "
# It's really what people call intuition and make such a fuss about. 
# Intuition is like reading a word without having to spell it out. 
# A child can't do that, because it has had so little experience. 
# But a grown-up person knows the word because he's seen it often before.
# "
# 
# This passage strongly reminds me of what we're trying to achieve when we learn a language model by means of a neural network. We're trying to force the network to learn some kind of intuition about the language it's trained on, just like a child absorbs natural language - by being constantly exposed to linguistical input. So in the sense of statistics humans and networks are similar - the more data they get, the better they learn the model. The only difference (rather enormous, unfortunately for Machine Learning) is that a human being is able to take these statistics a few steps further than the most sophisticated and computationally advanced network as of today. A human is able to interpret such a data and imply in a very natural and so far obscure way how to apply this knowledge to infinite number of different real and abstract life situations. The machines are getting better at this but still far behind us. So the phrase "reading a word without having to spell it out" means that a person doesn't need a numerical (or whatever else) encoding of a word to be able to perceive it. The machines in contrary are helpless without a decent encoding.
# 
# Another parallel to our assignment from this passage is hidden in comparing a child to a neural network at its first epochs. Both don't know much about the language - both just gather some first observations - statistics and context. When a child grows up, its knowledge is more similar to the powerful neural network that contains a comprehensive language model under the hood. But obviously, as I already mentioned, the deep learning, as we are familiar with it today, is quite limited and it cannot top the limitation set by statistics, even when it's not possible for a human to explain it clearly.

# In[ ]:

'''

import numpy as np

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

if __name__ == '__main__':
    print(sample([0.3, 0.4, 0.3]))
    exit()

