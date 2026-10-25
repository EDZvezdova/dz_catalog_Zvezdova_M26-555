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



def count_long_movies(movie_list, threshold=120):
    count = 0
    for movie in movie_list:
        duration = movie.get("duration_min", 0)
        if duration > threshold:
            count += 1 
    return count

def duration_in_hours(minutes: int) -> str:
    """Переводит минуты в строку формата 'Xч Yм'."""
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}ч {remaining_minutes}м"


def normalize_title(title: str) -> str:
    """
    Приводит строку к Title Case без str.title().
    Разбивает по пробелам, вручную делает первую букву заглавной через срез.
    """
    if not title:
        return ""
    
    words = title.split(" ")
    normalized_words = []
    
    for word in words:
        if not word:
            normalized_words.append(word)
            continue
        # Меняем только первую букву вручную: word[0].upper() + word[1:]
        normalized_word = word[0].upper() + word[1:]
        normalized_words.append(normalized_word)
    
    return " ".join(normalized_words)


def make_slug(title: str) -> str:
    """
    Превращает название в слаг: все буквы в нижний регистр, пробелы → дефисы.
    Использует .lower() и .replace().
    """
    lower_title = title.lower()
    slug = lower_title.replace(" ", "-")
    return slug


def format_report_line(movie: dict) -> str:
    """
    Возвращает единую строку с описанием фильма в формате:
    '"<Название>" (<год>) — <рейтинг>/10, <длительность>, жанры: <жанр1, жанр2>'
    
    Обязательно использует f-строку и вызывает duration_in_hours.
    Жанры отсортированы по алфавиту.
    """
    title = movie.get("title", "")
    year = movie.get("year", "?")
    rating = movie.get("rating", "?")
    duration_min = movie.get("duration_min", 0)
    genres = movie.get("genres", set())
    
    # Нормализуем название
    norm_title = normalize_title(title)
    
    # Получаем длительность через функцию из этапа 1
    duration_str = duration_in_hours(duration_min)
    
    # Сортируем жанры по алфавиту и собираем в строку
    sorted_genres = sorted(genres)
    genres_str = ", ".join(sorted_genres)
    
    # Собираем итоговую строку через f-строку в требуемом формате
    report = f'"{norm_title}" ({year}) — {rating}/10, {duration_str}, жанры: {genres_str}'
    return report
# Примеры для проверки отдельных функций
print(normalize_title("silent hours"))      # "Silent Hours"
print(make_slug("Silent Hours"))            # "silent-hours"

# Пример для format_report_line (для фильма movies[7] — "The Quiet Algorithm")
if len(movies) > 7:
    print(format_report_line(movies[1]))
    # Ожидаемый вывод:
    # "The Quiet Algorithm" (2024) — 9.2/10, 1ч 58м, жанры: drama, sci-fi



