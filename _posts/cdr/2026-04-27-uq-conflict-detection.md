---
title: "Uncertainty quantification on state-based conflict detection - distance at closest point of approach"
date: 2026-04-27
tags: [math, probability, conflict detection, cd&r]
excerpt: "A less formal, more playful version of my paper [uncertainty quantification on state-based conflict detection and resolution](https://www.sciencedirect.com/science/article/pii/S0951832025013109)."
---

This post/note is a less formal, more playful version of my paper [uncertainty quantification on state-based conflict detection and resolution](https://www.sciencedirect.com/science/article/pii/S0951832025013109).

The paper focuses on doing forward propagation of navigation uncertainty, both position and velocity, into the decision variables in conflict detection and resolution. For this blog, let us first discuss the state-based conflict detection, continued by the navigation uncertainty model, and see the forward-propagated variable.

## State-based conflict detection

State-based conflict detection works by projecting the position and velocity of an ownship and intruder into the future. Using the relative position ($\xrel = \xint - \xown$) and relative velocity ($\Vrel = \Vo - \Vi$), we can calculate the time to closest point of approach ($\tCPA$) and subsequently distance at closest point of approach ($\dCPA$) and time to intrusion ($\tin$) as following.

$$\tCPA = \frac{\Vrel \cdot \xrel}{\norm{\Vrel}^2},$$

$$\dCPA = \xrel - \Vrel \cdot \tCPA,$$

$$ \tin = \tCPA - \frac{\sqrt{\RPZ^2 - \norm{\dCPA}^2}}{\norm{\Vrel}}, $$

with $\RPZ$ being the radius of protected zone.

Here, we will only discuss the distance at closest point of approach ($\dCPA$) because there's a beautiful property of it that is previously less elaborated. For the other two variables, you can find it in the [paper](https://www.sciencedirect.com/science/article/pii/S0951832025013109). Now let us build the navigation uncertainty model.

## Navigation uncertainty model

Let's model the position and velocity uncertainty of the ownship and intruder as a 2D Gaussian distribution for simplicity and tractability reasons. Using the addition property (the sum of two Gaussian distribution is also Gaussian), we can then construct the distribution of the noisy relative position ($\xrel$) and noisy relative velocity ($\Vrel$) as shown below:

$$\xrel \sim \mathcal{N}(\boldsymbol{\mu}_{\mathrm{rel}},\ \Sigma_{\mathrm{rel}}),$$

$$\Vrel \sim \mathcal{N}(\boldsymbol{\nu}_{\mathrm{rel}},\ \Sigma_{V_{\mathrm{rel}}}),$$

with $$\boldsymbol{\mu}_{\mathrm{rel}}$$ and $$\Sigma_{\mathrm{rel}}$$ as the mean and covariance of the relative position and $$\boldsymbol{\nu}_{\mathrm{rel}}$$ and $$\Sigma_{V_{\mathrm{rel}}}$$ as the mean and covariance of the relative velocity.

## Forward-propagated noise

Now, as I have shown in the [paper](https://www.sciencedirect.com/science/article/pii/S0951832025013109), when we consider the velocity as a deterministic variable and only the position is a random variable, the $\dCPA$ follows a normal distribution! This is because the relative velocity vector is fixed (no noise), and only the position is moving around. When we project the 2D Gaussian of relative position measurement into the relative velocity vector, we also get a Gaussian distribution. Subsequently, if we measure $\norm{\dCPA}$, we get a folded-normal distribution.

The plot below illustrates the relative velocity vector, samples of relative position, the sample of ${\dCPA}$ in the ${\dCPA}$ space, and histogram of $\norm{\dCPA}$.

{% include conflict_detection_widget.html %}