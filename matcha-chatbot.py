from nltk.chat.util import Chat,reflections

pairs=[
    ['My name is (.*)',['Hi %1']],
    ["(hey|hello|yo|hi|hola|what's good?)",
     ["Hello, I'm glad that you are thinking of switching to Green Tea, or as I call it: Matcha !"
      ,'Nice to meet you!',"Hope you're doing good","Hi there! How can I help you?"]],
    ['(.*) is fun',['%1 is indeed fun']],
    ["(what is your name?|what are you?|who are you?|your name please?)",
    ["Hi I'm Mat","Call me Mat","I'm Mat, nice to meet you"]],
    ["(bye|see you later|goodbye|nice chatting with you)",
     ["Hope you enjoy your matcha!","Congratulations on switching to a healthier lifestyle","enjoy your green tea"]],
    ["(thanks|thank you|that's helpful|awesome,thanks|thanks for helping me)",
     ["happy to help!","anytime","no problem, you're making healthier choices"]],
    ["(How can you help me?| What can you do?|What help you provide?|help?|How can you be helpful?|What support do you offered|What do you know?)",
     ["I can tell you the benefits of matcha green tea."]],
    ["(What do you know about matcha?|tell me about matcha?|Is matcha healthier than coffee?|what exactly do you know about matcha?)",
    [ "I know all about matcha and its benefits",
        "I know some key words like benefits, impact, weight loss and coffee to mention a few",
        "Ask me a question about matcha and I will answer to the best of my knowledge"]],
    ["(What is matcha?|What is matcha green tea?|matcha|difference between matcha and green tea)",
    ["Matcha is a highly concentrated form of green tea."]],
    ["( What are the benefits of matcha?|List the benefits of matcha?|Do you know the benefits of matcha?|benefits?)",
    ["1.The combination of caffeine with l-theanine in matcha green tea provides a stable and extended boost of energy without the anxious jitters or side effects like you might have previously experienced with coffee and energy drinks\n2.Some things simply require a lot of thought. The combination of caffeine and l-theanine do wonders for concentration.\n3.Matcha green tea Fortifies the immune system and limits the invasion and growth of viruses and bacteria in the body\n4.EGCg and caffeine work together to naturally boost your metabolism and increase the number of calories you burn on a daily basis.\n5.L-theanine is a rare amino acid found in high concentrations in matcha that crosses the blood-brain barrier and promotes a feeling of relaxation while reducing mental and physical stress."]],
    ["(How do I get started?|start?|How do I quit coffee then?|How much should I consume everyday?|list the full tennis wears)",
    ["To be safe, make sure to consume matcha in moderation. It's best to stick to 1–2 cups per day and look for certified organic varieties to take advantage of matcha's many health benefits without risking any side effects. There are many ways to prepare matcha, so you can choose the one you like best."]],
    ["(How do I prepare matcha?|How to prepare it?|prepare?)",
    [       "1.Sift 1-2 tsp matcha into a cup using a small sifter.\n2.Add 2oz hot water. For best results use water just under a boil.\n3.Whisk vigorously in a zig zag motion until the tea is frothy.\n4.Enjoy your matcha tea straight from the bowl or add water or milk.\n Tip: We recommend adding lemon zest to make it healthier!"]],
    ["(Are there any side effects?|side effects?|What are the side effects?|Can you tell me the side effects of matcha?)",
    ["Matcha doesn't appear to cause significant side effects when consumed in moderation, but high doses providing large amounts of caffeine may cause headaches, diarrhea, insomnia, and irritability. Pregnant women should use caution."]],
    ["(What are the brands which sell matcha?|brands?|Where do I buy matcha from?|Where can I find Matcha?)",
    ["You can find matcha sold by various brands on Amazon. Starting price: $5.99"]],
    ["(Does matcha help in weight loss?|weight loss?)",
    [  "Yes!! Matcha contains EGCg (epigallocatechin gallate), which increases CCK (cholecystokinin), the hormone  responsible for making you feel full. Drinking matcha between meals will help you feel full and resist those sneaky snacks that are full of calories."]],
    
    
    #['(.*)(loacation|city)?',['Gurgaon,India!!']],
    ['(.*) (created you)?',['Spardha']],
    #['(.*) (is your name)?',['Zac']]
]

my_reflections={ "hi":"hello"}   

chat=Chat(pairs,my_reflections)
#chat._substitute('hi')
chat.converse()
