import fresh_tomatoes
import media

# Creating movie objects for 5 of my favorite movies
# TODO put in a database
toy_story = media.Movie("Toy Story",
                        81,
                        "A little boy named Andy loves to be in his room,"
                        " playing with his toys, especially his doll named"
                        " 'Woody'. But, what do the toys do when Andy is not"
                        " with them, they come to life. Woody believes that he"
                        " has life (as a toy) good. However, he must worry"
                        " about Andy's family moving, and what Woody does not"
                        " know is about Andy's birthday party. Woody does not"
                        " realize that Andy's mother gave him an action figure"
                        " known as Buzz Lightyear, who does not believe that"
                        " he is a toy, and quickly becomes Andy's new favorite"
                        " toy. Woody, who is now consumed with jealousy, tries"
                        " to get rid of Buzz. Then, both Woody and Buzz are"
                        " now lost. They must find a way to get back to Andy"
                        " before he moves without them, but they will have to"
                        " pass through a ruthless toy killer, Sid Phillips.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        media.Video.VALID_RATINGS[1])
movie2 = media.Movie("The Bourne Identity",
                     119,
                     "Based very loosely on Robert Ludlum's novel,"
                     " the Bourne Identity is the story of a man whose wounded"
                     " body is discovered by fishermen who nurse him back to"
                     " health. He can remember nothing and begins to try to"
                     " rebuild his memory based on clues such as a Swiss"
                     " bank account, the number of which is implanted in his"
                     " hip. He soon realizes that he is being hunted and"
                     " takes off with Marie on a search to find out who he is"
                     " - and why he is being hunted.",
                     "https://upload.wikimedia.org/wikipedia/en/a/ae/BourneIdentityfilm.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=cD-uQreIwEk",
                     media.Video.VALID_RATINGS[2])
movie3 = media.Movie("The Bourne Supremacy",
                     108,
                     "After escaping from the emotional and physical pain he"
                     " previously encountered. Jason Bourne and his girlfriend"
                     " Marie begin a new life as far away as possible. But"
                     " when an assassination attempt on Bourne goes horribly"
                     " wrong, Bourne must re-enter the life he wanted to leave"
                     " behind, in order to find out the truth why they are"
                     " still after him",
                     "https://upload.wikimedia.org/wikipedia/en/3/30/Bourne_supremacy_ver2.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=rmOxVvT5lmw",
                     media.Video.VALID_RATINGS[2])
movie4 = media.Movie("The Bourne Ultimatum",
                     115,
                     "Bourne is once again brought out of hiding, this time"
                     " inadvertently by London-based reporter Simon Ross who"
                     " is trying to unveil Operation Blackbriar--an upgrade"
                     " to Project Treadstone--in a series of newspaper"
                     " columns. Bourne sets up a meeting with Ross and"
                     " realizes instantly they're being scanned. Information"
                     " from the reporter stirs a new set of memories, and"
                     " Bourne must finally, ultimately, uncover his dark past"
                     " whilst dodging The Company's best efforts in trying to"
                     " eradicate him.",
                     "https://upload.wikimedia.org/wikipedia/en/f/fe/The_Bourne_Ultimatum_%282007_film_poster%29.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=OTskAEZvRuU",
                     media.Video.VALID_RATINGS[2])
movie5 = media.Movie("Inside Out",
                     95,
                     "Growing up can be a bumpy road, and it's no exception"
                     " for Riley, who is uprooted from her Midwest life when"
                     " her father starts a new job in San Francisco. Like all"
                     " of us, Riley is guided by her emotions - Joy, Fear,"
                     " Anger, Disgust and Sadness. The emotions live in"
                     " Headquarters, the control center inside Riley's mind,"
                     " where they help advise her through everyday life. As"
                     " Riley and her emotions struggle to adjust to a new life"
                     " in San Francisco, turmoil ensues in Headquarters."
                     " Although Joy, Riley's main and most important emotion,"
                     " tries to keep things positive, the emotions conflict on"
                     " how best to navigate a new city, house and school.",
                     "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=yRUAzGQ3nSY",
                     media.Video.VALID_RATINGS[1])

# Adding the movies to the list
movies = [toy_story, movie2, movie3, movie4, movie5]

# opens the browser and shows the generated html file
fresh_tomatoes.open_movies_page(movies)
