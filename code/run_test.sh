# pre-trained language model
export PLM=../trymore/
export Dataset_Name=ag_news
#Task for AGnews: classify_question_first classify_with_choices_question_first recommend
# which_section_choices which_section classify_with_choices classify
export Task_Name=classify_question_first

# Number of test examples
export N=100

python test.py \
  --model_name_or_path ${PLM} --dataset ${Dataset_Name} --task ${Task_Name} \
  --number_test_examples ${N} --seed 42 --max_new_tokens 1024 \
  --do_sample True --num_beams 10 --num_return_sequences 1 \
  --ground_response_file ground_label.txt --generated_text_file generated_text.txt --answer_file answer.txt