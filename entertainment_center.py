import media
import fresh_tomatoes

# Define all instances from class Movie
kung_fu_panda = media.Movie("Kung Fu Panda", "In the Valley of Peace, a land in ancient China inhabited by anthropomorphic animals, the giant panda Po is a kung fu fanatic who idolizes the Furious Five Tigress, Monkey, Mantis, Viper, and Crane a quintet of kung fu students trained by the red panda Master Shifu. As he helps his adoptive goose father Mr. Ping in his noodle restaurant, Po is unable to pursue his dream of becoming a kung fu master himself.", "https://www.infoescola.com/wp-content/uploads/2009/11/po-kung-fu-panda.jpg", "https://www.youtube.com/watch?v=0dzBQL41MOI")

monsters_inc = media.Movie("Monsters Inc", "The city of Monstropolis in the monster world is powered by energy from the screams of human children. At the Monsters, Inc. factory, skilled monsters employed as 'scarers' venture into the human world to scare children and harvest their screams, through doors that activate portals to children's bedroom closets. It is considered dangerous work, as human children are believed to be toxic. Energy production is falling because children are becoming less easily scared, and Monsters, Inc.'s chairman, Henry J. Waternoose, is determined to find a solution.", "https://alchetron.com/cdn/Monsters-Inc-images-7ff5a969-1c9f-402f-beb3-7f6ecf9f0f0.jpg", "https://www.youtube.com/watch?v=bdmRtnQTjaE")

enchanted = media.Movie("Enchanted", "In the animated fairy tale kingdom of Andalasia, the evil Queen Narissa schemes to protect her claim to the throne, which she will lose once her stepson, Prince Edward, finds his true love and marries her. She enlists her loyal henchman Nathaniel to keep Edward distracted. Giselle, a young woman, dreams of meeting a prince and experiencing a 'happy ever after'. Edward hears Giselle singing and sets off to find her. Nathaniel sets free a captured troll to kill Giselle, but Edward rescues her in time. When they meet, they instantly fall in love and plan to get married the following day.", "https://i.pinimg.com/564x/2e/4b/31/2e4b3185d8b56303bc942beb93c4119d.jpg", "https://www.youtube.com/watch?v=gDs0ijmCYf4")

white_chicks = media.Movie("White chicks", "The plot begins in a convenience store where two FBI agents and brothers, Kevin and Marcus Copeland (Shawn Wayans and Marlon Wayans), try to capture members of an organization that sells drugs inside ice cream boxes, posing as Cuban clerks. Unfortunately, the first arrival turns out to be a genuine ice cream delivery, and the actual drug dealers manage to get away. The situation is worsened by the fact that Kevin and Marcus have decided to resolve this bust by themselves.", "https://upload.wikimedia.org/wikipedia/pt/d/de/White_chicks.jpeg", "https://www.youtube.com/watch?v=cjnmsoJavj0")

tropa_de_elite = media.Movie("Elite Squad", "Captain Roberto Nascimento (Wagner Moura), of BOPE, narrates the film, briefly explaining how the police and the drug lords of Rio de Janeiro cooperate with each other (policemen collect periodic bribes and drug lords are left free to operate) in the 1990s.", "https://upload.wikimedia.org/wikipedia/pt/2/2a/TropaDeElitePoster.jpg", "https://www.youtube.com/watch?v=A6W-nNPl1T8")

# Define a list with all movies from entertainment center
movies = [kung_fu_panda, monsters_inc, enchanted, white_chicks, tropa_de_elite]

# Open page with posters and movie trailers
fresh_tomatoes.open_movies_page(movies)
