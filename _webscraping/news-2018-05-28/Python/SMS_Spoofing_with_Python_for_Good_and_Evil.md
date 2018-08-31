SMS Spoofing with Python for Good and Evil
==========================================

It all started with the best of intentions. I was an excitable graduate going through the second puberty of discovering that if you propositioned customers in the right way, a small percentage of them would buy your stuff.

Having been reasonably successful with personalized emails, it seemed that SMS was fair game as an extension. Fuck, Dominos and Royal Mail do it, and they’re only partially more time-relevant than a sale on a website you bought a novelty Luis Suarez biting bottle opener from two years ago. Turned out that my at-the-time boss didn’t agree, reacting in a way that can be summarized as “strongly negative” when he looked at a shirt on our site and simultaneously received a text which said something to the tune of “that shirt would go great with the brown size 11 shoes you bought 82 days ago.”



via GIPHY

(But bosssssss, it’s a nexus of many technologies! Absolutely no way? Bahhh, okay then. No, yeah, I’ve totally been working on other stuff too.)

I digress, though. Nobody cares about that.

It was the “misusing the tech to banter your friends” stage of that development which, ultimately, led to the discovery of something much creepier.

Experience gained from that same stage of development during my email days led me to start off with volume and persistence, because if there’s one thing that computers are good at (and there is), it’s the old water torture. Clockwork SMS, who will do your bidding at £0.05 per message, seemed as good a bet as any to me, so that’s who I “pip install”d. (And then angrily “sudo pip install”d, of course.)

Lolling delightedly to myself, I set this baby loose…

```

from clockwork import clockwork
import time

api = clockwork.API("Your API code here")

lyrics = open("Bohemian Rhapsody Lyrics.txt", "r").readlines()

for line in lyrics:
    payload = line.replace("\n", "")
    message = clockwork.SMS(from_name = "F Mercury", to = "447000123456", message = payload)
    response = api.send(message)
    print(response)
    time.sleep(300)

```

… and, with the warm fuzzy feeling that accompanies the knowledge that a computer is busy doing one’s dirty work, retired to enjoy my evening partaking in my favourite pastime of throwing stones at traffic.

My friend was sent a line from “Bohemian Rhapsody” every 5 minutes until the song was done. Picture it: the numbingly-familiar “ding” of an incoming text and the muscle memory that responds by reaching for your nearby phone, maybe even the rational thought that, in all probability, this was just the latest in the pontifications of one F. Mercury, but the agonizing, irresistible, small-but-not-negligible chance THAT IT’S A LEGIT TEXT. No real hardship just to check. That bastard. Wish I hadn’t checked. Not going to check the next one. Sublime.



Turned out he was really ill and I made a basic arithmetic error which resulted in the texts continuing through the night instead of being spread over a couple of hours, so that was rather less funny than it could have been, but I was hardly to know that at the time. And anyway, the fires of curiosity had been stoked in my mind.

Because of course, annoying though this is, it’s fairly obviously banter. Beyond seeking a restraining order, it’s not really going to influence people. Now, saying that, I should also say that this is where the “in the field” element of my noble research ended: what follows involved the phones of others, but also always their knowledge and consent. The life-wrecking potential of unleashing this shit on people fo’ real should be reserved for elected governments and security agencies. DISCLAIMER: don’t do it etc.

You’ll have noticed that the “from” argument in the call is what appears on the recipient’s phone when the SMS comes in. That in mind, the logical extension from “F Mercury”, or any other experimental name, is “Mum”.

```

message = clockwork.SMS(from_name = "Mum", to = "447000123456", message = "SURPRISE MUTHAFUCKA! Yo punk ass goin down bitch boi!")

```



Tehehehehe. Excellent. What a time to be alive.

There’s one pig in the poke, though: my phone is clever enough to know that this is only from “Mum” in a superficial sense. If I were forced to guess why this was, I’d probably go with the fact that this is from a string, not a number, which is where my real messages from “Mum” come from. So this message isn’t part of any thread. The real messages labeled as “Mum” come, at a presumably more fundamental level, from a phone number, which is saved under an alias in my contacts.



I wonder. I JUST WONDER.

The magic step is absurdly simple. What would happen if I put the from address as a phone number, the phone number stored under “Mum” in my contacts?

```

message = clockwork.SMS(from_name = "07999654321", to = "447000123456", message = "You don't know anything, and you stink.")

```



Long have critics conjectured on the inspiration behind Lionel Ritchie’s time-immemorial opus “Hello, is it Me You’re Looking For?”. Now we know.

Here you have a trivially simple method of injecting legit-looking messages into text conversations with anyone, providing you know how your target stores the spoofee sender in their contacts. In the UK, that’s largely the difference between starting with 07, and +447.

The utterly exquisite reality is that, if your target then replies, that reply goes to the real sender, who is overwhelmingly likely to reply something like “what the hell are you on about?”, this being the first they’ve heard of this shady business. Does that look like backtracking or denial? I ain’t no Member of Parliament, but it sure sounds like it to me.

And if I may quote Mouse from The Matrix, that makes you wonder about a lot of things. How many friendships and/or relationships have fallen afoul of a simple misunderstanding, a simple miscommunication, one statement taken the wrong way, such as could be easily achieved through the above means?

How many fledgling romances need a seductive kick-start to get them over the stalemate of shyness?

Given that your communication is limited to one-way, what series of messages should you go with for maximum impact, and maximum imperviousness to whatever the replies might be?

Could you even construct some confusing pseudo-two-way thing, if you knew the numbers of both parties? Like two colleagues maybe?

Doesn’t bear thinking about, really. Much.