Trello Automator
================

This is a quick way that I use to automate Trello - I prefer to choose what not to do, instead of picking what to do.
Otherwise, I end up automating something :)
Every morning, I want the cards in the 'Tomorrow' list to be moved in the 'Today' list.
At the same time, the cards in my 'Later this week' list should be moved in the 'Tomorrow' list.
With this, every evening I just pick what I don't want to do tomorrow and put it back in the 'Later this week' list.

You can make your own rules just by modifying this code. Enjoy!

````
    later_list = get_list_id_from_name('Later This Week')
    tomorrow_list = get_list_id_from_name('Tomorrow')
    today_list = get_list_id_from_name('Today')
    move_cards(tomorrow_list, today_list)
    move_cards(later_list, tomorrow_list)
````

