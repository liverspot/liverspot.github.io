---
layout: post
title:  "MELD Score Explanation and Real-World Example"
date:   2024-02-19 07:00:00 -0700
categories:
  - story
tags:
  - cirrhosis
  - creatinine
  - meld
author: Mark Fussell
---



In 2021 I went to Stanford Emergency after several months of getting progressively sicker. Ultimately I had both liver and kidney failure when in the hospital, 
<!--more--> and with liver failure a very important term comes out: &quot;MELD Score&quot;. Over the next few months and years, I would understand MELD scores quite a bit better but had never looked into the actual calculation and &#x27;drivers&#x27; sufficiently to describe them.

<h3>MELD Score</h3>
<p>The MELD score is a way to prioritize patients in need of transplants. It is &#x27;objective&#x27; in that it is solely based on measurements, and it is supposed to correlate with probability of survivability without a transplant so those most in critical need get transplants before those that can wait. The formula has changed over the year, but the goal remains unchanged. Because MELD is a calculation, it is not in any test result. Most of the components are from normal blood work, so their contribution to the score is easily calculable, but the INR (blood clotting) test is not commonly prescribed.</p>
<h3>MELD Calculation</h3>
<p>
    The MELD score is commonly opaque to many patients. It is just a number a doctor told them. There are online calculators (see <a href="/topics#meld">MELD</a>) 
 that can take the component values and tell you your score, which is sufficient for many patients wanting to have a bit more insight.
</p>
<figure class="w-richtext-align-center w-richtext-figure-type-image">
    <div>
        <img src="https://cdn.prod.website-files.com/654c35b90c33f91f6457b77b/65d6a25989a67c36cb1ddeed_Screenshot%202024-02-21%20at%205.23.38%20PM.png" loading="lazy" alt=""/>
    </div>
</figure>
<p>But to truly understand the number, you need to know the details of how it is calculated. Fortunately, the MELD calculation is very simple. </p>
<h4>Components</h4>
<p>The main components of the MELD score are:</p>
<ul role="list">
    <li>Bilirubin — A waste product that should be removed by the liver. High levels produce jaundice (yellowing)</li>
    <li>Sodium — Salt level in blood stream</li>
    <li>Albumin — A liver-created protein</li>
    <li>Creatinine — A waste product that should be removed by the kidneys</li>
    <li>INR — A normalized value for how fast your blood clots</li>
</ul>
<p>Of the above, the INR value needs a special test, but can also be &#x27;assumed&#x27; to be &#x27;1&#x27; (normal) if you don&#x27;t know it. The rest are on a metabolic blood panel that is commonly prescribed.</p>
<h4>Normalization</h4>
<p>The above component values have a number of different ranges, so to use them together in a MELD score calculation, they need to be normalized into a similar scale system. Going through each one:</p>
<ul role="list">
    <li>Bilirubin — Is exponentional (the value increases a lot with small physical differences), so it needs to have a logarithm (reverse of an exponent) function applied to the test value.</li>
    <li>Sodium — Has a normal value of 137 (Baseline for good) and higher values are not relevant to what the MELD is trying to calculate. So the test value is subtracted from 137 and the result is zero if the calculated result is negative.</li>
    <li>Albumin — Has a normal value of 3.5 and higher values are not relevant.</li>
    <li>Creatinine — Is exponential, so a logarithm is applied. Maximal value before logarithm is 3.0, and a patient under dialysis is treated as a 3.0.</li>
    <li>INR — Is exponential, so a logarithm is applied.</li>
</ul>
<h4>Contribution</h4>
<p>After doing all the above transormations, each component now has a reasonable baseline (zero value) and scales similarly to other components, but their contribution to survivability (and so the MELD score) is different. To deal with how these components correlate with survivability, research doctors weighted them. The following is the weighting values for these component in the MELD3 score.</p>
<ul role="list">
    <li>Bilirubin — 4.56</li>
    <li>Sodium — 0.82</li>
    <li>Albumin — 1.85</li>
    <li>Creatinine — 11.14</li>
    <li>INR — 9.09</li>
</ul>
<h4>Other Components</h4>
<p>
    There are a few other components to the formula: there is a historic baseline (no problems) value of &#x27;6&#x27; for  MELD scores, women&#x27;s numbers are slightly undervalued compared to the data, and there is a bit of correlation (double counting) of similar bloodwork components that are combined into the final MELD score. See the following equation and <a href="/topics#meld">MELD</a>
     for more details.
