# 2023-USENIX-Educator-Perspectives-of-Exam-Proctoring
This repository contains supplemental material to enable replication of our study as submitted to the [artifact evaluation for USENIX Security 2023](https://www.usenix.org/conference/usenixsecurity23/call-for-artifacts).
These include:

* The complete survey presented to participants as both QSF and .txt files
* Codebooks used for qualitative analysis of free-text responses
* Qualitative coding worksheets with a breakdown of IRR values from each round of coding, and Scripts for computing IRR
* Analysis scripts used to process data including:
  * R scripts for data processing
  * input data files in csv format
* All generated figures included in the paper
* A PDF of the paper itself

## Repository Structure:

* __Survey-Instruments__: The survey as presented to participants as Qualtrics export (QSF) and as a .txt document.
  * QSF-survey-file(s)
  * TXT-survey-file(s)
* __Scripts__ 
  - Quantitative_analysis: *Scripts used for both initial processing of quantitative data, and for exploratory analysis*
    - R_script_files
  - Qualitative_analysis: *Scriptss for assessing qualitative analysis*
    - irr.py
* __Data__
  - Quantitative_data
    - Likert_response_data_files
  - *Qualitative_data
    - Free_text_response_files
    - Qualitative_codebok_files
* __Figures__
  * Rendered_figure_files
  * Table_filies (R script outputs and .tex files)
* __PDFs__
  * USENIX-paper-pdf
  * Arxiv-paper-pdf

## Reference Paper:
David G. Balash, Rahel A. Fainchtein, Elena Korkes, Miles Grant, Micah Sherr, and Adam J. Aviv.
“Educators’ Perspectives of Using (or Not Using) Online Exam Proctoring”.
_Proceedings of the 32nd USENIX Security Symposium (USENIX 2023)._ 

(Extended version avaialble on [arXiv](https://arxiv.org/abs/2302.12936))

