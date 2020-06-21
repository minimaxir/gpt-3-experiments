**OpenAI researchers today released a paper describing the development of GPT-3, a state-of-the-art language model made up of 175 billion parameters.**

**For comparison, the previous version, GPT-2, was made up of 1.5 billion parameters. The largest Transformer-based language model was released by Microsoft earlier this month and is made up of 17 billion parameters.**

**“GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic,” the researchers stated in their paper. “We find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans.”**

GPT-3 used two significant changes to the Transformer model. First, the researchers compared the output of four Transformer encoders. Each Transformer is unrolled to create a vector of representations which is then lensed together. In this case, the researchers found better results by including four encoders each made up of utterances from Google’s BN-2000 and BN-2100 corpora. Second, three Transformer decoders were added instead of one.

One of the objectives of the new GPT-3 language model was to pick up more synonyms. To do this, the researchers first trained the model on synonyms using the word-level ground truth in the Europarl corpus. A co-training objective function was used to improve the efficiency of this multi-task training.

The researchers believe that the benefits of this model demonstrate how state-of-the-art, deep learning approaches can be used to build language models.

This work to advance GPT began a while back. It was influential upon Deep Mind’s machine learning framework WaveNet, which was released last year. It also inspired the joint work last year from Google, Deep Mind, OpenAI, and others to create WaveNet-like models called Sequence-to-Sequence model families.

Both WaveNet and Sequence-to-Sequence language models have the advantage over architecture which simulate acoustic models, adjusting parameters for input sound waveforms. This process is slower and called audio credit assignment.

GPT’s 1.5 billion parameters is $40-50 each using current services on AWS. GPT-3’s 175 billion parameters comes at a cost of “a bit under” $1,000 using Google’s TPUs (pod three from the seven offered by Google).

---

**OpenAI researchers today released a paper describing the development of GPT-3, a state-of-the-art language model made up of 175 billion parameters.**

**For comparison, the previous version, GPT-2, was made up of 1.5 billion parameters. The largest Transformer-based language model was released by Microsoft earlier this month and is made up of 17 billion parameters.**

**“GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic,” the researchers stated in their paper. “We find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans.”**

On translating large Spanish sentences to English, GPT-3 outranks the previous version, GPT-2, as well as translations from Google’s “Star Trek system.”

As reported by VentureBeat in September, OpenAI’s language model was pre-trained from 6.6 billion words of English Wikipedia spread across 64,000 snippets. The pre-training process took two weeks on 256 GPUs.

In July, researchers from Europe and Canada took language modeling a step further with an OpenAI-like neural network that came up with its own “graphically-rich and semantically coherent language” to describe images. Some of the phrases that came out of the model’s 303 layers were “figures dressed as pinatas walk on a fake metal road” and “a picture of a blimp hovering above a tennis player, whose body appears to be made of two long, vertical rectangles, with different shades of blue horizontal stripes.”

Other notable continents and countries didn’t like their pre-trained phrases being made fun of and soon “started trying to harm our reference sentences by repeatedly translating them.” Two months later, the system’s English-to-phoneme model surpassed the state of the art.

---

**OpenAI researchers today released a paper describing the development of GPT-3, a state-of-the-art language model made up of 175 billion parameters.**

**For comparison, the previous version, GPT-2, was made up of 1.5 billion parameters. The largest Transformer-based language model was released by Microsoft earlier this month and is made up of 17 billion parameters.**

**“GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic,” the researchers stated in their paper. “We find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans.”**

The research is partially available as an open-source package. Some of the code will be available on GitHub and, additionally, researchers have made a small “language kit” consisting of about 100 million words of sentences.

The researchers argue that the greater complexity will help in a number of ways. They said it can enable state-of-the-art performance on sentences with two different meanings (“John is a pig,” which can either describe that the speaker sees John as cunning or a large animal). More complex neural language models will also allow people to generate some sentences that combine words and structures that aren’t normally possible from our underlying lexicon, they said.

