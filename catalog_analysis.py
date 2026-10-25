movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]
import math

def average_rating(movies):
    if not movies:
        return 0.0
    
    total = sum(movie['rating'] for movie in movies)
    avg = total / len(movies)
    return round(avg, 1)


def catalog_age_stats(movies, current_year=2026):
    if not movies:
        return (0, 0, 0)
    
    ages = [current_year - movie['year'] for movie in movies]
    
    oldest = max(ages)
    newest = min(ages)
    average_age = math.ceil(sum(ages) / len(ages))
    
    return (oldest, newest, average_age)


def duration_in_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "отличный фильм" if rating > 8 else "хорошо"
    elif rating >= 5:
        return "средне"
    else:
        return "слабо"


def decade_label(year):
    match True:
        case _ if year > 2020:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _ if year < 2015:
            return "старые"


for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    print(movie["title"])


def find_first_masterpiece(movie_list):
    index = 0
    while index < len(movie_list):
        if movie_list[index]["rating"] > 9.0:
            print(f"Первый шедевр найден: {movie_list[index]['title']} (рейтинг {movie_list[index]['rating']})")
            break
        index += 1
    else:
        print("Шедевров не найдено")

find_first_masterpiece(movies)


def count_long_movies(movie_list, threshold=120):
    count = 0
    for movie in movie_list:
        duration = movie.get("duration_min", 0)
        if duration > threshold:
            count += 1 
    return count

result = count_long_movies(movies, threshold=120)
print(f"Количество фильмов длиннее 120 минут: {result}")
