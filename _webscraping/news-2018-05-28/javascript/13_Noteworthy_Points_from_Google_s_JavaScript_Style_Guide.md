13 Noteworthy Points from Google’s JavaScript Style Guide
=========================================================

For anyone who isn’t already familiar with it, Google puts out a style guide for writing JavaScript that lays out (what Google believes to be) the best stylistic practices for writing clean, understandable code.

These are not hard and fast rules for writing valid JavaScript, only proscriptions for maintaining consistent and appealing style choices throughout your source files. This is particularly interesting for JavaScript, which is a flexible and forgiving language that allows for a wide variety of stylistic choices.

Google and Airbnb have two of the most popular style guides out there. I’d definitely recommend you check out both of them if you spend much time writing JS.

The following are thirteen of what I think are the most interesting and relevant rules from Google’s JS Style Guide.

They deal with everything from hotly contested issues (tabs versus spaces, and the controversial issue of how semicolons should be used), to a few more obscure specifications which surprised me. They will definitely change the way I write my JS going forward.

For each rule, I’ll give a summary of the specification, followed by a supporting quote from the style guide that describes the rule in detail. Where applicable, I’ll also provide an example of the style in practice, and contrast it with code that does not follow the rule.

#### Use spaces, not tabs

The guide later specifies you should use two spaces (not four) for indentation.

```
// badfunction foo() {∙∙∙∙let name;}// badfunction bar() {∙let name;}// goodfunction baz() {∙∙let name;}
```

#### Semicolons ARE required

Although I can’t imagine why anyone is opposed to this idea, the consistent use of semicolons in JS is becoming the new ‘spaces versus tabs’ debate. Google’s coming out firmly here in the defence of the semicolon.

```
// badlet luke = {}let leia = {}[luke, leia].forEach(jedi => jedi.father = 'vader')
```

```
// goodlet luke = {};let leia = {};[luke, leia].forEach((jedi) => {  jedi.father = 'vader';});
```

#### Don’t use ES6 modules (yet)

```
// Don't do this kind of thing yet:
```

```
//------ lib.js ------export function square(x) {    return x * x;}export function diag(x, y) {    return sqrt(square(x) + square(y));}//------ main.js ------import { square, diag } from 'lib';
```

#### Horizontal alignment is discouraged (but not forbidden)

Horizontal alignment is the practice of adding a variable number of additional spaces in your code, to make certain tokens appear directly below certain other tokens on previous lines.

```
// bad{  tiny:   42,    longer: 435, };
```

```
// good{  tiny: 42,   longer: 435,};
```

#### Don’t use var anymore

I still see people using var in code samples on StackOverflow and elsewhere. I can’t tell if there are people out there who will make a case for it, or if it’s just a case of old habits dying hard.

```
// badvar example = 42;
```

```
// goodlet example = 42;
```

#### Arrow functions are preferred

I’ll be honest, I just thought that arrow functions were great because they were more concise and nicer to look at. Turns out they also serve a pretty important purpose.

```
// bad[1, 2, 3].map(function (x) {  const y = x + 1;  return x * y;});// good[1, 2, 3].map((x) => {  const y = x + 1;  return x * y;});
```

#### Use template strings instead of concatenation

```
// badfunction sayHi(name) {  return 'How are you, ' + name + '?';}// badfunction sayHi(name) {  return ['How are you, ', name, '?'].join();}// badfunction sayHi(name) {  return `How are you, ${ name }?`;}// goodfunction sayHi(name) {  return `How are you, ${name}?`;}
```

#### Don’t use line continuations for long strings

Interestingly enough, this is a rule that Google and Airbnb disagree on (here’s Airbnb’s spec).

While Google recommends concatenating longer strings (as shown below) Airbnb’s style guide recommends essentially doing nothing, and allowing long strings to go on as long as they need to.

```
// bad (sorry, this doesn't show up well on mobile)const longString = 'This is a very long string that \    far exceeds the 80 column limit. It unfortunately \    contains long stretches of spaces due to how the \    continued lines are indented.';
```

```
// goodconst longString = 'This is a very long string that ' +     'far exceeds the 80 column limit. It does not contain ' +     'long stretches of spaces since the concatenated ' +    'strings are cleaner.';
```

#### “for… of” is the preferred type of ‘for loop’

This is a strange one if you ask me, but I thought I’d include it because it is pretty interesting that Google declares a preferred type of for loop.

I was always under the impression that for... in loops were better for objects, while for... of were better suited to arrays. A ‘right tool for the right job’ type situation.

While Google’s specification here doesn’t necessarily contradict that idea, it is still interesting to know they have a preference for this loop in particular.

#### Don’t use eval()

The MDN page for eval() even has a section called “Don’t use eval!”

```
// badlet obj = { a: 20, b: 30 };let propName = getPropName();  // returns "a" or "b"eval( 'var result = obj.' + propName );
```

```
// goodlet obj = { a: 20, b: 30 };let propName = getPropName();  // returns "a" or "b"let result = obj[ propName ];  //  obj[ "a" ] is the same as obj.a
```

#### Constants should be named in ALL_UPPERCASE separated by underscores

If you’re absolutely sure that a variable shouldn’t change, you can indicate this by capitalizing the name of the constant. This makes the constant’s immutability obvious as it gets used throughout your code.

A notable exception to this rule is if the constant is function-scoped. In this case it should be written in camelCase.

```
// badconst number = 5;
```

```
// goodconst NUMBER = 5;
```

#### One variable per declaration

```
// badlet a = 1, b = 2, c = 3;
```

```
// goodlet a = 1;let b = 2;let c = 3;
```

#### Use single quotes, not double quotes

```
// badlet directive = "No identification of self or mission."
```

```
// badlet saying = 'Say it ain\u0027t so.';
```

```
// goodlet directive = 'No identification of self or mission.';
```

```
// goodlet saying = `Say it ain't so`;
```

#### A final note

As I said in the beginning, these are not mandates. Google is just one of many tech giants, and these are just recommendations.

That said, it is interesting to look at the style recommendations that are put out by a company like Google, which employs a lot of brilliant people who spend a lot of time writing excellent code.

You can follow these rules if you want to follow the guidelines for ‘Google compliant source code’ — but, of course, plenty of people disagree, and you’re free to brush any or all of this off.

I personally think there are plenty of cases where Airbnb’s spec is more appealing than Google’s. No matter the stance you take on these particular rules, it is still important to keep stylistic consistency in mind when write any sort of code.