“Our eventual goal is to develop a language model which generates fluid, coherent text that is indistinguishable from human-written text,” the researchers wrote. “Our hope is that such a model would contribute to future technologies for personalized and interactive storytelling, responsive computational essays, and fluent generation of natural language from structured data.”

GPT-2 was classed as a deep Gaussian process factor model. We summarized the concept as, each character in a sentence is represented by a latent Gaussian process model, and the one with the highest output is activated to determine the next character in the sentence.

GPT-3 pushes this deeper, and the representation is far more complex because it works for inputs longer than just a single character. They work in relatively similar ways, but GPT-3 is about three times larger in terms of parameter space being explored. As a result, it can yield more fine-grained insights about the sentence structure and context.

To train GPT-3, the researchers pressed it against 21 different benchmarks, among them movie reviews, Stack Overflow question-and-answer pairs and passage-based translations, which tend to be difficult in neural language models.

While this prospect of generating sentences completely out of imagination is a relatively new concern in the field of NLP topics being explored, it isn’t the most unnerving. Indeed, the research paper focused primarily on sentiment classifiers and sentence chunk reordering, drawing limited attention to what else these capabilities could mean for AI models down the road.

Source: This AI Can Now Generate Sophisticated Passages of Text Out of Sentence Structure and Context | Google Blog

Advertisements

---

**OpenAI researchers today released a paper describing the development of GPT-3, a state-of-the-art language model made up of 175 billion parameters.**

**For comparison, the previous version, GPT-2, was made up of 1.5 billion parameters. The largest Transformer-based language model was released by Microsoft earlier this month and is made up of 17 billion parameters.**

**“GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic,” the researchers stated in their paper. “We find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans.”**

“In touting our replacing of nouns by verbs, we did not mean to imply that it could not have been done by humans but ourselves undertaking composition,” Mark Zuckerberg wrote in a Facebook post. “I would like to clear up any possible misconceptions that this means our platform, or Facebook, is uncreative. That isn’t what the sentence indicated, as clear as it could have been, given TLDR attention spans, and we are sorry for any confusion there. Our apologies if we fumbled a punt; unlike bots, humans aren’t perfect.”

---

**OpenAI researchers today released a paper describing the development of GPT-3, a state-of-the-art language model made up of 175 billion parameters.**

**For comparison, the previous version, GPT-2, was made up of 1.5 billion parameters. The largest Transformer-based language model was released by Microsoft earlier this month and is made up of 17 billion parameters.**

**“GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic,” the researchers stated in their paper. “We find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans.”**

The researchers note that they intend for the model to be used in provably-correct systems that carry out tasks compelled by law and policy, “if we have a nice model and a nice task and we know exactly what the task is,” explained Ian Goodfellow, a research scientist and one of the paper’s co-authors. Wrong or inappropriate actions, Goodfellow said, are just the beginning of a checklist of the issues that have to be analyzed when releasing a human-level model.

The difference between a GPT-2 and GPT-3 model is that GPT-3 is able to understand the context in which a question is asked, similar to how machine translation systems have improved during the past few years. Google Translate, for example, can now determine the type of query people are asking, from giving a simple definition of a word to answering complex questions in the form of a natural language translation.

A notable example can be found in a description of a recent paper about GPT-3 that OpenAI posted on its website. A journalist uncovered an error in the paper, but she was wrong about the direction of the error.

“The model responded by performing an arithmetic operation that was similar but not identical to the one that the journalist was expecting,” the description said. “By predicting error and reasoning about it, GPT-3 was able to come up with a different but correct response even though it had never specifically seen that operation before.”

Goodfellow said the research team didn’t specifically test for this re-deployable ability; they only tuned parameters for specific tasks such as translation or natural language tasks. However, he noted that the system is capable of re-deploying functions across all tasks, including synthesis.

It is also said that machine learning models not only have to go over language models, but the language model is currently the model to beat, since it is a key component in creating applications that can build off of language capabilities, such as voice assistants that use dialogue.

“The NLP community has been outperformed by the translation community for many years now,” Goodfellow said. “The next big breakthrough in NLP will probably be done using a complex model for generative capacities.”

