from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory store for posts. In a real app this would be a database.
posts = []

@app.route('/')
def timeline():
    """Display the timeline of posts."""
    # Posts are shown in reverse chronological order
    ordered = sorted(posts, key=lambda p: p['date'], reverse=True)
    return render_template('timeline.html', posts=ordered)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    """Create a new timeline entry."""
    if request.method == 'POST':
        post = {
            'title': request.form['title'],
            'content': request.form['content'],
            'date': request.form['date'],
            'visibility': request.form['visibility']
        }
        posts.append(post)
        return redirect(url_for('timeline'))
    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)
