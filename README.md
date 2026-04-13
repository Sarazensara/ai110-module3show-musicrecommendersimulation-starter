# 🎵 Music Recommender Simulation

## Project Summary

This project simulates a simple music recommendation system using a content-based approach. Songs are represented using features such as genre, mood, energy, and tempo, while a user profile defines preferred values for those features. The system scores each song based on how closely it matches the user’s preferences and then ranks songs to recommend the top results. This project demonstrates how data can be transformed into personalized predictions using simple scoring logic.

## How The System Works

This recommender system uses a content-based approach to suggest songs based on a user's preferences.

### Song Features
Each song is represented using:
- genre
- mood
- energy (0.0–1.0)
- tempo_bpm

### User Profile
The user profile stores:
- favorite_genre
- favorite_mood
- target_energy
- target_tempo_bpm

### Scoring Logic
Each song is given a score based on how well it matches the user profile:

- +2.0 points for matching genre
- +1.5 points for matching mood
- Additional points based on how close the song’s energy is to the target energy
- Additional points based on how close the tempo is to the target tempo

Songs that are closer to the user’s preferences receive higher scores.

### Recommendation Process
1. Load all songs from the dataset
2. Score each song using the scoring function
3. Sort songs from highest to lowest score
4. Return the top K songs as recommendations

You can include a simple diagram or bullet list if helpful.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

I experimented with changing the importance of different features in the scoring function.

When I reduced the weight of genre and increased the weight of energy, the recommendations became more focused on matching the overall “vibe” instead of the category. This made the results feel more flexible but sometimes less consistent.

I also tested different user profiles such as high-energy pop, chill lofi, and intense rock. Each profile produced different results, which showed that the system responds well to changes in user preferences.

When I removed mood from the scoring, the recommendations became less accurate because songs with the right energy but wrong emotional tone started appearing higher in the rankings.

---

## Limitations and Risks

This recommender system has several limitations.

First, it only uses a small dataset, so the recommendations are limited and may repeat often. Second, it relies heavily on genre and mood labels, which can create a filter bubble and reduce variety. Third, it does not understand deeper aspects of music such as lyrics, context, or cultural meaning.

Because the scoring system is simple, it may also favor certain features too strongly, which can bias the results toward specific types of songs.

---

## Reflection

This project helped me understand how recommendation systems turn user data into predictions. Even with a simple scoring system, the recommendations changed in meaningful ways depending on the user profile and feature weights.

It also showed me how bias can appear in systems like this. For example, giving too much importance to genre can limit diversity and create repetitive recommendations. This made me realize that real-world systems must carefully balance multiple factors to avoid unfair or narrow results.

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