Goodfellow, who joined OpenAI after the formation of the nonprofit startup in December 2015, used to work at Google Brain until early

---

**OpenAI researchers today released a paper describing the development of GPT-3, a state-of-the-art language model made up of 175 billion parameters.**

**For comparison, the previous version, GPT-2, was made up of 1.5 billion parameters. The largest Transformer-based language model was released by Microsoft earlier this month and is made up of 17 billion parameters.**

**“GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic,” the researchers stated in their paper. “We find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans.”**

Interested in working with this exciting natural language processing technology? OpenAI is opening-source for your use. It’s now available as a managed service online.

---

**OpenAI researchers today released a paper describing the development of GPT-3, a state-of-the-art language model made up of 175 billion parameters.**

**For comparison, the previous version, GPT-2, was made up of 1.5 billion parameters. The largest Transformer-based language model was released by Microsoft earlier this month and is made up of 17 billion parameters.**

**“GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic,” the researchers stated in their paper. “We find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans.”**

Like past iterations of the GPT family of language models, GPT-3 is a simple stack of several recurrent neural networks coupled with the OpenAI Recurrent Convolutions library. GPT-3 expands upon GPT-2 with a wide deployment of two new components: quotation encodings and relations between variables and previous outputs.

“Prior to GPT-3, these encodings were designed for our internal use, so we had no strong theoretical foundation for expected improvements in language model performance,” the researchers explained. “We now have evidence that the GPT-3 gains achieved through these components are correlated with scores on standard NLP performance benchmarks.”

The researchers also found that the robustness and composability of recurrent neural network architectures made it possible to rapidly and efficiently attach and test different components of GPT-3.

All in all, the assembly of GPT-3 appears to be far more complicated than the general case of Read full article…

Source: Android Authority

---

**OpenAI researchers today released a paper describing the development of GPT-3, a state-of-the-art language model made up of 175 billion parameters.**

**For comparison, the previous version, GPT-2, was made up of 1.5 billion parameters. The largest Transformer-based language model was released by Microsoft earlier this month and is made up of 17 billion parameters.**

**“GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic,” the researchers stated in their paper. “We find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans.”**

The paper provides an overview of this model and details some of the experiments performed. OpenAI applied GPT-3 to questions in the TRAINS 2014 CRF question-answering dataset on questions with three answer choices. Here, GPT-3 outperformed previous models, indicating that it “can achieve high accuracy with simple supervision.”

To more directly evaluate performance of systems such as GPT-3, the researchers evaluate whether similar questions elicit similar responses and, if this is true, whether answers to questions are varied. They found that the architectures of variable word-level translation models’ answer kernels scale immensely well with vocabulary, but the mouthpiece kernels do not; the mouthpiece kernels were found to only be useful at a few thousand words. This has damaging implications for some of the translations performed by GPT-2, which gain their expressive power by modeling all possible output combinations at test-time.

“At this point, we cannot claim that the expressive power of Transformer models is all in the mouthpieces,” the researchers wrote. “It’s possible that Transformer architectures benefit so much from parallelism that they are difficult to scale even with high reps. This difference between interpretability and computational tractability has been observed in the software engineering literature. On the other hand, the fact that specialized versions of N-gram models obtain competitive performance on evaluation metrics suggests that mouthpieces may not be critical for capturing complex correspondences in the data.”

OpenAI also asked 20 people to evaluate English generated by GPT-2 and GPT-3. Based on these judgments, GPT-3 fares worse than human-written work in all categories except article readability. However, the readability category is controversial, as some people judge worse than human-written material and others judge the same.

“It seems that there isn’t a 100% agreement among people on the system’s quality, but it’s clear that the representation used by our model does not map unambiguously to the intentions of a human writer,” the researchers wrote. “Nevertheless, this is our starting point for understanding how GPT-3 generalizes and we plan to investigate a wide range of extensions to discover techniques that can improve expressivity.”

