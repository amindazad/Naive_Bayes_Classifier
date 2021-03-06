# Naive_Bayes_Classifier
Naive Bayes classifier from scratch

The Naive Bayes algorithm is a classification technique based on Bayes Theorem. It assumes that the presence of a feature in a class is unrelated to the presence on any other feature. The algorithm rely on the posterior probability of the class given a predictor, as we can see in the following formula:

![proba](https://wikimedia.org/api/rest_v1/media/math/render/svg/52bd0ca5938da89d7f9bf388dc7edcbd546c118e)

where:

**P(c\|x)** - *The posterior probability of class given a predictor*.

**P(x\|c)** - *The probability of the predictor X given the class. Also known as Likelihood.*.

**P(c)** - *The prior probability of the class.*.

**P(x)** - *The prior probability of predictor.*.

Or using Bayesian probability terminology, the Guassian Naive Bayes classifier equation can be written as

![proba](https://wikimedia.org/api/rest_v1/media/math/render/svg/d0d9f596ba491384422716b01dbe74472060d0d7)

Find [here](https://medium.com/@amindazad/classification-model-from-scratch-49f24bdd0636) the blog post for a better understanding.