from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# --- Global Variables (Simple Integers) ---
tasks = {}      # {1: 'Run 5km', 2: 'Buy Milk'}
next_id = 1     # The ID dispenser
done_count = 0  # Counter for completed tasks

@app.route("/")
def home():
    global done_count
    
    # If the dictionary is empty, reset the counter to zero
    if not tasks:
        done_count = 0
        progress = 0
    else:
        total = len(tasks) + done_count
        progress = int((done_count / total) * 100)
        
    return render_template("index.html", tasks=tasks, progress=progress)

@app.route("/add", methods=["POST"])
def add():
    global next_id  # Needed to change the integer
    title = request.form.get("title")
    if title:
        tasks[next_id] = title  # Add to dictionary
        next_id += 1            # Move to next unique ID
    return redirect("/")

@app.route("/done/<int:tid>", methods=["POST"])
def done(tid):
    global done_count  # Needed to change the integer
    if tid in tasks:
        tasks.pop(tid) # Remove by ID key
        done_count += 1
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)