from cohere_sagemaker.response import CohereObject
from typing import List


class TokenLikelihood(CohereObject):
    def __init__(self, token: str, likelihood: float) -> None:
        self.token = token
        self.likelihood = likelihood


class Generation(CohereObject):
    def __init__(self,
                 text: str,
                 token_likelihoods: List[TokenLikelihood]) -> None:
        self.text = text
        self.token_likelihoods = token_likelihoods


class Generations(CohereObject):
    def __init__(self,
                 generations: List[Generation]) -> None:
        self.generations = generations
        self.iterator = iter(generations)

    def __iter__(self) -> iter:
        return self.iterator

    def __next__(self) -> next:
        return next(self.iterator)
