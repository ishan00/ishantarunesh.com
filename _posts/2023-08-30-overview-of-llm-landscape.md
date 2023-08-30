---
title: 'Overview of LLM landscape: Usage, latency, pricing and more.'
layout: post
date: 2023-08-30 14:00 +0530
tags: technical
permalink: overview-of-llm-landscape
---

## Introduction

With an array of large language models (LLMs) available today, selecting
the right one for your specific use case can be daunting. Each model
comes with its trade-offs. By understanding the trade-offs involved in
the mode of usage, latency, pricing, and overall performance, you\'ll be
empowered to make informed decisions about the selection. In this post,
we will list and compare various large language models, delving into
their respective strengths, limitations, and feasibility for different
applications. We have clustered the model into groups based on how one
can access them. Let\'s go over the groups one-by-one.

## Private models available through API

The first cluster of models that we will cover are models that are
available as an API. The model weights aren\'t exposed to the public.
This includes models from OpenAI, Cohere, and Vertex AI.

[OpenAI](https://openai.com/) is at the forefront of
developing large language models, with GPT-4 being its most powerful
offering. GPT-4 is available on the
[web](https://chat.openai.com/) at a \$20/month
subscription, but the API access is still on the waitlist. The other
flagship models for completion (text-davinci-002, text-davinci-003) and
chat (gpt-3.5-turbo) are available on the web and as an API.

[Cohere](https://cohere.com/) offers multiple flagship
models for specialized use cases such as classification, embeddings,
summarisation, and reranking apart from the generation model. Using a
specialized model, for example, for classification, works better than
using the generation model with classification examples given in the
prompt. Similar to OpenAI, these models can be accessed through API.
Cohere also uniquely offers [fine-tuning models on your own
dataset](https://docs.cohere.com/docs/training-custom-models).

[Vertex AI](https://cloud.google.com/vertex-ai) (ML
platform within Google Cloud Platform) upgraded their offerings with the
latest released [PaLM
2](https://blog.google/technology/ai/google-palm-2-ai-large-language-model/)
models. PaLM 2 models are multilingual and also explicitly trained for
reasoning and coding application. The family of the model consists of 4
different models --- Gecko, Otter, Bison, and Unicorn (in increasing
order of size). The largest publicly available model is Bison, and can
be accessed as an API through GCP.

There are multiple other private models that are still in BETA. The
companies developing them aren\'t providing API access yet. In the
future, we can expect these models with an API-type access as well once
the companies figure out their business models. We\'ll list down some
models that fall into this category

[Claude](https://www.anthropic.com/index/introducing-claude),
famously called the rival of ChatGPT from the company Anthropic has been
trained to perform well in language generation, information retrieval,
and assisting with code writing. There is a waitlist for using Claude,
and most likely the, access is currently being granted to organizations
for the partner program. However, Claude is also available as a [slack
bot](https://www.anthropic.com/claude-in-slack) for trying
out.

Inflection AI, launched its super powerful personal assistant named
[Pi](https://heypi.com/talk). The model is available for
demo on their [website](https://heypi.com/talk) and also
through Whatsapp, Instagram, or SMS. There is no mention of an API
access yet, so likely it isn\'t going to be available for commercial use
anytime soon. Pi is closer to a personal assistant than any other model
in the post. It claims to be more kind and helpful in conversations.

[LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/)
is a family of foundational models ranging from 7B to 65B parameters
released by META. Among the models in the list, this has only been
released for research purposes and not commercial use. The model weights
can be downloaded upon filling out a
[form](https://docs.google.com/forms/d/e/1FAIpQLSfqNECQnMkycAp2jP4Z9TFX0cGR4uf7b_fBxjY_OjhJILlKGA/viewform).
Despite being smaller in size, LLaMA and models based on it (Alpaca and
Vicuna) are highly powerful in their generation quality.

### Open-source models

The second cluster of models are models that are released as
open-source. These models are available for download through the
huggingface hub. However, due to their size, some models are still
better off being used through an API than running locally.

Google released the Flan family of models trained using the novel method
of instruction tuning over pre trained T5 or BERT. We include the
[Flan-T5](https://huggingface.co/docs/transformers/model_doc/flan-t5)
models in our article for analysis. These are the smallest models in the
post ranging from 80M (flan-t5-small) to 11B (flan-t5-xxl), and can run
on a laptop locally.

[MPT](https://www.mosaicml.com/blog/mpt-7b) is a family of
LLM models released by Mosaic ML (now part of Databricks). Open-sourced
and available for commercial use, MPT models are trained on large
amounts of data (1T) and offer large context windows (65K for
MPT-7B-StoryWriter-65k+). The 7B parameter models is available in
multiple formats (MPT-7B, MPT-7B-Instruct, MPT-7B-Chat) and
[outperforms](https://assets-global.website-files.com/61fd4eb76a8d78bc0676b47d/64547b623e779885728099ec_image5.png)
all other models in the same parameter range.

[EleutherAI](https://www.eleuther.ai/) is a non-profit
research institute that evolved from a Discord server. It\'s a group of
full-time and part-time researchers, along with volunteers, that aim to
democratize the development of LLMs. Models include GPT Neo family with
sizes ranging from 125M to 20B.

The [BLOOM](https://huggingface.co/bigscience) family of
models, by BigScience, results from the largest collaboration of AI
researchers worldwide. With 176 billion parameters, BLOOM can generate
text in 46 languages. They offer various model sizes ranging from 560M
to 176B. BLOOM also offers a chat model along with a completion model.

[Vicuna](https://lmsys.org/blog/2023-03-30-vicuna/) is an
open-source chatbot model trained by fine-tuning LLaMA on user-shared
conversations. It claims to perform at 90% of the quality of GPT-4 and
outperform other models while only being 13B in parameter size. The code
and weights are available for use. The online demo can be found
[here](https://chat.lmsys.org/)

[Falcon](https://huggingface.co/blog/falcon) is the most
recently released model in the list, and it tops the [public
leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard).
Released by Technology Innovation Institute (TII), the models come with
Apache 2.0 software license that opens it up for public and commercial
use.

Next we move on the analysing these models on their pricing, latency and
mode of usage (local, hosting, API).

### Analysis of model trade-offs (usage, latency and pricing)

The three models (OpenAI, Cohere and Vertex AI) available through API
follow a pay-per-usage pricing model and have competitive pricing.

For OpenAI, the cost is \$0.02/1000 tokens for text-davinci-003 and
\$0.002/1000 tokens for text-davinci-002 and gpt-3.5-turbo. Due to
excessive use however, OpenAI models offer poor guarantee on latency.
For Cohere, the generate API costs \$0.015/1000 tokens (equivalent of
\$0.02 for text-davinci-003). It's recommended to use task specific APIs
for classify, summarise rather than the generate API as task specific
models are more accurate and lower priced (\$0.2 for 1000
classifications). For Vertex AI, The cost is \$0.05/1000 tokens
(considering 5 character per token) for complete (text-bison-001) and
\$0.025/1000 tokens for chat.

Models available on Huggingface hub fall into two buckets.

-   Models small enough to run locally.
-   Models that require API inference or Hosting.

The first bucket includes flan models, gpt-neo models, falcon-7b, MPT-7B
etc. These can run on a local PC (\~16GB of RAM) which reduces inference
time drastically (no API call). From the group falcon-7b and MPT-7B
model are good at generation task.

The models in the second bracket can be accessed through their public
API for free. Popular models on the hub suffer the same problem of
contention and thus the API call take \~30s to complete. When using the
free API it is advisable to use slightly smaller model within the model
family. HF hub doesn't keep all models loaded for the inference so the
first call to the API might include the time for loading the model in
memory (the latency analysis here will depend on how frequent the API
calls are for the use case)

In order to alleviate the issues of latency, one can host these models
on AWS, GCP etc. Huggingface also allows quick integration to these
cloud providers through it's [inference
endpoints](https://huggingface.co/docs/inference-endpoints/index).
Based on the region of use, one can choose a nearby server location. The
pricing here is based on the hardware and users are charged on a hourly
basis. The cheapest offering being \$0.6/hr for a NVIDIA T4 (14GB) to
\$45.0/hr for 8 NVIDIA A100 (640GB).

API calls to GPT-4 require \>20s and deem it unsuitable for real-time
interactions. If your use-case is time critical (such as real time
conversations or chat), GPT-4 is unsuitable. However it's the best
offering for offline tasks (summarisation, storytelling etc).

If a larger context window is needed, MPT-7B-StoryWriter-65k+ offers a
context window of 65k (even more than text-davinci-003). If your use
case involves language other than english, BLOOM and Vertex AI supports
multilingual models.

The choice of models depends on the task at hand. Within the subset of
local models, if you want really fast inference time for generation
task, it is highly recommended to use falcon-7b. and for simpler task
such as classification, one can use even smaller models such as Flan-T5.
If time is not critical for your application, text-davinci-002 performs
well with few-shot prompting on a classfication task. For generation
however it suffers and we recommend using text-davinci-003.

If you are planning to host a model from huggingface hub, the choice of
model will also depend on the the hardware requirement (pricing
proportional to hardware). In that case we can look at models in
different parameter ranges. For models with parameters of order 7B,
falcon-7b is highly recommended.

If you are looking to use models just for personal use (as a search
engine or to get basic task done), you should checkout Pi, Claude and
GPT-4 (web)