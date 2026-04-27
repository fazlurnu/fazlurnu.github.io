---
title: "Uncertainty quantification on state-based conflict detection - distance at closest point of approach"
date: 2026-04-27
tags: [math, probability, cd&r]
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

Here, we will only discuss the distance at closest point of approach ($\dCPA$) because there's a beautiful property of it that is previously less elaborated. For the other two variables, we can find it in the [paper](https://www.sciencedirect.com/science/article/pii/S0951832025013109). Now let us build the navigation uncertainty model.

## Navigation uncertainty model

Let's model the position and velocity uncertainty of the ownship and intruder as a 2D Gaussian distribution for simplicity and tractability reasons. Using the addition property (the sum of two Gaussian distribution is also Gaussian), we can then construct the distribution of the noisy relative position ($\xrel$) and noisy relative velocity ($\Vrel$) as shown below:

$$\xrel \sim \mathcal{N}(\boldsymbol{\mu}_{\mathrm{rel}},\ \Sigma_{\mathrm{rel}}),$$

$$\Vrel \sim \mathcal{N}(\boldsymbol{\nu}_{\mathrm{rel}},\ \Sigma_{V_{\mathrm{rel}}}),$$

with $$\boldsymbol{\mu}_{\mathrm{rel}}$$ and $$\Sigma_{\mathrm{rel}}$$ as the mean and covariance of the relative position and $$\boldsymbol{\nu}_{\mathrm{rel}}$$ and $$\Sigma_{V_{\mathrm{rel}}}$$ as the mean and covariance of the relative velocity.

## Position uncertainty

Now, as I have shown in the [paper](https://www.sciencedirect.com/science/article/pii/S0951832025013109), when we consider the velocity as a deterministic variable and only the position is a random variable, the $\dCPA$ follows a normal distribution! This is because the relative velocity vector is fixed (no noise), and only the position is moving around. When we project the 2D Gaussian of relative position measurement into the relative velocity vector, we also get a Gaussian distribution. Subsequently, if we measure $\norm{\dCPA}$, we get a folded-normal distribution.

The plot below illustrates the relative velocity vector, samples of relative position, the sample of ${\dCPA}$ in the ${\dCPA}$ space, and histogram of $\norm{\dCPA}$.

{% include conflict_detection_widget_position.html %}

From the plot above, we can see that the $\dCPA$ distribution forms a line in the $\dCPA$ space. This line itself is a Gaussian distribution, as mentioned before. Then, the norm of $\dCPA$, which is the distance of each realisation to the origin, forms a folded-normal Gaussian (think of it as putting an absolute operator in the Gaussian distribution). This expression has a closed-form and can be found in my [paper](https://www.sciencedirect.com/science/article/pii/S0951832025013109).

Another observation we can have from the plot is, regardless of the relative velocity vector, the shape of the $\dCPA$ distribution is always a line and this line is a Gaussian distribution. Also note that this line is exactly oriented as the $\dCPA$ vector in the conflict geometry illustration.

Since this one is not a journal paper, no one will ask about why I have weird-shaped position distribution (if we ask, the answer because it is fun). In the drop-down menu, we can change the position uncertainty distribution, for fun! Then, adding some samples, we see that even for a non-standard Gaussain distribution the $\dCPA$ vector still follows a line. This is because the nature of the projection, from 2D position into the relative velocity subspace, making it restricted to a line. Of course, when we look at the $\norm{\dCPA}$, the distribution is no longer a folded-normal Gaussian.

## Velocity uncertainty

Now, let's move on to the other uncertainty, the velocity uncertainty. For this case, we fix the relative position and only the relative velocity has the uncertainty. When we do the sampling, we get an arc!

{% include conflict_detection_widget_velocity.html %}

In this velocity uncertainty case, we no longer have a projection into the relative velocity subspace. For this case, the relative velocity actually "rotates" in every realisations. This make the projection of the intruder position traces an arc. In some specific cases, this arc can be extended into a full circle. The proof, and the exact formulation, can be found (again) in my [paper](https://www.sciencedirect.com/science/article/pii/S0951832025013109).

Another interesting fact is, because the relative velocity follows a 2D Gaussian distribution, the $\dCPA$ vector also still follows a Gaussian distribution, but wrapped! Think of it like this: I have a Gaussian distribution, but instead of laying on a line, it is spread across an arc. This is commonly known as [projected-normal distribution](https://en.wikipedia.org/wiki/Projected_normal_distribution). However, when plotting the histogram of the $\norm{\dCPA}$, the distribution no longer follows a folded-normal and it simply doesn't have any closed-form expression. One interesting question is, if the case makes the $\dCPA$ distribution follow a full circle and the uncertainty is high enough, how does the histogram looks like in the wrapped circle?

I excluded two things to play with from this plot: varying the uncertainty model of the velocity and the relative position. I let the readers explore those two cases, or read my paper for the answer in the latter case.

## Conclusion

In this paper, we have discussed the state-based conflict detection, navigation uncertainty model, and the forward-propagation of uncertainty. We have seen that when position uncertainty exists, the $\dCPA$ follows a line in the $\dCPA$ space. On the other hand, for velocity uncertainty, it traces an arc in the same space. The mixture of the two, when both position and uncertainty exists, are left to the reader to explore.
