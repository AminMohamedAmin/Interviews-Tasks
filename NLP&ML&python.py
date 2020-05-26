class API(object):
    def one(self):
        import json
        from ibm_watson import NaturalLanguageUnderstandingV1
        from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
        from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions, SentimentOptions

        authenticator = IAMAuthenticator('-GEDGacgnI36ctk77Aa4X5k3PAXBA_AaRQIxp6G71sOP')
        natural_language_understanding = NaturalLanguageUnderstandingV1(
            version='2019-07-12',
            authenticator=authenticator
        )
        natural_language_understanding.set_service_url('https://api.eu-gb.natural-language-understanding.watson.cloud.ibm.com/instances/b61e5fb9-726b-4cba-8b4b-12f1403ed4a1')

        # ii = "Hello, I'm having a problem with your service. Nothing is working well. The service here is very bad. I am really very upset. I was expecting better than that. And my service has been stopped since yesterday. I have been suffering from this problem for a long time and cannot find a solution. The service here is bad most of times. Why you do not solve these problems. Some had left your service for this reason. The network is weak all the time, and it stops at the call. why this happen!? I wait. I'm fed up with complaining from the service."
        ii = "Hello, I need some help. I've subscribed to some news services and want to cancel them.They were not helpful with me plus they used a lot of balance. I feel bad because I used this service. Please remove it and try to improve these services. It has more harm than good. I hope to improve some services and offer some offers soon. I have another problem. My service has been disabled since yesterday. I have been suffering from this problem for a different times and cannot find a solution. It affects my work and communication in some important times."
        response1 = natural_language_understanding.analyze(
            text=ii,
            features=Features(emotion=EmotionOptions(targets=[ii.split()[1]]))).get_result()

        response2 = natural_language_understanding.analyze(
            text=ii,
            features=Features(sentiment=SentimentOptions(targets=[ii.split()[1]]))).get_result()
        global sad, joy, fear, disgust, anger, sentiment_label, sentiment
        sad = response1['emotion']['document']['emotion']['sadness']
        joy = response1['emotion']['document']['emotion']['joy']
        fear = response1['emotion']['document']['emotion']['fear']
        disgust = response1['emotion']['document']['emotion']['disgust']
        anger = response1['emotion']['document']['emotion']['anger']
        sentiment_label = response2['sentiment']['document']['label']
        sentiment = response2['sentiment']['document']['score']

        print(sad, joy, fear, disgust, anger, sentiment_label, sentiment)

###########################################################################

    def two(self):
        import pandas as pd
        data = pd.read_csv("final_dataset.csv")

        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(data[["sadness", "joy", "fear", "disgust", 'anger', 'score']],
                                                            data["label_state"], test_size=0.4)
        from sklearn.svm import LinearSVC
        lsvm = LinearSVC()
        prid = lsvm.fit(X_train, y_train)

        accuracy = lsvm.score((X_test), y_test)
        # print(accuracy)

        out = lsvm.predict((X_test))
        from sklearn.metrics import classification_report

        # print(classification_report(out, y_test))

        lls = [sad, joy, fear, disgust, anger, sentiment]
        predict = lsvm.predict([lls])
        ss = predict

        if predict == [0]:
            predict = "leave"
        else:
            predict = "stay"

        print(lsvm.predict([lls]))
        print(predict)

# o = API()
# o.one()
# o.two()
###################################################################

#     import matplotlib.pyplot as plt
#
#     plt.xlabel('Emotion_Name')
#     plt.ylabel('Emotion_Value')
#     plt.title('Personality_Emotions')
#     left = [1, 2, 3, 4, 5, 6]
#
#     if sentiment < 0:
#         sentiment = -1 * sentiment
#         height = [sad, joy, fear, disgust, anger, sentiment]
#         tick_label = ['sadness', 'joy', 'fear', 'disgust', 'anger', 'neg_sent']
#
#     elif sentiment > 0:
#         height = [sad, joy, fear, disgust, anger, sentiment]
#         tick_label = ['sadness', 'joy', 'fear', 'disgust', 'anger', 'pos_sent']
#     else:
#         height = [sad, joy, fear, disgust, anger, sentiment]
#         tick_label = ['sadness', 'joy', 'fear', 'disgust', 'anger', 'neural_sent']
#
#     # plotting a bar chart
#     plt.bar(left, height, tick_label=tick_label,
#             width=0.7, color=['red', 'green', 'blue', 'yellow', 'pink', 'orange'])
#
#     plt.show()
#
# #######################################################################
#
#     import numpy as np
#     import pandas as pd
#     import matplotlib.pyplot as plt
#     from matplotlib.widgets import CheckButtons
#
#     fig = plt.figure(figsize=(4, 1.5))
#     col = (1, 1, 1, 1)
#     rax = plt.axes([0.001, 1, 0.2, 0.6], facecolor=col)
#     ch = ss
#     if ch == 0:
#         check = CheckButtons(rax, ('stay', 'leave'), (0, 1))
#         for i, c in enumerate(["Silver", "green"]):
#             check.labels[i].set_color(c)
#             check.labels[i].set_alpha(0.9)
#     else:
#         check = CheckButtons(rax, ('stay', 'leave'), (1, 0))
#         for i, c in enumerate(["green", "Silver"]):
#             check.labels[i].set_color(c)
#             check.labels[i].set_alpha(0.9)
#     for r in check.rectangles:
#         r.set_facecolor("White")
#         r.set_alpha(0.5)
#     [ll.set_color("black") for l in check.lines for ll in l]
#     [ll.set_linewidth(3) for l in check.lines for ll in l]
#     plt.show()
#
#     plt.xlabel('State')
#     plt.ylabel('State_Value')
#     plt.title('Personality_State')
#
#     left = [1, 2]
#     height = [1, 1]
#     # labels for bars
#     tick_label = ['stay', 'leave']
#     plt.bar(left, height, tick_label=tick_label, width=0.5, color=['Silver', 'Silver'])
#     # heights of bars
#     if ss == 1:
#         plt.bar(left, height, tick_label=tick_label, width=0.5, color=['green', 'Silver'])
#     else:
#         plt.bar(left, height, tick_label=tick_label, width=0.5, color=['Silver', 'green'])
#     plt.show()
