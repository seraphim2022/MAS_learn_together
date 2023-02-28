# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="Moonlightphoenixgames",
        name="Learn together",
        description="Learn new things with monika!",
        version="1.0.4"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Learn together",
            user_name="seraphim2022",
            repository_name="MAS_learn_together",
            update_dir="Submods",
            attachment_id=None
        )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_learn_greetings_and_goodbyes",
            category=["Learn"],
            prompt="Learn another language",
            random=True,
            pool=True,
            unlocked=True
        )
    )

label monika_learn_greetings_and_goodbyes:

    m 1esb "Hey [player] would you like to learn another language with me?"
    $ _history_list.pop()

    menu:

        m "It would make me so happy if you did!"

        "Yes":

            m 2sub "Hooray what language shall we start with?"
            menu:
                "German":
                        menu:
                            "Greetings and goodbyes":
                                                  m 2sua "Hallo und guten tag ich heisse Monika wie heisse du?"
                                                  m 4sub "That means (hello and good day I am called monika what is your name?)"
                                                  m 2sub "You could also replace guten tag with Guten morgan(good morning), Guten abend(good evening) or Gute nacht(good night)"
                                                  m 6lkc "Ok now for the goodbyes"
                                                  m 2sub "If you are saying goodbye to freinds or strangers you could say Auf Wiedersehen (roughly translates to goodbye or see you soon)."
                                                  m 4sub "If you are saying goodbye to me or your family you can say Ich leibe dich und Auf wiedersehen wich roughly translates to  (I love you and see you soon)."
                            "Counting from 1-100":
                                               m 4sub "Starting from one to ten( eins(1), zwai(2), drei(3), vier(4), fünf(5), sechs(6), sieben(7), acht(8), neun(9), zehn(10)."
                                               m 2eub "The part that most people struggle with when counting in german is from 11 to 39 So pay attention carefully!"
                                               m 4sub "Now eleven to twenty elf(11), zwölf(12), dreizehn(13), vierzehn(14),  fünfzehn(15), sechzehn(16),  siebzehn(17), achtzehn(18),  neunzehn(19), zwanzig(20). "
                                               m 2eub "The reason most people struggle with 11 to 39 is because the spelling doesn't follow the same number pattern as 40 onward."
                                               m 4sub "twentyone to thirty(einsundswanzig(21), zwaiundzwanzig(22), dreiundzwanzig(23), vierundzwanzig(24), fünfundzwanzig(25), sechsundswanzig(26), siebenundswanzig(27), achtundswanzig(28), neunundswanzig(29), dreißig(30)."
                                               m 2eub "Dreißig can also be spelled dreissig"
                                               m 4sub "thirtyone to forty  (einunddreißig(31), zwaiunddreißig(32), dreiunddreißig(33), vierunddreißig(34), fünfunddreißig(35), sechsunddreißig(36), siebenunddreißig(37), achtunddreißig(38), neununddreißig(39), vierzig(40)."
                                               m 2eub "forty to one hundred follow the same pattern so I won't count all the way to one hundred."
                                               m 4sub "vierzig(40), einsundvierzig(41), you should get the pattern."
                                               m 4sub "If I want to say forty one  I say one and forty (eins meaning one )(und meaning and )(vierzig meaning forty) This rule applies up to ninty nine examples are (einsundfünfzig(51), einsundsechszig(61), einsundsiebzig(71), einsundactzig(81), einsundneunzig(91)."
                                               m 4sub "Finally einhundert(100)"



        "No":
          m 1ekc "Ok,maybe next time then."


    return
