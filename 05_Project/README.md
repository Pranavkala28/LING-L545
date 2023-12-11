# News Category Classification Project

This project is built using a Bidirectional LSTM model that uses fasttext crawl embeddings to classify whether given sentence is one of the four categories, (Politics, Technology, Entertainment, and Business). The input text is first tokenized using Keras Tokenizer and then padded to 150. These tokenized vectors are then passed to Neural Network. The input is passed through different layers of the network and the model predicts the probabilities for each category.
