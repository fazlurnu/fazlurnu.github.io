---
title: "AI is to researchers what chess engine is to grandmasters"
date: 2026-08-19
tags: [AI, research, chess]
excerpt: "A self-refelction, should I keep doing chess/research?"
---

In 1997, for the first time, a computer defeated a reigning world chess champion, Garry Kasparov. The computer was named "Deep Blue," and it was programmed specifically to play chess. After that historic event, many predicted that chess would soon face the end of an era since the game is essentially solved. Instead, chess has regained traction in the past few years, partly thanks to the Netflix series The Queen's Gambit.

In recent years, artificial intelligence (AI) has progressed immensely. For this article, when I mention AI, I am referring to large language models (LLMs) such as OpenAI's GPT series, Anthropic's Claude, or Google's Gemini. These models are so good at processing information that Sam Altman, CEO of OpenAI, said in 2025 that AI can rival someone with a PhD. So, if they can rival someone with a PhD, is this also the end of a human researcher?

My short answer is no, and my proposition is

> AI is to researchers what chess engine is to grandmasters.

We should use AI as a tool for our research the same way grandmasters use a chess engine to analyze games. I explore this by drawing parallels to how a grandmaster prepares for a chess match. The article starts with the underlying assumptions behind my argument, then elaborates how a computer can expand the search space, to why fundamental matters in narrowing it down, the role of discussions. Finally, should I keep doing research?

## The Assumption

To start from common ground, let us first agree on a couple of things. This article is a self-reflection, so what I write here is therefore limited to my own practice of using AI as a researcher and my understanding of how a grandmaster uses a chess engine.

Next, we should agree on the goal in both cases. For a grandmaster, let us assume the goal is to win every match and ultimately become world chess champion. For a researcher, the goal is to solve existing problems in their specific domain. I honestly do not know what the "ultimate" goal of a researcher is, since it is highly subjective and incentive-dependent, so we will leave it ill-defined. We therefore focus on the short-term goals of both, that is winning matches and solving existing research problems.

The next assumption is that AI models are already far better than most humans at consuming and producing text for the purposes of research. They hold a vast corpus of knowledge, can be supplied with material they were never trained on, can write and test code quickly, and so on. The same holds for chess, it is already far better than most humans at analyzing a game as it can objectively calculate the best move many steps ahead. The word better in doing research of course needs a precise metric, but I will leave it naively defined as producing a paper with sufficiently sound math that improves a certain metric.

## The search space

When a chess game starts, there is an astronomically large number of possible move combinations. Some early sequences are popular and well studied, and they carry names like the Spanish or the Italian Game. Others are suboptimal, they weaken the position immediately, and you don’t need to bother learning their names.

<img src="/assets/images/posts/ai-chess-and-research/italian-game.webp" alt="Opening position of the Italian Game: 1.e4 e5 2.Nf3 Nc6 3.Bc4" style="max-width: 80%; display: block; margin: 0 auto;">
<p style="text-align: center; font-size: 0.85em; color: gray;">Italian Game, one of the most popular chess openings.</p>

With the usage of chess engines, some openings have grown more popular while others have disappeared from top-level games. GM Anish Giri explains that

> “the stronger the engine gets, the more it shows that variations that were considered bad before are no longer bad because the engine is able to defend them. Even what used to be a dubious opening turns out to be playable if you defend accurately and the engine shows how to defend.”

The engine, in other words, enables players to explore variations and innovations that were previously out of reach.

In my opinion, AI can enlarge the search space for researchers. It writes code quickly, turning an idea into an executable script in hours, if not minutes. With the right tool and research framework, we can quickly validate or invalidate ideas to further shrink the search space towards the meaningful ones. Besides that, with the help of AI, we can upload a paper, ask it to replicate the result, and get it done in minutes. I have done this myself a couple of times and it works almost flawlessly.

However, there’s a downside of this increasing search space for an individual researcher to the academic community itself. For instance, in mathematical research, numerous open problems have been claimed to be solved with the help of an AI. This is sometimes written without the human author’s own elaboration of the proof. While the search space is growing, how much of it is actually useful for the research community itself? A larger search space does not automatically translate into better solutions that are understandable by humans. Terence Tao, a Fields Medallist, recently stated that so many results are being generated that many go unverified by humans. A solution can be shown to be correct, but is it comprehensible?

<img src="/assets/images/posts/ai-chess-and-research/math-articles-arxiv.webp" alt="Monthly count of mathematics papers submitted to arXiv from 1992 to 2026" style="max-width: 100%; display: block; margin: 0 auto;">
<p style="text-align: center; font-size: 0.85em; color: gray;">Mathematical preprint submitted to ArXiv over years. Source: <a href="https://www.reddit.com/r/math/comments/1vf7v4r/math_papers_uploaded_to_arxiv_per_month_jan_1992/" target="_blank" rel="noreferrer">Reddit</a>.</p>

