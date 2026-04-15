# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

VibeFinder 1.0  

---

## 2. Intended Use  

This recommender system is designed to suggest songs from a small dataset based on a user’s preferences. It generates recommendations by comparing song features like genre, mood, energy, and tempo to a user profile.

The system assumes that users have clear preferences (for example, favorite genre and mood) and that similarity in these features reflects what they would enjoy.

This model is intended for classroom exploration only and is not meant for real-world users.

---

## 3. How the Model Works  

This system uses a content-based recommendation approach.

Each song includes features such as genre, mood, energy, and tempo. The user profile contains preferred values for these same features. The system compares each song to the user’s preferences and assigns a score.

Songs receive:
- points for matching genre
- points for matching mood
- additional points when energy is close to the user’s target
- additional points when tempo is close to the user’s target

After all songs are scored, they are ranked from highest to lowest, and the top songs are recommended.

---

## 4. Data  

The dataset is stored in a CSV file and contains a small number of songs (around 10–20 depending on additions).

Each song includes:
- title
- artist
- genre
- mood
- energy
- tempo_bpm

The dataset includes some variety in genre and mood, but it is still limited and does not fully represent all music tastes. It also relies on simplified labels rather than real listening behavior.

---

## 5. Strengths  

This system works well for users with clearly defined preferences, such as someone who enjoys high-energy pop or calm lofi music.

The recommendations are easy to understand because the scoring logic is simple and transparent. It is also easy to see why a song was recommended based on the matching features.

In many cases, the top results matched my expectations based on the user profile.

---

## 6. Limitations and Bias  

This recommender has several limitations.

It relies heavily on genre and mood labels, which can create a filter bubble where users only see similar types of songs. Songs from different genres with similar vibes may be ignored.

The dataset is small, so recommendations may lack variety and repeat often. The system also assumes all users have the same type of preference structure, which is not realistic.

In a real-world setting, this could lead to unfair exposure of certain genres or artists.

---

## 7. Evaluation  

I evaluated the system by testing different user profiles, such as high-energy pop, chill lofi, and intense rock.

I looked at whether the recommended songs matched the expected vibe for each profile. In most cases, the results made sense, but I noticed that genre had a strong influence on rankings.

I also tested edge cases, such as conflicting preferences (high energy with a sad mood), to see how the system behaved. I experimented with changing feature weights and observed how the recommendations changed.

---

## 8. Future Work  

If I continued this project, I would:

- expand the dataset with more songs and genres  
- add more features such as danceability or acousticness  
- introduce a diversity penalty to avoid repetitive recommendations  
- allow multiple scoring modes (e.g., mood-focused vs genre-focused)  

---

## 9. Personal Reflection  

This project helped me understand how recommendation systems turn user data into predictions. Even with a simple scoring system, the results felt personalized and changed depending on the inputs.

What surprised me most was how easily bias can appear. For example, prioritizing genre too much can limit diversity in recommendations.

This project showed me that recommendation systems are built on human decisions about data and weights, and those choices strongly influence what users see.