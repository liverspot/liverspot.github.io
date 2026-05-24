---
layout: post
title:  "Understanding your Dialysis Machine"
date:   2024-02-27 00:00:00 -0700
categories:
  - story
tags:
  - dialysis
author: Mark Fussell
---

If you do dialysis in a clinic you spend many hours a week sitting next to a dialysis machine. <!--more-->  It is possible you never need to concern yourself with how it works: it can be treated as just a black box that the RNs and technicians take care of.  It may also be out of your view, so if you do want a look, you may need to ask to have it turned a bit. 

<div class="w-richtext">
    <p>
        Understanding what the dialysis machine is doing can relieve boredom, provide education, and help avoid problems.  Potentially very painful and health-threatening problems.  Your doctor&#x27;s prescription and the clinic technicians enter the values for dialysis, and these may be the correct values.  In two years of dialysis, the values were mostly right for me.  In the last few months though (at a different dialysis center), &quot;mistakes were made&quot;.  By understanding the machine&#x27;s display I caught the errors at the start of the treatment.
        <br/>
    </p>
    <h3>My Dialysis Machine</h3>
    <p>My dialysis machine when I started dialysis in 2021 looked like this:</p>
    <figure class="w-richtext-align-center w-richtext-figure-type-image">
        <div>
            <img loading="lazy" alt="" src="https://cdn.prod.website-files.com/654c35b90c33f91f6457b77b/65de42937eae1ad756f9df22_IMG_5321_v1b2.png"/>
        </div>
    </figure>
    <p>Later the machine was updated to a new model and the display looked like this (the pump rate moved up onto the display), which makes it a bit easier to read and explain.</p>
    <figure class="w-richtext-align-center w-richtext-figure-type-image">
        <div>
            <img loading="lazy" alt="" src="https://cdn.prod.website-files.com/654c35b90c33f91f6457b77b/65de42ae45d72ed91228ba65_IMG_6610_v2.png"/>
        </div>
    </figure>
    <p>
        The dashboard (&#x27;Home&#x27;) mode is only one state of the machine, but it is the one you are most likely to see.  
        <br/>
    </p>
    <p>
        Using a diagram from the Fresenius Technical Documentation, you can see they agree with how it looks in real life (without the glare and perspective effects).
        <br/>
    </p>
    <figure class="w-richtext-align-center w-richtext-figure-type-image">
        <div>
            <img loading="lazy" alt="" src="https://cdn.prod.website-files.com/654c35b90c33f91f6457b77b/65de42d7c4208a0d07274644_Fresenius_paused.png"/>
        </div>
    </figure>
    <p>
        From: 
        <a href="https://fmcna.com/content/dam/fmcna/live/support/documents/techical-documentation/2008t-hemodialysis-systems/103324-01_Rev_B.pdf">https://fmcna.com/content/dam/fmcna/live/support/documents/techical-documentation/2008t-hemodialysis-systems/103324-01_Rev_B.pdf</a>
        <br/>
    </p>
    <h3>What is critical</h3>
    <p>There are more than twenty values displayed on this screen.  The following aspects are the most critical:</p>
    <ul role="list">
        <li>Session sanity (Session Length, Blood Pump Rate)</li>
        <li>Water removal (UF Goal, UF Time)</li>
    </ul>
    <h4>
        Session Sanity
        <br/>
    </h4>
    <h5>Session Length (via RTD)</h5>
    <p>
        The core value driving dialysis session length is in the initial value of the ‹RTD› (Remaining Time on Dialysis) field (e.g. &#x27;0:56&#x27; in the diagram).
        <br/>
    </p>
    <p>
        This is a countdown timer, so if you have a four hour session, it starts at four hours.  Initially it will match a clock time countdown (say a four-hour session starting at 2:00, after an hour should be 3-hours remaining), but as the session progresses dialysis could be paused.  The clock time will stop matching the RTD counter any time the dialysis session pauses.  Dialysis could be paused because you needed to leave the chair, but for me it was mostly based on whether my blood pressure dropped too low.  My session length was pretty much always four hours, although it could be reduced to 3.5 if there was a scheduling issue.
                <br/>
            </p>
            <h5>Blood Pump Rate</h5>
            <p>
                The ‹Blood Pump Rate› (e.g. &#x27;200&#x27;) is the speed the pump is pulling blood out of the catheter or fistula .  When I had a catheter it was 350 and with a matured fistula it went up to 400.
                <br/>
            </p>
            <p>
                The session length and pump rate should be values you expect.  If the pump rate is too low the dialysis will be less effective.  If the session length is too short, you may be happy it ended early (but likely not because of the water effect), but they aren&#x27;t going to just let you go.  Or your doctor will be unhappy you are not following the prescription.
                <br/>
            </p>
            <h4>Water Removal</h4>
            <h5>UF Goal</h5>
            <p>
                The ‹UF Goal› (e.g. &#x27;3000&#x27;) is the amount of water they expect to remove (through ‹Ultrafiltration›) during the dialysis session.  This should match the amount that your ‹Wet Weight› is above your ‹Dry Weight› as long as that isn&#x27;t too much for you to handle.  Values above 3 liters are risky for most people.  I could &#x27;try for&#x27; as much as 4 but usually would cramp out and fail.  
                <br/>
            </p>
            <p>
                If the ‹UF Goal› is too small, you will be water-heavy leaving from dialysis and are going to have to get rid of that water eventually (with more diuretics, paracentisis, or in subsequent dialysis sessions).  So that is not ideal.
                <br/>
            </p>
            <h5>UF Time</h5>
            <p>
                The ‹UF Time› (e.g. &#x27;0:56&#x27;) is a countdown timer for ultrafilteration, which will match the RTD countdown initially.  
                <br/>
            </p>
            <p>This is a second reason you want the RTD value to not be too short.  If the UF Time value is too short and the goal is correct, the machine is going to quickly pull a lot of water.  And you will likely have increased chances and severity for cramping.</p>
            <h3>What is interesting</h3>
            <p>Beyond the above values, the rest are mostly &#x27;just interesting&#x27;. </p>
            <ul role="list">
                <li>There are standard vital signs in the upper right corner: blood pressure and pulse.</li>
                <li>There are pressure readings starting from the left side that show how  forcefully the blood is being pulled into the machine, being returned, and crossing the membrane.</li>
                <li>The two profile charts in the bottom right show non-linear water and sodium removal (e.g. start strong and then ramp down as less is remaining)</li>
            </ul>
            <h4>More Technical Explanation</h4>
            <ul role="list">
                <li>
                    ‍
                    <a href="https://www.youtube.com/watch?app=desktop&amp;v=UCsWD2NyqOI">https://www.youtube.com/watch?app=desktop&amp;v=UCsWD2NyqOI</a>
                </li>
                <li>
                    <a href="https://hemodialysisaccess.yale.edu/the-basics/">https://hemodialysisaccess.yale.edu/the-basics/</a>
                </li>
            </ul>
            <p>‍</p>
        </div>