If we still consider ourselves, humans, to be the drivers of scientific progress, then results have to be written to be read by people.

## Learn The Fundamentals

When a grandmaster studies a game, they can use an engine to evaluate their position relative to the opponent's. Take this middle-game position, the engine evaluates it at +2.0 for White. A complete beginner cannot see why, the material is exactly equal, so where is White's advantage? In my own judgement, knowing only a little of the fundamentals, it is recognisable. White has far more space to manoeuvre, and Black's bishops are essentially trapped. A grandmaster would give a much more thorough reasoning.

<img src="/assets/images/posts/ai-chess-and-research/chess-position.webp" alt="Middle-game position from Karpov versus Unzicker, evaluated at +2.0 for White" style="max-width: 50%; display: block; margin: 0 auto;">
<p style="text-align: center; font-size: 0.85em; color: gray;">Karpov versus Unzicker, same number of pieces but white is winning.</p>

Today, a high schooler with the right set of words in a prompt can ask an AI how to solve a given problem. Say it returns three candidate solutions. Unless this student is an unusually brilliant mind, they will most likely be unable to separate signal from noise, or to tell which candidate is best. Hand the same three to someone deeply knowledgeable about the topic, and they may recognise the promising one immediately. Or even, more surprisingly, that the AI's proposal was taken from their own work.

I have tried prompting an AI to solve a problem without any specific command. Prompt is sent, the response is written, the metric seems to improve, but the solution is neither elegant nor concise enough to count as one. Another case is when I have an idea of solving a particular problem, ask an AI to draft it into code, the response is written, the metric seems to improve, but again at the end it is my own judgement to decide if it is sufficient or not.

When the search space becomes immensely wide, your job is to filter the candidates. The only way to filter is by understanding the first principles of your field of research. Someone who can understand a solution down to the smallest established piece of scientific knowledge is the one who will truly gain from using AI as a tool for research.

## Practise your understanding

Did you know that in the final round of the world chess championship, the two competing candidates have a team behind them? When I first learned about this, I could not really understand why the supposedly most capable chess player needed to discuss with another person, especially when there are chess engines.

The understanding is the actual load-bearing[^loadbearing] part. It is true that the chess engine can tell you which move is objectively winning. But again, you have to understand why that move is a winning one. And, it turns out that having human-peers actually helps the grandmasters understand what they have studied with the engine. Also, the human-peers can help point out potential improvements that are humanly acceptable, since some of the chess engine’s moves are simply incomprehensible even for grandmasters.

This can then translate into doing research. After using an AI to brainstorm ideas, I filter out what I think is sufficiently good to my standard. Then, I bring up this idea into discussions with my supervisors or my colleagues. The best part is when they doubt the idea, since it demands me to explain what my idea is, how it translates into the solution, and whether I can explain it to others or not. If I can’t explain it to others, I simply don’t understand it.

In chess, when grandmasters play a match, they do not have access to engines and they have to rely on themselves. In research, the AI model is almost always available at hand and no one would ask us to “*sit there and let me question you without your AI.*” This, in my opinion, should be a voluntary action. Open up a discussion, detach from AI, and let yourself be vulnerable to your own idea and explanation.

## Should I keep doing chess/research?

I have been playing chess for the past 5 years almost daily. It is true that an engine has already solved this game, but I’m not playing against an engine (maybe sometimes yes when someone cheats). At the end, the being-human part of playing chess is what makes it enjoyable. The excitement when you find a brilliant move. The frustration when you blunder. Or the self-doubt moment while playing.

<img src="/assets/images/posts/ai-chess-and-research/my-rapid-rating.webp" alt="My chess.com rapid rating history from 2021 to 2026" style="max-width: 75%; display: block; margin: 0 auto;">
<p style="text-align: center; font-size: 0.85em; color: gray;">My rapid rating over the past five years. Send a game invitation <a href="https://www.chess.com/member/toko_material" target="_blank" rel="noreferrer">here</a>.</p>

I am close to ending my PhD journey, a few months left. Reflecting on the future, I still want to do research. It is true that AI can now rival someone with a PhD degree, but I’m not doing a research to be consumed by an AI (maybe you will feed my research to an AI, but I hope your goal is to understand it). At the end, the being-human part of doing research is what makes it enjoyable. The excitement when you find a novel idea. The frustration when nothing seems to work. Or the self-doubt moment while writing.

[^loadbearing]: This is an actual human writing, intentionally written to sound Claud-ish.
