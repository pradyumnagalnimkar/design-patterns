from abc import ABC, abstractmethod


class TextProcessor(ABC):
    @abstractmethod
    def process_text(self, text):
        pass


class UpperCaseTextProcessor(TextProcessor):
    def process_text(self, text):
        return text.upper()


class LowerCaseTextProcessor(TextProcessor):
    def process_text(self, text):
        return text.lower()


class CapitalizeTextProcessor(TextProcessor):
    def process_text(self, text):
        return text.capitalize()


class TextStrategy:
    def __init__(self, text_processor):
        self.text_processor = text_processor

    def operate_text(self, text):
        return self.text_processor.process_text(text)


input_text = "this is an example text."
strategy = TextStrategy(CapitalizeTextProcessor())
print(strategy.operate_text(input_text))
