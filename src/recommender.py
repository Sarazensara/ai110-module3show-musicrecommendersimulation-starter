from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score_song_obj(self, user: UserProfile, song: Song) -> Tuple[float, List[str]]:
        score = 0.0
        reasons = []

        if song.genre.strip().lower() == user.favorite_genre.strip().lower():
            score += 2.0
            reasons.append("genre match (+2.0)")

        if song.mood.strip().lower() == user.favorite_mood.strip().lower():
            score += 1.5
            reasons.append("mood match (+1.5)")

        energy_gap = abs(song.energy - user.target_energy)
        energy_score = max(0.0, 1.5 - energy_gap * 1.5)
        score += energy_score
        reasons.append(f"energy similarity (+{energy_score:.2f})")

        if user.likes_acoustic:
            acoustic_score = song.acousticness
            score += acoustic_score
            reasons.append(f"acoustic bonus (+{acoustic_score:.2f})")

        return round(score, 2), reasons

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = []
        for song in self.songs:
            score, _ = self._score_song_obj(user, song)
            scored.append((song, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _, reasons = self._score_song_obj(user, song)
        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    print(f"Loading songs from {csv_path}...")
    songs = []

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs


def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    if song["genre"].strip().lower() == user_prefs["favorite_genre"].strip().lower():
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"].strip().lower() == user_prefs["favorite_mood"].strip().lower():
        score += 1.5
        reasons.append("mood match (+1.5)")

    energy_gap = abs(song["energy"] - user_prefs["target_energy"])
    energy_score = max(0.0, 1.5 - energy_gap * 1.5)
    score += energy_score
    reasons.append(f"energy similarity (+{energy_score:.2f})")

    if user_prefs.get("likes_acoustic", False):
        acoustic_score = song["acousticness"]
        score += acoustic_score
        reasons.append(f"acoustic bonus (+{acoustic_score:.2f})")

    return round(score, 2), reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda x: x[1], reverse=True)
    return scored_songs[:k]