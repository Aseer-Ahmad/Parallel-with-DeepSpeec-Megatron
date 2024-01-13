python tools/preprocess_data.py \
       --input dataset/databricks-dolly-15k.jsonl \
       --output-prefix my-gpt2 \
       --vocab-file gpt2/vocab.json \
       --dataset-impl mmap \
       --tokenizer-type GPT2BPETokenizer \
       --merge-file gpt2/merges.txt \
       --append-eod 



