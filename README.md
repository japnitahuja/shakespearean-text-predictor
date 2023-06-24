# Bardify: Shakespearean Text Prediction

This project aims to generate text in the style of Shakespearean English using Recurrent Neural Networks. The neural network model is based on an Encoder-Decoder architecture and is trained to predict the next word in a sequence based on the input context.

## Data Collection

All scenes from the Romeo and Juliet play were collected [open sourced shakespearean play archive](https://www.opensourceshakespeare.org/views/plays/play_view.php?WorkID=romeojuliet&Scope=entire&pleasewait=1&msg=pl). Each act and its scenes are stored in `datacollection/scenes`. After collecting the scenes,basic text preprocessing steps were performed as outlined in `datacollection/TextPreprocessor.py`. This involved removing extra spaces, HTML tags, and numbers from the text. Additionally, we removed stage directions that were present in the scenes to focus solely on the dialogue and monologues. The resulting monologues were consolidated into the  `datacollection/allmonologues.txt` file using `datacollection/combine_all_monologues.py`. Each monologue is separated by a new line for ease of use in subsequent data processing and modeling stages. A wordcloud of the monologues can be seen as follows:

![image](https://github.com/japnitahuja/shakespearean-text-predictor/assets/10168783/43d9a9ce-b83b-4e4b-8cdb-2c3679204647)

```
Number of monologues: 638
Number of unique words: 3256
```

## Neural Network Model Architecture

- Embedding Layer: Maps each word in the vocabulary to a dense vector representation of size 300. This layer is initialized with random weights.

- LSTM Layer: A recurrent neural network layer based on the Long Short-Term Memory (LSTM) architecture. It takes the embedded input sequence and processes it to capture the contextual information. The LSTM layer has an input size of 300 and a hidden size of 600.

- Linear Transformation: The hidden state output from the LSTM layer is passed through a linear layer (self.shrink) that reduces the dimensionality from 600 to 300.

- Dropout Layer: Applies dropout regularization to the output of the linear layer with a dropout probability of 0.5. Dropout helps prevent overfitting by randomly setting a fraction of the input elements to zero during training.

- Decode Layer: The output of the dropout layer is fed into a linear layer (self.decode) that predicts the probability distribution over the vocabulary for the next word. The weights of this layer are tied to the embedding layer, ensuring that the embeddings are updated during training

## Training and Prediction

During training, the model takes a sequence of words as input and predicts the next word in the sequence. The parameters of the model are optimized using cross-entropy loss, and gradient descent.

To generate Shakespearean-style text, the model takes a seed sequence as input and recursively predicts the next word based on the previous predictions. This process can be repeated to generate a desired length of text.

## Usage

To run this project, open `Shakespearean_bot.ipynb` on google collab. Run each cell there to train the model and then deploy on flask. Demo of the project is as follows:

https://github.com/japnitahuja/shakespearean-text-predictor/assets/10168783/2dcf4ffb-01fd-472e-ad25-f54ebc9944ba

## Contributing

Contributions to this project are welcome. If you have any ideas or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.




