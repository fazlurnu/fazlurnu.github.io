---
title: "Conditional Probability - 2D Distribution"
date: 2026-05-08
tags: [math, probability]
excerpt: "Conditional probability, but 2D, in my own words, less formal discussion."
---

This post is designed to be the continuation of my [previous post](https://fazlurnu.github.io/blog/conditional-probability-intro/) on the introduction of conditional probability. In that post, we mostly focus on discrete event and the conditional probability of that event. For this post, we are shifting to random continous variables, and assuming you are already familiar with the notion of Gaussian distribution. It will feel a bit jumpy from the previous one, but let's get started.

## Weight and height of babies as random variables

I have a 3-month-old baby, and since she still cannot speak, my wife and I cannot really tell how she's doing with her growth. Of course, as parents, we try to give the best to her. But, as new parents, sometimes anxiety hits us with questions like, "are we feeding her sufficiently?" Thanks to people who note down babies weight and height around the world, we can have a metric for the growth of the baby. I know, baby's growth is not only about numbers, but that is at least something we can measure.

<img src="/assets/images/posts/baby-age-weight-height.webp" alt="Baby age, weight, and height chart" style="max-width: 100%; display: block; margin: 0 auto;">
<p style="text-align: center; font-size: 0.85em; color: gray;">Source: <a href="https://grownsy.com/blogs/parenting/newborn-to-toddler-a-guide-to-weight-and-length-growth" target="_blank">Grownsy — Newborn to Toddler: A Guide to Weight and Height Growth</a></p>

The picture above shows the typical weight and height (in the graph it is length, but of course it is interchangeable) for babies, given their age in months. Since this data is collected with a large sample, and there are a lot of random factors included in the outcome of the weight and height of babies, it can be considered as a Gaussain distribution (without going into a more rigorous reasoning).

If you read it again, the keyword "given their age in months" there, is a sign of conditional probability. So, we can use this as an example of conditional probability in continous variables. For instance, if we select my baby's age, 3 months, then we can trace the 3-month line and end up in about 13.5 lb (6.1 kg) for the weight and 23.9 in (60.6 cm) for the height. That is the mean, and, with some eyeballing on the graph, let's assume the standard deviation is around 0.75 kg for the weight and 2.05 cm for the height. We can now completely model it mathematically!

Let $W$ be the weight (kg), $H$ be the height (cm), and $A$ be the age (months). The chart gives us the conditional distributions of weight and height given age:

$$W \mid (A = 3) \sim \mathcal{N}(\mu_W = 6.1,\ \sigma_W^2 = 0.75^2)$$

$$H \mid (A = 3) \sim \mathcal{N}(\mu_H = 60.6,\ \sigma_H^2 = 2.05^2)$$

We can of course add more "conditioning" on this distribution. For instance, we add the gender of the baby, nationality, or parents height. All of that will of course shift the mean and standard deviation of the baby weight and height.

With some eyeballing and quick prompt to LLMs, we can quantify the parameter of the weight and height at each age, given in the table below. Note that this table is a mixed between boys and girls, all over the world, and according to WHO as claimed by those good colleagues.

| Age (months) | Mean Weight (kg) | SD Weight (kg) | Mean Height (cm) | SD Height (cm) |
| ------------ | ---------------: | -------------: | ---------------: | -------------: |
| 1            |             4.35 |           0.55 |             54.2 |           1.85 |
| 2            |             5.35 |           0.65 |             57.8 |           1.95 |
| 3            |             6.10 |           0.75 |             60.6 |           2.05 |
| 4            |             6.70 |           0.75 |             63.0 |           2.15 |
| 5            |             7.20 |           0.85 |             65.0 |           2.25 |
| 6            |             7.60 |           0.85 |             66.7 |           2.35 |

From the table, we can build a visualization of how the weight and height varies as the age increases. For simplicity, we assume the weight and height of the baby is independent (this is almost surely wrong, but for simplicity). You can see in this visualization (and the table) that the mean of weight and height increases as the age. The standard deviation also grows as the age increases. There are many reasons for the increase in the standard deviation, but I'm not trained to tell the reason behind it.

{% include baby_weight_height_widget.html %}

Although the title of the post is 2D distribution, what is visualized there is actually "3D" since we included the age there as a conditional variable. I hope it is getting clearer for you of what conditional probability looks like for a continuous variable. Note that the age is not a random variable. Next, we move on to conditioning on another random variable.

## A touch on 2D Gaussian distribution

Let us get more fancy by formalizing what we have done previously. Our first assumption, is that the weight and height of the baby is not correlated. Therefore, mathematically, we can formulate it as follows, in a vector notation (fixing it for my baby's age, 3 months):

$$\begin{bmatrix}W \\ H\end{bmatrix} \Bigg| (A = 3)\ \sim\ \mathcal{N}\!\left(\boldsymbol{\mu},\, \boldsymbol{\Sigma}\right)$$

$$\boldsymbol{\mu} = \begin{bmatrix}\mu_W \\ \mu_H\end{bmatrix} = \begin{bmatrix}6.10 \\ 60.6\end{bmatrix}, \qquad \boldsymbol{\Sigma} = \begin{bmatrix}\sigma_W^2 & 0 \\ 0 & \sigma_H^2\end{bmatrix} = \begin{bmatrix}0.75^2 & 0 \\ 0 & 2.05^2\end{bmatrix}$$

This is basically the formulation of **2D Gaussian distribution**, when there is no correlation between the weight and height of the baby.

Suddenly, someone from *CJG (Centrum Jeugd & Gezin)* comes to you and tell you, "*meneer, wie hebben een problem*, your model is wrong. I know for sure that the weight and height are correlated and here's the coefficient." The officer of course is more knowledgable and they hand you a piece of paper with $\rho = 0.67$. This number is used here for illustration. A value of $0.67$ means a moderately strong positive correlation, heavier babies tend to be taller, which makes intuitive sense.

To include this, we need to update the covariance matrix $\boldsymbol{\Sigma}$ for a 3-month-old baby ($\sigma_W = 0.75$ kg, $\sigma_H = 2.05$ cm). The off-diagonal entries are no longer zero; they become $\rho \cdot \sigma_W \cdot \sigma_H$:

$$\boldsymbol{\Sigma} = \begin{bmatrix}\sigma_W^2 & \rho\,\sigma_W\sigma_H \\ \rho\,\sigma_W\sigma_H & \sigma_H^2\end{bmatrix} = \begin{bmatrix}0.5625 & 1.030 \\ 1.030 & 4.2025\end{bmatrix}$$

So the updated model for a 3-month-old baby becomes:

$$\begin{bmatrix}W \\ H\end{bmatrix} \Bigg| (A = 3)\ \sim\ \mathcal{N}\!\left(\boldsymbol{\mu},\, \boldsymbol{\Sigma}\right), \quad \boldsymbol{\mu} = \begin{bmatrix}6.10 \\ 60.6\end{bmatrix}, \quad \boldsymbol{\Sigma} = \begin{bmatrix}0.5625 & 1.030 \\ 1.030 & 4.2025\end{bmatrix}$$

The plot below is the comparison between the non-correlated and correlated 2D Gaussian distribution.

{% include corr_comparison_widget.html %}

## Conditioning on another random variable

Previously, we have answered the question, "if my baby is 3 months old, what does the weight and height distribution look like." In this section, we ask another question, "if my baby is 3 months old, has height of 60 cm, what is the distribution of the weight?" To answer this question, we need to do the conditioning on both the age and height. To avoid mouthful conditioning writing, we fixed anything after this to 3 months old babies, so please allow me to drop the age from the conditioning.

For the first case, where there is no correlation between the height and weight, we can say that regardless of the height of the baby, the weight will have a fixed mean and standard deviation. In the second case, when there is correlation between the two (and it is positive), then intuitively we can say that if the height is higher, than the weight is also higher. However, the construction above is only for a "non-random" variable. When the weight is a random variable, we instead need to state that the mean of the weight shifts as the height changes.

Mathematically, the conditional distribution of $W$ given $H = h$ is also a Gaussian:

$$W \mid H = h\ \sim\ \mathcal{N}\!\left(\mu_{W|H},\ \sigma_{W|H}^2\right)$$

with conditional mean and variance:

$$\mu_{W|H} = \mu_W + \rho\,\frac{\sigma_W}{\sigma_H}(h - \mu_H)$$

$$\sigma_{W|H}^2 = \sigma_W^2\left(1 - \rho^2\right)$$

Within the same formulation, we can notice several things. First, the conditional mean $\mu_{W\vert H}$ shifts linearly with $h$, as we said before the taller the baby the heavier we expect them to be. Second, the conditional variance $\sigma_{W\vert H}^2$ does not depend on the height, meaning that the width of the distribution remains unchanged even as the height shifts. The width of the distribution only depends on both $\sigma_W$ and $\rho$, which in our case is fixed to $\rho = 0.67$. We can also see that, when the correlation coefficient $\rho$ is zero, then the $\mu_{W\vert H}$ is exactly the same as $\mu_W$.

The interactive plot below makes this visually intuitive. Geometrically, conditioning on $H = h$ is equivalent to taking a horizontal slice through the 2D Gaussian at that height value. The resulting cross-section is the conditional distribution of $W$. When moving the slider for $\rho > 0$, the mean of the conditional weight shifts with $h$, while the width of the distribution stays the same.

{% include conditional_weight_widget.html %}

## Beyond baby growth

Up to this point, we have seen together simple examples of conditional probability in the case of baby growth. Beyond that case, it is actually widely used in statistical and engineering problems. For instance, in a topic that I recently learned about, the Gaussian process. Another case of conditional probability is when I worked on my second journal paper (on [preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6675278)), which uses conditional probability to combine position and velocity uncertainty propagation into a single formulation in $\dCPA$ space.

This simple idea, fixing/observing one variable and see the distribution of other variable, is the foundation to many applications.