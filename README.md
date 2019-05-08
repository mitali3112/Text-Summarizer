# Text-Summarizer
A project to implement extractive Text Summarization Using OCR and Attention NetworksIn this project, we propose to build a model that performs extractive summarization of a news article with the aid of Optical
Character Recognition and Attention Networks. We achieve this by building a model with the algorithms of Recurrent Neural Networks
and Bi-directional Long Short Term Memory. We use Bahadanu Attention with the neural architecture to achieve the Attention
Network. It’s main objective is to summarize the text from an image of an article and display it’s result.

## Getting Started
Basic software requirements-
1. Python 3
2. Anaconda for python 3
3. Tensorflow
4. Create Tensorflow environment
```
conda create -n tensorflow_env tensorflow
conda activate tensorflow_env
```
5. Install pytesseract
6. Install the following:
 - Git
 - Nodejs
 - NPM
 - Bower
7. Only for first time installation
```git clonehttps://github.com/mitali3112/Text-Summarizer.git```
8. Enter the server folder and execute the notebook titled "Text Summarization.ipynb"
-Compile and run all the cells
-Download the dataset from kaggle from the link given below
-Replace the paths in the notebook with relevant paths in your system
-Save the trained model, embeddings and tensorboard paths in your system.
-Train the model and complete executing all the cells
-Save the word vectors in pickle format in the server folder.
-Change the path for the trained model in the file testprocess.py
9. Enter that folder app/
-bower install
-npm install
-node run_app.js
Setup done
10. Keep relevant images or text ready for running the file.


### 
## Running the project
In different terminal tabs (All actvated under tensorflow environment created)
1. Got to app/
```node run_app.js```
2. Go to server/
```python3 server.py```
3.Now go to http://localhost:8000/ and the frontend is there.
4. To launch the tensorboard
```tensorboard --logdir='full path to tensorboard savepath' ```

### Example


## Built With

* Recurrent Neural Networks
* Long Short Term Memory
* Bahadanu Attention
* Adam Optimizer
* Tesseract OCR

## Authors

* **Mitali Sheth** - *Initial work* - [Mitali Sheth](https://github.com/mitali3112/Text-Summarizer)


## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc


