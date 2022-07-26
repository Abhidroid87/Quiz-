# To MAKE A QUIZ AN SAMPLE
from Qustion import Question

question_prompts = [
    "Which one of the following structures is haploid in its ploidy level?\n(a) Microspore Mother Cell\n(b) Protonemal cell of a moss\n(c) Primary endosperm nucleus in dicot\n(d) Primary Endospore Nucleus\n\n",
    "Select the correct statement related to the activity of cork cambium. \n(a) The cork differentiated from cork combium, is impervious to water due to deposition of tannins and resins.\n(b)  Cuts the cells only on the outer side.\n(c) Cuts the cells on inner as well as outer side.\n(d) The outer cells differentiate into phelloderm.\n\n",
    "Which one of the following process is responsible for the release of N₂ in the atmosphere?\n(a) Ammonification\n(b) Denitrification\n(c) Biological nitrogen fixation\n(d)Industrial Nitrogen fixation\n\n",
    "DNA replication is semi-conservative in nature was experimentally proved in eukaryotes by :\n(a) Macleod and McCarty\n(b) Meselson and Stahl\n(c) Talyor and his colleagues\n(d) Hershey and Chase\n\n",
    "High dose of UV-B causes inflammation of cornea as is called as:\n(a) Colour-blindness\n(b) Snow-blindness\n(c) UV-blindness\n(d) Evening-blindness\n\n",
    "Which of the following come under the Evil Quartet?\nHabitat loss and fragmentation\nOver-exploitation\nAlien species invasion\nMortality\nCompetition\nChoose the correct answer from the option given below:\n(1) (b), (c) and (d)\n(2) (a), (b) and (c) \n(3) (a), (b) and (d)\n(4) (a), (c) and (d)\n\n",
    "The process of individuals of the sum species that have come into the habitat from elsewhere during the time period under consideration is referred us \n(a) Emigration\n(b) Competition\n(c) Immigration\n(d) Association\n\n",
    "Given below are two statements one in labelled as Assertion (A) and the other is labelled as Reason (R).\nAssertion (A) = 1/2 growth of multicellular organism is due to mitosis.\nReason (R) Mitosis is also called as equational division and it offers genetic stability.\nIn the light of the above statements, choose the correct answer from the options given below :\n(a)  (A) is not correct but (R) is correct\n(b) Both (A) and (R) are correct and (R) is the correct explanation of (A)\n(c)  Both (A) and (R) are correct but (R) is not the correct explanation of (A)\n(d) (A) is correct but (R) is not correct\n\n",
    "Identify the correct set of statements with regard to properties of humus.\n(a) Highly resistant to microbial action.\n(b) Dark coloured amorphous substance.\n(c) End product of detritus food chain.\n(d) Reservoir of nutrients.. \n(e) Undergoes decomposition very fast.\nChoose the correct answer from the options given below:\n1  (a), (b) and (e) only\n2 (a) and (b) only\n3 (a), (b) and (c) only\n4 (a), (b) and (d) only\n\n",
    "The products of light reaction in photosynthesis are:\n(a) ATP, NADPH, O_{2} and H_{2}*O^ -\n(b) ATP, NADPH and H_{2}*O \n(c) ATP, NADPH and C*O_{2}\n(d) ATP, NADPH and O2\n\n",
    "Which one of the following expertes Foederick Griffith rished in the discovery of bacterial transformation?\n(a) S-train heat killed) + R-strain injected in to Mice Mice din \n(b) Strain injected in to Mice Mice died\n(c) Rstrain injected in to Mice Mice lived\n(d) S-strain (heat killed) injected in to Mice Mice lived\n\n",
    "Which hormone is used to induce immediate stomatal closure in leaves?\n(a) Gibberellin\n(b) Abscisic Acid\n(c) Auxin\n(d) Cytokinin\n\n",
    "Select the correct statements with respect to pleiotropism.\n(a) A gene is said to be pleiotropic if it affects more than one trait. \n(b) Phenylketonuria is an example of pleiotropy. \n(c) A condition where one gene has several alleles is referred to as pleiotropism. \n(d) A trait is said to be pleiotropic if several genes control it.\nChoose the correct answer from the options given below:\n1 (a) and (d) only\n2 (a), (b) and (c) only\n3 (b), (c) and (d) only\n4 (a) and (b) only\n\n",
]

questions = [
    Question(question_prompts [0], "b"),
    Question(question_prompts [1], "d"),
    Question(question_prompts [2], "c"),
    Question(question_prompts[3], ""),
    Question(question_prompts[4], ""),
    Question(question_prompts[5], ""),
    Question(question_prompts[6], ""),
    Question(question_prompts[7], ""),
    Question(question_prompts[8], ""),
    Question(question_prompts[9], ""),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " +str(score) + " out of " + str(len(questions))+ " correct")

run_test(questions)