</p>
<figure class="w-richtext-align-center w-richtext-figure-type-image">
    <div>
        <img loading="lazy" alt="" src="https://cdn.prod.website-files.com/654c35b90c33f91f6457b77b/65d3c40a9b50ce6aea74c2cb_Screenshot%202024-02-19%20at%2011.06.28%20AM.png"/>
    </div>
</figure>
<h4>MELD Sum</h4>
<p>With the five core terms and four other components, you get a MELD score that is basically:</p>
<ul role="list">
    <li>6 + Bilirubin-Term + Sodium-Term + Albumin-Term + Creatinine-Term + INR-Term</li>
</ul>
<p>The MELD is ultimately that simple.</p>
<h3>Example MELD Score</h3>
<p>When I first went into Stanford in March of 2021, I was very sick and was in the hospital for about a month and the ICU for more than a week. During this time, my doctors didn&#x27;t talk to me about a MELD score: it isn&#x27;t diagonistically useful although its components are. I had high Bilirubin, so they needed to treat that. My kidneys failed, so they needed to treat that. I had hepatic encephalopathy and went into a coma, so they had to treat that. There was no day-to-day MELD score because it was not relevant to the doctors, to me, or to my family.</p>
<p>But I did have a lot of bloodwork done, and from that data you can see the above components driving the MELD calculation during the period I was hospitalized.</p>
<h4>Components</h4>
<p>The basic blood test produced the following values. Note that the sodium is on such a different scale that it dwarfs the other values so is clearly not directly composable with them.</p>
<figure class="w-richtext-align-center w-richtext-figure-type-image">
    <div>
        <img alt="blood_test_measurements" src="/images/2024-02-19-meld-score-explanation/blood_test_measurements.png"/>
    </div>
</figure>
<h4>Normalization</h4>
<p>Normalization of these values so they have similar characteristics produce this:</p>
<figure class="w-richtext-align-center w-richtext-figure-type-image">
    <div>
        <img alt="normalized_values" src="/images/2024-02-19-meld-score-explanation/normalized_values.png"/>
    </div>
</figure>
<p>With this everything is within a plausibly similar range, has similar physical impacts, and badness is in the same direction (positive is bad).</p>
<h4>Contribution</h4>
<p>Scaling by MELD3 contribution gives:</p>
<figure class="w-richtext-align-center w-richtext-figure-type-image">
    <div>
        <img alt="meld_contribution" src="/images/2024-02-19-meld-score-explanation/meld_contribution.png"/>
    </div>
</figure>
<p>These are now point-for-point equal to the MELD scale. For example, as of June my Creatinine value was producing &#x27;12&#x27; points toward my &gt;20 MELD score.</p>
<h4>MELD Sum</h4>
<p>Summing these components all together (without the "+6" baseline) gives:</p>
<figure class="w-richtext-align-center w-richtext-figure-type-image">
    <div>
        <img alt="meld_component_stack" src="/images/2024-02-19-meld-score-explanation/meld_component_stack.png"/>
    </div>
</figure>
<p>Or more simply in final MELD score:</p>
<figure class="w-richtext-align-center w-richtext-figure-type-image">
    <div>
        <img alt="resulting_meld_score" src="/images/2024-02-19-meld-score-explanation/resulting_meld_score.png"/>
    </div>
</figure>
<p>When admitted to the hospital and as I moved to ICU, my MELD spiked to above 30. As the symptoms causing the Bilirubin and INR values were dealt with, my MELD dropped below 30. And finally as my second-instance of a Sodium issue was dealt with, my score dropped into the low 20s.</p>
<p>The <a href="/topics/#meld-3">MELD-3</a> curve is similar to the original MELD calculation, but was slightly lower initially: there are two new terms in the MELD-3 that 'backout' (subtract) overcounting of high values in correlated components, which includes both sodium and creatinine values [which were both very high for me]. </p>
<h3>Summary</h3>
<p>The MELD score prioritizes patients on the liver transplant list. The score is calculated with a relatively simple formula based on five bloodwork values (INR, Bilirubin, Albumin, Creatinine, and Sodium). So it can be calculated fairly often but is not clinically meaningful except in the context of needing a liver transplant. In other situations the componenents values can be important to treatment, but the MELD itself is too vague to base diagnosis on. You can have an accutely high MELD score but it can go down dramatically as the causes of symptoms (e.g. Bilirubin) are alleviated from medical treatment.   </p>
<p>The MELD score is only used medically when other treatments are no longer effective in further symptom reduction (and the MELD score is above a 17 or so) so a transplant may be the only way to achieve further physical improvement.</p>
