---
title: "Showing The Gaussian Distribution, Interactively"
date: 2026-04-26
tags: [math, probability]
excerpt: "A short visual intro to the normal distribution — with a live interactive widget you can play with."
---

The **Gaussian distribution** (also called the normal distribution) is one of the most popular, and probably important, probability distributions in statistics. Its shape is fully determined by two parameters:

- **μ (mean)** — where the peak is centered
- **σ (standard deviation)** — how spread out the curve is

The probability density function is:

$$p(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

Play with the sliders below to see how each parameter shapes the distribution:

{% include gaussian_widget.html %}

A few things to notice:

- Shifting **μ** moves the curve left or right without changing its shape.
- Increasing **σ** flattens and widens the curve — the total area stays 1.
- The dashed red line marks the mean; the dotted gray lines mark ±1σ (one standard deviation on each side), which contains ~68% of the probability mass.
