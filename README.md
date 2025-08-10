# Timelines

Timelines is a minimalistic web app for creating and sharing personal timelines. Each post captures a moment in time and can be marked as public or private. The interface keeps things simple so you can focus on memories.

## Features
- Create timeline posts with title, date, content, and visibility
- View posts in reverse chronological order
- Lightweight design using Flask and vanilla HTML/CSS

## Getting started

Install requirements and run the development server:

```bash
pip install -r requirements.txt
python app.py
```

The app now listens on all interfaces by default so it can be previewed
from a remote environment. To change the port, set the `PORT` environment
variable before running:

```bash
PORT=8000 python app.py
```

Then open `http://localhost:8000` (or the forwarded port in your environment)
to view your timeline.
