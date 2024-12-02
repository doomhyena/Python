import datetime
from collections import defaultdict

def read_file(file_path):
    """Beolvassa a fájl tartalmát és feldolgozza az adatokat."""
    episodes = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 5):
            date = lines[i].strip()
            title = lines[i+1].strip()
            season_episode = lines[i+2].strip()
            duration = int(lines[i+3].strip())
            watched = int(lines[i+4].strip())
            season, episode = map(int, season_episode.split('x'))
            episodes.append({
                'date': date,
                'title': title,
                'season': season,
                'episode': episode,
                'duration': duration,
                'watched': watched
            })
    return episodes

def count_known_dates(episodes):
    return sum(1 for ep in episodes if ep['date'] != 'NI')

def calculate_watched_percentage(episodes):
    total = len(episodes)
    watched = sum(1 for ep in episodes if ep['watched'] == 1)
    return round((watched / total) * 100, 2)

def total_watch_time(episodes):
    total_minutes = sum(ep['duration'] for ep in episodes if ep['watched'] == 1)
    days = total_minutes // (24 * 60)
    hours = (total_minutes % (24 * 60)) // 60
    minutes = total_minutes % 60
    return days, hours, minutes

def filter_unwatched_by_date(episodes, input_date):
    result = []
    for ep in episodes:
        if ep['date'] != 'NI' and ep['watched'] == 0 and ep['date'] <= input_date:
            result.append(f"{ep['season']}x{ep['episode']}\t{ep['title']}")
    return result

def Hetnapja(ev, ho, nap):
    napok = ["vasárnap", "hétfő", "kedd", "szerda", "csütörtök", "péntek", "szombat"]
    h = (nap + (13 * (ho + 1)) // 5 + ev + (ev // 4) - (ev // 100) + (ev // 400)) % 7
    return napok[h]

def filter_by_weekday(episodes, day):
    napok_rovid = {"h": "hétfő", "k": "kedd", "sze": "szerda", "cs": "csütörtök", "p": "péntek", "szo": "szombat", "v": "vasárnap"}
    nap = napok_rovid.get(day)
    if not nap:
        return "Érvénytelen nap rövidítés."

    result = set()
    for ep in episodes:
        if ep['date'] != 'NI':
            ev, ho, nap = map(int, ep['date'].split('.'))
            if Hetnapja(ev, ho, nap) == nap:
                result.add(ep['title'])

    return result if result else "Az adott napon nem kerül adásba sorozat."

def summarize_series(episodes):
    summary = defaultdict(lambda: {'total_time': 0, 'count': 0})
    for ep in episodes:
        summary[ep['title']]['total_time'] += ep['duration']
        summary[ep['title']]['count'] += 1

    with open('summa.txt', 'w', encoding='utf-8') as f:
        for title, data in summary.items():
            f.write(f"{title} {data['total_time']} {data['count']}\n")

def main():
    episodes = read_file('lista.txt')

    # 2. Ismert adásba kerülési dátumú epizódok száma
    print(f"2. feladat: {count_known_dates(episodes)}")

    # 3. Megtekintett epizódok aránya
    watched_percentage = calculate_watched_percentage(episodes)
    print(f"3. feladat: {watched_percentage:.2f}%")

    # 4. Megtekintett epizódok összes ideje
    days, hours, minutes = total_watch_time(episodes)
    print(f"4. feladat: {days} nap, {hours} óra, {minutes} perc")

    # 5. Epizódok dátumig
    input_date = input("Adj meg egy dátumot (éééé.hh.nn): ")
    unwatched = filter_unwatched_by_date(episodes, input_date)
    print("5. feladat:")
    for ep in unwatched:
        print(ep)

    # 6. Nap megadása alapján vetítés
    day_short = input("Adj meg egy napot rövidítve (h, k, sze, cs, p, szo, v): ")
    series_on_day = filter_by_weekday(episodes, day_short)
    print("6. feladat:")
    print(series_on_day)

    # 7. Összegzés sorozatokra
    summarize_series(episodes)

if __name__ == "__main__":
    main()
