import nltk
import os
import pickle
import pandas as pd
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from collections import Counter

import Summarizer
import summarizer_data_utils
import summarizer_model_utils

def processinput(story,headline):
    with open('w2iA.pickle','rb') as handle:
        word2ind=pickle.load(handle)
    with open('i2wA.pickle','rb') as handle:
        ind2word=pickle.load(handle)
    p_texts, p_summaries, w_counted = summarizer_data_utils.preprocess_texts_and_summaries(story,headline,keep_most=False)
    p_texts_clean = []
    p_summaries_clean = []

    #print(p_texts)

    #print(p_summaries)

    for t, s in zip(p_texts, p_summaries):
        if t != [] and s != []:
            p_texts_clean.append(t)
            p_summaries_clean.append(s)


    # converts words in texts and summaries to indices
    c_texts, unknown_w_in_texts = summarizer_data_utils.convert_to_inds(p_texts_clean,word2ind,eos = False)
    c_summaries, unknown_w_in_summaries = summarizer_data_utils.convert_to_inds(p_summaries_clean,word2ind,eos = True,sos = True)

    # model hyperparameters
    num_layers_encoder = 4
    num_layers_decoder = 4
    rnn_size_encoder = 300
    rnn_size_decoder = 300

    batch_size = 32
    epochs = 100
    clip = 5
    keep_probability = 0.8
    learning_rate = 0.0005
    max_lr=0.005
    learning_rate_decay_steps = 100
    learning_rate_decay = 0.90


    pretrained_embeddings_path = '/home/mitali/tf_hub_embedding_headlinesA.npy'
    summary_dir = os.path.join('/home/mitali/tensorboard/headlinesA')

    use_cyclic_lr = True
    inference_targets=True


    summarizer_model_utils.reset_graph()
    summarizer = Summarizer.Summarizer(word2ind,ind2word,'/home/mitali/models/headlines/my_modelA','INFER',num_layers_encoder = num_layers_encoder,num_layers_decoder = num_layers_decoder,batch_size = len(c_texts),clip = clip,keep_probability = 1.0,learning_rate = 0.0,beam_width = 5,rnn_size_encoder = rnn_size_encoder,rnn_size_decoder = rnn_size_decoder,inference_targets = False,pretrained_embeddings_path = pretrained_embeddings_path)
    summarizer.build_graph()
    preds = summarizer.infer(c_texts,restore_path =  '/home/mitali/models/headlines/my_modelA',targets = c_summaries)
    # show results
    at,acs,cs=summarizer_model_utils.sample_results(preds,ind2word,word2ind,c_summaries,c_texts)
    return at,acs,cs