The paper includes various other results as well as related work. We'll update the story with OpenAI comments on the technique it used to evaluate language models in the

---

**OpenAI researchers today released a paper describing the development of GPT-3, a state-of-the-art language model made up of 175 billion parameters.**

**For comparison, the previous version, GPT-2, was made up of 1.5 billion parameters. The largest Transformer-based language model was released by Microsoft earlier this month and is made up of 17 billion parameters.**

**“GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic,” the researchers stated in their paper. “We find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans.”**

With this type of language model, everything is generated according to statistical scores. For example, a person’s style differentiates their writing from a stranger. And while reading other authors’ pieces, we decode the writer’s personality, emotions, and memories.

According to the researchers, GPT-3 even outperforms data-augmented language models. “The only known method for surpassing GPT-3 is to acquire additional data from human signaling — which is limited by the rarity of human generation, low volume of communication, and can be viewed as costly for humans,” they said.

By releasing GPT-3 along with policy protocols and pseudo-code, the potential for artificial intelligence (AI) with language generation and manipulation grows exponentially.

“This research and code release marks a critically important moment in AI,” OpenAI machine generative, team member Jacob Devlin said on the OpenAI blog. “Our models reach superhuman performance (or even that they may be superhuman), and are introduced into the world in an open way that’s in alignment with our core mission of our team.”

AI practitioners around the world can use the pseudo-code to train a language model tailored specifically to their needs and use cases, as well as implement ethical guidelines that ensure human validation of AI projects is made more efficient.

Automatic human-augmented language generation is one of the code’s main capabilities. Users can take text from a database stored in a machine-readable format and route it through the code to transform it into audio and video.

Along with “long short-term memory” neural network development, GPT-3 can save hours of document cleanup for developers.

They will be able to generate documents and audio in different speaking styles from the new library. And researchers can test different styles and evaluate which works best for certain content.

“While we have convinced ourselves that this research meets the goals for the launch of OpenAI, further study is needed to establish clear guidelines for the future of AI development,” the team stated. “Flourishing research on this new model of text generation, making further progress, is of paramount importance.”

AI Development Stalls

Authorities around the world have in recent years voiced concerns that AI technology development has gone too far without anyone paying attention.

One nation that is keeping watch over the major

---

**OpenAI researchers today released a paper describing the development of GPT-3, a state-of-the-art language model made up of 175 billion parameters.**

**For comparison, the previous version, GPT-2, was made up of 1.5 billion parameters. The largest Transformer-based language model was released by Microsoft earlier this month and is made up of 17 billion parameters.**

**“GPT-3 achieves strong performance on many NLP datasets, including translation, question-answering, and cloze tasks, as well as several tasks that require on-the-fly reasoning or domain adaptation, such as unscrambling words, using a novel word in a sentence, or performing 3-digit arithmetic,” the researchers stated in their paper. “We find that GPT-3 can generate samples of news articles which human evaluators have difficulty distinguishing from articles written by humans.”**

The neural network developers at OpenAI generally eschew real-world data use due to privacy concerns, reinforcement bias, and concerns about fairness. GPT-3, however, uses a selection of Google News articles – "far more challenging than any natural language text previously" – as part of its training.

Google news articles were previously used in the development of neural network systems that are starting to be deployed in smartphones. One Google research engineer, Mikhail Lemeshko, has stated that he does not think it would be possible to create approximate commonsense reasoning systems in news articles without access to the full text of those articles.

The researchers say that conditions for democratising the distribution of robots with general-reasoning capabilities is still "a long way off," but stated that they are seeing rapid progress.

"This progress is truly remarkable," the researchers said. "In my first few years in this field, I eagerly followed news about expert demonstrations – which, if nothing else, gave me an opportunity to tell my non-AI friends that they were just a few years away from having their lives ruined by expert systems (or, often, painful muffled “laughs”). Later, I watched the AI_Status game from the sidelines, as the best published performance in Watson broke world records but clearly wasn't achieving human-equivalent performance. Now, in 2019, human level performance is well within reach, even for complex tasks, and we're seeing published results every month."

---

