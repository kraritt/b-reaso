![image](https://github.com/user-attachments/assets/54d940ac-7d33-441c-91e6-03279a2403e6)


<p align="center">
   🤗 <a href="https://huggingface.co/datasets/krarit/b-reaso" target="_blank">Hugging Face</a>  • 📃 <a href="" target="_blank">Paper</a> 
</p>

## B-REASO

This repo contains the evaluation code for the EMNLP Findings '25 paper ["B-REASO: A Multi-Level Multi-Faceted Bengali Evaluation Suite for Foundation Models"]().

## Introduction

We introduce B-REASO, the first complete Bengali evaluation suite designed to fully evaluate LLMs' advanced knowledge and reasoning skills in a Bengali environment, in an effort to close the gap between Bengali LLM development and assessment. B-REASO comprises 13497 multiple-choice test questions covering 50 different fields, from science and engineering to the humanities. Middle school, high school, college, and professional exams are the four difficulty levels from which the questions are gathered. We also provide B-REASO HEAVY as an accompanying benchmark, which is a subset of B-REASO's most difficult tasks that need very sophisticated thinking skills to complete, such college physics and advanced mathematics. With an accuracy of 48.53\%, B-REASO HEAVY is the first Bengali benchmark at this level and one of the few benchmarks for advanced reasoning where Gemini-1.5-Pro-002 still has trouble.

## Corpus
B-REASO is a Bengali educational assessment benchmark for large language models, covering 13,497 multiple-choice questions in 50 different subjects, divided into 4 levels of difficulty. More details can be found in [Hugging Face](https://huggingface.co/datasets/krarit/b-reaso).

## Leaderboard


| Model                  | Average                   | Social Science            | STEM                      | Humanities                | Bangladesh Specific       | Other                     |
| ---------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- | ------------------------- |
|                        | AO \| CoT                 | AO \| CoT                 | AO \| CoT                 | AO \| CoT                 | AO \| CoT                 | AO \| CoT                 |
|  |                           |                           |           *Proprietary Models*                |                           |                           |                           |
| **Claude-3.5-Sonnet**  | **68.53** \| **70.91**         | **74.73** \| **77.45**         | **49.21** \| **56.83**         | **72.34** \| **74.12**         | **83.06** \| **81.97**         | **63.29** \| **64.18**         |
| <ins>Gemini-1.5-Pro-002</ins>     | <ins>62.03 \| 64.75</ins> | <ins>69.72 \| 71.63</ins> | <ins>42.42 \| 49.27</ins> | <ins>66.76 \| 68.91</ins> | <ins>82.33 \| 80.15</ins> | <ins>48.91 \| 53.69</ins> |
| GPT-4o                 | 54.98 \| 59.12            | 61.02 \| 64.77            | 36.88 \| 44.95            | 57.03 \| 59.82            | 76.66 \| 74.31            | 43.31 \| 49.75            |
| Amazon-Nova-Pro        | 51.62 \| 52.87            | 58.23 \| 59.11            | 36.98 \| 41.35            | 50.11 \| 51.06            | 74.12 \| 72.89            | 38.65 \| 39.94            |
| Palmyra-X-004          | 49.85 \| 50.68            | 55.52 \| 56.37            | 35.91 \| 39.12            | 47.13 \| 48.95            | 72.85 \| 70.64            | 37.83 \| 38.52            |
| PaLM-2                 | 47.01 \| 46.83            | 52.12 \| 52.89            | 33.84 \| 36.15            | 47.26 \| 47.81            | 66.67 \| 63.42            | 35.17 \| 34.88            |
| Jamba-1.5-Large        | 47.01 \| 47.95            | 52.12 \| 53.64            | 33.84 \| 36.02            | 47.26 \| 48.97            | 66.67 \| 63.91            | 35.17 \| 36.21            |
| Solar-Pro              | 44.60 \| 44.33            | 41.83 \| 43.12            | 30.12 \| 32.87            | 40.92 \| 40.63            | 73.54 \| 71.85            | 36.58 \| 36.88            |
|  |                           |                           |            *Open-Weight Models*               |                           |                           |                           |
| **DeepSeek-v3**        | **61.74** \| **63.87**         | **65.82** \| **67.95**         | **46.22** \| **52.11**         | **64.13** \| **65.84**         | **78.62** \| **76.43**         | **53.91** \| **57.02**         |
| <ins>Llama-3.1-405B-Inst.</ins>   | <ins>55.35 \| 57.89</ins> | <ins>58.12 \| 60.34</ins> | <ins>39.46 \| 44.72</ins> | <ins>57.18 \| 59.03</ins> | <ins>74.87 \| 74.62</ins> | <ins>47.12 \| 50.84</ins> |
| DBRX-Instruct          | 44.66 \| 45.71            | 47.22 \| 48.03            | 31.14 \| 34.92            | 42.96 \| 43.75            | 68.15 \| 66.24            | 33.85 \| 35.81            |
| Arctic-Instruct        | 43.00 \| 43.65            | 45.36 \| 45.91            | 28.07 \| 30.45            | 42.12 \| 42.88            | 65.15 \| 63.07            | 34.28 \| 34.94            |
| Gemma-7B               | 41.92 \| 40.15            | 47.08 \| 46.22            | 32.03 \| 32.14            | 43.52 \| 42.37            | 57.51 \| 54.69            | 29.45 \| 28.53            |
| Command-R              | 37.62 \| 37.84            | 36.74 \| 36.95            | 23.15 \| 24.83            | 33.41 \| 33.62            | 63.02 \| 61.15            | 31.77 \| 32.65            |
| Yi-6B                  | 36.43 \| 35.67            | 37.12 \| 36.45            | 21.74 \| 23.11            | 37.22 \| 36.84            | 52.86 \| 50.77            | 33.21 \| 32.38            |
| Qwen1.5-7B             | 35.19 \| 35.92            | 36.83 \| 38.14            | 26.06 \| 28.33            | 31.17 \| 31.45            | 51.39 \| 49.12            | 30.48 \| 31.56            |
| Phi-2                  | 35.18 \| 33.15            | 37.27 \| 35.89            | 27.93 \| 24.76            | 36.81 \| 34.12            | 46.68 \| 43.95            | 27.22 \| 26.03            |
| Mistral-7B-v0.1        | 33.53 \| 34.88            | 36.51 \| 36.72            | 27.82 \| 29.65            | 38.12 \| 38.04            | 35.02 \| 33.41            | 30.19 \| 32.18            |
| OLMo-7B                | 26.27 \| 25.63            | 28.01 \| 27.45            | 20.83 \| 20.12            | 24.89 \| 23.91            | 33.54 \| 31.87            | 24.06 \| 24.20            |

## Citation

If you like, please cite the paper- here is the bibtex file:

```
@inproceedings{
hosain2025breaso,
title={B-{REASO}: A Multi-Level Multi-Faceted Bengali Evaluation Suite for Foundation Models},
author={Md Tanzib Hosain and Md Kishor Morol},
booktitle={The 2025 Conference on Empirical Methods in Natural Language Processing},
year={2025}
}
```
