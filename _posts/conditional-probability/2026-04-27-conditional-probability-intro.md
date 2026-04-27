---
title: "Conditional Probability - Intro"
date: 2026-04-27
tags: [math, probability]
excerpt: "Conditional probability, in my own words, less formal discussion."
---

In my years in Bandung, when I studied my bachelor, I learnt statistics very shallowly. Then, during my master, it was not taught as a separate subject but the concepts were everywhere (i.e. in robust control, state estimation). Allow me to write my few understandings on statistics, as a collections of posts, in my personal website. Although a bit sporadic, without a structured curriculum, it is better than nothing.

And in this post, I'm writing on conditional probability.

## Short story from a time traveler

Suppose you "time-travel" into a random day on earth and observe the situation in the hospital. On any day, say the hospital occupancy rate for specific symptoms (say coughing, runny nose, heavy breathing) is quite low, 0.01% (not a real number). For simplicity, we call the disease with these symptomps as Severe acute respiratory syndrome (SARS). Then, you happen to be on a day where the hospital occupancy rate for that mentioned symptomps jumps to 95%. You asked, "what's happening?", and someone answered, "we're in a pandemic, sir".

Let's formalize it a bit. Suppose $A$ is the event that a hospital is occupied by patients with SARS symptoms, and $B$ is the event that a SARS pandemic is ongoing. By statistics, thanks to people who always write things down, we know that $P(A) = 0.01\%$ on any ordinary day. Pandemics are also historically rare, so $P(B) = 0.001\%$.

Before you time-travel to another random day, you meet some SARS-pandemic-denier and he says that nothing is happening. Somehow he and his circle belong to group that is very immune to SARS and he doesn't read any news. You are kind enough to engage in a conversation with him, so you say, "I just went to the hospital, $P(A)$ is somehow large these days!" That observation, $P(A)$ being high, can be used as evidence that $B$ is happening right now, and we call it $P(B \mid A)$, or the probability of a pandemic occurring given the hospital occupancy is abnormally high.

With that example, you now have a slight intuition of what's conditional probability.

## Probability of a dice has a certain value, from two dice throw

This one is an example straight from [conditional probability wikipedia page](https://en.wikipedia.org/wiki/Conditional_probability#Example), a simple but very explanatory one. I've seen my wife did the same exercise on [Brilliant.org](brilliant.org).

Suppose that someone is throwing two independent dice, $D_1$ and $D_2$, and you are interested in observing several things. The first thing you are interested in is event $A$: $D_1 = 2$. You can write down the matrix (or build a mental model of it) of outcomes of $D_1$ and $D_2$ as an exercise, and you see that $P(A) = 6/36 = 1/6$.

Then, another interest is to observe $D_1 + D_2 \leq 5$, let's call it event $B$. From the matrix that you've created, you know the pairs of $D_1$ and $D_2$ that sum to at most 5 are $\{(1,1),\ (1,2),\ (1,3),\ (1,4),\ (2,1),\ (2,2),\ (2,3),\ (3,1),\ (3,2),\ (4,1)\}$. So, $P(B) = 10/36$.

Now you are interested in $P(A \mid B)$, the probability of $D_1 = 2$ given that $D_1 + D_2 \leq 5$. Mathematically:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{3/36}{10/36} = \frac{3}{10}$$

and you can verify it by looking at those pairs that sum to at most five and counting how many have $D_1 = 2$.

## Conditional probability, but A and B are independent

Let us have another example of event $A$ and $B$, but they are now completely independent. A simple example, $A$ is the probability of having number 3 from a die throw ($P(A) = 1/6$) and $B$ is the probability of having a head in a coin toss ($P(B) = 1/2$).

Someone then asks you, what's the probability of $P(B \mid A)$, having a head given that you observe 3 from your die throw?

Since the dice and coin are not related at all, we can say they are independent. So, what happens in $B$ has nothing to do with $A$. Thus, $P(B \mid A) = P(B)$.

$$P(B \mid A) = P(B) = \frac{1}{2}$$

By now hopefully it is a bit clearer what's conditional probability is, from a dependent and independent event.

The probability of having $D_1 = 2$ in the previous example can also be explained in this framework.

## Where in engineering is it?

One of the coolest application of conditional probability in engineering is [the Kalman Filter](https://en.wikipedia.org/wiki/Kalman_filter), the algorithm that helps sending people to the moon in 1960s. Let's discuss it a bit, but with a 1D robot example.

Suppose that you are trying to track a robot moving in a 1D plane. You have two sources of information, one is from your physics model and another one is from your sensor. You know for sure that your model is not perfect because you do not include the surface friction or air drag for simplicity reason. You also know that your sensor measurement is wrong because you bought it from a cheap online store for 1 Euro. You put it to test, and they both have different results! Which one do you trust?

Formulating it into equations, suppose $P(A)$ is your sensor measurement and $P(B)$ is your belief about the robot's position from your physics model. Then, $P(A \mid B)$ is how likely the sensor will give you that reading if $B$ is the ground truth. Lastly, we note $P(B \mid A)$ as your updated belief after incorporating the sensor measurement.

Without going into detail, we use [Bayes' theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem), which is the backbone of the Kalman Filter:

$$P(B \mid A) = \frac{P(A \mid B) \cdot P(B)}{P(A)}$$

So, when you have two value and they are dependent, you can use both to update your belief on the most accurate. Below is a short interactive example of how a simple Kalman Filter works (skipping the explanation on the mean and standard deviation and how the estimate state is calculated).

{% include kalman_widget.html %}

When you play with the interactive plot, you can see that if you know that the sensor is not reliable (standard deviation is high), the sensor estimate will tend to 'believe' the physics model given that its standard deviation is lower than the sensor's. And vice versa.

## Closure

So, that's a short introduction of conditional probability. I hope it can build an intuition and show a short example of how it is used in real life.

