# apply sensitivity analysis to news reporter prose from different political parties (first two paragraphs of each article) to see if the paper reports neutrally and objectively, or is more positively/negative directed towards given events.

paris_agreement_join = {
    "Fox": "Secretary of State Tony Blinken announced Friday that the United States formally rejoined the Paris climate agreement, arguing it will 'help us all avoid catastrophic planetary warming' and 'build resilience' around the world. The largely symbolic act comes as the Biden administration has quickly moved to reverse the energy policies of former President Donald Trump -- including revoking the Keystone XL pipeline permit. President Biden has also signed executive actions to eliminate federal subsidies for oil and other fossil fuels and moved to halt new oil and gas leases on federal lands and waters.",
    "The Huffington Post": "Hours after his inauguration Wednesday, President Joe Biden signed an executive order to rejoin the Paris Agreement, ending the United States’ brief but symbolic exit from the global pact to slash planet-heating emissions that virtually every nation has joined. Biden’s executive order kick-starts a relatively simple process. After sending a letter to the United Nations announcing its intentions to reenter the climate accord, the U.S. will again become a formal party to the global negotiations in 30 days. It was the third executive order he signed in the Oval Office. In separate executive orders, Biden is expected to lay the groundwork for the part that comes next and is much more of a challenge: reversing the Trump administration’s deregulatory legacy and setting ambitious new goals for decarbonizing the U.S. economy.",
    "WSJ": "In one of his first acts as president, Joe Biden issued an executive order returning the U.S. to the Paris Climate Agreement, which became official on Feb. 19 after a 30-day notice period. The U.S. had helped shape the accord under President Barack Obama but seven months after the pact took effect in late 2016, President Donald Trump withdrew the country. In a sign of how seriously Mr. Biden takes climate issues, one of the first overseas trips by a member of his administration is a swing this week through London, Brussels and Paris by John Kerry, the U.S. special presidential envoy for climate. Mr. Kerry, who helped negotiate the Paris agreement as secretary of state, is meeting with allies to prepare for upcoming climate summits in the U.S. and U.K. “Paris alone does not get the job done,” Mr. Kerry said."
    }

insurrection = {
    "Fox": "The article alleges that before Jan. 6, the joint session of Congress to certify the presidential election results, Trump 'repeatedly issued false statements asserting that the presidential election results were the product of widespread fraud and should not be accepted by the American people or certified by State or Federal officials.' The article claims that before the Jan. 6 joint session the president addressed a crowd in Washington where he 'reiterated false claims that 'we won this election, and we won it by a landslide,' and' willfully made statements that, in context, encouraged--and forseeably resulted in--lawless action at the Capitol.",
    "The Huffington Post":"Seven Republican members of the U.S. Senate voted to find former President Donald Trump guilty of inciting the Jan. 6 insurrection at the U.S. Capitol that left five people dead. By the end of this week, six of the seven may have faced censures from local and state Republican parties back home because of those votes. Together with the 10 Republican House members who voted to impeach Trump, the seven GOP senators made Trump’s second impeachment the most bipartisan in American history. But if those votes foreshadowed a looming civil war within the GOP, the hasty efforts to censure anyone who crossed Trump are a good indication of which side has the larger army. As the riot in the Capitol played out, even the GOP lawmakers who helped incite it briefly attempted to distance themselves from the mess they had created. But rather than a reckoning, the Republican Party is attempting a purge. From Congress to state legislatures, and in the state- and county-level parties that make up its base, the GOP’s rank and file has emerged from an insurrection and a second impeachment trial united against American democracy and the few members of the party still willing to stand up for it.",
    "WSJ": "WASHINGTON—The dramatic conclusion of former President Donald Trump’s second impeachment trial laid bare deep philosophical rifts between Republicans, as GOP senators splintered not only over the question of Mr. Trump’s guilt, but also the future of their party and Mr. Trump’s role in it. Seven GOP senators voted to convict the former president of inciting an insurrection on Jan. 6—not enough to find him guilty but, as Senate Majority Leader Chuck Schumer pointed out, the final tally was the most guilty votes cast by members of a president’s own party in any impeachment trial in American history. The rest of the Senate Republican conference—43 senators in total—voted to acquit Mr. Trump, but not without some angst, reflecting a party schism that has also fractured the House and will likely play out in primary elections in 2022 and 2024."
    }
    
    # look at sentiment analysis for each value in the dictionary
def headline_analysis(incident, nameincident):
    """ Conduct Sensivity Analysis on Incidents covered by different newspaper 
    Inputs: incident = dictionary with key:value pairs where keys are newspapers and values are fragments from their articles // nameincident = name of the incident, to be used to format outputs nicely and human-readable. 
    Outputs: conclusions on article sentiments on given event.
    """
    # generate sentiment analysis for each news paper.
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    sent = SentimentIntensityAnalyzer()
    for keys in incident:
        score = sent.polarity_scores(incident[keys])
    # summarize the conclusions for each incident 
        if score['compound'] <= -0.5:
            print(f"{keys}'s sentiments towards {nameincident} are indicated to be negative.")
        elif score['compound'] >= 0.5:
            print(f"{keys}'s sentiments towards {nameincident} are indicated to be positive.")
        else: 
            print(f"{keys}'s sentiments towards {nameincident} are indicated to be neutral.")

headline_analysis(paris_agreement_join, "the U.S. rejoing the Paris Climate Accord")
headline_analysis(insurrection, "Trump being convicted for the Insurrection")

def main():
    headline_analysis(paris_agreement_join, "the U.S. rejoing the Paris Climate Accord")
    headline_analysis(insurrection, "Trump being convicted for the Insurrection")

if __name__ == "__main__":
    main()