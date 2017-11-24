import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
"A great story about Andy and his toys. When Andy is out of the room the Toys come to life",
"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
"https://www.youtube.com/watch?v=Ny_hRfvsmU8",
"PG")

star_wars_1 = media.Movie("Star Wars: Episode IV - A New Hope",
"The film's plot focuses on the Rebel Alliance, led by Princess Leia (Fisher), and its attempt to destroy the Galactic Empire's space station, the Death Star.",
"https://upload.wikimedia.org/wikipedia/en/8/87/StarWarsMoviePoster1977.jpg",
"https://www.youtube.com/watch?v=vP_1T4ilm8M",
"U")

indiana_jones = media.Movie("Indiana Jones and the Last Crusade",
"In the film, set largely in 1938, Indiana searches for his father, a Holy Grail scholar, who has been kidnapped by Nazis.",
"https://upload.wikimedia.org/wikipedia/en/f/fc/Indiana_Jones_and_the_Last_Crusade_A.jpg",
"https://www.youtube.com/watch?v=a6JB2suJYHM",
"PG")

back_to_the_future = media.Movie("Back to the Future",
"It stars Michael J. Fox as teenager Marty McFly, who is sent back in time to 1955, where he meets his future parents in high school and accidentally becomes his mother's romantic interest. Christopher Lloyd portrays the eccentric scientist Dr. Emmett 'Doc' Brown, Marty's friend who helps him repair the damage to history by helping Marty cause his parents to fall in love. Marty and Doc must also find a way to return Marty to 1985.",
"https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg",
"https://www.youtube.com/watch?v=qvsgGtivCgs",
"PG")

sunset_boulevard = media.Movie("Sunset Boulevard",
"The film stars William Holden as Joe Gillis, an unsuccessful screenwriter, and Gloria Swanson as Norma Desmond, a faded silent film star who draws him into her fantasy world where she dreams of making a triumphant return to the screen, with Erich von Stroheim as Max von Mayerling, her devoted servant. Nancy Olson, Fred Clark, Lloyd Gough and Jack Webb play supporting roles. Director Cecil B. DeMille and gossip columnist Hedda Hopper play themselves, and the film includes cameo appearances by leading silent film actors Buster Keaton, H. B. Warner and Anna Q. Nilsson.",
"https://upload.wikimedia.org/wikipedia/en/0/0a/SunsetBoulevardfilmposter.jpg",
"https://www.youtube.com/watch?v=xzYqUpV_B-A",
"PG")

pulp_fiction = media.Movie("Pulp Fiction",
"Pulp Fiction's narrative is told out of chronological order, and follows three main interrelated stories: Mob contract killer Vincent Vega is the protagonist of the first story, prizefighter Butch Coolidge is the protagonist of the second, and Vincent's partner Jules Winnfield is the protagonist of the third.[8] The stories intersect in various ways.",
"https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
"https://www.youtube.com/watch?v=s7EdQ4FqbhY",
"18")

raging_bull = media.Movie("Raging Bull",
"It stars Robert De Niro as Jake LaMotta, an Italian American middleweight boxer whose self-destructive and obsessive rage, sexual jealousy, and animalistic appetite destroyed his relationship with his wife and family.",
"https://upload.wikimedia.org/wikipedia/en/5/5f/Raging_Bull_poster.jpg",
"https://www.youtube.com/watch?v=YiVOwxsa4OM",
"18")

third_man = media.Movie("The Third Man",
"The film takes place in post-World-War-II Vienna. It centres on Holly Martins, an American who is given a job in Vienna by his friend Harry Lime, but when Holly arrives in Vienna he gets the news that Lime is dead. Martins then meets with Lime's acquaintances in an attempt to investigate what he considers a suspicious death.",
"https://upload.wikimedia.org/wikipedia/en/2/21/ThirdManUSPoster.jpg",
"https://www.youtube.com/watch?v=F-QWLAndD1E",
"PG")

network = media.Movie("Network",
"In this lauded satire, veteran news anchorman Howard Beale (Peter Finch) discovers that he's being put out to pasture, and he's none too happy about it. After threatening to shoot himself on live television, instead he launches into an angry televised rant, which turns out to be a huge ratings boost for the UBS network. This stunt allows ambitious producer Diana Christensen (Faye Dunaway) to develop even more outrageous programming, a concept that she takes to unsettling extremes.",
"https://upload.wikimedia.org/wikipedia/en/f/fc/Networkmovie.jpg",
"https://www.youtube.com/watch?v=1cSGvqQHpjs",
"15")

la_haine = media.Movie("La Haine",
"It is about three young friends and their struggle to live in the banlieues of Paris. The title derives from a line spoken by one of them, Hubert, 'La haine attire la haine!', 'hatred breeds hatred.'",
"https://upload.wikimedia.org/wikipedia/en/3/30/Haine.jpg",
"https://www.youtube.com/watch?v=5Hs6GwQPAQE&has_verified=1",
"15")

lion_king = media.Movie("The Lion King",
"This Disney animated feature follows the adventures of the young lion Simba (Zoe Leader), the heir of his father, Mufasa (Ernie Sabella). Simba's wicked uncle, Scar (Rowan Atkinson), plots to usurp Mufasa's throne by luring father and son into a stampede of wildebeests. But Simba escapes, and only Mufasa is killed. Simba returns as an adult (Jeremy Irons) to take back his homeland from Scar with the help of his friends Timon (Jonathan Taylor Thomas) and Pumbaa (Cheech Marin).",
"https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
"https://www.youtube.com/watch?v=4sj1MT05lAA",
"U")

movies = [toy_story, star_wars_1, indiana_jones, back_to_the_future, sunset_boulevard, pulp_fiction, raging_bull, third_man, network, la_haine, lion_king]

fresh_tomatoes.open_movies_page(movies)
