python tools/preprocess_data.py \
       --input dataset/databricks-dolly-15k_mod.jsonl \
       --output-prefix databricks \
       --vocab-file gpt2/vocab.json \
       --workers 2 \
       --dataset-impl mmap \
       --tokenizer-type GPT2BPETokenizer \
       --merge-file gpt2/merges.txt \
       --append-eod

