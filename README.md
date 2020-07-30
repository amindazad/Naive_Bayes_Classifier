# Naive_Bayes_Classifier
Naive Bayes classifier from scratch

The Naive Bayes algorithm is a classification technique based on Bayes Theorem. It assumes that the presence of a feature in a class is unrelated to the presence on any other feature. The algorithm rely on the posterior probability of the class given a predictor, as we can see in the following formula:

$$P(c|x) = \frac{P(x|c)*P(c)}{P(x)}$$

where:

$$P(c|x)$$ - the posterior probability of class $$c$$ given a predictor $$x$$
$$P(x|c)$$ - the probability of the predictor $$x$$ given the class $$c$$. Also known as Likelihood
$$P(c)$$ - the prior probability of the class
$$P(x)$$ - the prior probability of predictor.

Find [here]() the blog post for a better understanding.