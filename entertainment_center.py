import fresh_tomatoes
import m
a = m.M("3 Idiots",
        "Two friends are searching for their long lost companion",
        "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
        "www.youtube.com/watch?v=xvszmNXdM4w")
b = m.M("Ghajini",
        "A short-term memory avenge the death of his beloved girl.",
        "https://upload.wikimedia.org/wikipedia/en/9/97/Ghajini_Hindi.jpg",
        "https://www.youtube.com/watch?v=j_DshRUOm-o")
c = m.M("Dangal",
        "Mahavir Phogat train daughters for the Commonwealth Games",
        "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
        "www.youtube.com/watch?v=x_7YlGv9u1g")
d = m.M("PK",
        "An alien on Earth loses the device",
        "https://upload.wikimedia.org/wikipedia/en/c/c3/PK_poster.jpg",
        "www.youtube.com/watch?v=SOXWc32k4zA")
e = m.M("Kahaani",
        "a pregnant woman, travels to search for her missing husband",
        "https://upload.wikimedia.org/wikipedia/en/8/85/KahaaniPoster.jpg",
        "www.youtube.com/watch?v=j1wEeuAosNM")
f = m.M("Talvar",
        "cop deals with conflicting perspectives involving a murder",
        "https://upload.wikimedia.org/wikipedia/en/9/91/TalvarFilmPoster.jpg",
        "www.youtube.com/watch?v=aQNMsw8Ljjc")
g = m.M("Baby",
        "An team of the IIS strives to detect and eliminate terrorists",
        "https://upload.wikimedia.org/wikipedia/en/d/da/BABY_poster_2015.jpg",
        "https://www.youtube.com/watch?v=-Yu_2nyOP5o")
h = m.M("Special 26",
        "A team conduct raids to rob politician or businessmen of black money",
        "https://upload.wikimedia.org/wikipedia/en/7/7c/Special_26_poster.jpg",
        "https://www.youtube.com/watch?v=PiyQb28geOg")
i = m.M("Airlift",
        "an Indian man leads a successful life in Kuwait with his family",
        "https://upload.wikimedia.org/wikipedia/en/3/35/Airlift_poster.jpg",
        "https://www.youtube.com/watch?v=vb5xCMbMfZ0")
movies = {a, b, c, d, e, f, g, h, i}
fresh_tomatoes.open_movies_page(movies)
