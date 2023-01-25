# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="Moonlightphoenixgames",
        name="Learn together",
        description="Learn new things with monika!",
        version="1.0.1"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Learn together",
            user_name="seraphim2022",
            repository_name="MAS_learn_together",
            update_dir="game/Submods/Learn together",
            attachment_id=None
        )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_learn_greetings",
            category=["Learn"],
            prompt="Learn Greetings",
            random=True,
            pool=True,
            unlocked=True
        )
    )

label monika_learn_greetings:

    m 1esb "Hey [player] would you like to learn greetings in another language with me?"
    $ _history_list.pop()

    menu:

        m "It would make me so happy if you did!"

        "Yes":

            m 1sub "Hooray what language shall we start with?"
            menu:
                "German":

                       m 1sub "Hallo und guten tag ich heisse Monika wie heisse du?"
                       m 1sub "That means (hello and good day I am called monika what is your name?)"
                       m 1sub "You could also replace guten tag with Guten morgan(good morning), Guten abend(good evening) or Gute nacht(good night)"
        "No":

            m 1ekc "Ok,maybe next time then."
    
    return
        
        



         
        
      


   
    
   
        
       
    
    

        

