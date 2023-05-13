from tqdm import tqdm
import json
from datasets import load_dataset, load_from_disk
import torch
from transformers import LlamaTokenizer, LlamaForCausalLM
import argparse
import os
from template import Inputs_2_Instrcution, Number_2_Word

def parse_args():
    """Command line argument specification"""
    parser = argparse.ArgumentParser(description="The Samples Probability of Large Language Models")

    parser.add_argument(
        "--model_name_or_path",
        type=str,
        default="./vicuna-7b",
        help="The name of test model.",
    )
    parser.add_argument(
        "--dataset",
        type=str,
        default="imdb",
        help="The name of test dataset.",
    )
    parser.add_argument(
        "--task",
        type=str,
        default="Reviewer Opinion bad good choices",
        help="The name of task in dataset.",
    )
    parser.add_argument(
        "--number_test_examples",
        type=int,
        default=1000,
        help="The number of test examples in task.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="The seed of shuffle.",
    )
    parser.add_argument(
        "--max_new_tokens",
        type=int,
        default=20,
        help="Maximum number of new tokens to generate.",
    )
    parser.add_argument(
        "--do_sample",
        type=bool,
        default=True,
        help="Whether to generate using multinomial sampling.",
    )
    parser.add_argument(
        "--num_beams",
        type=int,
        default=5,
        help="Number of beams to use for beam search. 1 is normal greedy decoding",
    )
    parser.add_argument(
        "--num_return_sequences",
        type=int,
        default=1,
        help="The number of model return sequences",
    )
    parser.add_argument(
        "--ground_response_file",
        type=str,
        default="ground_label.json",
        help="The file of original response for input instruction.",
    )
    parser.add_argument(
        "--generated_text_file",
        type=str,
        default="generated_text.json",
        help="The file of model generation text.",
    )
    parser.add_argument(
        "--answer_file",
        type=str,
        default="answer.json",
        help="The file of answer for  generation response.",
    )
    args = parser.parse_args()
    return args

def test(args):

    # load dataset from huggingface
    raw_dataset = load_dataset(args.dataset, split="test")
    # load dataset from local
    # raw_dataset = load_from_disk(args.dataset)
    shuffled_dataset = raw_dataset.shuffle(args.seed)

    # construct prompt for dataset and task
    

    # load model and tokenizer
    tokenizer = LlamaTokenizer.from_pretrained(args.model_name_or_path)
    model = LlamaForCausalLM.from_pretrained(args.model_name_or_path, torch_dtype=torch.float16)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)

    # The response of model for input instruction
    ground_response = []
    original_output = []
    answer = []
    with torch.no_grad():
        for i in tqdm(range(args.number_test_examples)):
            
            tmp_data = list(shuffled_dataset[i].values())
            Input = tmp_data[0]
            Label = tmp_data[1]
            
            ground_response.append(Number_2_Word(Label,args.dataset))
            Input = Inputs_2_Instrcution(Input,args.dataset)
            
            tokenizer_input = tokenizer(Input, return_tensors="pt")
            tokenizer_input_ids = tokenizer_input["input_ids"].to(device)
            
            outputs = model.generate(
                inputs=tokenizer_input_ids,
                max_new_tokens=args.max_new_tokens,
                use_cache=True,
                num_return_sequences=args.num_return_sequences,
                do_sample=args.do_sample,
                num_beams=args.num_beams,
                early_stopping=True,
            )

            generated_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)[0].replace("\n","")
            answer.append(generated_text.split("ASSISTANT:")[-1].replace("\n",""))
            original_output.append(generated_text)
            
    out_dir = os.path.join("result", args.dataset, args.task)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    ground_response_file = os.path.join(out_dir, args.ground_response_file)
    with open(ground_response_file, 'w', encoding='utf-8') as f:
        for response in ground_response:
            f.write(response)
            f.write('\n')

    original_output_file = os.path.join(out_dir, args.generated_text_file)
    with open(original_output_file, 'w', encoding='utf-8') as f:
        for output in original_output:
            f.write(output)
            f.write('\n')

    answer_file = os.path.join(out_dir, args.answer_file)
    with open(answer_file, 'w', encoding='utf-8') as f:
        for text in answer:
            f.write(text)
            f.write('\n')

if __name__ == "__main__":
    args = parse_args()

    test(args)