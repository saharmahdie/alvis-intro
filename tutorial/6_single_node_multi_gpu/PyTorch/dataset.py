import torch
from torch.utils.data import Dataset, TensorDataset


class RandomCorpus(TensorDataset):

    def __init__(self, n_sentences, context_size, vocab_size):
        super().__init__(torch.randint(size=(n_sentences, context_size), high=vocab_size))


class RandomDataset(Dataset):

    def __init__(self, size, length):
        self.len = length
        self.data = torch.randn(length, size)
        self.target = self.data.max(1, keepdim=True)[0].sin()

    def __getitem__(self, index):
        return self.data[index], self.target[index]

    def __len__(self):
        return self.len
