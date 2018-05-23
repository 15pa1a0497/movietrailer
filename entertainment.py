import media
import fresh_tomatoes
# Create instances of the Movie class to hold information of favourite movies
Twi_light = media.movie("Twilight",
                        "Twilight was directed by Catherine Hardwicke\
                        and written by Melissa Rosenberg.",
                        "https://bit.ly/2GCjZy6",
                        "https://www.youtube.com/watch?v=QDRLSqm_WVg")
New_Moon = media.movie("New_Moon",
                       "The Twilight Saga: New Moon was directed by Chris Weitz\
                        and written by Melissa Rosenberg.",
                       "https://bit.ly/2IXxihI",
                       "https://www.youtube.com/watch?v=q58iQSHhZGg")
Ec_lipse = media.movie("Ec_lipse",
                       "The Twilight Saga Eclipse was directed by David Slade\
                        and written by Melissa Rosenberg.",
                       "https://bit.ly/2IYrKU8",
                       "https://www.youtube.com/watch?v=S2HIda5wSVU")
Breaking_dawn_1 = media.movie("Breakingdawn_1",
                              "The Twilight Saga: Breaking Dawn was directed\
                               by Bill Condon, and author Stephenie Meyer\
                               co-produced the film along with Karen Rosenfelt\
                               and Wyck Godfrey, with Melissa Rosenberg \
                               penning the script.",
                              "https://bit.ly/2rWCNn3",
                              "https://www.youtube.com/watch?v=PQNLfo-SOR4")
# Add the instances to a list
movies = [Twi_light, New_Moon, Ec_lipse, Breaking_dawn_1]
# Generate a web page that displays the movies in the list
fresh_tomatoes.open_movies_page(movies)
