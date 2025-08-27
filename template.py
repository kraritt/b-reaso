def parse_example(example: dict[str, str]) -> tuple[str, str, str, str]:
    question = example['question'].replace('\n\n', '\n').strip()
    choices_prompt = ''
    for i in range(6):
        choice = chr(i + ord('A'))
        if example[choice] is not None:
            choices_prompt += f'({choice}) {example[choice]}\n'
        else:
            break
    answer = example['answer'].strip()
    choices_prompt = choices_prompt.strip()
    cot = example['explanation'].strip()
    return question, choices_prompt, answer, cot


def hf_template(example: dict[str, str], use_cot: bool = False, include_ans: bool = False) -> str:
    question, choices_prompt, answer, cot = parse_example(example)

    full_prompt = f'প্রশ্ন: {question}\n{choices_prompt}'
    if include_ans:
        if use_cot:
            full_prompt += f'\nআসুন ধাপে ধাপে এটি নিয়ে ভাবি। \n{cot}\nসঠিক উত্তর：({answer})'
        else:
            full_prompt += f'\nসঠিক উত্তর：({answer})'
    else:
        if use_cot:
            full_prompt += ''
    return full_prompt


def openai_template(
    example: dict[str, str], use_cot: bool = False, include_ans: bool = False
) -> str:
    question, choices_prompt, answer, cot = parse_example(example)

    full_prompt = f'প্রশ্ন: {question}\n{choices_prompt}'
    if include_ans:
        if use_cot:
            full_prompt += f'\nআসুন ধাপে ধাপে এটি নিয়ে ভাবি। \n{cot}\nসঠিক উত্তর：({answer})'
        else:
            full_prompt += f'\nসঠিক উত্তর：({answer})'
    else:
        if use_cot:
            full_prompt += '\nআসুন ধাপে ধাপে এটি নিয়ে ভাবি। \n'
        else:
            full_prompt += '\nসঠিক উত্তর：('
    return full_prompt


def anthropic_template(
    example: dict[str, str], use_cot: bool = False, include_ans: bool = False
) -> str:
    question, choices_prompt, answer, cot = parse_example(example)

    full_prompt = f'প্রশ্ন: {question}\n{choices_prompt}'
    if include_ans:
        if use_cot:
            full_prompt += f'\nআসুন ধাপে ধাপে এটি নিয়ে ভাবি। \n{cot}\nসঠিক উত্তর：({answer})'
        else:
            full_prompt += f'\nসঠিক উত্তর：({answer})'
    else:
        if use_cot:
            full_prompt += ''
    return full_prompt


def google_template(
    example: dict[str, str], use_cot: bool = False, include_ans: bool = False
) -> str:
    question, choices_prompt, answer, cot = parse_example(example)

    full_prompt = f'প্রশ্ন: {question}\n{choices_prompt}'
    if include_ans:
        if use_cot:
            full_prompt += f'\nআসুন ধাপে ধাপে এটি নিয়ে ভাবি। \n{cot}\nসঠিক উত্তর：({answer})'
        else:
            full_prompt += f'\nসঠিক উত্তর：({answer})'
    else:
        if use_cot:
            full_prompt += '\nআসুন ধাপে ধাপে এটি নিয়ে ভাবি। \n'
        else:
            full_prompt += '\nসঠিক উত্তর：('
    return full_prompt
