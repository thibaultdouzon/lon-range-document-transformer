# coding=utf-8
# Copyright 2018 The Microsoft Research Asia Linformer Team Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" Tokenization class for model Linformer."""


from transformers.utils import logging
from transformers.models.bert.tokenization_bert_fast import BertTokenizerFast
from .tokenization_linformer import LinformerTokenizer


logger = logging.get_logger(__name__)

VOCAB_FILES_NAMES = {"vocab_file": "vocab.txt", "tokenizer_file": "tokenizer.json"}

PRETRAINED_VOCAB_FILES_MAP = {
    "vocab_file": {
        "linformer-base-uncased": "https://huggingface.co/microsoft/layoutlm-base-uncased/resolve/main/vocab.txt",
        "linformer-large-uncased": "https://huggingface.co/microsoft/layoutlm-large-uncased/resolve/main/vocab.txt",
    },
    "tokenizer_file": {
        "linformer-base-uncased": "https://huggingface.co/microsoft/layoutlm-base-uncased/resolve/main/tokenizer.json",
        "linformer-large-uncased": "https://huggingface.co/microsoft/layoutlm-large-uncased/resolve/main/tokenizer.json",
    },
}


PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES = {
    "linformer-base-uncased": 512,
    "linformer-large-uncased": 512,
}


PRETRAINED_INIT_CONFIGURATION = {
    "linformer-base-uncased": {"do_lower_case": True},
    "linformer-large-uncased": {"do_lower_case": True},
}


class LinformerTokenizerFast(BertTokenizerFast):
    r"""
    Constructs a "Fast" LinformerTokenizer.

    :class:`~transformers.LinformerTokenizerFast` is identical to :class:`~transformers.BertTokenizerFast` and runs
    end-to-end tokenization: punctuation splitting + wordpiece.

    Refer to superclass :class:`~transformers.BertTokenizerFast` for usage examples and documentation concerning
    parameters.
    """

    vocab_files_names = VOCAB_FILES_NAMES
    pretrained_vocab_files_map = PRETRAINED_VOCAB_FILES_MAP
    max_model_input_sizes = PRETRAINED_POSITIONAL_EMBEDDINGS_SIZES
    pretrained_init_configuration = PRETRAINED_INIT_CONFIGURATION
    slow_tokenizer_class = LinformerTokenizer
