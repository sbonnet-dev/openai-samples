#!/bin/sh

export OPENAI_API_KEY="sk-XXXXXXXXXXX"

openai tools fine_tunes.prepare_data -f ./dataset.jsonl
openai api fine_tunes.create -t "dataset_prepared.jsonl"
openai api completions.create -m curie:ft-personal-2023-01-14-13-11-07 -p "Whos is Yrag?"
