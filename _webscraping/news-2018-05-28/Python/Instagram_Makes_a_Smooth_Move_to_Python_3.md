Instagram Makes a Smooth Move to Python 3
=========================================

#### 
Analysis / Case Study / Technology / Global 

#### 
		14 Jun 2017 2:00am,

		by 
Michelle Gienow 


Each day, over 95 million photos and videos are shared on Instagram. The unstoppable photo-centric social media platform has over 600 million registered users — 400 million of whom are active every day. Talk about operating at scale: Instagram kills it at levels most companies can barely even dream about.

Even more impressive, though, is the fact that Instagram serves this incredible amount of traffic, reliably and steadily so, by running Python (with a little help from Django) under the hood. Yes, that Python — the easy to learn, jack-of-all-trades general purpose programming language. The one everybody in the industry dismisses as, “Yeah, Python is great in so many ways, too bad it’s not really scalable.”

Ahem. Four. Hundred. Million. Users. Per. Day. Not only has Instagram scaled to become the biggest Python user in the world, but the company recently moved over to Python 3 with zero user experience interruption. Instagram engineers Hui Ding and Lisa Guo talked with The New Stack to share the Python love and describe the Python 3 migration experience.

How was it that Instagram started with Python in the first place?

Hui Ding: I joined Instagram as the first engineer to be hired after the acquisition [Instagram was founded in 2010, bought by Facebook in 2012]. Since then we have gone from six engineers to 300. I wasn’t there at the very beginning, but I worked closely with [Instagram cofounder] Mike Krieger in the early days when we were still a very small team, so I have a lot of context for the history of why we chose Python.

The reasons were consistent with Instagram’s engineering motto of “Do the simple things first”: Python is user-friendly for engineers — it’s easy to get up to speed and get out the product, allowing the team to concentrate on user facing features. Python is simple and clean and favors pragmatism. It is a proven technology. And, finally, it’s a really popular language, which makes growing the engineering team easier.

What issues led Instagram to consider a new stack?

Ding: As we grew, it became obvious Python was not the fastest language by any means.  AWS made it easier to throw more machines at it as we needed to grow, but there is a point of diminishing returns — at a certain point, there is more resource going to performance regression than user growth. And within three to five years from now, we are looking at an estimated one billion users joining our community, so the time came when we did have to consider other options. Our first question was, would there be high enough return to justify?

Instagram user growth is rising steadily – but not as fast as server growth.

Lisa Guo: We were faced with a specific challenge of increasing network I/O activity on our servers. So we needed a more parallel way to process the user requests. Realistically, PHP and Python are the best-supported ecosystems at Facebook, and going with any other platforms would require both a learning curve and a whole lot of new training for our engineers.

So we did a portal typing comparison with PHP, which is used by Facebook web servers.

Ding: Had we seen orders of magnitude faster performance improvements, we would have changed over, but ultimately those gains simply were not there.

So the numbers were not compelling, and we had a lot of tools and investment in Python already. We had been able to get to a few hundred million users with our Python/Django stack, so we decided we would continue. Also significant in the decision was that our engineers really love Python. It’s actually a reason people want to come work for us.

Was this the point where the team decided to move to Python 3?

Ding: The decision at that time was, do we invest in a version of the language that was mature, but wasn’t going anywhere — or the language that was the next version and had great and growing community support? It made sense that, if we were going to stay on Python for the next ten years, we should invest in the latest version of the language. Then shortly after we decided to push to Python 3, it was announced that v2.7 would no longer be supported after 2020.

Performance speed is no longer the primary worry. Time to market speed is. — Hui Ding

Guo: There were three major motivations behind the push to Python 3. First, Python traditionally is not a typed language, so there would be a lot of development conflicts when we started working new pieces of code. So a big motivation for us was the announcement that Python v3.5 would start to support typing — our devs were very excited at this news.

Second, networking is increasingly a bottleneck for us.

Third, Python was not fast, but each newer version continues to get faster runtime — v2.7, nobody’s working to make that any faster. With the latest release we have the version the community is working on, and also we get to contribute back.

So what did the push process look like?

Guo: Overall it took about ten months, in different stages.

First, the team undertook massive code modification. This took two to three months, and included replacing incompatible third-party packages with ones supporting Python 3 — the working rule was, “No Python 3, no new package” — and also deleting unused packages.

Then unit testing, which took two months. Then we undertook slow but steady rollout, over four months. By early February 2017, we were completely running Python 3.

Instagram’s infrastructure engineering team took a total of 10 months to complete the migration to Python 3.

By all reports, things went really smoothly — how did the team make it happen so seamlessly?

Guo: An important factor was, if you look at how we were migrating, we would constantly check in small changes into the master branch, so we were never merging major diffs. Getting the most bugs fixed, with a smaller audience iterating in small steps: that was the key approach to maintaining stability while still moving quickly.

Ding: It’s not there were no pitfalls, given the incompatibility of the two versions. The key is taking the time upfront to thoroughly scope your solutions with respect to your problems. So we started with profiling, getting a clear understanding of the potential benefits and tradeoffs. Scope the problem really well, and then doing what makes the most sense. That said, doing the simple thing first doesn’t mean that we move slow or that we don’t take risks.

The Handoff: Seamless transition between Python 2 and Python 3, with no interruption to user experience.

How has Python 3 performed since then?

Ding: We did not have performance gain expectations for Python 3 right out of the box. So it was a pleasant surprise to see 12 percent CPU savings (on uswgi/Django) and 30 percent memory savings (on celery). It’s only been four months since rollout, we don’t expect to see constant 10 percent performance improvement, but that was a very promising start.

One of the very common mechs we use is Thrift which is written in Python, and our team is working at Facebook to make the serialization faster.

Any last words of advice for engineers considering migrating to Python 3?

Guo: The query I get most is, “How do I convince my manager that we should do Python?” And it can be hard to sell given Python’s reputation for being slow. But efficiency work is my specialty and Python’s efficiency was a big draw for me, so efficiency is one place to push back against worries over speed.

Ding: Performance speed is no longer the primary worry. Time to market speed is.

Guo: So my advice is, start with small modules and show the benefit — that will get more people excited about changing over.

Ding: People in the industry, other companies still struggling with migration, have reached out to me asking me how we did it so well.

And it was exactly what Lisa said: The “small steps” approach we took to drive the migration is what made it go so well. Which is the very same approach that made Instagram the world’s number one visual social platform.