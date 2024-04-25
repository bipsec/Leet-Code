def split_the_string():
    audio_str = ['M_09_SHUMANTA_S_10_FEAR_2.wav', 'F_09_CHAITY_S_3_FEAR_5.wav']
    emotion_label = ['F', 'F', 'W', 'W', 'W', 'A', 'W', 'T', 'W', 'W', 'L', ]

    emotion_dict = {
        'W': 'anger',
        'L': 'boredom',
        'E': 'disgust',
        'A': 'anxiety/fear',
        'F': 'happiness',
        'T': 'sadness',
        'N': 'neutral version'
    }

    for item in audio_str:
        get_contributor = item.split("_")[2]
        emotion = item.split("_")[5]
        print(get_contributor)
        print(emotion)

    #
    # for item in range(len(emotion_label)):
    #     val = emotion_dict[emotion_label[item]]
    #     emotion_label[item] = val
    # print(emotion_label)


split_the_string()
