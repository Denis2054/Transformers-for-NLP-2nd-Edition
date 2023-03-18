# BONUS : Enjoy the present, explore the future!

<table class="noBorder">
  <tr>
    <td width="50%" height="50%"> 
      <img src="https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Transformers.JPG">
    </td>
    <td valign="top">
      <H2>Features</H2>
      <ul>
      <li> This BONUS directory contains notebooks on SOA transformer functionality </li>
      <li> Each BONUS notebook is related to Transformers for Natural Language Processing, 2nd Edition </li>
      <li> These notebooks focus on OpenAI ChatGPT, davinci, ada, and DALL-E transformer models </li>
      </ul>
    </td>
  </tr>
 </table>
 
 ## Notebooks
 
Here are some tips to get started:

1.To use the OpenAI:
Install Openai. Make sure you have the latest version of pip:
<pre>
```python
!pip install --upgrade pip
!pip install openai.
'''
</pre>
 
2.Make sure to obtain an API key from OpenAI

3.March 2023. ChatGPT is available as GPT-3.5-turbo and GPT-4
You can try either version by specifyling the name of model directly in your code.
as in notebook #4, *Dialog_with_ChatGPT*
Or you can modify the notebooks for your project and add the model as a parameter to call the dialog function:
<pre>
```python
#1.Choose a model that you will use for dialog function in your admin user interface:
#convmodel="gpt-3.5-turbo"
#convmodel="gpt-4"
#2.Call the dialog function with the model you need for a specific task

def dialog(iprompt,convmodel):
    response = openai.ChatCompletion.create(
        model=convmodel,
        messages=iprompt
    )
    return response
 '''
</pre>

You can also run GPT-3, GPT-3.5-turbo, and GPT-4 in the same notebook to compare the outputs and see which model is the best for a project. For that go to notebook #11, *Exploring_GPT_4_API*
 
### 1. [Jump_Starting_ChatGPT_with_the_OpenAI_API.ipynb](https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Jump_Starting_ChatGPT_with_the_OpenAI_API.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Jump_Starting_ChatGPT_with_the_OpenAI_API.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Jump_Starting_ChatGPT_with_the_OpenAI_API.ipynb)

Get started with a ChatGPT API in a few lines of code.

### 2. [Prompt_Engineering_as_an_alternative_to_fine_tuning.ipynb](https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Prompt_Engineering_as_an_alternative_to_fine_tuning.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Prompt_Engineering_as_an_alternative_to_fine_tuning.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Prompt_Engineering_as_an_alternative_to_fine_tuning.ipynb)

Fine-tuning is not always possible nor is it always necessary.
Learn how advanced prompt engineering can help you customize ChatGPT for your project.

### 3. [Speaking_with_ChatGPT.ipynb](https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Speaking_with_ChatGPT.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Speaking_with_ChatGPT.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Speaking_with_ChatGPT.ipynb)

Add speech-to-text and text-to-speech to ChatGPT. A step-by-step process.

### 4. [Dialog_with_ChatGPT.ipynb](https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Dialog_with_ChatGPT.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Dialog_with_ChatGPT.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Dialog_with_ChatGPT.ipynb)

A speech-to-text and text-to-speech to ChatGPT. A one-click function to create an indefinite dialog with ChatGPT(keep an eye on your OpenAI token budget!)

### 5. [Whisper_&_gttS.ipynb](https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Whisper_%26_gttS.ipynb)  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Whisper_&_gttS.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Whisper_&_gttS.ipynb)

gTTS(Google text-to-speech) and Whisper(OpenAI speech-to-text) tools to enhance and use in your conversational AI applications(ChatGPT, davinci, other).


### 6. [ChatGPT_as_a_Cobot_ChatGPT_versus_davinci_instruct.ipynb](https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/ChatGPT_as_a_Cobot_ChatGPT_versus_davinci_instruct.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/ChatGPT_as_a_Cobot_ChatGPT_versus_davinci_instruct.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/ChatGPT_as_a_Cobot_ChatGPT_versus_davinci_instruct.ipynb)

ChatGPT or davinin_instruct? What is best for your project? This notebook deals with one of the many aspects of your choice.

### 7. [GPT_2_&_ ChatGPT_the_Origins.ipynb](https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/GPT_2_%26_ChatGPT_the_Origins.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/GPT_2_&_ChatGPT_the_Origins.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/GPT_2_&_ChatGPT_the_Origins.ipynb)

Let’s go back to the origins to understand ChatGPT. ChatGPT is a sibling of the GPT instruct series.

### 8. [Q&A_DR.ipynb](https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Q%26A_DR.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Q%26A_DR.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Q%26A_DR.ipynb)

A Scientific approach to transformers.

### 9. [Generating_images_with_the_OpenAI_DALL_E_API.ipynb](https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Generating_images_with_the_OpenAI_DALL_E_API.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Generating_images_with_the_OpenAI_DALL_E_API.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Generating_images_with_the_OpenAI_DALL_E_API.ipynb)

DALL-E will take you into the wonderful world of creative image generation. Get started with DALL-E API to create, modify or generate variations of an image.

### 10. [Getting_Started_with_GPT_4.ipynb](https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Getting_Started_with_GPT_4.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Getting_Started_with_GPT_4.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Getting_Started_with_GPT_4.ipynb)

This notebook shows you how to generate programs with GPT-4 and obtain explanations on the SOA GPT models.

### 11. [Exploring_GPT_4_API.ipynb](https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Exploring_GPT_4_API.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Exploring_GPT_4_API.ipynb) [![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/Denis2054/Transformers-for-NLP-2nd-Edition/blob/main/Bonus/Exploring_GPT_4_API.ipynb)

Run OpenAI with the API on GPT-3, GPT-3.5-turbo(ChatGPT), and GPT-4. Find out which one is best for your project!

